import datetime
import os
import pytz
import sys
import time

from google.transit import gtfs_realtime_pb2
from loguru import logger

import db.main as db
import preprocess_gtfs_data
stop_times = preprocess_gtfs_data.process_stop_times()
from gtfs_data.trips import trips

logger.remove()
logger.add(sys.stderr, level="DEBUG")
logger.add("bkk.log", rotation="500 MB")
logger.info(f"{__file__} loaded")

live_dir = "db/live"
archive_dir = "db/archive"

def process_pb_files():
    live_files = os.listdir(live_dir)
    live_files.sort(reverse=True)
    file_i = 1
    for file_name in live_files:
        logger.debug(f"Processing file {file_i}/{len(live_files)}")
        file_i += 1
        pb_dict = pb_to_dict(file_name)
        timestamp = pb_dict['timestamp']
        weekday = datetime.datetime.fromtimestamp(timestamp).weekday()
        hour = datetime.datetime.fromtimestamp(timestamp).hour
        check_value = db.create_lateness_list(timestamp, weekday, hour,)
        if timestamp == check_value:
            on_time_count = 0
            late_count = 0
            on_time_count_n = 0
            late_count_n = 0
            vehicle_list = []
            for id in pb_dict['vehicles']:
                vehicle = pb_dict['vehicles'][id]
                if vehicle['delay'] > 0:
                    late_count += 1
                else:
                    on_time_count += 1
                if vehicle['delay'] > 60:
                    late_count_n += 1
                else:
                    on_time_count_n += 1
                vehicle_list.append(vehicle)
            db.save_lateness_bulk(vehicle_list, timestamp)
            db.update_lateness_list_stats(timestamp, on_time_count, late_count, on_time_count_n, late_count_n)
            os.rename(os.path.join(live_dir, file_name),os.path.join(archive_dir, file_name))
    pass



def check_if_late(expected_time, actual_time):
    current_date = datetime.datetime.fromtimestamp(actual_time).date()
    date_time_str = f"{current_date} {expected_time}"
    date_time_obj = datetime.datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
    epoch_time = int(time.mktime(date_time_obj.timetuple()))
    datetime1 = datetime.datetime.fromtimestamp(epoch_time, pytz.timezone("Europe/Budapest"))
    datetime2 = datetime.datetime.fromtimestamp(actual_time, pytz.timezone("Europe/Budapest"))
    time_difference = datetime2 - datetime1
    if datetime1 < datetime2:
        time_difference = datetime2 - datetime1
        return time_difference.seconds
    else:
        return 0


def unix_to_human(timestamp):
    datetime_obj = datetime.datetime.fromtimestamp(timestamp)
    human_readable = datetime_obj.strftime('%H:%M:%S')
    return human_readable

def read_pb_file(file_name):
    feed = gtfs_realtime_pb2.FeedMessage()
    with open(os.path.join(live_dir, file_name), 'rb') as f:
        feed.ParseFromString(f.read())
    return feed


def pb_to_dict(file_name):
    pb_dict = {}
    feed = read_pb_file(file_name)
    pb_dict['timestamp'] = feed.header.timestamp
    pb_dict['vehicles'] = {}
    for entity in feed.entity:
        try:
            vehicle = entity.vehicle
            trip_id = vehicle.trip.trip_id
            if trip_id in trips:
                stop_id = vehicle.stop_id
                expected_time = stop_times[trip_id][stop_id]['departure_time']
                delay_seconds = check_if_late(expected_time, vehicle.timestamp)
                pb_dict['vehicles'][trip_id] = {
                    'latitude': vehicle.position.latitude,
                    'longitude': vehicle.position.longitude,
                    'delay': delay_seconds,
                    'route_id': vehicle.trip.route_id,
                    'trip_id': trip_id,
                    'speed': vehicle.position.speed,
                    'current_status': vehicle.current_status
                }
        except Exception:
            pass
    return pb_dict

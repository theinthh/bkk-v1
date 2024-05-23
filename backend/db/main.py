import sqlite3
from loguru import logger

import db.create_lateness_list
import db.get_histogram_data
import db.get_histogram_pred_data
import db.get_histogram_data_n
import db.get_histogram_pred_data_n
import db.get_latest_lateness
import db.get_scatter_data
import db.get_top_bottom
# import db.save_lateness
import db.save_lateness_bulk
import db.update_lateness_list_stats

#Double-check that live and archive folders are present
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
live_folder_path = os.path.join(current_directory, "live")
logger.info("Checking if 'live' and 'archive' folders exist")
if not os.path.exists(live_folder_path):
    os.makedirs(live_folder_path)
    archive_folder_path = os.path.join(current_directory, "archive")
    os.makedirs(archive_folder_path)
    logger.info("Folders were not found, creating")

con_lateness = sqlite3.connect("db/lateness.db")

with con_lateness:
    con_lateness.execute('''
        CREATE TABLE IF NOT EXISTS entry_lists (
            list_id INTEGER PRIMARY KEY,
            timestamp TEXT,
            processed INTEGER,
            weekday INTEGER,
            hour INTEGER,
            on_time_count INTEGER,
            late_count INTEGER,
            on_time_count_n INTEGER,
            late_count_n INTEGER,
            temp INTEGER,
            rain REAL,
            wind INTEGER
        )
    ''')
    con_lateness.execute('''
        CREATE TABLE IF NOT EXISTS latenesses (
            list_id INTEGER,
            latitude REAL,
            longitude REAL,
            delay INTEGER,
            route_id TEXT,
            trip_id TEXT,
            speed REAL,
            current_status INTEGER,
            FOREIGN KEY(list_id) REFERENCES entry_lists(list_id)
        )
    ''')

def create_lateness_list(timestamp, weekday, hour):
    return db.create_lateness_list.main(con_lateness, timestamp, weekday, hour)

def save_lateness(vehicle, list_id):
    db.save_lateness.main(con_lateness, vehicle, list_id)
    pass

def update_lateness_list_stats(list_id, on_time_count, late_count, on_time_count_n, late_count_n):
    db.update_lateness_list_stats.main(con_lateness, list_id, on_time_count, late_count, on_time_count_n, late_count_n)
    pass

def save_lateness_bulk(vehicle_list, list_id):
    db.save_lateness_bulk.main(con_lateness, vehicle_list, list_id)
    pass

def get_top_bottom():
    return db.get_top_bottom.main(con_lateness)

def get_histogram_data():
    return db.get_histogram_data.main(con_lateness)
def get_histogram_pred_data():
    return db.get_histogram_pred_data.main(con_lateness)


def get_histogram_data_n():
    return db.get_histogram_data_n.main(con_lateness)
def get_histogram_pred_data_n():
    return db.get_histogram_pred_data_n.main(con_lateness)

def get_histogram_seconds_data():
    return db.get_histogram_seconds_data.main(con_lateness)
def get_histogram_seconds_pred_data():
    return db.get_histogram_seconds_pred_data.main(con_lateness)

def get_scatter_data():
    return db.get_scatter_data.main(con_lateness)
def get_scatter_wind_lateperc():
    return db.get_scatter_wind_lateperc.main(con_lateness)

def get_scatter_rain_late():
    return db.get_scatter_rain_late.main(con_lateness)
def get_scatter_rain_laten():
    return db.get_scatter_rain_laten.main(con_lateness)


def get_weather_line_chart():
    return db.get_weather_line_chart.main(con_lateness)


def get_all_delays():
    return db.get_all_delays.main(con_delays)

def get_all_random():
    return db.get_all_delays_random.main(con_delays)

def get_latest_lateness():
    return db.get_latest_lateness.main(con_lateness)

def print_all_delays():
    db.print_all_delays.main(con_delays)
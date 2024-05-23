import datetime
import pytz

from loguru import logger

def main(con):
    sql = "SELECT max(list_id) FROM entry_lists;"
    c = con.cursor()
    c.execute(sql)
    timestamp = c.fetchone()[0]
    start_of_day = get_start_of_day(timestamp)
    sql = f"SELECT delay, speed, route_id FROM latenesses WHERE list_id > {start_of_day} AND current_status = 2;"

    all = [['Lateness','Speed']]
    trips = {}
    with con:
        data = con.execute(sql)
        for row in data:
            if row[2] not in trips:
                trips[row[2]] = {}
                trips[row[2]]['speeds'] = []
                trips[row[2]]['delays'] = []
            trips[row[2]]['speeds'].append(row[1])
            trips[row[2]]['delays'].append(row[0])
    for trip_id in trips:
        all.append([
            sum(trips[trip_id]['delays']) / len(trips[trip_id]['delays']),
            sum(trips[trip_id]['speeds']) / len(trips[trip_id]['speeds'])
            ])
    return all


def get_start_of_day(timestamp):
    date = datetime.datetime.fromtimestamp(timestamp, pytz.timezone("Europe/Budapest"))
    start_of_day = date.replace(hour=0, minute=0, second=0, microsecond=0)
    start_of_day_timestamp = int(start_of_day.timestamp())
    return start_of_day_timestamp

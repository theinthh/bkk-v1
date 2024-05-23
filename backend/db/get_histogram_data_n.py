import datetime
import pytz

from loguru import logger

def main(con):
    sql = "SELECT max(list_id) FROM entry_lists;"
    c = con.cursor()
    c.execute(sql)
    timestamp = c.fetchone()[0]
    start_of_day = get_start_of_day(timestamp)
    sql = f"SELECT hour, on_time_count_n, late_count_n FROM entry_lists WHERE list_id > {start_of_day};"

    all = [[]]*24
    for i in range(0, 24):
        all[i] = [str(i),[],""]

    with con:
        data = con.execute(sql)
        for row in data:
            total_count = row[1] + row[2]
            late_percentage = row[2] / total_count * 100
            all[row[0]][1].append(late_percentage)

    sql = f"SELECT weekday,hour FROM entry_lists WHERE list_id = {timestamp};"
    c = con.cursor()
    c.execute(sql)
    r_data = c.fetchone()

    day = r_data[0]
    hour = r_data[1]

    sql_pred = f"SELECT hour, on_time_count_n, late_count_n FROM entry_lists WHERE weekday = {day} AND hour > {hour};"

    with con:
        data = con.execute(sql_pred)
        for row in data:
            total_count = row[1] + row[2]
            late_percentage = row[2] / total_count * 100
            all[row[0]][1].append(late_percentage)


    #average out all the findings
    for i in range(0, 24):
        try:
            all[i][1] = sum(all[i][1]) / len(all[i][1])
            if i > hour:
                all[i][2] = 'opacity: 0.2'
        except Exception as e:
            all[i][1] = 0
    return all

def get_start_of_day(timestamp):
    date = datetime.datetime.fromtimestamp(timestamp, pytz.timezone("Europe/Budapest"))
    start_of_day = date.replace(hour=0, minute=0, second=0, microsecond=0)
    start_of_day_timestamp = int(start_of_day.timestamp())
    return start_of_day_timestamp
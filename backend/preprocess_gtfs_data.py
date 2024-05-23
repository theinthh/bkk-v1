import csv
import sys

from loguru import logger

logger.remove()
logger.add(sys.stderr, level="DEBUG")
logger.add("bkk.log", rotation="500 MB")
logger.info("preprocess_gtfs_data.py loaded")

def savetofile(filename, variable, name):
        file1 = open(filename, "w", encoding="utf-8")
        file1.write(f"{name} = ")  # + str(variable).encode('utf8'))
        file1.write(str(variable))
        file1.close()
        logger.info(f"Processed {name}.txt to {filename}")

def process_stop_times():
    logger.info("Processing stop_times.txt")
    file_name = "gtfs_data/stop_times.txt"
    stop_times = {}
    with open(file_name, "r", encoding="utf-8") as data:
        for line in csv.reader(data):
            if stop_times.get(line[0]) == None:
                stop_times[line[0]] = {}
            stop_times[line[0]][line[1]] = {}
            stop_times[line[0]][line[1]]['arrival_time'] = line[2]
            stop_times[line[0]][line[1]]['departure_time'] = line[3]
    return stop_times

def save_stop_times():
    stop_times = process_stop_times()
    savetofile("gtfs_data/stop_times.py", stop_times ,"stop_times")

def process_trips():
    logger.info("Processing trips.txt")
    file_name = "gtfs_data/trips.txt"
    trips = {}
    with open(file_name, "r", encoding="utf-8") as data:
        for line in csv.reader(data):
            if line[1] != "trip_id":
                trips[line[1]] = line[0]
    savetofile("gtfs_data/trips.py", trips ,"trips")

def process_routes():
    logger.info("Processing routes.txt")
    file_name = "gtfs_data/routes.txt"
    routes = {}
    with open(file_name, "r", encoding="utf-8") as data:
        for line in csv.reader(data):
            if line[1] != "route_id":
                routes[line[1]] = [line[2],line[5], line[6], line[7]]
    savetofile("gtfs_data/routes.py", routes ,"routes")

def process_gtfs_data():
    save_stop_times()
    process_trips()
    process_routes()




if __name__ == "__main__":
    logger.info("Running in stand-alone")
    process_gtfs_data()
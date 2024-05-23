import datetime
from os.path import exists
import sys
from time import sleep

from loguru import logger


if (not exists("gtfs_data/stop_times.txt") or not exists("gtfs_data/trips.txt")):
    logger.error("GTFS Static data not found")
    logger.info("Please download the GTFS static data from BKK OpenData Portal")
    logger.info("The .txt files should be added to backend/gtfs_data/")
    exit()

from preprocess_gtfs_data import process_gtfs_data
if (not exists("gtfs_data/stop_times.py") or not exists("gtfs_data/trips.py")):
    logger.info("GTFS static data not preprocessed, processing now")
    process_gtfs_data()
    logger.info("The next imports will need to cache stop_times.py, this might take some time")

import process

logger.remove()
logger.add(sys.stderr, level="DEBUG")
logger.add("bkk.log", rotation="500 MB")
logger.info(f"{__file__} loaded")

def main():
    schedule_tasks()

def schedule_tasks():
    logger.debug("Scheduler started")
    while True:
        now = datetime.datetime.now()
        seconds = int(now.strftime("%S"))
        if ( seconds < 15 and seconds > 5):
            logger.debug(f"Running tasks")
            process.process_pb_files()
            now = datetime.datetime.now()
            seconds = int(now.strftime("%S"))
            logger.debug(f"Sleeping until next minute")
            if (seconds < 15):
                sleep(15)
        sleep(2)

if __name__ == "__main__":
    main()
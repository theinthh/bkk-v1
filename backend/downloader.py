from datetime import datetime
import os
import sys
from time import sleep
import urllib.request

from dotenv import load_dotenv
load_dotenv()
from loguru import logger

bkk_key = os.environ["BKK_KEY"]
logger.remove()
logger.add(sys.stderr, level="DEBUG")
logger.add("bkk.log", rotation="500 MB")
logger.info(f"{__file__} loaded")

db_path = "db/live/"
vehicle_positions_url = f"https://go.bkk.hu/api/query/v1/ws/gtfs-rt/full/VehiclePositions.pb?key={bkk_key}"

def schedule():
    while True:
        now = datetime.now()
        seconds = int(now.strftime("%S"))
        if ( seconds < 5):
            timestamp = now.strftime("%Y%m%d_%H%M")
            file_name = f"vehicle_positions_{timestamp}.pb"
            download(vehicle_positions_url, file_name)
            logger.debug(f"Sleeping until next minute")
            sleep(15)
        sleep(2)

def download(url, file_name):
    try:
        urllib.request.urlretrieve(url, f"{db_path}{file_name}")
        logger.info(f"File {file_name} downloaded successfully!")
    except Exception as e:
        logger.error(f"Download failed: {e}")

if __name__ == "__main__":
    logger.info("Running in stand-alone")
    schedule()
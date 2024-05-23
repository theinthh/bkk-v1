from loguru import logger
def main(con, timestamp, weekday, hour):
    try:
        sql = f'INSERT INTO entry_lists (list_id, timestamp, hour, processed, weekday) values(?,?,?,?,?);'
        data = [(timestamp, timestamp, hour, 0, weekday
         )]
        with con:
            con.executemany(sql, data)
        logger.info(f"Created lateness list for {timestamp}")
        return timestamp
    except Exception as error_msg:
        logger.error(f"Unable to create list {timestamp}")
        logger.error(error_msg)
        return 0
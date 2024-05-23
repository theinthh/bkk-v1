from loguru import logger
def main(con, list_id, on_time_count, late_count, on_time_count_n, late_count_n):
    try:
        sql = f'UPDATE entry_lists SET on_time_count = {on_time_count}, late_count = {late_count}, on_time_count_n = {on_time_count_n}, late_count_n = {late_count_n} WHERE list_id = {list_id}'
        with con:
            con.execute(sql)
        logger.info(f"Added on_time_count for list {list_id}")
    except Exception as error_msg:
        logger.error(f"Unable to update list {list_id}")
        logger.error(error_msg)
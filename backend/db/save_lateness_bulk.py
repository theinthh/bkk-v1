from loguru import logger
def main(con, vehicle_list, list_id):
    sql_data_list = []
    for vehicle in vehicle_list:
        sql_data_list.append((list_id, 
         vehicle['latitude'],
         vehicle['longitude'],
         vehicle['delay'],
         vehicle['route_id'],
         vehicle['trip_id'],
         vehicle['speed'],
         vehicle['current_status']
         ))
    try:
        sql = f'INSERT INTO latenesses (list_id, latitude, longitude, delay, route_id, trip_id,speed, current_status) values(?,?,?,?,?,?,?,?);'
        data = sql_data_list
        with con:
            con.executemany(sql, data)
        logger.info(f"Added {len(sql_data_list)} latenesses for list {list_id}")
    except Exception as error_msg:
        logger.error(f"Unable to save lateness")
        logger.error(error_msg)
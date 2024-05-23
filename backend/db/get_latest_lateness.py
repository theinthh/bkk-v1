from loguru import logger
def main(con):
    sql = "SELECT max(list_id) FROM entry_lists;"
    all = []
    c = con.cursor()
    c.execute(sql)
    timestamp = c.fetchone()[0]
    sql = f"SELECT latitude,longitude,delay FROM latenesses WHERE list_id = {timestamp};"
    all = []
    with con:
        data = con.execute(sql)
        for row in data:
            all.append(row)
    return all
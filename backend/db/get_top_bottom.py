from loguru import logger
from gtfs_data.routes import routes as routes_static

def main(con):
    sql = "SELECT max(list_id) FROM entry_lists;"

    c = con.cursor()
    c.execute(sql)
    timestamp = c.fetchone()[0]
    sql = f"SELECT delay, route_id FROM latenesses WHERE list_id > {timestamp - 3630};"
    routes = {}
    with con:
        data = con.execute(sql)
        for row in data:
            route_id = row[1]
            if route_id not in routes:
                routes[route_id] = []
            routes[route_id].append(row[0])

    all = []
    for route in routes:
        all.append([routes_static[route][0], sum(routes[route]) / len(routes[route]),
                    f"color: {routes_static[route][2]}",
                    f"{routes_static[route][1]}"
                    ])
    sorted_data = sorted(all, key=lambda x: x[1])
    result = [sorted_data[0:10], sorted_data[-11:-1]]
    result[1].reverse()
    
    #convert bottom into minutes
    for i in range (0, len(result[1])):
        result[1][i][1] = result[1][i][1]/60

    return result
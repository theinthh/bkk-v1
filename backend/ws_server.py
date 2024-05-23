import asyncio
import datetime
import json
import sys
import time

from aiohttp import web
from loguru import logger

import db.main as db

logger.remove()
logger.add(sys.stderr, level="DEBUG")
logger.add("bkk.log", rotation="500 MB")
logger.info(f"{__file__} loaded")

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async def send_data_periodically():
        while True:
            data = {
                "timestamp": datetime.datetime.now().isoformat(),
                "currentLateness": db.get_latest_lateness(),
                "histogram": db.get_histogram_data(),
                "histogram_pred": db.get_histogram_pred_data(),
                "histogram_n": db.get_histogram_data_n(),
                "histogram_pred_n": db.get_histogram_pred_data_n(),
                "topbottom": db.get_top_bottom(),
                "scatter": db.get_scatter_data(),
                }
            await ws.send_str(json.dumps(data))
            await asyncio.sleep(60)

    asyncio.create_task(send_data_periodically())

    async for msg in ws:
        print(msg.data)
        if msg.type == web.WSMsgType.TEXT:
            await ws.send_str("Message received: " + msg.data)
        elif msg.type == web.WSMsgType.ERROR:
            print(f'WebSocket connection closed with exception: {ws.exception()}')
    return ws

def start_server(port = 61354):
    app = web.Application()
    app.router.add_get('/ws', websocket_handler)
    web.run_app(app, port=port)
    pass


if __name__ == "__main__":
    logger.info("Running in stand-alone")
    start_server()
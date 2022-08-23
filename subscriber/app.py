import asyncio
from contextlib import AsyncExitStack, asynccontextmanager
from datetime import datetime
from random import randrange
from asyncio_mqtt import Client, MqttError
import os
import json
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

load_dotenv()

MQTT_HOST = os.environ.get("MQTT_HOST")
MQTT_PORT = os.environ.get("MQTT_PORT")
MQTT_TOPIC = os.environ.get("MQTT_TOPIC")
DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, echo=True)


async def start():
    async with Client(MQTT_HOST) as client:
        async with client.filtered_messages(MQTT_TOPIC) as messages:
            await client.subscribe(MQTT_TOPIC)
            async for message in messages:
                stock = json.loads(message.payload.decode())
                print(stock)
                data = {"stock_id": stock["stock_id"],
                        "name": stock["name"],
                        "price": int(stock["price"]),
                        "availability": int(stock["availability"]),
                        "timestamp": datetime.fromisoformat(stock["timestamp"])}
                try:
                    async with engine.begin() as conn:
                        await conn.execute(text("""INSERT INTO stock_events (stock_id,name,price, availability, timestamp) VALUES (:stock_id,:name,:price,:availability,:timestamp)"""),
                                           data)
                    await engine.dispose()
                except Exception as e:
                    print(e)


async def main():
    reconnect_interval = 3  # [seconds]
    print("Connecting to broker")
    while True:
        try:
            await start()
        except MqttError as error:
            print(
                f'Error "{error}". Reconnecting in {reconnect_interval} seconds.')
        finally:
            await asyncio.sleep(reconnect_interval)


asyncio.run(main())

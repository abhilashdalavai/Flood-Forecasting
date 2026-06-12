# app/realtime/mqtt_listener.py

import json
import threading
import paho.mqtt.client as mqtt
from flask import current_app
from app.realtime.stream_processor import process_stream


MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "weather/station"


def on_connect(client, userdata, flags, rc):
    current_app.logger.info("MQTT Connected")
    client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    process_stream(payload)


def start_mqtt_listener(app):
    """
    Run MQTT listener in background thread
    """

    def run():
        with app.app_context():
            client = mqtt.Client()
            client.on_connect = on_connect
            client.on_message = on_message

            client.connect(MQTT_BROKER, MQTT_PORT, 60)
            client.loop_forever()

    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()

    app.logger.info("MQTT Listener Started")
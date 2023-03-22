import paho.mqtt.client as paho
from repeat_timer import RepeatedTimer

def heart_beat(mqtt_client: paho.Client(), topic: str):
    heart_beat_topic = topic + "/heartbeat"
    mqtt_client.publish(heart_beat_topic, "on")

topic = "RoverAction/rover0"
client = paho.Client()
client.connect("test.mosquitto.org")


repeat_timer = RepeatedTimer(10, heart_beat, client, topic)
client.loop_forever()
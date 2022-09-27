import argparse
from datetime import datetime
from rover_mqtt_client import RoverMqttClientSubscriber
from mbot_move import parseJSON
import json

def begin():
    arguments = get_arguments()
    
    if arguments.config is not None:
        with open(arguments.config) as f:
            config = json.load(f)
    else:
        raise Exception("Missing config")

    if not config["mqtt_server_ip"] or not len(config["mqtt_server_ip"]):
        raise Exception("Invalid config -- missing server ip")

    username = config["username"]
    passwd = config["password"]
    host = config["mqtt_server_ip"]
    topic = config["mqtt_topic"]

    mqtt_client_subscriber = RoverMqttClientSubscriber(username, passwd, host, on_message, topic)

    print("start listening to message")
    mqtt_client_subscriber.start()
   
def on_message(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))
    parseJSON(message.payload.decode("utf-8"))
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)	
    print("----------------")

def get_arguments():
    parser = argparse.ArgumentParser(description='Mbot4STEM start up arguments:')
    parser.add_argument('-c', '--config', required=True)

    return parser.parse_args()

if __name__ == "__main__":
    begin()

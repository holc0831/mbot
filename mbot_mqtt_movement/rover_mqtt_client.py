import paho.mqtt.client as paho

class RoverMqttClientSubscriber():
    def __init__(self, username, passwd, host, on_message_callback, topic):
        self.username = username
        self.passwd = passwd
        self.host = host
        self.client = paho.Client()

#         self.client.username_pw_set(self.username, self.passwd)
        self.client.connect(host)
        self.client.on_message = on_message_callback
        self.client.subscribe(topic, 2)

    
    def start(self):
        self.client.loop_forever()
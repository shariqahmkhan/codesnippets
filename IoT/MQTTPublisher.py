import paho.mqtt.client as mqt
c = mqt.Client()
c.connect("broker.hivemq.com",1883)
c.publish("joinee", "hi! we are glad to have you on board", retain = True)
#c.disconnect() this does not let command to be send and before that the program disconnects

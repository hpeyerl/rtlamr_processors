import sys
import json
import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while 1:
    try:
        line = sys.stdin.readline()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        break

    if not line:
        break

    rec = json.loads(line)
    print("Time: {0} Meter ID: {1} Consumption: {2}".format(rec["Time"], rec["Message"]["ID"], rec["Message"]["Consumption"]))
    v = rec["Message"]
    topic = "{0}/vol".format(v["ID"])
    pay = "{0}".format(v["Consumption"])
    print("Publishing: {0} : {1}".format(topic,pay))
    try:
        client.publish(topic, payload=pay, retain=False)
    except:
        print("An error or some sort.")
    time.sleep(1)

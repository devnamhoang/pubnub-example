import os
import time

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener


# this will print out the subscription status to console
class Listener(SubscribeListener):
    def status(self, pubnub, status):
        print(f'Status: \n{status.category.name}')


# here we create configuration for our pubnub instance
config = PNConfiguration()
config.subscribe_key = 'demo'
config.publish_key = 'demo'
config.user_id = 'example'
config.enable_subscribe = True
config.daemon = True

pubnub = PubNub(config)
pubnub.add_listener(Listener())

subscription = pubnub.channel('example').subscription()
subscription.on_message = lambda message: print(f'Message from {message.publisher}: {message.message}')
subscription.subscribe()

time.sleep(1)
publish_result = pubnub.publish().channel("example").message("Hello from PubNub Python SDK").sync()

time.sleep(3)

pubnub.stop()
time.sleep(1)
print('Bye.')
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
from kafka import SimpleProducer, KafkaClient
from datetime import datetime

#Create Variable contain user credentials to access twtter API
ACCESS_TOKEN ="200845625-sgsxvWTgRq8ysOSIAIwSOgB2A5qXWg8RxVYEoN3H"
ACCESS_TOKEN_SECRET ="Shbr0rY0JsQJqJKellTBsTBJFfDqP7qfuXUIYNnFADluO"
CONSUMER_KEY ="A2uY5HdVOBcc0S6tz7kiexX5k"
CONSUMER_SECRET ="trU5jfOMJXGbpgKLlWU9vl6e1unhVimN9X726zsPLhjw1Z4Thw"


topicName = 'YashawantParab07'                   #YashawantParab07 need to call in brojer in kafk

print('\nStart time of program: ', datetime.now().strftime("%c"))

class StdOutListener(StreamListener):
    def on_data(self, data):
        if (time.time() - self.start_time) < self.limit:
            producer.send_messages(topicName, data.encode('utf-8'))
#            print (data)
            return True
        else:
            print
            return False
        
    def on_error(self, status):
        print (status)
    
    def __init__(self, time_limit=5):     # SPECIFY THE TIME IN SECONDS
        self.start_time = time.time()
        self.limit = time_limit
        super(StdOutListener, self).__init__()

kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
l = StdOutListener()
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
stream = Stream(auth, l)
stream.sample()

print('\nDone processing at: ', datetime.now().strftime("%c"))
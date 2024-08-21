from mrjob.job import MRJob
from datetime import datetime
import csv
# import logging
# logging.basicConfig(filename='mapper.log', level=logging.INFO)

class MapReduce3(MRJob):
    def mapper(self, _, line):
        tweets_reader = csv.reader([line])
        tweets = list(tweets_reader)

        for tweet in tweets:

            text_lower = tweet[2].lower()  
            createdAt =  datetime.strptime(tweet[0], "%Y-%m-%d %H:%M:%S")

            lat = None
            long = None

            if tweet[13] != '':
                lat = float(tweet[13])

            if tweet[14] != '':
                long = float(tweet[14])
            

            bothCandidate = 0
            biden = 0
            trump = 0

            if "donald trump" in text_lower and "joe biden" in text_lower:
                bothCandidate = 1

            elif "donald trump" in text_lower:
                 trump = 1

            elif "joe biden" in text_lower:
                biden = 1

            if  9 <= createdAt.hour <= 17 and long != None and lat != None:
                if 40.4772 < lat < 45.0153 and -79.7624 < long <-71.7517:
                    yield 'New York', (bothCandidate, biden, trump, 1)

                if 32.5121 < lat < 42.0126 and -124.6509 < long <-114.1315:
                    yield 'California', (bothCandidate, biden, trump, 1)



    def reducer(self, key, values):
        bt, b, t, total = zip(*values)
        count_bt = sum(bt)
        count_b = sum(b)
        count_t = sum(t)
        total_num = sum(total)
        
        yield key, (count_bt/total_num, count_b/total_num, count_t/total_num, total_num)

if __name__ == '__main__':
    MapReduce3.run()        

from mrjob.job import MRJob
from datetime import datetime
import csv
# import logging


# logging.basicConfig(filename='mapper.log', level=logging.INFO)

class MapReduce2(MRJob):
    def mapper(self, _, line):
        tweets_reader = csv.reader([line])
        tweets = list(tweets_reader)

        for tweet in tweets:

            text_lower = tweet[2].lower()  
            state = tweet[18]
            createdAt =  datetime.strptime(tweet[0], "%Y-%m-%d %H:%M:%S")

            states = ['New York', 'Texas', 'California', 'Florida']

            bothCandidate = 0
            biden = 0
            trump = 0


            if state in states and  9 <= createdAt.hour <= 17:
                if "donald trump" in text_lower and "joe biden" in text_lower:
                    bothCandidate = 1

                elif "donald trump" in text_lower:
                    trump = 1

                elif "joe biden" in text_lower:
                    biden = 1
                yield state, (bothCandidate, biden, trump, 1)
                

    def reducer(self, key, values):
        bt, b, t, total = zip(*values)
        count_bt = sum(bt)
        count_b = sum(b)
        count_t = sum(t)
        total_num = sum(total)
        
        yield key, (count_bt/total_num, count_b/total_num, count_t/total_num, total_num)

if __name__ == '__main__':
    MapReduce2.run()        
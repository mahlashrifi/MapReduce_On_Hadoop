from mrjob.job import MRJob
import csv
# import logging


# logging.basicConfig(filename='mapper.log', level=logging.INFO)

class MapReduce1(MRJob):
    def mapper(self, _, line):

        tweets_reader = csv.reader([line])
        tweets = list(tweets_reader)
    

        for tweet in tweets:
            text_lower = tweet[2].lower()  
            webApp = 0
            iphone = 0
            android = 0
            source = tweet[5]
         
            if source == "Twitter Web App":
                webApp = 1
            elif source == "Twitter for iPhone":
                iphone = 1
            elif source == "Twitter for Android":
                android = 1
           
            num_likes = float(tweet[3])
            num_retweets = float(tweet[4])

            if "donald trump" in text_lower and "joe biden" in text_lower:
                yield "Both Candidate", (num_likes, num_retweets, webApp, iphone, android)  

            elif "donald trump" in text_lower:
                yield "Donald Trump", (num_likes, num_retweets, webApp, iphone, android)

            elif "joe biden" in text_lower:
                yield "Joe Biden", (num_likes, num_retweets, webApp, iphone, android)

    def reducer(self, key, values):
        likes, retweets, webApps, iphones, androids = zip(*values)

        count_likes = sum(likes)
        count_retweets = sum(retweets)
        count_webApp = sum(webApps)
        count_iphone = sum(iphones)
        count_android = sum(androids)
        
        yield key, (count_likes, count_retweets, count_webApp, count_iphone, count_android)

if __name__ == '__main__':
    MapReduce1.run()
      
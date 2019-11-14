#pip install twitterscraper

from twitterscraper import query_tweets
import pandas as pd
from multiprocessing import Pool
#from IPython.display import display
import sys
import datetime as dt
from datetime import timedelta
import time
import sys, os
import subprocess
import multiprocessing


def get_twitter_info(twitter_query):
    tweets =  query_tweets(twitter_query['query'],limit=twitter_query['limit'],begindate=twitter_query['startDate'],enddate=twitter_query['endDate'],poolsize=20,lang=twitter_query['language'])
    return pd.DataFrame(t.__dict__ for t in tweets).head(twitter_query['limit'])

def main():
    queries = [
        {'query': 'New Orleans', 'startDate':  dt.date(2019, 11, 6), 'endDate': dt.date(2019, 11, 9), 'language': 'english', 'limit': 1000 },
        {'query': 'elonmusk', 'startDate':  dt.date(2019, 11, 6), 'endDate': dt.date(2019, 11, 9), 'language': 'english', 'limit': 1000 }
    ]


    pool_size = len(queries)
    if pool_size < 8:
        pool = Pool(pool_size)
    else:
        pool = Pool(8)

    for info in pool.map(get_twitter_info, queries):
        print(info.to_string())
        print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))


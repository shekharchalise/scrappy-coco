from twitterscraper import query_tweets
import pandas as pd
from multiprocessing import Pool
import sys
import datetime as dt
from datetime import timedelta
import time


def get_twitter_info(twitter_query):
    tweets =  query_tweets(twitter_query['query'],limit=twitter_query['limit'],begindate=twitter_query['startDate'],enddate=twitter_query['endDate'],poolsize=20,lang=twitter_query['language'])
    return pd.DataFrame(t.__dict__ for t in tweets).head(twitter_query['limit'])

def dateSplitter(queries):
  dates = []
  for u in queries:
    end = u['endDate']
    start = u['startDate']
    timeDiff = end - start
    no_of_threads = timeDiff.days
    if (no_of_threads > 1):
      for i in range (no_of_threads):
        dates.append({'query': u['query'] , 'startDate': start + timedelta(days=i), 'endDate': start + timedelta(days=i+1), 'language':  u['language'], 'limit': int(u['limit']/no_of_threads) })
    else:
      dates.append({'query': u['query'] , 'startDate': start, 'endDate': end, 'language':  u['language'], 'limit': u['limit'] })
  return dates


def main():
    threads = 8
    queries = [
        {'query': 'New Orleans', 'startDate': dt.date(2019, 11, 6), 'endDate': dt.date(2019, 11, 9), 'language': 'english', 'limit': 1000 },
        {'query': 'elonmusk', 'startDate': dt.date(2019, 11, 6), 'endDate': dt.date(2019, 11, 9), 'language': 'english', 'limit': 1000 }
    ]

    splittedQueries = dateSplitter(queries)
    print(splittedQueries)

    pool_size = len(splittedQueries)
    if pool_size < threads:
        pool = Pool(pool_size)
    else:
        pool = Pool(threads)

    for info in pool.map(get_twitter_info, splittedQueries):
        print(info.to_string())
        print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    
    # processes = []
    # for i in range(1, 100):
    #     p = multiprocessing.Process(target=get_twitter_info, args=(queries))
    #     processes.append(p)
    #     p.start()

    # for process in processes:
    #     process.join()

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))





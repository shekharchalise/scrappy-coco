I utilized the python multithreading to complete my twitter scrapping. I used a third party library due to the search policy of the twiiter and OAuths. I had to go through all the docs and create an app for this purpose in twitter developers.

How to run it?

1: Install Twitter Scrapper - (sudo) pip3 install twitterscraper
2: Go to the folder where the files are located
3: To run serial implementation run - python3 scrappy_coco.py
4: To run parallel implementation run - python3 scrappr_coco_parallel.py



If you want to dig deeper into python multi-threading follow the link below.

https://docs.python.org/2/library/multiprocessing.html

Note:
* That the pool size depends on the number of queries. In my parallel implementation, I am dividing the dates into multiple days of queries to achieve more parallelism.
* For for example

users = [
          {'query': 'New Orleans', 'startDate': dt.date(2016, 11, 6), 'endDate': dt.date(2016, 11, 9), 'language': 'english', 'limit': 1000 },
          {'query': 'elonmusk', 'startDate': dt.date(2019, 11, 6), 'endDate': dt.date(2019, 11, 8), 'language': 'english', 'limit': 1000 }
]

Take the 2 above queries

This will be divided into multiple queries as below:
[{'query': 'New Orleans', 'startDate': datetime.date(2016, 11, 6), 'endDate': datetime.date(2016, 11, 7), 'language': 'english', 'limit': 333},
 {'query': 'New Orleans', 'startDate': datetime.date(2016, 11, 7), 'endDate': datetime.date(2016, 11, 8), 'language': 'english', 'limit': 333}, 
{'query': 'New Orleans', 'startDate': datetime.date(2016, 11, 8), 'endDate': datetime.date(2016, 11, 9), 'language': 'english', 'limit': 333},
 {'query': 'elonmusk', 'startDate': datetime.date(2019, 11, 6), 'endDate': datetime.date(2019, 11, 7), 'language': 'english', 'limit': 500},
 {'query': 'elonmusk', 'startDate': datetime.date(2019, 11, 7), 'endDate': datetime.date(2019, 11, 8), 'language': 'english', 'limit': 500}]

I wanted to divide the queries into hours now to achieve more parallism. But due to time limitations, I could only do days and there were some issues with twitter api not supporing microseconds so I ended up scrapping my code to just split the days. But I have to code to split the dateTime into multiple equal timeframes.(splitToEqualTimeFrame.py).










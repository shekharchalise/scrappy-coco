# code to split the datetime to multiple queries

import datetime
from dateutil import rrule
no_of_threads = 10
thread_start_end_dates = []
date_a = datetime.datetime(2019, 8, 10, 8, 24, 30, 993352)
date_b = datetime.datetime(2016, 8, 10, 6, 24, 30, 993358)
timeDiff = date_a.timestamp() - date_b.timestamp()
d = timeDiff/no_of_threads
for i in range(no_of_threads):
   start = date_b.timestamp() + (d * i)
   dt_start = datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S.%f')
   end = date_b.timestamp() + (d * (i+1))
   dt_end = datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S.%f')
   thread_start_end_dates.append([dt_start,dt_end])
# print the start/end dates
for i in range(len(thread_start_end_dates)):
   print("Thread "+str(i+1)+" start date: "+str(thread_start_end_dates[i][0]))
   print("Thread "+str(i+1)+"  end  date: "+str(thread_start_end_dates[i][1]))

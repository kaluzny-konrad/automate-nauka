import datetime
import time

ilosc_sekund = 5

time_delay = thousandDays = datetime.timedelta(seconds=ilosc_sekund)
start_time = datetime.datetime.now()
good_time = start_time + time_delay

while datetime.datetime.now() < good_time:
    print(f'Czekam już {(datetime.datetime.now()-start_time).seconds} sekund!')
    time.sleep(1)
print('Nareszcie gotowe')
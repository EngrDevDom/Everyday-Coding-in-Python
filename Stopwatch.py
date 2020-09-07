# Stopwatch.py

import time

print('Press ENTER to start the Stopwatch.')
print('Press ctrl+C to stop!')

while True:
    try:
        input()
        start_time = time.time()
        print('Stopwatch Started...!')
    except:
        print('Stopwatch Stopped!')
        end_time = time.time()
        print('Total time: ', round(end_time-start_time, 2), ' seconds.')
        break


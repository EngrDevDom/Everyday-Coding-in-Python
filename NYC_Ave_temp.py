# NYC_Ave_temp.py
'''
    A graph showing the average annual temperature of New York City
    during the years 2000-2012.
'''

from pylab import plot, show

nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
years = range(2000, 2013)
plot(years, nyc_temp, marker='o')
show()

# File  :   Date_convert.py
# Desc  :   Converts a date in form "mm/dd/yyyy" to "month day year"

def main():
    # get the date
    dateStr = input("Enter the date today (mm/dd/yyyy): ")

    # split into components
    monthStr, dayStr, yearStr = dateStr.split("/")
    
    # convert monthStr to month name'
    months = ["January,", "February", "March", "April",
                "May", "June", "July", "August",
                "September", "October", "November", "December"]

    month = int(monthStr)
    monthStr = months[month-1]

    # output result in month day, year format
    print("Today is:", monthStr, dayStr + ",", yearStr)

main()

'''
Enter the date today (mm/dd/yyyy): 09/07/2020
Today is: September 07, 2020
'''
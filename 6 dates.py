'''
There are no clear distinctions between mm/dd/yyyy or dd/mm/yyyy if dd and mm <= 12. 
This is dependedent on the format looped through first.
'''

from datetime import datetime

def parse_dates(txt_path):
    dates = []
    with open(txt_path, "r") as data: # insert txt_path here
        for row in data:
            date = row.split(',', 1)[0]
            for format in ('%Y/%m/%d', '%d/%m/%Y', '%d/%m/%Y', '%d/%b/%Y'):
                try:
                    dates.append(datetime.strptime(date, format))
                except ValueError:
                    continue
    if not dates:
        print('No dates in text file')
    else:
        return len(dates)

print('No. of dates = {}'.format(parse_dates(txt_path)))
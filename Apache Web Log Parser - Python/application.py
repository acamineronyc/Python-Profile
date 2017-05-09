import re
from collections import Counter
import csv

# This is an Apache Log Parser with Python and the data is exported to a CSV file.
# Select the titles you want to parse from the regular expression variable (regexp)

def reader(filename):

    regexp = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(.*)\] \"(\w{3,6}.* \w{0,4}/\d\.\d)\" (\d\d\d) (\d+)'

    with open(filename) as f:
        log = f.read()
        title_list = re.findall(regexp, log)
        return title_list

def count(title_list):

    count = Counter(title_list)
    return count

def write_csv(count):

    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        header = ['IP ADDRESS', 'TIME', 'REQUEST', 'STATUS', 'BODY BYTES', 'HTTP REFERER', 'USER AGENT', 'HTTP X FORWARD']
        writer.writerow(header)
        for item in count:
            writer.writerow((item, count[item]))


if __name__ == '__main__':

    write_csv(count(reader('weblog.log')))





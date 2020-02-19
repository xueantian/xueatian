#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-
# for self-exercise 
# email:xueatian@cisco.com


def main():
    import datetime
    date1 = datetime.datetime.today()
    hour1 = datetime.datetime.now()
    a = input('what is day is it today ?')
    print(a,'today is ' ,date1 , 'now time is ' ,hour1)
    print('Year is ',hour1.year)
    print('Month is ', hour1.month)
    print('Day is ', hour1.day)
    time_file = str(date1)+'.txt'
    myfile = open(time_file,'w')
    myfile.write(str(a))
    myfile.write('\n')
    myfile.write(str(hour1))

    #print( date1, 'hello')
if __name__ == '__main__':
    main()
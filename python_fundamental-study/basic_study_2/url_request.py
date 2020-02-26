#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-
# for self-exercise 
# email:xueatian@cisco.com


def main_urllib():

    from urllib import request
    with request.urlopen('https://www.google.com') as f:
        data = f.read()
        print('Status:',f.status,f.reason)

def main_requests():
    import requests
    r = requests.get('https://www.baidu.com')
    u = r.url
    print(u)

def cpu_status():
    import psutil
    for x in range(10):
      #  print(psutil.cpu_percent(interval=1,percpu=True))
        print(psutil.test())






if __name__ == '__main__':
    #main_requests()
    cpu_status()
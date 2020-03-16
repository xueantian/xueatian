#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-
# for self-exercise 
# email:xueatian@cisco.com


def main():
    import requests
    import ast

    url = 'http://deckofcardsapi.com/api/deck/new/'

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    a = response.json() # JSON 格式 能直接变成python 里面的Dict
    print(a)
    deck_id = a['deck_id']
    print(deck_id)
    for key,value in a.items():
        print(key,'\t',value)




if __name__ == '__main__':
    main()
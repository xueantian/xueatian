#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-
# for self-exercise 
# email:xueatian@cisco.com
import requests

def main():
    import requests
    import json
    url = "https://api.ciscospark.com/v1/messages"

    payload = {'text': 'Hello David!',
               'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vYmQ0NDNlZDAtNTg5MS0xMWVhLWEwMmEtNWQ4YjZiZjU4MmFj'}
    files = [

    ]
    headers = {
        'Authorization': 'Bearer MzIzNTBiMGEtOTI2YS00ZjYyLTkwZGMtMjM5YmJmNDJlYWUzOTQxMTUyNDYtOWM0_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload), files=files)

    print(response.text.encode('utf8'))


if __name__ == '__main__':
    main()
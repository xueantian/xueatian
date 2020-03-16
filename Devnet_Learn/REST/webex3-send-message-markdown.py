#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-
# for self-exercise 
# email:xueatian@cisco.com


def main():
    import requests
    token = "MGRlZmZjNDUtNTZiNC00NDk0LWE1MTMtMDMyOThhMDBiOTEwOWEwMGE2OTctNmVj_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
    roomId = "Y2lzY29zcGFyazovL3VzL1JPT00vYmQ0NDNlZDAtNTg5MS0xMWVhLWEwMmEtNWQ4YjZiZjU4MmFj"
    webex_content_type = 'application/json'

    url = "https://api.ciscospark.com/v1/messages"
    data = {"roomId":roomId,"text":"Hello good day!"}
    webex_header = {"Authorization":"Bearer "+token,"Content-type":webex_content_type}
    response=requests.post(url=url, json=data, headers=webex_header)
    messages = ["**Warning!!!**", "_Warning!!!_", "[Danger, Will !!!](https://en.wikipedia.org/wiki/Lost_in_Space#Catchphrases)"]
    for message in messages:
        data = {"roomId":roomId,"markdown":message}
        response=requests.post(url=url,json=data,headers=webex_header)
        print(response.text)
        print(response.status_code)


if __name__ == '__main__':
    main()
#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-
# for self-exercise 
# email:xueatian@cisco.com

def environment_Here():

    SDWAN_IP1 = "10.10.30.190"
    SDWAN_USERNAME = "admin"
    SDWAN_PASSWORD = "admin"
    return SDWAN_IP1, SDWAN_USERNAME, SDWAN_PASSWORD

def main():
    import requests
    import sys
    import json
    import click
    #import environment
    #import tabulate
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    SDWAN_USERNAME = environment_Here()
    SDWAN_IP = environment_Here()

    SDWAN_PASSWORD = environment_Here()

    if SDWAN_IP is None or SDWAN_USERNAME is None or SDWAN_PASSWORD is None:
        print("CISCO SDWAN details must be set via environment variables before running.")
        print("   export SDWAN_IP=10.10.30.190")
        print("   export SDWAN_USERNAME=admin")
        print("   export SDWAN_PASSWORD=admin")
        print("")
        exit("1")
    else:
        print("Login Successfull")



if __name__ == '__main__':

    main()
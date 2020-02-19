#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-
# for self-exercise 
# email:xueatian@cisco.com


def main():

    import os
    file_name = []
    filelist = os.listdir(os.getcwd())

    for files in filelist:
        if os.path.isfile(files):
            for file_line in open(files):
                if 'world' in file_line:
                    file_name.append(files) #insert file to file_name
    print('World is on here!:')
    for files in file_name:
        print(files, end ='\n')
        print(files, file=open('456.txt','w'))


    print('hello world')





if __name__ == '__main__':
    main()
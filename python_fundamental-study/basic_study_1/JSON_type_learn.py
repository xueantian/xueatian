#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-
# for self-exercise 
# email:xueatian@cisco.com


def main():
    import json
    from source_db import bookname,number

    print('trasfer python dict to JSON file')
    with open('json_bookname.json', 'w', encoding='utf-8') as f:
        json.dump(bookname,f,ensure_ascii=False)


    with open('json_number.json', 'w', encoding='utf-8') as f:
        json.dump(number, f, ensure_ascii=False)

if __name__ == '__main__':
    main()
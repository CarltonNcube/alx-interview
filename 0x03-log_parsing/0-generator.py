#!/usr/bin/python3
'''A script that generates random HTTP request logs.
'''
import random
import sys
import datetime
from time import sleep

for i in range(10000):
    ip_address = f"{random.randint(1, 255)}.{random.randint(1, 255)}." \
                 f"{random.randint(1, 255)}.{random.randint(1, 255)}"
    timestamp = datetime.datetime.now()
    url_path = '/projects/1216'
    http_protocol = 'HTTP/1.1'
    http_status_code = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    response_size = random.randint(1, 1024)

    log_line = "{ip} - [{timestamp}] \"GET {url_path} {protocol}\" " \
               "{status_code} {size}\n".format(
                   ip=ip_address,
                   timestamp=timestamp,
                   url_path=url_path,
                   protocol=http_protocol,
                   status_code=http_status_code,
                   size=response_size
               )

    sleep(random.random())
    sys.stdout.write(log_line)
    sys.stdout.flush()

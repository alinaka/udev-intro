#!/usr/bin/python3

import datetime

with open("connected.txt", "w") as f:
    f.write(datetime.datetime.now().isoformat())


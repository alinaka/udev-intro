#!/bin/bash

stty -F /dev/$1 115200 && echo "hello" > /dev/$1


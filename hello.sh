#!/bin/bash

stty 9600 < /dev/$1 && echo "hello" > /dev/$1


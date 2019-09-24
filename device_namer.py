#!/usr/bin/python3
import random
import sys

values = ("ttyHEADS", "ttyTAILS")
sys.stdout.write(f"{values[random.randint(0,1)]}")


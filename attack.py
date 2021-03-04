import random
import re
import sys
from hashlib import md5

"""Finds has collision"""

while True:
    guess = str(random.randint(0, sys.maxsize)).encode()
    if re.search(rb"'='", md5(guess).digest()):
        print(guess)
        break

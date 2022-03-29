from utils import say_halllo
import people
from people import name
say_halllo()
PN = name.names()

import os
#sports = open('print_names.txt', 'w')
#print(PN)
import skiing
import climbing
from skiing import Skiing
from climbing import Climbing

def error_handle():
    try:
        Skiing.equipment()
    except:
        print('no error')

error_handle()
#!/usr/bin/python3

from Producer import *
from random import randint

host = "http://mml.arces.unibo.it:8000/sparql"
update = "INSERT DATA { <http://ns#test1> <http://ns#test2> %s }"

kp = Producer(host)
kp.produce(update % str(randint(0,100))

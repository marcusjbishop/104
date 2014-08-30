#!/usr/bin/python
from random import randint
v=[0,0,0,0,0,0,0,0,0,0,0]
for x in range(200):
  y=randint(1,6)+randint(1,6)
  v[y-2]+=1
print v



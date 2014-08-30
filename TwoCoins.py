#!/usr/bin/python
from random import randint
hh=0
ht=0
tt=0
for x in range(200):
  y=randint(0,1)
  z=randint(0,1)
  if y==0 and z==0:
    hh+=1
  if y==0 and z==1 or y==1 and z==0:
    ht+=1
  if y==1 and z==1:
    tt+=1
print hh,ht,tt



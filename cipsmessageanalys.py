# -*- coding: utf-8 -*-

import os

def messageanalys(messageitself):
    b = messageitself +'333'
    return(messageitself,b)

a = '12345'
d = messageanalys(a)
print(d[-1])

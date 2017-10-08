# -*- coding: utf-8 -*-
import time,os
import random

from flask import Flask

ko=[0,2,5]

def vc():
    m=random.randint(0,2)
    e=ko[m]
    return e

app = Flask(__name__)


@app.route('/play')
def play():
    p=vc()
    return str(p)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
 

 

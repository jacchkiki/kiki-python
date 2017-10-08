# -*- coding: utf-8 -*-
import time,os
import random

from flask import Flask

k={"Scissors":"剪刀","stone":"石頭","cloth":"布"}
c=["Scissors","stone","cloth"]

def y():
    m=random.randint(0,2)
    e=c[m]
    f=k[e]
    return f

s=y()
print s

app = Flask(__name__)


@app.route('/play')
def play():
    p=y()
    return p


if __name__ == '__main__':
    app.run(host='0.0.0.0')
 

 

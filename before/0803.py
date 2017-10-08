# -*- coding: utf-8 -*-
import time,os
import random
from flask import Flask



mora1={"Scissors":"剪刀","stone":"石頭","cloth":"布"}

mora2=["Scissors","stone","cloth"]

def mora3():
    m=random.randint(0,2)
    c=mora2[m]
    d=mora1[c]
    return d




app = Flask(__name__) 


@app.route('/')
def hello():
    p=mora3()
    return p


if __name__ == '__main__':
    app.run(host='0.0.0.0')
 

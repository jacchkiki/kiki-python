# -*- coding: utf-8 -*-
import time,os
import random

from flask import Flask


dic={"Scissors":"剪刀","stone":"石頭","cloth":"布"}

direction={"up":"上","down":"下","left":"左","right":"右"}

bi=["up","down","left","right"]

bic=["Scissors","stone","cloth"]

def mora():
    m=random.randint(0,2)
    a=bic[m]
    b=dic[a]
    #vicky=["剪刀","石頭","布"]
    return b

def qr():
    m=random.randint(0,3)
    a=bi[m]
    b=direction[a]
    #vicky=["上","下","左","右"]
    return b


#g=mora()
#print g


app = Flask(__name__) 


@app.route('/play')
def play():
    p=mora()
    return p


if __name__ == '__main__':
    app.run(host='0.0.0.0')
 

 

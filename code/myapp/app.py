#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: bryn
"""
from jieba import cut 
from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)

@app.route('/success/<res>')
def success(res):
   return render_template('result.html', result=res)

@app.route('/text_seg',methods = ['POST', 'GET'])
def text_seg():
   if request.method == 'POST':
      text = request.form['text']
      text = ' | '.join(cut(text))
      return redirect(url_for('success',res = text))
   else:
      text = request.args.get('text')
      text = ' | '.join(cut(text))
      return redirect(url_for('success',res = text))

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug = True)

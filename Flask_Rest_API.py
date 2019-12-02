# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 01:46:54 2019

@author: sunny
"""


# Creating a Flask instance in main module or in the __init__.py 
from flask import Flask, jsonify, request 


#Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__) 
#the module is being run standalone by the user and we can do corresponding appropriate actions.


# Every Python module has it’s __name__ defined and if this is ‘__main__’, 
# It implies ort this script as a module in another script, the __name__ is set to the name of the script/module.

# Python files can act as either reusable modules, or as standalone programs.

@app.route('/', methods = ['GET', 'POST'])
def index():
    if (request.method =='POST'):
        some_json = request.get_json()
        return jsonify({'you snet' : 'some_json'}), 201
    else:
        return jsonify({'about' : 'HELLO BABE'})

@app.route('/multi/<int:num>', methods = ['GET'])
def get_multiply10(num):
    return jsonify({'result' : num*10 })
    
# if __name__ == “main”: is used to execute some code only if the file was run directly, and not imported.
if __name__ == '__main__':
    app.run(debug=True)

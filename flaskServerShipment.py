from flask import Flask,jsonify,json,request
from flask_cors import CORS, cross_origin
import base64
import io
from PIL import Image
import requests
import os
import ctypes
from tax import tax_returnVal
import clientpython
import random
## Init app

##def get_encoded_img(image_path):
##    img = Image.open(image_path, mode='r')
##    img_byte_arr = io.BytesIO()
##    img.save(img_byte_arr, format='PNG')
##    my_encoded_img = base64.encodebytes(img_byte_arr.getvalue()).decode('ascii')
##    return my_encoded_img

username=""
status=""
app = Flask(__name__)
CORS(app)

@app.route("/getRequest",methods=["POST"])
def getRequest():
    data = request.get_json()
    print(data)
    global username,status
    username = data["username"]
    status = "Order received"
    print("status",status)
    return jsonify({"status":"Order received"}),200

@app.route("/updateStatus",methods=["POST"])
def updateStatus():
    data = request.get_json()
    print(data)
    
    global status
    print(status)
    status=data['status']
    print(status)

    return jsonify({"status":data['status']}),200
@app.route("/getStatus")
def getStatus():
    global status
    print(status)
    return jsonify({"status":status}),200


if __name__ == '__main__':
    app.run(port=5001)


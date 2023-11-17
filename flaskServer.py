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

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="GreetingCardProject"
)

status=""

def anotherFun(image_path):
    encoded_string=""
    image_file = open(image_path, "rb")
    encoded_string = base64.b64encode(image_file.read()).decode('ascii')
    return encoded_string

app = Flask(__name__)
CORS(app)

@app.route("/getProduct")
def getProducts():
    data = request.get_json()
    mycursor = mydb.cursor()
    #mycursor2 = mydb.cursor()
    #data['code'] a list
    prnt("hi")
    mycursor.execute("SELECT * FROM Products where ProductCode =%s",data['code'])

    myresult = mycursor.fetchall()
    print(type(myresult))
    mycursor.close()
    data_li={}
    i=0
    for x in myresult:
        new_product_dict={}
        new_product_dict['BranchID']=x[1]
        new_product_dict['ProductCode']=x[2]
        new_product_dict['ProductTitle']=x[3] 
        new_product_dict['ProductQuantity']=x[4]
        new_product_dict['ProductPrice']=x[5]
        new_product_dict['ProductDescription']=x[6]
        new_product_dict['Category']=x[7]
        new_product_dict['Color']=x[8] 
        new_product_dict['Width_cm']=x[9]
        new_product_dict['Height_cm']=x[10]
        new_product_dict['Type']=x[11]
        data_li[int(i)]=new_product_dict
        i=i+1
    response_data = {"image": list_Images,"len":len(list_Images),"products":data_li,"file_names":list_names}
##    response = app.response_class(
##        response=json.dumps(response_data),
##        status=200,
##        mimetype='application/json'
##    )
##    return response
    print(response_data['file_names'])
    return jsonify(response_data)  
    
@app.route("/login",methods=["POST"])
def loginAuthenticate():
    data = request.get_json()
    print(data)
    mycursor = mydb.cursor()
    #mycursor2 = mydb.cursor()
    mycursor.execute("SELECT password FROM credentials where username = %s",(data['username'],))

    myresult = mycursor.fetchone()
    
    print(myresult)
    mycursor.close()
    if myresult==None:
        messe="no such account found. Please register"
    else:
        if data['password'] == myresult[0]:
            messe="successfull"
        else:
            messe="wrong password"
    messag={"status":messe}
    
    return jsonify(messag),200
    
@app.route("/register",methods=["POST"])
def registerAuthenticate():
    data = request.get_json()
    print(data)
    
    try:
        mycursor = mydb.cursor()
        #mycursor2 = mydb.cursor()
        val = mycursor.execute("Insert into credentials values(%s,%s)",(data['username'],data['password']))
        mydb.commit()
        print(val)
        mycursor.close()
        messe="successful"
    
    except Exception:
        messe="Some Problem Occcured. Couldn't Register"
    finally:
        messag={"status":messe}
    
    return jsonify(messag),200
@app.route("/getProfile",methods=["POST"])
def getProfi():
    data = request.get_json()
    print("data",data)
    mycursor = mydb.cursor()
    mycursor.execute("select roomNo,buidlingStreet,city,states,pincode from customerAddress where username = %s",(data['username'],))
    val1 = mycursor.fetchall()
    print(val1)
    mycursor.execute("select * from credentials where username = %s",(data['username'],))
    val2 = mycursor.fetchone()
    print(val2)
    #val=[]type(val1)
    print(type(val1))
    

    send_data={"credentials":(),"addresses":[]}
    send_data['credentials'] = val2
    if isinstance(val1,list):
        #multiple addresses
        send_data['addresses']=val1
    else:
        send_data['addresses']=[val1]
    print(send_data)
    mycursor.close()
    return jsonify(send_data),200  
    
@app.route("/updateProfile",methods=["POST"])
def updateProfi():
    data = request.get_json()
    print("data",data)
    try:
        mycursor = mydb.cursor()
        mycursor.execute("update credentials set username = %s,password = %s where username = %s",\
                         (data['username'],data['password'],data['username']))
        mydb.commit()
        #mycursor.execute("update credentials set username = %s where password = %s",(data['username'],data['password']))
        #mydb.commit()
        mycursor.close()
        m="success"
    except Exception:
        print(Exception)
        print("excpetion occured")
        m="not updated data"
        
    return jsonify({"status":m}),200  
     
@app.route("/saveAddress",methods=["POST"])
def saveAddress():
    data = request.get_json()
    print("data",data)
    try:
        mycursor = mydb.cursor()
        mycursor.execute("insert into customerAddress values(%s,%s,%s,%s,%s,%s)",
                         (data['username'],data['roomNo'],data['buidlingStreet'],data['city'],data['state'],data['pincode']))
        mydb.commit()
        mycursor.close()

        m="success"
    except Exception:
        print("exception occured")
        m="sorry, couldn't save address" 
        
    return jsonify({"status":m}),200



@app.route("/updateAddress",methods=["POST"])
def updateAddress():
    data = request.get_json()
    print("data",data)
    
    try:
        mycursor = mydb.cursor()
        mycursor.execute("update customerAddress set roomNo = %s,buidlingStreet = %s,city = %s,states = %s,pincode = %s where roomNo = %s and buidlingStreet = %s and city = %s and states = %s and pincode =%s",
                         (data['roomNo'],data['buidlingStreet'],data['city'],data['state'],data['pincode'],data['old_roomNo'],data['old_buidlingStreet'],data['old_city'],data['old_state'],data['old_pincode']))
        
        mydb.commit()
        mycursor.close()

        m="success"
    except Exception:
        print("exception occured")
        m="sorry, couldn't save address"
    return jsonify(m),200

@app.route("/getTax",methods=["POST"])
def getTax():
    tax=tax_returnVal()
    print(tax)
    data = request.get_json()
    print("data",data)
    #if data['state'] == 'maharashtra':
    tax_amt = (data['Amount']*tax)/100
    print(tax_amt)
    return jsonify({"tax":tax,"tax_amt":tax_amt}),200
    
    


    
@app.route("/applyMember")
def applyMember():
    path = os.getcwd()
    clibrary = ctypes.CDLL('D:/EAI/CFiles/readfile.so')
      
    clibrary.main.restype = ctypes.POINTER(ctypes.c_char)
    #x = ctypes.POINTER(ctypes.POINTER(ctypes.c_char))
    x = clibrary.main()
    print(x)
    print("-")
    new_list = []
    for i in range(1,130):
        new_list.append(x[i].decode())
    print(new_list)
    val=""
    new=[]
    for i in new_list:
        if i!="\n":
            val=val+i
        else:
            new.append(val)
            val=""
    print(new)
    offers=[]
    for i in range(1,len(new)):
        offers.append(new[i].split(","))
    print(offers)
    offers_dict_li=[]
    for j in offers:
        new_di={}
        new_di["Plan_Name"] = j[0]
        new_di["Monthly_Amount"] =j[1]
        new_di["Yearly_Amount"]=j[2]
        new_di["Offers"]=j[3]
        offers_dict_li.append(new_di)
        
    print(offers_dict_li)
    return jsonify(offers_dict_li),200

@app.route("/getMemebershipDetails",methods=["POST"])
def getMebershipDetails():
    data = request.get_json()
    print("data",data)
    mycursor = mydb.cursor()
    mycursor.execute("select * from customermembership where username = %s",(data['username'],))
    val1 = mycursor.fetchone()
    mycursor.close()
    print(val1)
    val_status = "success"
    if val1==None:
        val_status = "no membership found"
    print(val_status)
    return jsonify({"status":val_status,"data":val1}),200  
@app.route("/getProductsList",methods=["POST"])
def getProductsList():
    data = request.get_json()
    print("data",data)  
    
    
    product=[]
    pro_di={}
    #mycursor2 = mydb.cursor()
    for i in data['data']:
        print(i)
        mycursor = mydb.cursor()
        mycursor.execute("select ProductTitle,ProductPrice from Products where ProductCode = %s",(i,))
        val = mycursor.fetchone()
        product.append(val)
        pro_di[str(i)]=val
        #myresult = mycursor.fetchone()
        mycursor.close()


    
    return jsonify(pro_di),200    

@app.route("/getOffersCoupons",methods=["POST"])
def getOffersCoupons():
    offers_di = clientpython.getOffersCoupons()
    print(offers_di)
    data = request.get_json()
    print("data",data)
    applicOffers=[]
    mycursor = mydb.cursor()
    mycursor.execute("select membership from customermembership where username = %s",(data['username'],))
    val1 = mycursor.fetchone()
    mycursor.close()
    print(val1)
    for i in offers_di:
        if i['Patype'] ==data['paymentMethod']:
            if float(i['Min'])<=data['amount']:
                applicOffers.append(i)
        if i['Subscription'] ==val1[0]:
            if float(i['Min'])<=data['amount']:
                applicOffers.append(i)
        if float(i['Min'])<=data['amount']:
            applicOffers.append(i)
    print(applicOffers)
            
                
            
    
    
    return jsonify(applicOffers),200  

@app.route("/orderPlace",methods=["POST"])
def OrderPlace():
    data = request.get_json()
    print("data",data)
    no = str(random.randrange(100))
    global status
    res = requests.post("http://127.0.0.1:5001/getRequest",json={"username":data["username"]})
    status = res.json()
    
    
##    try:
##        mycursor = mydb.cursor()
##        mycursor.execute("insert into cart values(%s,%s,%s,%s,%s,%s)",
##                         (no,data['proCode'],data['proTitle'],data['Quan'],data['single'],data['total'],data['old_city'],data['old_state'],data['old_pincode']))
##        
##        mydb.commit()
##        mycursor.close()
##        
##        m="success"
##    except Exception:
##        print("exception occured")
##        m="sorry, couldn't save address"
    return jsonify({}),200   
@app.route("/trackOrder")
def trackOrder():
    
    
##    try:
##        mycursor = mydb.cursor()
##        mycursor.execute("insert into cart values(%s,%s,%s,%s,%s,%s)",
##                         (no,data['proCode'],data['proTitle'],data['Quan'],data['single'],data['total'],data['old_city'],data['old_state'],data['old_pincode']))
##        
##        mydb.commit()
##        mycursor.close()
##        
##        m="success"
##    except Exception:
##        print("exception occured")
##        m="sorry, couldn't save address"
    global status
    res = requests.get("http://127.0.0.1:5001/getStatus")
    status=res.json()
    print(status)
    return jsonify(status),200 
@app.route("/getImages")
def sendImages():
    # Get the list of all files and directories
    path = "D:\EAI\ImagesFolder"
    dir_list = os.listdir(path)
     
    print("Files and directories in '", path, "' :")
    list_Images=[]
    list_names=[]
    for i in dir_list:
        print(i)
        list_Images.append(anotherFun(path+"\\"+i))
        list_names.append(i.split(".")[0])

    mycursor = mydb.cursor()
    #mycursor2 = mydb.cursor()
    mycursor.execute("SELECT * FROM Products")

    myresult = mycursor.fetchall()
    print(type(myresult))
    mycursor.close()
    data_li={}
    i=0
    for x in myresult:
        new_product_dict={}
        new_product_dict['BranchID']=x[1]
        new_product_dict['ProductCode']=x[2]
        new_product_dict['ProductTitle']=x[3] 
        new_product_dict['ProductQuantity']=x[4]
        new_product_dict['ProductPrice']=x[5]
        new_product_dict['ProductDescription']=x[6]
        new_product_dict['Category']=x[7]
        new_product_dict['Color']=x[8] 
        new_product_dict['Width_cm']=x[9]
        new_product_dict['Height_cm']=x[10]
        new_product_dict['Type']=x[11]
        data_li[int(i)]=new_product_dict
        i=i+1
    response_data = {"image": list_Images,"len":len(list_Images),"products":data_li,"file_names":list_names}
##    response = app.response_class(
##        response=json.dumps(response_data),
##        status=200,
##        mimetype='application/json'
##    )
##    return response
    print(response_data['file_names'])
    return jsonify(response_data)  


##    img_path = 'assets/test.png'
##    with open('test.jpg', 'rb') as f:
##        im_b64 = base64.b64encode(f.read())
##
##    payload = {'id': '123', 'type': 'jpg', 'box': [0, 0, 100, 100], 'image': im_b64}

@app.route("/setShipment")
def setShipment():
    url = 'http://localhost:10000'
    myobj = {'pickup': 'somevalue','destination':'dsf'}

    x = requests.post(url, json = myobj)
    return jsonify({"a":"d"}),200
                      
@app.route("/shipmentDetails",methods=["Post"])
def shipmentDetails():
    print(request.get_json())
    return jsonify({"q":"d"}),200
    






if __name__ == '__main__':
    app.run(port=5000)


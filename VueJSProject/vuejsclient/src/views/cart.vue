<template>
  <div class="mainPage">
    <span v-if="show1=='first'">
    <table  class="table1" cellpadding="10" cellspacing="10" border="1">
      <tr>
        <th class="th1" style="background-color:green;color:white;">Product Title</th>
        <th class="th1" style="background-color:green;color:white;">Product Price</th>
        <th class="th1" style="background-color:green;color:white;">Product Quantity</th>
        <th class="th1" style="background-color:green;color:white;">Product Total Amount</th>
      </tr>
      <tr v-for="(index,recVal) in data" :key="recVal"><td class="td1">{{index[0]}}</td>
      <td class="td1">{{index[1]}}</td>
      <td class="td1">{{recCountVal[recVal]}}</td><td class="td1">{{index[1]*recCountVal[recVal]}}</td></tr>
      <tr>
        <th class="th1" style="background-color:rgb(190, 255, 190);" colspan="3">Total Amount</th>
        <td class="td1">{{sum}}</td>
      </tr>
        <tr>
        <th class="th1" style="background-color:rgb(190, 255, 190);" colspan="3">Tax</th>
        <td class="td1">{{tax['tax']}}%</td>
      </tr>
      <tr>
        <th class="th1" style="background-color:rgb(190, 255, 190);" colspan="3">TaxAmount</th>
        <td class="td1">{{tax['tax_amt']}}</td>
      </tr>
      <tr>
        <th class="th1" style="background-color:lightgreen;" colspan="3">Total Amount To Pay</th>
        <th class="th1">{{total}}</th>
      </tr>
    </table>
    <button @click="proceedCheckOut()" class="button1">checkOut</button>
</span>
<span v-if="show1=='second'">
  <div class="Address" style="align-text:center;">
    <p style="position:absolute;top:3%;font-size:21px;left:32%;"><b>Select Address for Delivery</b></p>
    <table class="table1" style="position:absolute;left:7%;top:26%;" cellpadding="10" cellspacing="10" border="1">
           <tr v-for="(val,index) in data2['addresses']" :key="index">
            <td class="td1"><input type="radio" @click="addressSave(val)" name="rdoAddress" ></td>
            <td class="td1">
                {{val[0]+","+val[1]+","+val[2]+","+val[3]+","+val[4]}}
               
                
            </td>
            
            </tr>
      </table>
  </div>
  <div class="Address" style="top:60%;height:33%;">
    <p style="position:absolute;top:1%;font-size:21px;left:34%;"><b>Select Payment method</b></p>
    <span style="position:absolute;top:33%;left:39%;"><input v-model="paymentMet" v-bind:value="'cash'" type="radio" name="rdoPay">Cash</span>
    <span style="position:absolute;top:48%;left:39%;"><input v-model="paymentMet"  v-bind:value="'card'" type="radio" name="rdoPay">Credit/Debit Card</span>
    <button class="button1"  style="position:absolute;left:36%;bottom:5%;" @click="paymentMethod()">Proceed to Payment</button>
  </div>
</span>
<span v-else-if="show1=='third'">
  <div class="Address" style="left:10%;height:79%; width:73%; overflow:scroll;"><p>Please Select a offer <i>(only one offer is applicable)</i></p>
    <button class="button1" @click="getOffers()">Get offers</button>
    <table v-if="showThird" class="table1" style="position:absolute;left:12%;top:26%;height:90%;" cellpadding="10" cellspacing="10" border="1">
           <tr v-for="(val,index) in offers" :key="index">
            <td class="td1"><button style="padding:7px;background-color:green;color:wheat;border:2px solid reen;" @click="offerSave(val)" >Apply</button></td>
            <td class="td1">
               <span v-if="val['Code']!='null'"> Code: {{val["Code"]}}</span>
                <span v-if="val['Gift']!='null'"> Gift: {{val['Gift']}}</span>
                  <span v-if="val['Min']!='null'"> Minimum Money: {{val['Min']}}</span>
                  <span v-if="val['Money']!='null'"> Money discounted: {{val['Money']}}</span>
                    <span v-if="val['Patype']!='null'"> Patype: {{val['Patype']}}</span>
               
                
            </td>
            
            </tr>
      </table>
  </div>
</span>
<span v-else-if="show1=='fourth'">
  <div style="position:absolute;overflow:scroll;height:100%;width:100%;">
  <table class="table1" style="top:10px;left:6%;width:90%;" cellpadding="10" cellspacing="10" border="1">
      <tr>
        <th class="th1" style="background-color:green;color:white;">Product Title</th>
        <th class="th1" style="background-color:green;color:white;">Product Price</th>
        <th class="th1" style="background-color:green;color:white;">Product Quantity</th>
        <th class="th1" style="background-color:green;color:white;">Product Total Amount</th>
      </tr>
      <tr v-for="(index,recVal) in data" :key="recVal"><td class="td1">{{index[0]}}</td>
      <td class="td1">{{index[1]}}</td>
      <td class="td1">{{recCountVal[recVal]}}</td><td class="td1"><span>+ </span>{{index[1]*recCountVal[recVal]}}</td></tr>
      <tr>
        <th class="th1" style="background-color:rgb(190, 255, 190);" colspan="3">Total Amount</th>
        <td class="td1"><span>= </span>{{sum}}</td>
      </tr>
        <tr>
        <th class="th1" style="background-color:rgb(190, 255, 190);" colspan="3">Tax</th>
        <td class="td1">{{tax['tax']}}%</td>
      </tr>
      <tr>
        <th class="th1" style="background-color:rgb(190, 255, 190);" colspan="3">TaxAmount</th>
        <td class="td1">{{"+ "+tax['tax_amt']}}</td>
      </tr>
      <tr>
        <th class="th1" style="background-color:rgb(190, 255, 190);" colspan="3">Total</th>
        <td class="td1"><span>= </span>{{parseInt(tax['tax_amt']+parseInt(sum))}}</td>
      </tr>
      <tr>
        <th class="th1" style="background-color:lightgreen;" colspan="3">Address</th>
        <td class="th1">{{address[0]+","+address[1]+","+address[2]+","+address[3]+","+address[4]}}</td>
      </tr>
      <tr>
        <th class="th1" style="background-color:lightgreen;" colspan="3">Offer Applied</th>
        <td class="th1">{{offerChoosen}}<p>{{"subtracted(-)"+offerChoosen['Money']}}</p></td>
      </tr>
      <tr>
        <th class="th1" style="background-color:lightgreen;" colspan="3">Total Amount To Pay</th>
        <th class="th1"><span>= </span>{{total}}</th>
      </tr>
            <tr>
        <th class="th1" style="background-color:lightgreen;" colspan="3">Payment Method</th>
        <td class="th1">{{paymentMet}}</td>
      </tr>
    </table>
    <button  @click="pay()" style="position:fixed;bottom:10px;background-color:green;width:10%;" class="button1">Pay</button>
  </div>
</span>

  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'cart',
      data() {                                   // <== changed this line
      return {
       img:[],
       names:[],
       oldIndex1:-3,
       oldIndex2:-2,
       oldIndex3:-1,
       data:{},
       recCountVal:{},total:0,
       show1:'first',
       sum:0,
       tax:{},
       data2:{"credentials":[],"addresses":[]},
       paymentMet:"",
       address:"",
       offers:[],
       offerChoosen:{},
       showThird:false,
       sendData:{}
      }
    },
    mounted(){
      var li =localStorage.getItem("Items");
      console.log(li)
      axios.post("http://127.0.0.1:5000/getProductsList",JSON.parse(li))
      .then((response)=>{console.log(response.data);
      this.data=response.data
      var items_li=JSON.parse(li)['data']
      for(var i=0;i<items_li.length;i++){
        if(this.recCountVal[items_li[i]]==undefined){
          this.recCountVal[items_li[i]]=0
          for(var j=0;j<items_li.length;j++){
            if(items_li[i] == items_li[j]){
              this.recCountVal[items_li[i]]=this.recCountVal[items_li[i]]+1
              console.log(this.recCountVal[items_li[i]])

            }
           
          }
          
        }
        console.log(this.recCountVal)

      }
              console.log("kk",this.data)
      console.log(this.data)
      this.sum=0
          for(const obj in this.data){
      console.log(this.data[obj],obj,this.recCountVal[obj])

      this.sum=this.sum+(this.recCountVal[obj]*this.data[obj][1])

      this.calTax();
    }
    console.log(this.sum)

      })
      .catch((error)=>{console.log(error)});
          
    




     
       
        
    
           
    },

          methods : {
 

            proceedCheckOut(){
              if(localStorage.getItem('user')){ 
                
                console.log(this.show1)
                axios.post("http://127.0.0.1:5000/getProfile",{"username":localStorage.getItem("user")})
                .then((response)=>{console.log(response.data);this.data2=response.data
                })
                .catch((error)=>{console.log(error)})
                

              }else{
                alert("You haven't logged in yet. \nPlease login")
                this.$router.push("/LoginRegister")
              }
              this.show1 ="second"
            },
            calTax(){
              axios.post("http://127.0.0.1:5000/getTax",{"Amount":this.sum}).then((response)=>{
                 this.tax= response.data
                 console.log(this.tax)
                 this.total = this.sum + this.tax['tax_amt']
              }).catch()
            },
            paymentMethod(){
              console.log("dd",this.paymentMet=="cash")
              if(this.paymentMet=="cash"){
                console.log(this.address,this.address.length)
                if(this.address.length!=0){
                this.show1="third"
                }else{
                  alert("please select address")
                }

              }else if(this.paymentMet=="card"){
                                if(this.address.length!=0){
                this.show1="third"
                }else{
                  alert("please select address")
                }

              }
            },
            addressSave(valAdd){
              
              this.address = valAdd
              console.log(this.address)

            },
            pay(){
              console.log(this.paymentMet)
              if (this.paymentMet=="cash"){
                //const date = new Date();
                  axios.post("http://127.0.0.1:5000/orderPlace",{'username':localStorage.getItem("user"),"address":this.address})
                .then((response)=>{console.log(response.data)})
                .catch()  

                          
                alert("order placed. Please tcak order in the track option of the profile")

              }else{
                    
              }

            },
            getOffers(){

              if(localStorage.getItem("user")){
              axios.post("http://127.0.0.1:5000/getOffersCoupons",{"paymentMethod":this.paymentMet,"amount":this.total,"username":localStorage.getItem("user")})
              .then((response)=>{
                console.log(response.data)
                this.offers =response.data
                this.showThird=true
              })
              .catch()
              }
            },
              offerSave(val){
                this.offerChoosen =val
                console.log(this.offerChoosen)
                this.total = this.total - this.offerChoosen['Money']
                this.show1 = "fourth"

                
              }
        }

}
</script>
<style scoped>
body,html{

  width:90%;
  height:90%;
  
}

.mainPage{
  position:absolute;
  top:5%;
  left:5%;
  width:90%;
  height:90%;
  background-color: transparent;
  box-shadow: 0px 0px 10px 2px grey;
}
img{
  height:50;
  width:50;
}
.table1{
  position: absolute;
  top:10%;
  left:27%;
  text-align: center;
    box-shadow: 0px 0px 10px 2px rgb(196, 196, 196);
  border:2px solid lightgreen;
  border-radius: 10px 10px ;
  background-color: white;
}

.td1,.th1{
  border:2px solid lightgreen;
  border-radius: 1px 10px;
}
.button1{
  position: absolute;
  bottom:3%;
  left:47%;
  border-radius: 10px 10px;
  background-color: white;
  padding:12px;
  color:black;
  border:2px solid lightgreen;
  font-size: 18px;
}
.button1:hover{
    background-color: rgb(30, 121, 30);
  color:rgb(255, 255, 255);
  border:2px solid lightgreen;
  box-shadow: 0px 0px 10px 2px grey;

}
.paymentMethod{
  position: absolute;
  bottom:30%;
  left:50%;
  height:29%;
  width:50%;
}
.Address{
  position: absolute;
  top:33px;
  width:50%;
  left:25%;
  height: 45%;
  align-content: center;
  background-image: linear-gradient(rgb(210, 255, 155),white,transparent,transparent,white,rgb(210, 255, 155));
 
  border-radius: 10px 10px;
  box-shadow: 0px 0px 10px 2px grey;
  text-align: center;
  font-size: 19px;
  
}

</style>
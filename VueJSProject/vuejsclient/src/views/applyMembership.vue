<template>
    <div class="Profile">
        <div v-if="show">
        <div class="profileEdit">
            <b>Choose Membership Type</b><br><br>
            <input type="radio" v-model="val" v-bind:value="'gold'"  name="membership" @change="amtPay()">gold
            <br>
            <input type="radio" v-model="val" v-bind:value="'silver'" name="membership" @change="amtPay()">silver
            <br><br>
            <div v-if="val"><input type="radio" v-model="val2" v-bind:value="'monthly'"  name="membershipDurat" @change="amtPay()">monthly
            <br>
            <input type="radio" v-model="val2" v-bind:value="'yearly'" name="membershipDurat" @change="amtPay()">yearly
            <br><br>
            <p><b>Amount to pay: </b>{{Amount}}</p>
            </div>
            <button @click="applyMem()">Apply for membership</button>
        </div>
                   <div class="profileEdit" style="position:absolute;width:63%;height:79%;background-color:hsl(102, 91%, 64%);left:32%;top:5%;overflow:scroll">
                <h2>Plan Information</h2>
                <div style="background-image:linear-gradient(white,lightyellow);padding:10px;margin:19px;box-shadow:0px 0px 10px 2px grey;" v-for="(value,index) in data" :key="index">
                 
                   <p><b>Plan_Name :</b> {{ value['Plan_Name']}}</p>
                   <p><b>Monthly_Amount :</b>  {{ value['Monthly_Amount']}}</p>
                   <p> <b>Yearly_Amount : </b> {{ value['Yearly_Amount']}}</p>
                   <p><b>Offers : </b> {{ value['Offers']}}</p>
                  
                </div>
            </div>
        </div>
        <div v-else>
            
            <p>Your applied Membership is as follows:</p>
            <p><b>Membership type: </b>{{userData[1]}}</p>
           <p><b>Date Applied: </b>{{userData[2]}}</p>
           <p> <b>Valid till: </b>{{userData[3]}}</p>
          
        
        </div>
                


    </div>
</template>
<script>
import axios from 'axios'

export default {
    data(){
        return{
           data:"",
           val:"",
           userData:"",
           val2:"",
           Amount:0,
           show:true
        }
    },
    methods:{
        showMembership(){
           console.log(this.val)
            axios.get("http://127.0.0.1:5000/applyMember")
            .then((response)=>{console.log(response.data);
            this.data=response.data
            for(var i=0;i<this.data.length;i++){
                this.data[i]['Plan_Name']
            }
            
            }).catch((error)=>{console.log(error)});
            
        },
        amtPay(){
          
                if(this.val2=="monthly"){
                   for(const obj in this.data){
                    if(this.data[obj]['Plan_Name']==this.val){
                                this.Amount =this.data[obj]['Monthly_Amount']
                    }
                    }

                } else if(this.val2=="yearly"){
                   for(const obj in this.data){
                    if(this.data[obj]['Plan_Name']==this.val){
                                this.Amount =this.data[obj]['Yearly_Amount']
                    }
                    }
                }
            
        },
        applyMem(){
            alert("you have applied for membership")
        }

    },
    mounted(){
        if(localStorage.getItem("user")){
        axios.post("http://127.0.0.1:5000/getMemebershipDetails",{"username":localStorage.getItem("user")})
        .then((response)=>{console.log(response.data);
        if(response.data['status']=="success"){
            this.userData=response.data['data']
            console.log(this.userData)
            this.show=false
            

        }else{
            //this.showMembership()
            this.show=true
 axios.get("http://127.0.0.1:5000/applyMember")
            .then((response)=>{console.log(response.data);
            this.data=response.data
            for(var i=0;i<this.data.length;i++){
                this.data[i]['Plan_Name']
            }
            
            }).catch((error)=>{console.log(error)});
            
        }
        
        }).catch((error)=>{console.log(error)})
        
        }
    }
}
</script>
<style scoped>
.Profile{
    position: absolute;
    text-align: center;
    left:5%;
    top:11%;
    width:89%;
    height:75%;
    background-image: linear-gradient(rgb(255, 254, 223),transparent,rgb(255, 250, 224));
    border: 2px solid wheat;
    font-size: 23px;
    color: black;

    text-shadow:  1px 1px rgb(255, 255, 255);

}
.profileEdit{
    position: absolute;
    top:21%;
    left:3%;
    background-color: hsl(102, 91%, 64%);
    padding: 20px;
    border-radius: 10px 10px;
    box-shadow: 0px 0px 9px 3px grey;

}
.address{
    position: absolute;
    top:20%;
    right:3%;
    padding: 10px;
    width: 55%;
    border-radius: 10px 10px;
    background-color: rgb(108, 223, 108);
    box-shadow: 0px 0px 9px 3px grey;


}
input{
    font-size:19px;
    border-radius: 10px 10px;
    border:2px solid green;
}
button{
    background-color: green;
    color: white;
    border:2px solid rgb(177, 240, 177);
    border-radius: 10px 10px;
    padding: 10px;
    font-size: 19px;

}
button:hover{
    background-color: rgb(5, 57, 5);
    border: 1px solid rgb(235, 255, 235);
    box-shadow: 0px 0px 9px 5px grey;
  

}
</style>
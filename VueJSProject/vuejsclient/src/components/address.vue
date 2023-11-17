<template>
<div class="address">
    <p>Please fill all the detailss</p>
    <label>Room No.</label>&nbsp;
     <input v-model="roomNo" type="text"><br>
     <label>Building/Street</label>&nbsp;
      <input v-model="buidlingStreet" type="text"><br>
      <label>City</label>&nbsp;
       <input v-model="city" type="text"><br>
       <label>State</label>&nbsp;
        <input v-model="state" type="text"><br>
        <label>Pincode</label>&nbsp;
    <input v-model="pincode" type="text"><br><br>
    <span v-if="msgToDo=='save'">
        <button @click="addressSave()">Save Address</button>
    </span>
    <span v-else-if="msgToDo=='update'">
        <button @click="addressUpdate()">Update Address</button>
    </span>

</div>
    
</template>
<script>
import axios from 'axios'

export default {
    name:"address",
    data(){
        return{
            roomNo:"",
            buidlingStreet:"",
            city:"",
            state:"",
            pincode:"",
            old_roomNo:"",
            old_buidlingStreet:"",
            old_city:"",
            old_state:"",
            old_pincode:""
        }
    },
    props:{
        msgToDo: String,
        val2:Array
    },
    mounted(){
        if(this.msgToDo == "update"){
            this.roomNo= this.val2[0],
             this.buidlingStreet=this.val2[1],
             this.city=this.val2[2],
             this.state=this.val2[3],
             this.pincode=this.val2[4]
        }
    },

    methods:{
        addressSave(){
            
            axios.post("http://127.0.0.1:5000/saveAddress",{"username":localStorage.getItem("user"),"roomNo":this.roomNo,"buidlingStreet":this.buidlingStreet,"city":this.city,"state":this.state,"pincode":this.pincode})
            .then((response)=>{
                if(response.data['status']=="success"){
                    alert("address successfully saved")
                }else{
                    alert(response.data['status'])
                }
            }).catch()

        },
    addressUpdate(){
        console.log(this.val2)
        
                    axios.post("http://127.0.0.1:5000/updateAddress",
                    {"roomNo":this.roomNo,"buidlingStreet":this.buidlingStreet,
                    "city":this.city,"state":this.state,"pincode":this.pincode,
                    "old_roomNo":this.val2[0],"old_buidlingStreet":this.val2[1],
                    "old_city":this.val2[2],"old_state":this.val2[3],"old_pincode":this.val2[4]})
            .then((response)=>{
                if(response.data['status']=="success"){
                    alert("address successfully saved")
                }else{
                    alert(response.data['status'])
                }
            }).catch()

        }
    }

        



    
}
</script>
<style scoped>
body,html{
    position: absolute;
    top:0px;left:0px;
     background-color: white;
    width:90%;
    height:90%;
    overflow: none;
}

.address{
    position: absolute;
    top:90px;
    left:0px;
    width:100%;
    height:100%;
    font-size:21px;
    color:black;
    overflow: none;

}
input{
    border-radius:10px 10px;
    font-size: 19px;
    border:2px solid green;
    padding:5px;
margin-top: 10px;
}
button{
    border-radius: 10px 10px;
    background-color: green;
    color:white;
    padding: 9px;
    font-size: 19px;
    border:2px solid lightgreen;

}
button:hover{
    background-color: white;
    box-shadow: 0px 0px 12px 2px grey;
    color: rgb(2, 33, 2);
    border:2px solid rgb(3, 37, 3);
}
</style>
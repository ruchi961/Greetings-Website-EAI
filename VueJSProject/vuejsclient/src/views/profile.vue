<template>
    <div class="Profile">
        <div class="profileEdit">
            <label>Username</label>&nbsp;&nbsp;&nbsp;<input v-model="data['credentials'][0]" type="text"><br>
        <label>Password</label>&nbsp;&nbsp;&nbsp;<input v-model="data['credentials'][1]" type="text"><br><br>
        <button @click="updateInfo()">Update Information</button>
        </div>
        <div v-if="addressShow" class="address">
            <table cellpadding="7" cellspacing="9">
                <tr>
           <th>Saved Addresses:</th>
           </tr>
           <tr v-for="(val,index) in data['addresses']" :key="index">
            <td>
                {{val[0]+","+val[1]+","+val[2]+","+val[3]+","+val[4]}}
               
                
            </td>
            <td><p> <button @click="addAddress('edit',index)">Edit</button></p></td>
            </tr>
            </table>
            <button @click="addAddress('add')">Add new Address</button>
            

        </div>
        <div class="address2" v-else>
           <span v-if="edit">
            <addressCom class="add" msgToDo="update" :val2="data['addresses'][indexValll]"></addressCom>
           </span>
           <span v-else>
           <addressCom class="add" msgToDo="save"></addressCom>
           </span>
           
        </div>

    </div>
</template>
<script>
import axios from 'axios'
import addressCom from "@/components/address.vue"
export default {
    data(){
        return{
           data:{"credentials":[],"addresses":[]},
           addressShow:true,
           edit:true,
           indexValll:0
        }
    },
    components:{
        addressCom

    },
 
       methods:{
        updateInfo(){
            if(this.data['credentials'][0]!="" || this.data['credentials'][1]!=""){
                if(this.data['credentials'][1].length>=9){
                
                axios.post("http://127.0.0.1:5000/updateProfile",{"username":this.data['credentials'][0],"password":this.data['credentials'][1]})
                .then((response)=>{console.log(response.data);
                if(response.data['status']=="success"){
                alert("credentials updated successfully")

                }else{
                alert(response.data['status'])
                }})
                .catch((error)=>{console.log(error)})
                }else{
                alert("Password must be of ataest length 9")
                }      
            }else{
                alert("username and password can't be empty.")
            }
        },
        addAddress(val,index){
            console.log(val,index)
             this.addressShow = false
             
              if(val=='add'){
           this.edit = false
            }else{
                this.indexValll=index
            }
        }

    },
    mounted(){
        axios.post("http://127.0.0.1:5000/getProfile",{"username":localStorage.getItem("user")}).then((response)=>{console.log(response.data);this.data=response.data}).catch((error)=>{console.log(error)})
        
    }
}
</script>
<style scoped>
.Profile{
    position: absolute;
    text-align: center;
    left:5%;
    top:14%;
    width:89%;
    height:75%;
    background-image: linear-gradient(rgb(255, 255, 205),transparent,white,transparent,rgb(255, 255, 205));
    border: 2px solid rgb(255, 255, 255);
    border-radius: 10px 10px;
    font-size: 23px;
    color: rgb(29, 64, 13);

    text-shadow:  1px 1px rgb(237, 237, 237);
    box-shadow: 0px 0px 13px 3px grey;

}
.profileEdit{
    position: absolute;
    top:21%;
    left:3%;
    background-image: linear-gradient(rgb(238, 255, 230),rgb(196, 255, 169),rgb(152, 255, 104),rgb(152, 255, 104),rgb(157, 245, 157));
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
    height:73%;
    border-radius: 10px 10px;
    background-image: linear-gradient(rgb(238, 255, 230),rgb(196, 255, 169),rgb(152, 255, 104),rgb(152, 255, 104),rgb(157, 245, 157));
    box-shadow: 0px 0px 9px 3px grey;
    overflow:scroll;

}
.address2{
    position: absolute;
    top:10%;
    right:3%;
    padding: 10px;
    width: 55%;
    height:79%;
    border-radius: 10px 10px;
    background-image: linear-gradient(rgb(238, 255, 230),rgb(196, 255, 169),rgb(152, 255, 104),rgb(152, 255, 104),rgb(157, 245, 157));
    box-shadow: 0px 0px 9px 3px grey;
    overflow:none;

}
input{
    font-size:19px;
    border-radius: 10px 10px;
    border:2px solid green;
    padding: 5px;
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
td{
    
    background-color:white;
    width:90%;height:10px;
    border:2px solid rgb(156, 231, 133);
    border-radius: 10px 10px;

}
.add{
    position: absolute;
   
    width:100%;
    top:0px;
    height:100%;
    background-image: linear-gradient(wheat,white);
    overflow: none;
}
</style>
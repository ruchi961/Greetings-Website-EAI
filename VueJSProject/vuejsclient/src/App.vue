<template>
  <div id="nav">
    <div class="top">

      <div class="links">
        <router-link to="/"><img id="cart" class="icons" src="../src/assets/home3.png" width=50 height=50></router-link> &nbsp;
       <router-link to="/cart"><img id="cart" class="icons" src="../src/assets/cart3.png" width=50 height=50></router-link>
       <span style="position:absolute;top:3px;left:110px;color:white;">{{cart_items}}</span> &nbsp;
       <router-link to="/LoginRegister"><img id="pro" class="icons" src="../src/assets/profile2.png" width=50 height=50></router-link> &nbsp;
       <img style="position:absolute;top:1px;left:221px;color:white;" class="icons" src="../src/assets/loc.png" width=50 height=50> &nbsp;
       
       <span class="locText">{{this.city}},
{{this.region}},
{{this.country}}</span>

    </div>
          <img class="logoo" src="../src/assets/logo.png" height=128 width=210>
    </div>
    <div class="bottom">
      
       <router-link to="/"></router-link> 
        <router-view/>   
</div>
    <!--<router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>-->

  </div>
</template>
<script>
import axios from 'axios'
export default {
 data() {
   return {
     city: '',
     region: '',
     country: '',
     errorMessage: '',
     cart_items:0,
   }
 },
 methods: {
  async getGeolocationInformation() {
     const API_KEY = '822f3dfcc43b46ba8dfc171e83c7c609';
     const API_URL = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + API_KEY;
     try {
       this.errorMessage = '';
  
       const apiResponse = await fetch(API_URL);
       const data = await apiResponse.json();
       const {city, country, region} = data;
       this.city = city;
       this.region = region;
       this.country = country;
     } catch (error) {
       this.errorMessage = error.message;
     }
   }
 },
 mounted() {
   this.getGeolocationInformation();
        if(localStorage.getItem('cartItems')){
  this.cart_items = parseInt(localStorage.getItem('cartItems'));
  console.log(this.cart_items)
}
  window.addEventListener('cartItems-key-localstorage-changed', (event) => {
    this.cart_items = event.detail.storage;
    
  });
  console.log(this.cart_items)
 }
}
</script>
<style scoped>
body{
 
}
#nav{
    position:absolute;
  top:0px;
  left:0px;
  width:100%;
  height:100%;
  
}
.top{
    position:fixed;
  top:0px;
  left:0px;
  width:100%;
  height:10%;
  background-image: url("../src/assets/top.png");
  background-color: rgb(255, 126, 66);
  box-shadow:0px 0px 3px 3px grey;
  z-index:2;
}
.bottom{
    position:absolute;
  top:10%;
  left:0px;
  width:100%;
  height:90%;
   background-image: url("../src/assets/back3.png");
   background-size: 100% 100%;

}
.links{
  position:absolute;
  right:1%;
  top:3px;
  width:36%;

  height:90%;
  vertical-align: center;
  border-radius:50px 50px;
  border:2px solid rgb(237, 237, 237);
 
  box-shadow: 0px 0px 2px 1px rgb(223, 223, 223);
}
a{
  font-size: 20px;
  color:rgb(6, 62, 13);
  
  position:relative;
  top:2px;
  left:20px;
  text-decoration: none;

}
.logoo{position: absolute;
top:9px;
  border:2px solid grey;
  border-radius:100px 100px;
  z-index:1;
  left:10px;
  box-shadow:0px 0px 3px 3px grey;
}
.icons{
    border:2px solid rgb(255, 255, 255);
  border-radius:100px 100px;
  z-index:1;
  
  


}
.locText{
  position: absolute;
  font-size:18px;
  color:rgb(201, 133, 16);
  text-shadow: 1px 1px grey;
  top:15%;
  left:46%;
  height:30%;
  width:48%;
  background-color:white;
  z-index:-1;
  border-radius: 50px 50px;
  text-align:center;
  padding:10px;
  
  

}
#pro:hover, #cart:hover{
  box-shadow: 0px 0px 5px 6px rgb(244, 255, 150);
  border:1px solid rgb(39, 39, 39);
}
</style>

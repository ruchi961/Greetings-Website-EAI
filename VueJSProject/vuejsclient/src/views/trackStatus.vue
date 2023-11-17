<template>
  <div class="track">
    <p style="position:absolute;top:21%;left:39%;padding:51px;background-color:lightgreen;box-shadow:0px 0px 10px 2px grey;font-size:19px;">Current Order status</p>
   <p style="position:absolute;top:56%;left:43%;padding:21px;background-color:white;box-shadow:0px 0px 10px 2px grey;font-size:19px;">{{status}}</p>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  data(){
    return{
        stat:"",
        status:""
    }
  },
  mounted(){
    axios.get("http://127.0.0.1:5000/trackOrder")
    .then((response)=>{this.status = response.data["status"]
    }).catch()


    
  }
}
</script>
<style scoped>
.track{
    position: absolute;
    top:20%;
    text-align:center;
    width:79%;
    height:69%;
    left:10%;
    background-color: transparent;
    border:2px solid grey;
    box-shadow: 0px 0px 12px 2px grey;
}
</style>
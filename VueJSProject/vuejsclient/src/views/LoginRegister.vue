<template>
  <div class="mainPage">
    <span v-if="logg">
    <div class="boxLR">
      <div class="head"><button @click="changeLog()" ref="login">Login</button>
        <button @click="changeReg()" ref="register">Register</button>
      </div>
      <div class="body">
        <div class="login" v-if="showLog==true">
          <br><br>
          <span>Email ID</span><br>
          <input v-model="username" type="email"><br><br>
          <span>Password</span><br>
          <input v-model="password" type="password"><br>
          <br><button class="buttLR"  @click="login()">Login</button>
        </div>
        <div class="register" v-if="showRe">        
          <br><br>
          <span>Email ID</span><br>
          <input v-model="username" type="email"><br><br>
          <span>Password</span><br>
          <input v-model="password" type="password"><br>
          <br><button class="buttLR" @click="register()">Register</button>
        </div>
      </div>
    </div>

    </span>
    <span v-else>

    
      <button class="options" @click="applyMembership()">Apply Membership</button><br>
      
      <button class="options" @click="trackStatus()">Track Order</button><br>
      <button class="options" @click="profilePage()">Edit Profile</button><br>
      <button class="options" @click="logout()">Log out</button>

   
    </span>
  </div>
</template>

<script>
import axios from'axios'
export default{
  data(){
    return{
      showLog:true,
      showRe:false,
      username:"",
      password:"",
      showProfileOptions:false,
      logg:true
    }
  },methods:{
    changeLog(){
      this.showLog=true
      this.showRe=false
      this.username=""
      this.password=""
      console.log(this.showPage)
    },
    changeReg(){
      this.showLog=false
      this.showRe=true
      this.username=""
      this.password=""

    },
    login(){
      if(this.username=="" || this.password==""){
        alert("Please enter all the credentials")
      }else{
      
      axios.post("http://127.0.0.1:5000/login",{'username':this.username,'password':this.password})
      .then((response)=>{
        console.log(response.data)
          if (response.data['status'] =="successfull"){
            this.showProfileOptions=true
            this.showLog=false
            this.showRe=false
            localStorage.setItem("user",this.username)
            this.logg=false

          }else{
            alert(response.data['status'])
          }

      })
      .catch((error)=>{console.log(error)})
      }

    },
    register(){
      if(this.username=="" || this.password==""){
        alert("Please enter all the credentials")
      }else{
      
      axios.post("http://127.0.0.1:5000/register",{'username':this.username,'password':this.password})
      .then((response)=>{
        console.log(response.data)
          if (response.data['status'] =="successful"){
alert("successfully registered. Please login to continue.")
      this.showLog=true
      this.showRe=false
      this.username=""
      this.password=""


          }else{
            alert(response.data['status'])
          }

      })
      .catch((error)=>{console.log(error)})
      }

    },
    logout(){
      localStorage.removeItem("user")
      alert("You have loged out successfully")
      this.$router.push("/")
      
    },
    profilePage(){
      this.$router.push("/profile")

    },
    applyMembership(){
           this.$router.push("/applyMembership");
    },
    trackStatus(){
      this.$router.push("/track");

    }

  },
  mounted(){
    this.$refs.login.focus()
    if(localStorage.getItem('user')){
      this.logg=false
}
  }
}
</script>
<style scoped>
.boxLR{
  position: absolute;
  top:21%;
  left:39%;
  text-align: center;
  font-size: 19px;
  padding:3%;
  border-radius:10px 10px;
  border:2px solid rgb(255, 217, 146);
  box-shadow: 0px 0px 19px 3px wheat;
  background-image: linear-gradient(white,transparent,lightyellow,lightyellow,white,transparent);

}
input{
  font-size: 19px;
  border-radius: 10px 10px;
  padding:7px;
  border:2px solid green;
}
input:focus{
  box-shadow: 0px 0px 9px 1px rgb(140, 140, 140);
  border: 2px solid rgb(68, 202, 68);
  outline: none;
}
button{
  font-size: 20px;
    padding:3%;
  border-radius:10px 10px;
  border:none;
  background-color: rgb(234, 255, 215);
  box-shadow: 0px 0px 19px 3px rgb(255, 239, 211);

}
.buttLR{
  border-radius:10px 10px;
  border:2px solid rgb(255, 217, 146);
  box-shadow: 0px 0px 19px 3px wheat;
}
button:hover{
    border:2px solid rgb(221, 255, 198);
  background-color: rgb(32, 60, 7);
  box-shadow: 0px 0px 19px 3px rgb(255, 239, 211);
  color:white;
}
button:focus{
      border:2px solid rgb(221, 255, 198);
  background-color: rgb(32, 60, 7);
  box-shadow: 0px 0px 19px 3px rgb(255, 239, 211);
  color:white;
}
.head{
  background-color: rgb(232, 255, 219);
}
.options{
  position: relative;
  border-radius: 10px 10px;
  padding: 23px;
  width:250px;
  left:41%;
  margin-top:2%;border:2px solid rgb(250, 245, 109);
}
</style>
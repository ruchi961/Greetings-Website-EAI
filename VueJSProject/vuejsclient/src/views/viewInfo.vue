<template>
  <div class="mainPage">
<p v-for="value in names" :key="value">{{value}}<br></p>
<br><br>

  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
export default {
  name: 'viewInfo',
      data() {                                   // <== changed this line
      return {
       img:[],
      
       names:this.$route.params,
       oldIndex1:-3,
       oldIndex2:-2,
       oldIndex3:-1
      }
    },
    created(){
        
          this.names = this.$route.params;
          console.log(this.$route.params)
   
  
           
    },
          mounted(){
          var val = localStorage.getItem("o")
          console.log(val)
        axios
      .get('http://127.0.0.1:5000/getImages')
      .then((response) => {
        console.log(response.data.products);
        this.img=response.data.image,
        this.names=response.data.products[val]
        this.ImgNames=response.data.file_names
        console.log(response.data.file_names);
      })
  
           
    },

          methods : {
 
            // Creating function
            show: function(){


            },
            oo:function(){
                this.names = this.$route.params;
          console.log(this.$route.params)
            }
        }

}
</script>
<style scoped>
body,html{

  width:100%;
  height:100%;
  
}

.mainPage{
  position:absolute;
  top:3px;
  left:0px;
  width:100%;
  height:100%;
  background-color: transparent;
  overflow: scroll;

}
img{
  height:50;
  width:50;
}
p{
  position: relative;
  top:21%;
  left:12%;
  width:69%;
  font-size: 30px;
  background-color: white;
}
</style>

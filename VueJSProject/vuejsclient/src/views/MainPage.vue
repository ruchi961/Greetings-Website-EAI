<template>
  <div class="mainPage">

    <div class>
     <table cellpadding="10" cellspacing="15">
      
      <tr>
<span v-for="(Products,index) in names" :key="index">
      
        <td >
          <img :src="'data:image/jpg;base64,' + findImgName(Products.ProductCode) " height=370 width=370>
          <p>{{Products.ProductTitle}}</p>
          <button v-on:click="viewInfo(index)">View</button>&nbsp;
          <button v-on:click="cartUpdate(Products.ProductCode)">Add to Cart</button>
        </td>
      <!--  <td v-if="index==oldIndex2+3">
          <img :src="'data:image/jpg;base64,' + findImgName(Products.ProductCode) " height=370 width=370>
          <p>{{Products.ProductTitle}}</p>
          <button v-on:click="viewInfo(index)">View</button>&nbsp;
          <button v-on:click="cartUpdate(Products.ProductCode)">Add to Cart</button>
        </td>
        <td v-if="index==increase('oldIndex3',oldIndex3)">

          <img :src="'data:image/jpg;base64,' + findImgName(Products.ProductCode) " height=370 width=370>
          <p>{{Products.ProductTitle}}</p>
                    <button v-on:click="viewInfo(index)">View</button>&nbsp;
          <button v-on:click="cartUpdate(Products.ProductCode)">Add to Cart</button>
        </td>-->
       <!-- <td v-if="index%2==0">
          
          {{Products.ProductTitle}}
          </td>
        <td v-else>
          {{Products.ProductTitle}}
          </td>-->
          </span>
      </tr>
      </table>


</div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'mainPage',
      data() {                                   // <== changed this line
      return {
       img:[],
       names:[],
       ImgNames:[],
       oldIndex1:-3,
       oldIndex2:-2,
       oldIndex3:-1,
       val:0,
       cartData:{"data":[]}
      }
    },
    mounted(){
          
        axios
      .get('http://127.0.0.1:5000/getImages')
      .then((response) => {
        console.log(response.data.products);
        this.img=response.data.image,
        this.names=response.data.products
        this.ImgNames=response.data.file_names
        console.log(response.data.file_names);
        if(localStorage.getItem('Items')){
        this.cartData=JSON.parse(localStorage.getItem('Items'))
        console.log(this.cartData,typeof(this.cartData))
        }
        if(localStorage.getItem('cartItems')){
  this.val = parseInt(localStorage.getItem('cartItems'));
  console.log(this.val)
}
      })
  
           
    },

          methods : {
 
            // Creating function
            show: function(){

        axios
      .get('http://127.0.0.1:5000/getImages')
      .then((response) => {
        console.log(response.data.products);
        this.img=response.data.image,
        this.names=response.data.products,
        this.ImgNames=response.data.file_names
        this.cartData['data']=localStorage.getItem('Items')
        //console.log(response.data.file_names);

      })
  
            },
            cartUpdate:function(code){
             console.log("sed",this.cartData['data'])
             this.cartData["data"].push(code)
              console.log(this.cartData['data'])
localStorage.setItem('Items', JSON.stringify(this.cartData));
if(localStorage.getItem('cartItems')){
  this.val = parseInt(localStorage.getItem('cartItems'));
}
              this.val= this.val+1;
              console.log(this.val)
              localStorage.setItem('cartItems', this.val)
console.log(localStorage.getItem('Items'))
window.dispatchEvent(new CustomEvent('cartItems-key-localstorage-changed', {
  detail: {
    storage: localStorage.getItem('cartItems')
  }
}));

            },
            viewInfo(index){
              let data = {
                BranchID : this.names[index]["BranchID"],
                ProductCode: this.names[index]["ProductCode"],
ProductTitle:this.names[index]["ProductTitle"],
ProductQuantity:this.names[index]["ProductQuantity"],
ProductPrice :this.names[index]["ProductPrice"],
ProductDescription:this.names[index]["ProductDescription"],
Category:this.names[index]["Category"],
Color:this.names[index]["Color"],
Width_cm:this.names[index]["Width_cm"],
Height_cm:this.names[index]["Height_cm"],
Type:this.names[index]["Type"],
              };
              localStorage.setItem("o",index)
              //console.log(data);
                    this.$router.push({

        name: "viewInfo", //use name for router push
        params: {id:"1"}
      });

            },
            findImgName(val){
              //console.log(val)
              //console.log(this.ImgNames)
              for(var i=0;i<this.ImgNames.length;i++){
                //console.log(this.ImgNames[i])
                if(this.ImgNames[i]==val){
                 /* console.log("sdsdm",this.ImgNames[i],this.img[i])*/
                  return this.img[i]
                  
                }
              }
            },
            increase(val,val2){
             // console.log(val=="oldIndex3",this.oldIndex3)
              if (val=="oldIndex3"){
                this.oldIndex3 = this.oldIndex3+3;
                console.log(this.oldIndex3)
                val2 = val2+3;
              return val2;
              }

            }
        }

}
</script>
<style scoped>
body,html{

  width:100%;
  height:90%;
    
  
}

.mainPage{
  position:absolute;
  top:9%;
  width:90vw;
  height:79vh;
  left:5%;
  background-image:linear-gradient(rgb(255, 250, 241),transparent,rgb(255, 243, 222));
  background-color: transparent;
  border-radius: 10px 10px ;
  box-shadow: 0px 0px 3px 4px rgb(160, 160, 160);
  overflow-y: scroll;
  scroll-behavior: smooth;
scrollbar-width: none; /* Firefox */
    -ms-overflow-style: none;  /* Internet Explorer 10+ */
}
.mainPage::-webkit-scrollbar { /* WebKit */
    width: 0;
    height: 0;
}
img{
  height:50;
  width:50;
}
button{
  font-size:18px;
  background-color: rgb(255, 127, 200);
  color: white;
  border:none;
  padding: 5px;
  text-shadow: 1px 1px rgb(65, 65, 65);
  border-radius:5px 2px;
  box-shadow: 0px 0px 2px 1px grey;
  

}
button:hover{
  background-color: rgb(237, 22, 144);
  border:1px solid wheat;



}
td{
  text-align: center;
  background-color: rgb(5, 84, 34);
  color: wheat;
  font-size: 18px;
  position: relative;
}
table{
  margin:2%;
}
</style>

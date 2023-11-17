package main

import (
    "bytes"
    "encoding/json"
    "fmt"
    "io/ioutil"
    "log"
    "net/http"
)
type Todo struct {
	UserID    int    `json:"userId"`
	ID        int    `json:"id"`
	Title     string `json:"title"`
	Completed bool   `json:"completed"`
}
type inputData struct {
    pickup   string 
    destination string
}
type test_struct struct {
    pickup string
    destination string
}
func homePage(w http.ResponseWriter, r *http.Request){
    if err := r.ParseForm(); err != nil {
        fmt.Fprintf(w, "ParseForm() err: %v", err)
        return
    }
    fmt.Fprintf(w, "Post from website! r.PostFrom = %v\n", r.PostForm)
   /* name := r.FormValue("name")
    address := r.FormValue("address")
    fmt.Fprintf(w, "Name = %s\n", name)
    fmt.Fprintf(w, "Address = %s\n", address)
    fmt.Fprintf(w, "Welcome to the HomePage!")
    fmt.Printf("Name = %s\n", name)
    fmt.Printf( "Address %s\n", address)
    fmt.Println("Welcome to the HomePage!")
    fmt.Println("Endpoint Hit: homePage")*/

   /* reqBody, err := ioutil.ReadAll(r.Body)
              if err != nil {
                      log.Fatal(err)
              }

              fmt.Println("fd", string(reqBody))
              var inp inputData
              err = json.Unmarshal([]byte(reqBody), &inp)
              if err != nil {
                  // panic
              }
          
              fmt.Println(string(reqBody))*/
            

              body, err := ioutil.ReadAll(r.Body)
              if err != nil {
                  panic(err)
              }
              log.Println(string(body))
              var t test_struct
              err = json.Unmarshal(body, &t)
              if err != nil {
                  panic(err)
              }
              log.Println(t.pickup)
              fmt.Println("va",t.destination)
            
    fmt.Println("2. Performing Http Post...")
    todo := Todo{1, 2, "lorem ipsum dolor sit amet", true}
    jsonReq, err := json.Marshal(todo)
    resp, err := http.Post("http://localhost:5000/shipmentDetails", "application/json; charset=utf-8", bytes.NewBuffer(jsonReq))
    if err != nil {
        log.Fatalln(err)
    }

    defer resp.Body.Close()
    bodyBytes, _ := ioutil.ReadAll(resp.Body)

    // Convert response body to string
    bodyString := string(bodyBytes)
    fmt.Println(bodyString)

    // Convert response body to Todo struct
    var todoStruct Todo
    json.Unmarshal(bodyBytes, &todoStruct)
    fmt.Printf("%+v\n", todoStruct)
}

func handleRequests() {
    http.HandleFunc("/", homePage)
    log.Fatal(http.ListenAndServe(":10000", nil))
}

func main() {
    handleRequests()
}
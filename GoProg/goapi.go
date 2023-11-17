package main

import (
    "fmt"
    "net/http"
)

func homePage(w http.ResponseWriter, r *http.Request){
    fmt.Fprintf(w, "Welcome to the HomePage!")
    fmt.Println("Endpoint Hit: homePage")
    fmt.Println("2. Performing Http Post...")
    todo := Todo{1, 2, "lorem ipsum dolor sit amet", true}
    jsonReq, err := json.Marshal(todo)
    resp, err := http.Post("https://localhost:5000/shipmentDetails", bytes.NewBuffer(jsonReq))
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
    http.ListenAndServe(":10000", nil)
}

func main() {
    handleRequests()
}
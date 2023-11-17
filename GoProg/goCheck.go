package main

import (
	"fmt"
	"net"
	"os"
	"encoding/csv"

    "log"
    "encoding/json"
"io/ioutil"
)

type OffersRecord struct {

    Code	string 
    Patype	string
    Subscription	string
    Min	string
    Money	string
    Percenta	string
    Gift string

}

const (
	hostname string = "127.0.0.1"
	port     string = "8000"
)
func createOffersList(data [][]string) []OffersRecord {
    var OffersList []OffersRecord
    for i, line := range data {
        if i > 0 { // omit header line
            var rec OffersRecord
            for j, field := range line {
                if j == 0 {
                    rec.Code= field	

                } else if j == 1 {
                    rec.Patype= field
                }else if j ==2 {
                    rec.Subscription= field
                }else if j == 3 {
                    rec.Min= field
                }else if j == 4 {
                    rec.Money= field
                }else if j == 5 {
                    rec.Percenta= field
                }else if j == 6 {
                    rec.Gift= field
                }
            }
            OffersList = append(OffersList, rec)
fmt.Println("dd",OffersList)
        }
    }
fmt.Println("ee",OffersList)
    return OffersList
}


func main() {


	addrs, err := net.LookupHost(hostname)
	checkError(err)

	fmt.Println("Server address: ", addrs, ":", port)

	// service: address:8000
	service := addrs[0] + ":" + port

	tcpAddr, err := net.ResolveTCPAddr("tcp4", service)
	checkError(err)

	conn, err := net.DialTCP("tcp", nil, tcpAddr)
	checkError(err)


    f, err := os.Open("D:/EAI/GoProg/Offers.csv")
    if err != nil {
        log.Fatal(err)
    }

    // remember to close the file at the end of the program
    defer f.Close()

    // read csv values using csv.Reader
    csvReader := csv.NewReader(f)
    data, err := csvReader.ReadAll()
    if err != nil {
        log.Fatal(err)
    }

    // convert records to array of structs
    offersList := createOffersList(data)
message:=""
fmt.Println(offersList)
 for i := 0; i < len(offersList); i++ {
        fmt.Println(offersList[i])
out, err := json.Marshal(offersList[i])
    if err != nil {
        panic (err)
    }

    fmt.Println(string(out))
message+=string(out)
}

	

	fmt.Println("Send message: ", message)
	_, err = conn.Write([]byte(message))
	checkError(err)

	fmt.Println("Send message: ", message)
	_, err = conn.Write([]byte("stop"))
	checkError(err)
	

	result, err := ioutil.ReadAll(conn)
	checkError(err)

	fmt.Println("Receive message: " + string(result))
	os.Exit(0)

}

func checkError(err error) {
	if err != nil {
		fmt.Fprintf(os.Stderr, "Fatal error: %s", err.Error())
		os.Exit(1)
	}
}
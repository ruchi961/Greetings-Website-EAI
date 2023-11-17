package main

import (
	"fmt"
	"net"
	"os"
	"encoding/csv"

    "log"
    "encoding/gob"
)

type OffersRecord struct {

    code	string 
    patype	string
    subscription	string
    min	string
    money	string
    percenta	string
    gift string

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
                    rec.code= field	

                } else if j == 1 {
                    rec.patype= field
                }else if j ==2 {
                    rec.subscription= field
                }else if j == 3 {
                    rec.min= field
                }else if j == 4 {
                    rec.money= field
                }else if j == 5 {
                    rec.percenta= field
                }else if j == 6 {
                    rec.gift= field
                }
            }
            OffersList = append(OffersList, rec)
        }
    }
    return OffersList
}

func main() {
    // open file
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

    // print the array
    fmt.Printf("%+v\n", offersList)
    
	addrs, err := net.LookupHost(hostname)
	//checkError(err)

	//fmt.Println("Server address: ", addrs, ":", port)

    	// service: address:8000
	service := addrs[0] + ":" + port

	tcpAddr, err := net.ResolveTCPAddr("tcp4", service)
	//checkError(err)

	//conn, err := net.Dial("tcp", niltcpAddr)
	//heckError(err)
    conn, err :=net.DialTCP("tcp", nil,tcpAddr)

	message :=offersList
	fmt.Println("Send message: ", message)
	enc := gob.NewEncoder(conn)
	enc.Encode(message)
  


	fmt.Println("sone ")
	os.Exit(0)
}

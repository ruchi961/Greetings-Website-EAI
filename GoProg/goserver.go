// socket-server project main.go
package main
import (
	"fmt"
	"net"
	"os"
	"encoding/csv"

    "log"
    "encoding/json"

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
const (
        SERVER_HOST = "localhost"
        SERVER_PORT = "9988"
        SERVER_TYPE = "tcp"
)
func main() {
        fmt.Println("Server Running...")
        server, err := net.Listen(SERVER_TYPE, SERVER_HOST+":"+SERVER_PORT)
        if err != nil {
                fmt.Println("Error listening:", err.Error())
                os.Exit(1)
        }
        defer server.Close()
        fmt.Println("Listening on " + SERVER_HOST + ":" + SERVER_PORT)
        fmt.Println("Waiting for client...")
        for {
                connection, err := server.Accept()
                if err != nil {
                        fmt.Println("Error accepting: ", err.Error())
                        os.Exit(1)
                }
                fmt.Println("client connected")
                go processClient(connection)
        }
}
func processClient(conn net.Conn) {
        buffer := make([]byte, 1024)
        mLen, err := conn.Read(buffer)
        if err != nil {
                fmt.Println("Error reading:", err.Error())
        }
        fmt.Println("Received: ", string(buffer[:mLen]))
if(string(buffer[:mLen])=="sendData"){
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
	

	fmt.Println("Send message: ", message)
	_, err = conn.Write([]byte("stop"))
	
     /*   _, err = connection.Write([]byte("Thanks! Got your message:" + string(buffer[:mLen])))
        connection.Close()*/

}

}
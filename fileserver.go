package main

import (
	"log"
	"net/http"
)

const (
	addr = "127.0.0.1:3000"
)

func main() {
	fs := http.FileServer(http.Dir("./"))
	http.Handle("/", http.StripPrefix("/", fs))
	log.Println("Server is up:", addr)
	log.Fatal(http.ListenAndServe(addr, nil))
}

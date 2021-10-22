package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"

	"github.com/axetroy/go-upload/config"
	"github.com/axetroy/go-upload/http"
)

func main() {

	var (
		err error
	)

	sigc := make(chan os.Signal, 1)
	signal.Notify(sigc,
		syscall.SIGHUP,
		syscall.SIGINT,
		syscall.SIGTERM,
		syscall.SIGQUIT)
	go func() {
		s := <-sigc
		fmt.Print("signal: ", s)
		os.Exit(1)
	}()

	// init anything
	if err = config.Init(); err != nil {
		panic(err)
		return
	}

	http.RunServer()
}

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	s, _ := reader.ReadString('\n')

	words := strings.Split(s, " ")
	var cnt int
	for _, word := range words {
		if word != "\n" && word != "" {
			cnt++
		}
	}
	fmt.Println(cnt)
}

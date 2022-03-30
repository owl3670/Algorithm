package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type cnt map[rune]int

func main() {
	var s string
	reader := bufio.NewReader(os.Stdin)
	fmt.Fscanln(reader, &s)

	s = strings.ToUpper(s)
	charMap := make(cnt)

	for _, c := range s {
		val, exists := charMap[c]
		if !exists {
			charMap[c] = 1
		} else {
			val++
			charMap[c] = val
		}
	}

	max := 0
	char := '?'
	for key, val := range charMap {
		if max < val {
			max = val
			char = key
		} else if max == val {
			char = '?'
		}
	}
	fmt.Println(string(char))
}

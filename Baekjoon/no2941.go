package main

import (
	"fmt"
	"strings"
)

type cnt map[rune]int

func main() {
	var s string
	fmt.Scanln(&s)

	var arr []string
	arr = []string{"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="}

	result := 0
	for _, alpha := range arr {
		cnt := strings.Count(s, alpha)
		s = strings.ReplaceAll(s, alpha, "!")
		result += cnt
	}

	s = strings.ReplaceAll(s, "!", "")
	result += len(s)
	fmt.Println(result)
}

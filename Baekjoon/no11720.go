package main

import (
	"fmt"
	"strconv"
)

func main() {
	var n int
	fmt.Scanln(&n)
	var s string
	fmt.Scanln(&s)

	var sum int
	for i := 0; i < n; i++ {
		num, _ := strconv.Atoi(string(s[i]))
		sum += num
	}
	fmt.Println(sum)
}

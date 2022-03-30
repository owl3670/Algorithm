package main

import "fmt"

func main() {
	var n int
	fmt.Scanln(&n)

	var counting [10001]int
	for i := 0; i < n; i++ {
		var num int
		fmt.Scanln(&num)
		counting[num]++
	}

	for i, count := range counting {
		for j := 0; j < count; j++ {
			fmt.Println(i)
		}
	}
}

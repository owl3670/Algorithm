package main

import "fmt"

func main() {
	var n int
	fmt.Scanln(&n)

	for i := 0; i < n; i++ {
		var cnt int
		var str string
		fmt.Scanln(&cnt, &str)
		for _, c := range str {
			for j := 0; j < cnt; j++ {
				fmt.Print(string(c))
			}
		}
		fmt.Println()
	}
}

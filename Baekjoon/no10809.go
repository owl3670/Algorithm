package main

import "fmt"

func main() {
	var s string
	fmt.Scanln(&s)

	var chars []rune
	for i := 0; i < 26; i++ {
		chars = append(chars, rune(97+i))
	}

	for _, char := range chars {
		idx := -1
		for i, s := range s {
			if s == char {
				idx = i
				break
			}
		}
		fmt.Printf("%d ", idx)
	}
	fmt.Println()
}

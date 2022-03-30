package main

import "fmt"

func main() {
	var a, b int
	fmt.Scanln(&a, &b)

	a = reverseNumber(a)
	b = reverseNumber(b)

	result := 0
	if a > b {
		result = a
	} else {
		result = b
	}

	fmt.Println(result)
}

func reverseNumber(num int) int {
	reversedNum := 0
	for num > 0 {
		reversedNum *= 10
		reversedNum += num % 10
		num /= 10
	}

	return reversedNum
}

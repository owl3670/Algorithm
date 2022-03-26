package main

import "fmt"

func main() {
	var arr [10001]bool

	for i := 1; i < len(arr); i++ {
		if arr[i] == false {
			fmt.Println(i)
			checkHaveConstructorNum(&arr, i)
		}
	}
}

func checkHaveConstructorNum(a *[10001]bool, num int) {
	cur := num
	for cur <= 10000 {
		temp := cur
		for temp > 0 {
			cur += temp % 10
			temp /= 10
		}
		if cur <= 10000 {
			a[cur] = true
		}
	}
}

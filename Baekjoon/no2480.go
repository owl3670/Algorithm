package main

import "fmt"

func main() {
	var arr [6]int
	var num int
	for i := 0; i < 3; i++ {
		fmt.Scan(&num)
		arr[num-1] += 1
	}

	lastIdx := 0
	for i, cnt := range arr {

		if cnt == 3 {
			fmt.Println(10000 + (i+1)*1000)
			return
		} else if cnt == 2 {
			fmt.Println(1000 + (i+1)*100)
			return
		} else if cnt == 1 {
			lastIdx = i
		}
	}
	fmt.Println((lastIdx + 1) * 100)
}

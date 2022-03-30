package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)

	cnt := 0
	if n < 100 {
		cnt = n
	} else {
		num := 100
		cnt = 99
		for num <= n && num < 1000 {
			temp := num
			var s []int
			for temp > 0 {
				s = append(s, temp%10)
				temp /= 10
			}
			num++
			if s[0]-s[1] != s[1]-s[2] {
				continue
			}

			cnt++
		}
	}

	fmt.Println(cnt)
}

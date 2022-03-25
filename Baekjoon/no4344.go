package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)

	var scores [1000]int
	for i := 0; i < n; i++ {
		var m int
		fmt.Scan(&m)

		avg := 0
		for j := 0; j < m; j++ {
			var score int
			fmt.Scan(&score)
			scores[j] = score
			avg += score
		}
		avg /= m

		cnt := 0
		for j := 0; j < m; j++ {
			if scores[j] > avg {
				cnt++
			}
		}

		fcnt := float64(cnt)
		fm := float64(m)
		fmt.Printf("%.3f%%\n", (fcnt/fm)*100)
	}
}

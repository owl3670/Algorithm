package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n int
	fmt.Scanln(&n)

	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var counting [10001]int
	for i := 0; i < n; i++ {
		var num int
		fmt.Fscanln(reader, &num)
		counting[num]++
	}

	for i, count := range counting {
		for j := 0; j < count; j++ {
			fmt.Fprintln(writer, i)
		}
	}
}

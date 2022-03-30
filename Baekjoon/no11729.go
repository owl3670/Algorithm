package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func main() {
	var n int
	writer := bufio.NewWriter(os.Stdout)
	fmt.Scanln(&n)
	fmt.Println(int(math.Pow(2, float64(n))) - 1)
	defer writer.Flush()

	hanoi(n, 1, 3, 2, writer)
}

func hanoi(n int, from int, to int, by int, writer *bufio.Writer) {
	if n == 1 {
		fmt.Fprintf(writer, "%d %d\n", from, to)
	} else {
		hanoi(n-1, from, by, to, writer)
		fmt.Fprintf(writer, "%d %d\n", from, to)
		hanoi(n-1, by, to, from, writer)
	}
}

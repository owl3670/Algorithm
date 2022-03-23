package main

import "fmt"

func main() {
	var hour, min, addMin, addHour int
	fmt.Scanln(&hour, &min)
	fmt.Scanln(&addMin)

	min += addMin
	if min >= 60 {
		addHour = min / 60
		min %= 60
	}
	hour += addHour
	if hour >= 24 {
		hour %= 24
	}

	fmt.Println(hour, min)
}

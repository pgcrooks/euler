package main

import "fmt"

func calculate(upTo int) int {
	total := 0
	fmt.Println("Calculate up to", upTo)
	for i := 0; i < upTo; i++ {
		if (i%3 == 0) || (i%5 == 0) {
			total += i
		}
	}

	return total
}

func main() {
	fmt.Println(calculate(1000))
}

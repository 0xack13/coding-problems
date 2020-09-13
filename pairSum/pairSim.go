package main

import "fmt"

func pairSum(t []int, sum int) {
	tries := 0
	for i := 0; i < len(t); i++ {
		currSum := t[i]
		for j := i + 1; j < len(t); j++ {
			tries += 1
			fmt.Println(tries)
			currSum += t[j]
			fmt.Println("Current Sum: ", currSum)
			if currSum == sum {
				fmt.Println("Found")
				return
			} else {
				currSum = 0
			}
		}
	}
	fmt.Println("Not found.")
}

func main() {
	t := []int{2, 3, 4, 22, 1, 44, 5}
	pairSum(t, 11)
}

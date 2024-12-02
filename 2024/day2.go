package main

import (
	"fmt"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
)

func main() {
	content, err := os.ReadFile("inputs/day2")
	if err != nil {
		log.Fatal(err)
	}
	reports := strings.Split(string(content), "\n")
	total := 0
	total2 := 0
	for _, r := range reports {
		level := []int{}
		for _, i := range strings.Split(r, " ") {
			conv, err := strconv.Atoi(i)
			if err != nil {
				panic(err)
			}
			level = append(level, conv)
		}
		if checkLevel(level) {
			total += 1
		}
		
		for i, _ := range level {
			if checkLevel(remove(level, i)) {
				total2 ++
				break
			}
		}
	}
	fmt.Println(total)
	fmt.Println(total2)
}

func checkLevel(level []int) bool {
	copy := slices.Clone(level)
	slices.Reverse(copy)
	if (!isMonIncreasing(level) && !isMonIncreasing(copy)) {
		return false
	}
	for i, x := range level {
		if i > 0 {
			if absDiffInt(x, level[i-1]) > 3 {
				return false
			}
		}
	}
	return true
}

func remove(slice []int, i int) []int {
    s := slices.Clone(slice)
	return append(s[:i], s[i+1:]...)
	
}




func absDiffInt(x, y int) int {
	if x < y {
	   return y - x
	}
	return x - y
 }

 func isMonIncreasing(x []int) bool {
	for i := len(x) - 1; i > 0; i-- {
		if x[i] <= x[i-1] {
			return false
		}
	}
	return true
 }

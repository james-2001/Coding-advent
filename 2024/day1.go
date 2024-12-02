package main

import (
	"log"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	// Replace "file.txt" with your file path
	content, err := os.ReadFile("inputs/day1")
	if err != nil {
		log.Fatal(err)
	}
	sides := [][]int{[]int{}, []int{}}
	for _, line := range strings.Split(string(content), "\n") {
		for i, side := range strings.Split(line, "   ") {
			converted, err := strconv.Atoi(side)
			if err != nil {
				panic(err)
			}
			sides[i] = append(sides[i], converted)
		}
	}

	for _, side := range sides {
		sort.Ints(side)

	}
	total1 := 0.0
	total2 := 0
	for i, x := range sides[0] {
		total1 += math.Abs(float64(x - sides[1][i]))
		total2 += x * countOccurrences(sides[1], x)
	}
	println(int(total1))
	println(total2)
}

func countOccurrences(slice []int, target int) int {
	count := 0
	for _, v := range slice {
		if v == target {
			count++
		}
	}
	return count
}

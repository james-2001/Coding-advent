package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"

	"github.com/juliangruber/go-intersect/v2"
)

func main() {
	dat, err := os.ReadFile("./data.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(dat), "\n")
	p1 := 0
	copies := []int{}
	for i := 0; i < len(lines); i++ {
		copies = append(copies, 1)
	}
	for j, card := range lines {
		card = strings.Split(card, ":")[1]
		card = strings.Replace(card, "  ", " ", -1)
		vals := [][]int{}
		for _, i := range strings.Split(card, "|") {
			x := []int{}
			for _, n := range strings.Split(strings.TrimSpace(i), " ") {
				number, err := strconv.Atoi(strings.TrimSpace(n))
				if err != nil {
					panic(err)
				}
				x = append(x, number)
			}
			vals = append(vals, x)
		}
		inter := intersect.HashGeneric(vals[0], vals[1])
		p1 += int(math.Pow(2, float64(len(inter)-1)))
		for i := 1; i <= len(inter); i++ {
			copies[j+i] += copies[j]
		}

	}
	fmt.Println(p1)
	p2 := 0
	for _, i := range copies {
		p2 += i
	}
	fmt.Println(p2)
	fmt.Println(copies)
}

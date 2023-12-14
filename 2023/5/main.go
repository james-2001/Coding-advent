package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	dat, err := os.ReadFile("./data.txt")
	if err != nil {
		panic(err)
	}
	groups := strings.Split(string(dat), "\n\n")
	seedLine := groups[0]
	seeds := []int{}
	for _, i := range strings.Split(strings.TrimSpace(strings.Split(seedLine, ":")[1]), " ") {
		seedNumber, err := strconv.Atoi(strings.TrimSpace(i))
		if err != nil {
			panic(err)
		}
		seeds = append(seeds, seedNumber)
	}
	p2seeds := []int{}
	for i := 0; i < 10; i += 2 {
		p2seeds = append(p2seeds, i)
	}
	fmt.Println(solve(p2seeds, groups))
}

func solve(seeds []int, groups []string) int {
	p1 := seeds[0]
	for _, s := range seeds {

		for _, m := range groups[1:] {

			lines := strings.Split(m, "\n")
			mappings := [][]int{}
			for _, j := range lines[1:] {
				sVals := strings.Split(j, " ")
				vals := []int{}
				for _, v := range sVals {
					if x, err := strconv.Atoi(v); err == nil {
						vals = append(vals, x)
					}
				}
				mappings = append(mappings, vals)
			}
			// fmt.Println(mappings)
			s = getMapping(mappings, s)
		}
		if s < p1 {
			p1 = s
		}
	}
	return p1
}

func getMapping(mappings [][]int, inp int) int {
	for _, m := range mappings {
		if inp >= m[1] && inp < m[1]+m[2] {
			// fmt.Println("mapping from", inp, "to", m[0]+(inp-m[1]))
			return m[0] + (inp - m[1])
		}
	}
	return inp
}

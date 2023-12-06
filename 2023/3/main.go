package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
	"unicode"
)

// TODO: clean

type point struct {
	x int
	y int
}

func (p2 *point) add(p1 point) point {
	return point{
		p1.x + p2.x,
		p1.y + p2.y,
	}
}

func (p *point) inBounds(xBound, yBound int) bool {
	return p.x > 0 && p.x < xBound && p.y > 0 && p.y < yBound
}

func (p *point) get(lines []string) string {
	return string(lines[p.y][p.x])
}

func hasAdj(s []int, i int, lines []string) bool {
	neighbours := []point{{0, 1}, {0, -1}, {1, 1}, {-1, 1}, {1, -1}, {-1, -1}, {1, 0}, {-1, 0}}
	xSize := len(lines[0])
	ySize := len(lines)
	for x := s[0]; x < s[1]; x++ {
		n := point{x, i}
		for _, p := range neighbours {
			if j := n.add(p); j.inBounds(xSize, ySize) && j.get(lines) != "." && !unicode.IsDigit(rune(j.get(lines)[0])) {
				return true
			}
		}
	}
	return false
}

func main() {
	dat, err := os.ReadFile("./data.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(dat), "\n")
	p1 := 0
	gears := make(map[point][]int)
	for i, line := range lines {
		for _, s := range regexp.MustCompile(`\d+`).FindAllStringIndex(line, -1) {
			val, err := strconv.Atoi(line[s[0]:s[1]])
			if err != nil {
				fmt.Println(line[s[0]:s[1]])
				panic(err)
			}
			if hasAdj(s, i, lines) {
				p1 += val
			}
			neighbours := []point{{0, 1}, {0, -1}, {1, 1}, {-1, 1}, {1, -1}, {-1, -1}, {1, 0}, {-1, 0}}
			xSize := len(lines[0])
			ySize := len(lines)
			for x := s[0]; x < s[1]; x++ {
				n := point{x, i}
				for _, p := range neighbours {
					if j := n.add(p); j.inBounds(xSize, ySize) && j.get(lines) == "*" {
						seen := false
						for _, g := range gears[j] {
							if g == val {
								seen = true
							}
						}
						if !seen {
							gears[j] = append(gears[j], val)
						}
					}
				}
			}

		}
	}
	fmt.Println(p1)
	p2 := 0
	for _, v := range gears {
		if len(v) == 2 {
			p2 += v[0] * v[1]
		}
	}
	fmt.Println(p2)
}

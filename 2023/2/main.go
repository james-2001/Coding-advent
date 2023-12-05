package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type round struct {
	id    int
	red   int
	blue  int
	green int
}

func main() {

	dat, err := os.ReadFile("./data.txt")
	if err != nil {
		panic(err)
	}
	counter1 := 0
	counter2 := 0
	for i, line := range strings.Split(string(dat), "\n") {
		game := strings.Split(line, ":")[1]
		if validGame(game) {
			counter1 += i + 1
		}
		counter2 += minCubes(game)
	}
	fmt.Println(counter1)
	fmt.Println(counter2)
}

func validGame(line string) bool {
	pulls := strings.FieldsFunc(line, func(r rune) bool {
		return r == ';' || r == ','
	})
	for _, m := range pulls {
		round := strings.Split(strings.TrimSpace(m), " ")

		taken, err := strconv.Atoi(round[0])
		if err != nil {
			panic(err)
		}
		switch round[1] {
		case "red":
			if taken > 12 {
				return false
			}
		case "green":
			if taken > 13 {
				return false
			}
		case "blue":
			if taken > 14 {
				return false
			}
		}
	}
	return true
}

func minCubes(line string) int {
	red, blue, green := 0, 0, 0
	pulls := strings.FieldsFunc(line, func(r rune) bool {
		return r == ';' || r == ','
	})
	for _, m := range pulls {
		round := strings.Split(strings.TrimSpace(m), " ")

		taken, err := strconv.Atoi(round[0])
		if err != nil {
			panic(err)
		}
		switch round[1] {
		case "red":
			if taken > red {
				red = taken
			}
		case "green":
			if taken > green {
				green = taken
			}
		case "blue":
			if taken > blue {
				blue = taken
			}
		}
	}
	return red * blue * green
}

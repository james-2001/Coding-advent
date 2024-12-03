package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	content, err := os.ReadFile("inputs/day3")
	if err != nil {
		log.Fatal(err)
	}
	re := regexp.MustCompile(`mul\(\d*,\d*\)`)
	re2 := regexp.MustCompile(`mul\((\d*),(\d*)\)|(don't)|(do)`)
	total := 0
	for _, m := range re.FindAllString(string(content), -1) {
		total += parseMul(m)
	}
	fmt.Println(total)
	total = 0
	shouldAdd := true
	for _, m := range re2.FindAllString(string(content), -1) {
		if m == "don't" {
			shouldAdd = false
		} else if m == "do" {
			shouldAdd = true
		} else if re.MatchString(m) && shouldAdd {
			total += parseMul(m)
		}
	}
	fmt.Println(total)

}

func parseMul(m string) int {
	numbers := strings.Split(m[4 : len(m)-1], ",")
		a, err := strconv.Atoi(numbers[0])
		if err != nil {
			panic(err)
		}
		b, err := strconv.Atoi(numbers[1])
		if err != nil {
			panic(err)
		}
		return a*b
}
package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	dat, err := os.ReadFile("./data.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(dat), "\n")
	p1Counter := 0
	p2Counter := 0
	for _, line := range lines {
		p1Counter += countNumbers(line)
		line = replaceAll(line)

		p2Counter += countNumbers(line)

	}
	fmt.Println(p1Counter)
	fmt.Println(p2Counter)
}

func countNumbers(line string) int {
	re := regexp.MustCompile("[0-9]")
	digits := re.FindAllString(line, -1)
	n, err := strconv.Atoi(digits[0] + digits[len(digits)-1])
	if err != nil {
		panic(err)
	}
	return n
}

func replaceAll(line string) string {
	for k, v := range map[string]string{"one": "one1one", "two": "two2two", "three": "three3three", "four": "four4four", "five": "five5five", "six": "six6six", "seven": "seven7seven", "eight": "eight8eight", "nine": "nine9nine"} {
		line = strings.ReplaceAll(line, k, v)
	}
	return line
}

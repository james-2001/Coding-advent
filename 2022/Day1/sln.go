package main

import (
	"os"
	"strconv"
	"strings"
	"text/template"
)

type Input struct {
	Calories string
}

func main() {
	cal, calErr := os.ReadFile("input.txt")
	if calErr != nil {
		panic(calErr)
	}
	input := Input{Calories: string(cal)}
	tplFuncMap := make(template.FuncMap)
	tplFuncMap["Split"] = strings.Split
	tplFuncMap["Add"] = func(a int, b int) int {
		return a + b
	}
	tplFuncMap["Int"] = func(s string) int {
		i, err := strconv.Atoi(s)
		if err != nil {
			panic(err)
		}
		return i
	}
	t, err := template.New("sln").Funcs(tplFuncMap).ParseFiles("sln")
	err = t.Execute(os.Stdout, input)
	if err != nil {
		panic(err)
	}
}

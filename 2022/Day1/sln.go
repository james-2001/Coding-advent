package main

import (
	"os"
	"text/template"

	"github.com/Masterminds/sprig/v3"
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
	t, err := template.New("sln").Funcs(sprig.FuncMap()).ParseFiles("sln")
	err = t.Execute(os.Stdout, input)
	if err != nil {
		panic(err)
	}
}

import { readFileSync } from "fs"
import {zipWith} from "lodash"

type NewGeneric<T> = { val: T }

let a: NewGeneric<number> = {
    val : 2
}


var data = readFileSync('Day18/test.txt', 'utf-8');
var lava = data.split("\n").map((v): number[] => {
    var split = v.split(",") 
    return [parseInt(split[0]), parseInt(split[1]), parseInt(split[1])]
});

function getSides(c: number[]): number[][] {
    let sides: number[][] = [[1,0,0], [-1,0,0], [0,1,0], [0,-1,0], [0,0,1], [0,0,-1]]
    return sides.map((val) => zipWith(val, c, (a,b)=>a+b))
};

function exclIntersection(array1: number[][], array2: number[][]): number[][] {
    return array1.filter(value => !array2.includes(value));
}

lava.forEach((cube) => {
    getSides(cube).forEach((s) => {
        
    })
})

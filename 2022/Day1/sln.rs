use std::fs;

fn main() {
    let contents = fs::read_to_string("./Day1/input.txt").unwrap();
    let calories = contents.split("\n\n")
        .map(|x| x.lines().map(|x|
             x.parse::<i32>().unwrap()));
    let mut total_cals: Vec<i32> = calories.map(|x| x.sum::<i32>()).collect();
    total_cals.sort_by(|a,b| b.cmp(a));
    print!("Part 1: {}\n", total_cals[0]);
    print!("Part 2: {}\n", total_cals[..=2].iter().sum::<i32>())
}
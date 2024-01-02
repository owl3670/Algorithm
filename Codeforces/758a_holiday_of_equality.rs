use std::io;

fn main(){
    let mut n = String::new();
    io::stdin().read_line(&mut n).expect("Read Error");
    let _n: u32  = n.trim().parse().expect("Parse Error");

    let mut numbers = String::new();
    io::stdin().read_line(&mut numbers).expect("Read Error");
    let numbers: Vec<u32> = numbers.split_whitespace()
        .map(|s| s.trim().parse().expect("Parse Error"))
        .collect();
    
    let mut result: u32 = 0;

    let mut max: u32 = 0;
    for num in numbers.iter() {
        if *num > max {
            max = *num;
        }
    }

    for num in numbers.iter() {
        result += max - *num;
    }

    println!("{}", result);
}

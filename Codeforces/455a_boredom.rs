use std::io;

fn main(){
    let mut n = String::new();
    io::stdin().read_line(&mut n).expect("Read error");

    let mut a = String::new();
    io::stdin().read_line(&mut a).expect("Read error");
    let a: Vec<i32> = a.trim().split_whitespace().(|x| x.parse().expect("Parse error")).collect();
}
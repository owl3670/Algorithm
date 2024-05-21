use std::io;

fn main(){
    let mut n = String::new();
    io::stdin().read_line(&mut n).expect("Read error");
    let n: u32 = n.trim().parse().expect("Parse error");

    let b = format!("{:b}", n);
    let result = b.chars().filter(|&c| c == '1').count();

    println!("{}", result);
}
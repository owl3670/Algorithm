use std::io;

fn main(){
    let mut n = String::new();
    io::stdin().read_line(&mut n).expect("Error");
    let n: u64 = n.trim().parse().expect("Error");
    println!("25");
}
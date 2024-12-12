// Codeforces 1699A Division?

use std::io;

fn get_division_number(n: i32) -> i32{
    if 1900 <= n {
        1
    } else if 1600 <= n {
        2
    } else if 1400 <= n {
        3
    } else {
        4
    }
}

fn main(){
    let mut t = String::new();
    io::stdin().read_line(&mut t).expect("Error");
    let t: u64 = t.trim().parse().expect("Error");
    for _ in 0..t {
        let mut n = String::new();
        io::stdin().read_line(&mut n).expect("Error");
        let n: i32 = n.trim().parse().expect("Error");
        let d: i32 = get_division_number(n);
        println!("Division {d}")
    }
}

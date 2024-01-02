use std::io;

fn main(){
    let mut n = String::new();
    io::stdin().read_line(&mut n).expect("Failed to read line");
    let n: i32 = n.trim().parse().expect("Please type a number!");

    let mut a = 4;
    let mut b = n-4;
    loop {
        if is_composite(a) && is_composite(b) {
            println!("{} {}", a, b);
            break;
        }
        a += 1;
        b -= 1;
    }
}

fn is_composite(n: i32) -> bool {
    let mut i = 2;
    while i < n {
        if n % i == 0 {
            return true;
        }
        i += 1;
    }
    false
}
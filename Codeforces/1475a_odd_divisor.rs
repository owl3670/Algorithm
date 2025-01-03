use std::io;

fn read_number() -> i64 {
    let mut t = String::new();
    io::stdin().read_line(&mut t).expect("Read error");
    t.trim().parse::<i64>().expect("Parse error")
}

fn main() {
    let t = read_number();

    for _ in 0..t {
        let n: i64 = read_number();
        
        if (n & n-1) > 0 {
            println!("YES");
        } else {
            println!("NO");
        }
    }
}
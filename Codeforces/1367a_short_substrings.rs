use std::io;

fn main(){
    let mut n = String::new();
    io::stdin().read_line(&mut n).expect("Read error");
    let n: u32 = n.trim().parse().expect("Parse error");

    for _ in 0..n {
        let mut s = String::new();
        io::stdin().read_line(&mut s).expect("Read error");
        let s: Vec<char> = s.trim().chars().collect();

        let mut result = String::new();
        result.push(s[0]);
        for i in 1..s.len() {
            if i % 2 == 1 {
                result.push(s[i]);
            }
        }

        println!("{}", result);
    }
}

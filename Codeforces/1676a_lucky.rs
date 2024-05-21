use std::io;

fn main(){
    let mut n = String::new();
    io::stdin().read_line(&mut n).expect("Read Error");
    let n = n.trim().parse().expect("Parse Error");

    for _ in 0..n{
        let mut s = String::new();
        io::stdin().read_line(&mut s).expect("Read Error");
        let s: Vec<u32> = s.trim().chars().map(|x| x.to_digit(10).unwrap()).collect();

        if s[0] + s[1] + s[2] == s[3] + s[4] + s[5] {
            println!("YES");
        } else {
            println!("NO");
        }
    }
}

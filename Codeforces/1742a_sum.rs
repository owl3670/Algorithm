// Codeforces 1742A Sum

use std::io;

fn main(){
    let mut t = String::new();
    io::stdin().read_line(&mut t).expect("Error");
    let t: u64 = t.trim().parse().expect("Error");
    for _ in 0..t {
        let mut n = String::new();
        io::stdin().read_line(&mut n).expect("Error");
        let before = n.split_whitespace().collect::<Vec<&str>>();
        let mut numbers: Vec<u64> = Vec::new();
        for i in 0..before.len() {
            let num = before[i].parse::<u64>().unwrap();
            numbers.push(num);
        }
        if numbers[0] + numbers[1] == numbers[2] {
            println!("YES");
            continue;
        }
        if numbers[0] + numbers[2] == numbers[1] {
            println!("YES");
            continue;
        }
        if numbers[1] + numbers[2] == numbers[0] {
            println!("YES");
            continue;
        }
        println!("NO");
    }
}

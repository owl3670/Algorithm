use std::io;

fn main(){
    let mut t = String::new();
    io::stdin().read_line(&mut t).expect("Failed to read line");
    let t: i32 = t.trim().parse().expect("Please type a number!");

    for _ in 0..t {
        let mut n = String::new();
        io::stdin().read_line(&mut n).expect("Failed to read line");
        let _: i32 = n.trim().parse().expect("Please type a number!");

        let mut nums = String::new();
        io::stdin().read_line(&mut nums).expect("Failed to read line");
        let nums: Vec<i32> = nums.split_whitespace()
            .map(|s| s.parse().expect("parse error"))
            .collect();

        let mut map = std::collections::HashMap::new();
        for num in &nums {
            let count = map.entry(num).or_insert(0);
            *count += 1;
        }

        for (key, value) in map {
            if value == 1 {
                println!("{}", nums.iter().position(|&x| x == *key).unwrap() + 1);
                break;
            }
        }
    }    
}

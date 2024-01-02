use std::io;

fn main(){
    let mut nums = String::new();
    io::stdin().read_line(&mut nums).expect("Read Error");
    let nums: Vec<u32> = nums.split_whitespace()
        .map(|s| s.trim().parse().expect("Parse Error"))
        .collect();

    let k = nums[1];

    let mut persons = String::new();
    io::stdin().read_line(&mut persons).expect("Read Error");
    let persons: Vec<u32> = persons.split_whitespace()
        .map(|s| s.trim().parse().expect("Parse Error"))
        .collect();

    let mut count = 0;
    for p in persons {
        if p + k <= 5 {
            count += 1;
        }
    }

    println!("{}", count / 3);
}

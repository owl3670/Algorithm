use std::io;

fn main(){
    let mut n = String::new();
    io::stdin().read_line(&mut n).expect("Failed to read line");
    let n: i32 = n.trim().parse().expect("Please type a number!");

    let mut numbers = Vec::new();
    let mut i = 0;
    while numbers.len() <= 1000 {
        i += 1;
        if i % 3 == 0 || i % 10 == 3 {
            continue;
        }

        numbers.push(i);
    }

    for _ in 0..n {
        let mut k = String::new();
        io::stdin().read_line(&mut k).expect("Failed to read line");
        let k: u32 = k.trim().parse().expect("Please type a number!");

        println!("{}", numbers[k as usize - 1]);
    }
}
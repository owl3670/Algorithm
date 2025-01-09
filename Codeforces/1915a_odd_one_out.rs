use std::io;

fn read_number() -> i32 {
    let mut t = String::new();
    io::stdin().read_line(&mut t).expect("Read error");
    t.trim().parse::<i32>().expect("Parse error")
}

fn read_splitnumber()->Vec<i32>{
        let mut line = String::new();
        io::stdin().read_line(&mut line).expect("Error");
        return line.trim().split_whitespace().map(|x| x.parse::<i32>().unwrap()).collect();
}

fn main() {
    let t = read_number();

    for _ in 0..t {
        let nums = read_splitnumber();

        if nums[0] == nums[1] {
            println!("{}", nums[2]);
        } else if nums[0] == nums[2] {
            println!("{}", nums[1]);
        } else {
            println!("{}", nums[0]);
        }
    }
}
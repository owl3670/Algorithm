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
        let numbers = read_splitnumber();
        let mut min = numbers[0];
        let mut max = numbers[0];
        let mut med = numbers[0];

        for i in numbers {
            if min > i {
                med = min;
                min = i;
            } else if max < i {
                med = max;
                max = i;
            } else {
                med = i;
            }
        }

        println!("{med}");
    }
}
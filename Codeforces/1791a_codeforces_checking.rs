use std::collections::HashSet;
use std::io;

fn read_number() -> i32 {
    let mut t = String::new();
    io::stdin().read_line(&mut t).expect("Read error");
    t.trim().parse::<i32>().expect("Parse error")
}

fn contains(c: char, set: &HashSet<char>) -> bool {
    set.contains(&c)
}

fn main() {
    let t = read_number();

    let codeforces_set: HashSet<char> = "codeforces".chars().collect();

    for _ in 0..t {
        let mut c = String::new();
        io::stdin().read_line(&mut c).expect("Read error");

        if let Some(ch) = c.trim().chars().next() {
            if contains(ch, &codeforces_set) {
                println!("YES");
            } else {
                println!("NO");
            }
        } else {
            println!("Invalid input");
        }
    }
}

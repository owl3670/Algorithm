use std::io;

fn main(){
    let mut t = String::new();
    io::stdin().read_line(&mut t).expect("Error");
    let t: u64 = t.trim().parse().expect("Error");
    for _ in 0..t {
        let mut chr = String::new();
        io::stdin().read_line(&mut chr).expect("Error");
        let chr = chr.trim().to_lowercase();

        match chr == "yes" {
            true => println!("YES"),
            _ => println!("NO")
        }
    }
}
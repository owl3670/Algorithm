use std::io;

fn main(){
    let mut n = String::new();
    io::stdin().read_line(&mut n).expect("Read error");
    let n: u32 = n.trim().parse().expect("Parse error");

    let mut students = String::new();
    io::stdin().read_line(&mut a).expect("Read error");
    let students: Vec<u32> = students.trim().split_whitespace().map(|x| x.parse().expect("Parse error")).collect();

    let mut result: Vec<Vec<u32>> = vec![vec![], vec![]];

    for i in 0..n as usize {
        if students[i] == 1 {
            result[0].push(i as u32 + 1);
        } else if students[i] == 2 {
            result[1].push(i as u32 + 1);
        } else if students[i] == 3 {
            result[2].push(i as u32 + 1);
        }
    }

    println!("{}", min);

    for i in 0..min {
        println!("{} {} {}", result[0][i], result[1][i], result[2][i]);
    }
}
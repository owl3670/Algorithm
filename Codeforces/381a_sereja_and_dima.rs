// Codeforces Round #222 (Div. 2)
// URL: http://codeforces.com/problemset/problem/381/A

use std::io;

fn main(){
    let mut n = String::new();
    io::stdin().read_line(&mut n).expect("Failed to read line");
    let n: i32 = n.trim().parse().expect("Please type a number!");

    let mut cards = String::new();
    io::stdin().read_line(&mut cards).expect("Failed to read line");
    let cards: Vec<u32> = cards.split_whitespace()
        .map(|s| s.parse().expect("parse error"))
        .collect();

    let mut sereja = 0;
    let mut dima = 0;
    let mut i:i32 = 0;
    let mut j:i32 = n - 1;
    let mut turn = true;
    while i <= j {
        if cards[i as usize] > cards[j as usize] {
            if turn {
                sereja += cards[i as usize];
            } else {
                dima += cards[i as usize];
            }
            i += 1;
        } else {
            if turn {
                sereja += cards[j as usize];
            } else {
                dima += cards[j as usize];
            }
            j -= 1;
        }
        turn = !turn;
    }
    println!("{} {}", sereja, dima); 
}

use std::io;
use std::cmp;

fn main(){
    let mut n = String::new();
    io::stdin().read_line(&mut n).expect("Read error");
    let n: usize = n.trim().parse().expect("Parse error");

    let mut a = String::new();
    io::stdin().read_line(&mut a).expect("Read error");
    let a: Vec<usize> = a.trim().split_whitespace().map(|x| x.parse().expect("Parse error")).collect();

    let mut cnt = vec![0; 100001];
    for i in 0..n {
        cnt[a[i]] += 1;
    }

    let mut dp = vec![0; 100001];
    dp[0] = 0;
    dp[1] = cnt[1];
    for i in 2..100001 {
        dp[i] = cmp::max(dp[i-1], dp[i-2] + i * cnt[i]);
    }

    println!("{}", dp[100000]);
}
use std::io;
use std::cmp;
<<<<<<< HEAD
 
=======

>>>>>>> af220e5e0477b52a80a472675983b7b3dbb2048f
fn main(){
    let mut n = String::new();
    io::stdin().read_line(&mut n).expect("Read error");
    let n: usize = n.trim().parse().expect("Parse error");
<<<<<<< HEAD
 
    let mut a = String::new();
    io::stdin().read_line(&mut a).expect("Read error");
    let a: Vec<usize> = a.trim().split_whitespace().map(|x| x.parse().expect("Parse error")).collect();
 
=======

    let mut a = String::new();
    io::stdin().read_line(&mut a).expect("Read error");
    let a: Vec<usize> = a.trim().split_whitespace().map(|x| x.parse().expect("Parse error")).collect();

>>>>>>> af220e5e0477b52a80a472675983b7b3dbb2048f
    let mut cnt = vec![0; 100001];
    for i in 0..n {
        cnt[a[i]] += 1;
    }
<<<<<<< HEAD
 
=======

>>>>>>> af220e5e0477b52a80a472675983b7b3dbb2048f
    let mut dp = vec![0; 100001];
    dp[0] = 0;
    dp[1] = cnt[1];
    for i in 2..100001 {
        dp[i] = cmp::max(dp[i-1], dp[i-2] + i * cnt[i]);
    }
<<<<<<< HEAD
 
=======

>>>>>>> af220e5e0477b52a80a472675983b7b3dbb2048f
    println!("{}", dp[100000]);
}
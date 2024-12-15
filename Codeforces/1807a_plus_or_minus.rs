
use std::io;

fn read_number()->i64{
    let mut line = String::new();
    io::stdin().read_line(&mut line).expect("Error");
    let num = line.trim().parse::<i64>().unwrap();
    num
}

fn read_splitnumber()->Vec<i64>{
        let mut line = String::new();
        io::stdin().read_line(&mut line).expect("Error");
        return line.trim().split_whitespace().map(|x| x.parse::<i64>().unwrap()).collect();
}

fn main(){
   let t = read_number();

   for _ in 0..t{
     let numbers = read_splitnumber();
     if numbers[0] + numbers[1] == numbers[2] {
        println!("+")
     } else {
        println!("-")
     }
   }
}

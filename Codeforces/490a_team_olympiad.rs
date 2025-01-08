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

fn main(){
    let _n = read_number();
    let t = read_splitnumber();

    let mut vec1 = Vec::new();
    let mut vec2 = Vec::new();
    let mut vec3 = Vec::new();

    for i in 0..t.len() {
        match t[i] {
            1 => vec1.push(i + 1),
            2 => vec2.push(i + 1),
            3 => vec3.push(i + 1),
            _ => ()
        }
    }

    let mut len_vec = Vec::new();
    len_vec.push(vec1.len());
    len_vec.push(vec2.len());
    len_vec.push(vec3.len());

    let mut min = 5001;

    for l in len_vec {
        if min > l {
            min = l;
        }
    }

    println!("{min}");

    for i in 0..min {
        println!("{} {} {}", vec1[i], vec2[i], vec3[i]);
    }
}
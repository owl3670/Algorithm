
use std::io;
use std::collections::HashMap;

fn read_number()->i64{
    let mut line = String::new();
    io::stdin().read_line(&mut line).expect("Error");
    let num = line.trim().parse::<i64>().unwrap();
    num
}

fn main(){
    let t = read_number();

    for _ in 0..t {
        let _n = read_number();
        let mut s = String::new();
        io::stdin().read_line(&mut s).expect("Error");
        let s = s.trim();

        let mut cmap = HashMap::new();
        for c in s.chars() {
            let count = cmap.entry(c).or_insert(0);
            *count += 1;
        }

        let (max_char, _) = cmap
            .iter()
            .max_by_key(|&(_, count)| count) // count가 가장 높은 문자
            .unwrap();

        let (min_char, _) = cmap
            .iter()
            .min_by_key(|&(_, count)| count) // count가 가장 낮은 문자
            .unwrap();
        
        let mut idx: Option<usize> = None;
        for (i, c) in s.char_indices() {
            if c == *min_char{
                idx = Some(i);
                break;
            }
        }


        if let Some(index) = idx {
            let mut chars: Vec<char> = s.chars().collect();
            chars[index] = *max_char;
            let modified: String = chars.into_iter().collect();
            println!("{}", modified);
        } else {
            println!("{}", s);
        }
    }
}


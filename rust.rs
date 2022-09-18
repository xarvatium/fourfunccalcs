use std::io;
use std::io::Write;
use std::io::stdout;


struct Calculator {
    first_num: u32,
    second_num: u32,
}

impl Calculator {
    fn add(&self) -> u32 {
        self.first_num + self.second_num
    }

    fn sub(&self) -> u32 {
        self.first_num - self.second_num
    }

    fn mul(&self) -> u32 {
        self.first_num * self.second_num
    }

    fn div(&self) -> u32 {
        self.first_num / self.second_num
    }
}

fn main() {
    let mut operator_raw = String::new();
    print!("Enter your operator: ");
    stdout().flush().unwrap();
    io::stdin().read_line(&mut operator_raw).expect("Error");


    let mut num1_raw = String::new();
    print!("Enter your first number: ");
    stdout().flush().unwrap();
    io::stdin().read_line(&mut num1_raw).expect("Error");

    let mut num2_raw = String::new();
    print!("Enter your second number: ");
    stdout().flush().unwrap();
    io::stdin().read_line(&mut num2_raw).expect("Error");

    let operator = operator_raw.trim();
    let num1 = num1_raw.trim();
    let num2 = num2_raw.trim();

    let calc = Calculator {
        first_num: num1.parse().unwrap(),
        second_num: num2.parse().unwrap()
    };

    match operator {
        "+" => {
            println!("{} + {} = {}", num1, num2, calc.add())
        }
        "-" => {
            println!("{} - {} = {}", num1, num2, calc.sub())
        }
        "*" => {
            println!("{} * {} = {}", num1, num2, calc.mul())
        }
        "/" => {
            println!("{} / {} = {}", num1, num2, calc.div())
        }
        _ => {

        }
    }
}

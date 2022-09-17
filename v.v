import os

fn main() {
	mut operator := ""
	mut check := 1

	ops_array := ['+', '-', '*', '/']

	for check == 1 {
		operator = os.input('Enter your operator: ')

		if operator in ops_array {
			check = 0
		} else {
			println("Invalid operator detected!")
		}
	}
	

	num1 := os.input('Enter your first number: ')
	num2 := os.input('Enter your second number: ')

	match operator {
		"+" {
			print("Your sum is: ") 
			println(add(num1.int(), num2.int())) 

		}
		"-" { 
			print("Your difference is: ") 
			println(sub(num1.int(), num2.int())) 
		}
		"*" { 
			print("Your product is: ") 
			println(mul(num1.int(), num2.int())) 
		}
		"/" { 
			print("Your quotient is: ") 
			println(div(num1.int(), num2.int())) 
		}
		else { 
			println("End of match") }
	}
}

fn add(x int, y int) int {
	return x + y
}

fn sub(x int, y int) int {
	return x - y

}

fn mul(x int, y int) int {
	return x * y
}

fn div(x int, y int) int {
	return x / y
}

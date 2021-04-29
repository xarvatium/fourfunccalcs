package main

import "fmt"

func main() {
	s := true
	for s {
		if s {
			fmt.Printf("Enter your operator (+, -, *, /, or 'z' to exit): ")
			var operator string
			fmt.Scanln(&operator)

			if operator == "z" {
				fmt.Println("Exiting...")
				s = false
				break
			}

			fmt.Printf("Enter Your First Number: ")
			var first int
			fmt.Scanln(&first)

			fmt.Printf("Enter Second Number: ")
			var second int
			fmt.Scanln(&second)

			switch operator {
			case "+":
				response := fmt.Sprint("The sum of ", first, " and ", second, " is: ", first+second, "\n")
				fmt.Print(response)

			case "-":
				response := fmt.Sprint("The difference of ", first, " and ", second, " is: ", first-second, "\n")
				fmt.Print(response)

			case "*":
				response := fmt.Sprint("The product of ", first, " and ", second, " is: ", first*second, "\n")
				fmt.Print(response)

			case "/":
				response := fmt.Sprint("The quotient of ", first, " and ", second, " is: ", first/second, "\n")
				fmt.Print(response)

			default:
				fmt.Println("Invalid input")
			}
		}
	}
}

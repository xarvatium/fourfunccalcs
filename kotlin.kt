import java.util.Scanner

fun main() {
    val reader = Scanner(System.`in`)
    print("Please select your operator (+, -, *, /): ")
    val operator = readLine()
    print("Please input your first number: ")
    val num1 = reader.nextInt()
    print("Please input your second number: ")
    val num2 = reader.nextInt()
    when(operator) {
        "*" -> {
            val product:Int = num1 * num2
            print("The product of $num1 and $num2 is $product")
        }
        "/" -> {
            if(num2 == 0) {
                println("Error: Cannot divide by 0")
            } else {
                val quotient:Int = num1 / num2
                print("The quotient of $num1 and $num2 is $quotient")
            }
        }
        "+" -> {
            val sum:Int = num1 + num2
            print("The sum of $num1 and $num2 is $sum")
        }
        "-" -> {
            val difference: Int = num1 - num2
            print("The difference of $num1 and $num2 is $difference")
        }
    }
}

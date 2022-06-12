using System;

namespace Calculator
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter your first number: ");
            string firstNum = Console.ReadLine();

            Console.Write("Enter your second number: ");
            string secondNum = Console.ReadLine();

            Console.Write("Enter your operator: ");
            string op = Console.ReadLine();

            switch (op)
            {
                case "+":
                    Console.WriteLine($"The sum of {firstNum} and {secondNum} is {Addition(Convert.ToInt32(firstNum), Convert.ToInt32(secondNum))}");
                    break;

                case "-":
                    Console.WriteLine($"The difference of {firstNum} and {secondNum} is {Subtraction(Convert.ToInt32(firstNum), Convert.ToInt32(secondNum))}");
                    break;

                case "*":
                    Console.WriteLine($"The product of {firstNum} and {secondNum} is {Multiply(Convert.ToInt32(firstNum), Convert.ToInt32(secondNum))}");
                    break;

                case "/":
                    Console.WriteLine($"The quotient of {firstNum} and {secondNum} is {Divide(Convert.ToInt32(firstNum), Convert.ToInt32(secondNum))}");
                    break;
                default:
                    Console.WriteLine("Error");
                    break;
            }
        }

        static int Addition(int first, int second) => first + second; 

        static int Subtraction(int first, int second) => first - second;

        static int Multiply(int first, int second) => first * second; 

        static int Divide(int first, int second) => first / second; 
    }
}

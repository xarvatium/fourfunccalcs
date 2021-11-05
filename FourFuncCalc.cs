/* 
Author: Xarvatium
Description: Just a 4 function calculator in C#, might break
*/

using System;

namespace Calculator
{
    class Program
    {
        static void Main(string[] args)
        {
            int result;
            bool check = true;
            while (check)
            {
                Console.Write("Enter first number: ");
                string firstNum = Console.ReadLine();

                Console.Write("Enter operator (+, -, *, /, 'z' to exit): ");
                string op = Console.ReadLine();

                Console.Write("Enter second number: ");
                string secondNum = Console.ReadLine();


                switch (op)
                {
                    case "+":
                        result = Convert.ToInt32(firstNum) + Convert.ToInt32(secondNum);
                        Console.WriteLine("The result is: " + result);
                        break;
                    case "-":
                        result = Convert.ToInt32(firstNum) - Convert.ToInt32(secondNum);
                        Console.WriteLine("The result is: " + result);
                        break;
                    case "*":
                        result = Convert.ToInt32(firstNum) * Convert.ToInt32(secondNum);
                        Console.WriteLine("The result is: " + result);
                        break;
                    case "/":
                        result = Convert.ToInt32(firstNum) / Convert.ToInt32(secondNum);
                        Console.WriteLine("The result is: " + result);
                        break;

                    case "z":
                        check = false;
                        Console.WriteLine("Exiting...");
                        break;

                    default:
                        Console.WriteLine("Error: Invalid Operator detected, the current acceptable ones are: \"+, -, *, /\"");
                        break;

                }
            }
        }
    }
}

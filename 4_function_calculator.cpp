#include <iostream>
#include <stdlib.h>
#include <string>

int main() {
    double Num1, Num2, Num3;
    char Operator;
    const bool T(true), F(false);

    do {
        std::cout << "Please enter the first number: \n";
        std::cout << "Number 1: ";
        std::cin >> Num1;
        std::cout << "Please enter the operator (+, -, *, / or type X to exit and Z to restart): " << "\n";
        std::cout << "Operator: ";
        std::cin >> Operator;
        
    } while(Operator == 'Z');

    while(!F) {
        switch(Operator) {
            case '+' :
                std::cout << "Enter the second number: \n";
                std::cout << "Second number: ";
                std::cin >> Num2;
                Num3=Num1+Num2;
                std::cout << Num1 << " + " << Num2 << " = " << Num3 << "\n";
                T;
                break;

            case '-' :
                std::cout << "Enter the second number: \n";
                std::cout << "Second number: ";
                std::cin >> Num2;
                Num3  =Num1 - Num2;
                std::cout << Num1 << " - " << Num2 << " = " << Num3 << "\n";
                T;
                break;

            case '*' : 
                std::cout << "Enter the second number: \n";
                std::cout << "Second number: ";
                std::cin >> Num2;
                Num3 = Num1 * Num2;
                std::cout << Num1 << " * " << Num2 << " = " << Num3 << "\n";
                T;
                break;

            case '/' : 
                std::cout << "Enter the second number: \n";
                std::cout << "Second number: ";
                std::cin >> Num2;
                    if (Num2 == 0) {
                        std::cout << "Error: Cannot divide by 0, enter a new divisor: ";
                        std::cin >> Num2;
                }
                    else Num3 = Num1 / Num2;
                    std::cout << Num1 << " / " << Num2 << " = " << Num3 << "\n";
                T;
                break;

            case 'Z' : 
            case 'z' :
                Num1=0;
                std::cout << "Enter first number: \n";
                std::cin >> Num1;
                T;
                break;
            
            case 'X' : 
            case 'x' :
                T;
                exit (0);
            break;


            default:
                F;
                std::cout << "Error: Invalid response " << Operator << " - Please enter a valid operation - Enter X to quit or C to clear" << "\n";
        }
        Num1=Num3;
        std::cout << "Enter a new operator:\n";
        std::cout << "New operator: ";
        std::cin >> Operator;
    }


}



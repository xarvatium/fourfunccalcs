#include <stdio.h>

int main() {
    int num1;
    int num2;
    char operator;

    while (operator != 'z') {
        printf("Operator (+, -, *, /, `z` to exit): ");
        scanf(" %c", &operator);

        if (operator == 'z') {
            printf("Exiting...\n");
            return 0;
        }

        printf("First: ");
        scanf("%d", &num1);

        printf("Second: ");
        scanf("%d", &num2);
        
        calculate(num1, num2, operator);
    }
    return 0;
}

int calculate(int num1, int num2, char op) {
    switch (op) {
    case '+':
            printf("%d %c %d = %d\n", num1, op, num2, num1 + num2);
            break;
        case '-':
            printf("%d %c %d = %d\n", num1, op, num2, num1 - num2);
            break;
        case '*':
            printf("%d %c %d = %d\n", num1, op, num2, num1 * num2);
            break;
        case '/':
            printf("%d %c %d = %d\n", num1, op, num2, num1 / num2);
            break;
        default:
            printf("Invalid input");
    }
    return 0;
}

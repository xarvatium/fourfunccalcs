import java.util.Arrays;
import java.util.Objects;
import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        String[] valid_ops = {"+", "-", "*", "/"};
        String operator = "";
        Scanner user_in = new Scanner(System.in);

        while (!Objects.equals(operator, "z")) {
            while (!Arrays.asList(valid_ops).contains(operator)) {
                System.out.print("Operator (+, -, *, /, `z` to exit): ");
                operator = user_in.nextLine();

                if ("z".equals(operator)) {
                    System.out.println("Exiting...");
                    System.exit(0);
                } else if (!Arrays.asList(valid_ops).contains(operator)) {
                    System.out.println("Invalid operator detected");
                }
            }

            try {
                System.out.print("First number: ");
                String first_num_string = user_in.nextLine();

                int first_num = Helpers.convert(first_num_string);

                System.out.print("Second number: ");
                String second_num_string = user_in.nextLine();
                int second_num = Helpers.convert(second_num_string);

                switch (operator) {
                    case "+" -> System.out.printf("Your sum is: %s%n", Calculations.add(first_num, second_num));
                    case "-" -> System.out.printf("Your difference is: %s%n", Calculations.sub(first_num, second_num));
                    case "*" -> System.out.printf("Your product is: %s%n", Calculations.mul(first_num, second_num));
                    case "/" -> System.out.printf("Your quotient is: %s%n", Calculations.div(first_num, second_num));
                    default -> System.out.println("Your operator was invalid");
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid number detected.");
            }
            operator = "";
        }
    }
}

class Calculations {
    public static int add(int num1, int num2) {
        return num1 + num2;
    }

    public static int sub(int num1, int num2) {
        return num1 - num2;
    }

    public static int mul(int num1, int num2) {
        return num1 * num2;
    }

    public static int div(int num1, int num2) {
        return num1 / num2;
    }
}

class Helpers {
    public static int convert(String num) {
        int val;

        val = Integer.parseInt(num);
        return val;
    }
}

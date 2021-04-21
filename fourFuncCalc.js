const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});


try {
  var readlineSync = require('readline-sync');

  bool = true

  // While loop that loops it until 'z' is entered
  while (bool == true) {
    // Get the operator from the user
    var operator = readlineSync.question("Please enter the expression to be used (*, +, -, /, %, **) or type 'z' to exit: ")

    // Switch statement that checks the operator
    switch (operator) {
      case '+': // Addition
        var firstNum = readlineSync.question("What is your first number? ")
        var secondNum = readlineSync.question("What is your second numder? ")
        var sum = parseInt(firstNum) + parseInt(secondNum)
        console.log(`The sum of ${firstNum} + ${secondNum} is:`,sum)
        break;

      case '-': // Subtraction
        var firstNum = readlineSync.question("What is your first number? ")
        var secondNum = readlineSync.question("What is your second numder? ")
        var difference = parseInt(firstNum) - parseInt(secondNum)
        console.log(`The difference of ${firstNum} - ${secondNum} is:`,difference)
        break;

      case '*': // Multiplication
        var firstNum = readlineSync.question("What is your first number? ")
        var secondNum = readlineSync.question("What is your second numder? ")
        var product = parseInt(firstNum) * parseInt(secondNum)
        console.log(`The product of ${firstNum} * ${secondNum} is:`,product)
        break;
      case '/': // Division
        var firstNum = readlineSync.question("What is your first number? ")
        var secondNum = readlineSync.question("What is your second numder? ")
        var quotient = parseInt(firstNum) / parseInt(secondNum)
        console.log(`The quotient of ${firstNum} / ${secondNum} is:`,quotient)
        break;

      case '%': // Modulo
        var firstNum = readlineSync.question("What is your first number? ")
        var secondNum = readlineSync.question("What is your second numder? ")
        var modulo = parseInt(firstNum) % parseInt(secondNum)
        console.log(`The remainder of ${firstNum} % ${secondNum} is:`,modulo)
        break;

      case '**': // Exponent
        var firstNum = readlineSync.question("What is your first number? ")
        var secondNum = readlineSync.question("What is your second numder? ")
        var result = parseInt(firstNum) ** parseInt(secondNum)
        console.log(`The result of ${firstNum} raised to the power of ${secondNum} is:`,result)
        break;
      
      case 'z': // Exit
        console.log("Exiting...")
        bool = false
        break;

      default: // Invalid Operator
        console.log("Please input an appropiate operator and try again!")
        break;
    }
  }
} catch(MODULE_NOT_FOUND){
  console.log("ERROR: Module Not Found, please ensure you have: readline-sync installed (npm install readline-sync)")
  process.exit(0)
}
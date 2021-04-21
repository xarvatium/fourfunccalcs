#!/bin/zsh

while [ true ]; do

    echo -n "Please input your operator (+, -, *, /, or 'z' to exit): "
    read operator

    if [ $operator = "z" ]; then
    break

    fi
    
    echo -n "Please input your first number: "
    read firstNum

    echo -n "Please input your second number: "
    read secondNum

    # If statement pattern looking for a correct/incorrect operator
    if [ $operator  = "+" ]; then

        sum=$(( $firstNum + $secondNum ))
        echo "The sum of $firstNum and $secondNum is $sum"
    
    elif [ $operator = "-" ]; then

        difference=$(( $firstNum - $secondNum ))
        echo "The difference of $firstNum and $secondNum is $difference"
    
    elif [ $operator = "*" ]; then

        product=$(( $firstNum * $secondNum ))
        echo "The product of $firstNum and $secondNum is $product"
    
    elif [ $operator = "/" ]; then

        if [ $secondNum = "0" ]; then
            echo "Sorry, you can't divide by zero."
        
        else

            quotient=$(( $firstNum / $secondNum ))
            echo "The quotient of $firstNum and $secondNum is $quotient"
        
        fi
    
    else

        echo "Invalid operator, please try again"
    
    fi

done
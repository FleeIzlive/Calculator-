while 1:     
    firstnum = float(input("Enter the first number: "))   # Asks user the first number
    secondnum = float(input("Enter the secon number: "))  # Asks user the second number
    asdm = input("What you wanna do? (a) for addition, (s) for subtraction, (d) for division, (m) for multiplication: ") 

    if asdm == 'a' or asdm == 'A':      # If statement for addition
        sum = firstnum + secondnum
        print("Your answer: ",sum)

    elif asdm == 's' or asdm == 'S':    # Elif statement for subtraction 
        difference = firstnum - secondnum  
        print("Your answer: ",difference)   

    elif asdm == 'd' or asdm == 'D':     # Elif statement for division
        quotient = firstnum // secondnum
        print("Your answer: ",quotient)

    elif asdm == 'm' or asdm == 'M':    # Elif statement for multiplication
        product = firstnum * secondnum
        print("Your answer: ",product)

    conti = input("Do you wanna continue (y/n): ")    # Asks user if they wanna continue using the calculator

    if conti == 'n' or conti == 'N':    # If statement if they don't wanna continue
        print("Goodbye!")
        break

    elif conti == 'y' or conti == 'Y':   # Elif statement if they wanna continue 
        print("Alright!")







    
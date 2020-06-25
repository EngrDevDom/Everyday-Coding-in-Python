""" Solving a System of Linear Equations
    Author: GM Jackson """
import Matrix as m
flag = "y"
while flag == "y":
    # Initialize variables:
    n = 0       # Number of equations and variables
    k = 0       # tracking f array. We want the biggest equation last and the smallest first.
    fir = 0     # for first equation of a sum pair
    sec = 0     # for second equation of a sum pair
    count = 0   # track b array
    i = 0
    j = 0
    r = 0
    matrix = []     # The equation matrix for variable coefficients
    mat_sum = []    # store equation m
    num_sum = []    # store constant m
    number = []     # The constants at the right side of the equal sign
    x = []          # The variable values
    comp = []       # computation list
    temp = []       # ditto
    comps = []      # ditto
    temps = []      # ditto
    # ////////// HOW MANY ROWS AND COLUMNS //////////
    flag2 = 0
    while flag2 == 0:
        try:
            n = int(input("How many rows and columns?\n"))
        except ValueError:
            print("Apparently, there's a failure to communicate!")
        else:
            flag2 = 1
    k = n   # store n in k for processing later
    matrix = m.Matrix(n,n)
    matrix = matrix.ini_matrix()
    mat_sum = m.Matrix(n,n)
    mat_sum = mat_sum.ini_matrix()
    num_sum = m.Matrix(n)
    num_sum = num_sum.ini_matrix()
    number = m.Matrix(n)
    number = number.ini_matrix()
    x = m.Matrix(n)
    x = x.ini_matrix()
    comp = m.Matrix(2,n)
    comp = comp.ini_matrix()
    temp = m.Matrix(2,n)
    temp = temp.ini_matrix()
    comps = m.Matrix(2)
    comps = comps.ini_matrix()
    temps = m.Matrix(2)
    temps = temps.ini_matrix()
    # ////////// DATA INPUT //////////
    for i in range(0,n):
        for j in range(0,n):
            flag2 = 0
            while flag2 == 0:
                try:
                    matrix[i][j] = float(input("Enter index " + str(i) + str(j) + ":\n"))
                except ValueError:
                    print("Did you eat paint chips when you were a kid? Try again!")
                else:
                    flag2 = 1
        # do the constant vector
        flag2 = 0
        while flag2 == 0:
            try:
                number[i] = float(input("Enter constant:\n"))
            except ValueError:
                print("OK, which parent dropped you on your head? Try again!")
            else:
                flag2 = 1
    # ///////////////////////// STORE FIRST EQUATION /////////////////////////
    while k > 0:
        # /////// TAKE EQUATIONS TWO AT A TIME AND COMPUTE NEW EQUATIONS WITH FEWER VARIABLES ///////
        fir = 0     # set up for first two equations
        sec = 1
        while sec < k:
        # Extract equations from matrix and number and put them into comp and comps
            for j in range(0,k):
                comp[0][j] = matrix[fir][j]
                comp[i][j] = matrix[sec][j]
            # /////// end for j //////////
            comps[0] = number[fir]
            comps[1] = number[sec]
            # Multiply first equation by last coefficient of second
            # Store result in temp arrays
            for j in range(0,k):
                temp[0][j] = comp[0][j] * comp[1][k-1]
            # ////////// end for j //////////
            temps[0] = comps[0] * comp[1][k-1]
            # Multiply second equation by -last coefficient of first
            # Store result in temp arrays
            for j in range(0,k):
                temp[1][j] = comp[1][j] * -1 * comp[0][k-1]
            # /////// end for j ///////
            temps[1] = comps[1] * -1 * comp[0][k-1]
            # /////// Add temp1 and temp2 and store in b array
            for j in range(0,k):    # start with 2 since 1 should be zero out when first terms are added
                mat_sum[count][j] = temp[0][j] + temp[1][j]
            # /////// end for j ///////
            num_sum[count] = temps[0] + temps[1]
            # Process next pair of equations
            fir += 1
            sec += 1
            count += 1
        # /////// end while sec < k ////////////////////////////////////////////
        # copy mat_sum into matrix and num_sum into number
        count = 0   # reset count
        k -= 1      # decrement k
        for i in range(0,k):
            for j in range(0,k+1):
                matrix[i][j] = mat_sum[i][j]
            # /////// end for j ///////
            number[i] = num_sum[i]
        # /////// end for i ///////
        # We are now full circle.
    # ///////// end while k > 0 ///////////////////////////////////////////////
    # ///////// SOLVE THE VARIABLES /////////
    i = 0
    j = 0
    while j < n:
        # solve x
        x[i] = number[i]/matrix[i][j]
        i += 1
        if i == n:
            break
        r = j   # store the value of j
        while j > -1:   # /////// Process each variable when there are multiple variables
            number[i] -= matrix[i][j] * x[j]    # /////// substitute value for x in the next equation,
            matrix[i][j] = 0    # /////// subtract from the left side to eliminate the variable
            j -= 1  # move back a variable and substitute its value
        # /////// end j -= 1 ///////////////////////////////////////////////
        j = r + 1   # restore the original value of j
        # increment and solve for y or the next variable
    # /////// end while j < n /////////////////////////////////////////////
    # /////// LIST RESULTS ////////////////////////////////////////////////
    print()
    for i in range(0,n):
        print("X" + str(i) + " = " + str(round(x[i],2)))
    # /////// end for i //////////////////////////////////////////////////
    flag = input("Solve another system? y=yes; n=no:\n")
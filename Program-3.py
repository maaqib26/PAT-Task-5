def fib(n):

    lst=[0,1]
    # Initialize the list with the first two Fibonacci numbers

    list(map(lambda i: lst.append(lst[-2]+lst[-1]), range(2,n)))
    # Calculate the next Fibonacci number by adding the last two numbers in the list and Append the next Fibonacci number to the list

    print("First", n, "fibonacci series: \n",)
    print(lst)
    # Print the Fibonacci series

fib(10)
# Call the fib function to generate the Fibonacci series up to the 50th term
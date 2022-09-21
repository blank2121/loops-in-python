# in coding, the break keyword is very important.
# here are some examples of how to use it!



numberList = [1,2,7,3,10,20,15,-10,5,9,13]

# say we want to find the first number in the list that is divisable
# by 3. we can use the power of loops and the break keyword to do so


for num in numberList:
    if num % 3 == 0:
        print("we found the number!!!")
        print(num)
        break


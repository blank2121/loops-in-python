# recursive looping is typically harder to learn and implement but it can be very
# helpful in some situations. for example the factorial function


# the factorial function takes in a number and multiplies it by itself minus 1 until it
# is 0. here is an example: f(10) = 10*9*8*7*6*5*4*3*2*1



def factorial(number):
    if number == 1:
        return 1
    
    else:
        return number * factorial(number-1)


# to get a good grasp of recursion I recommend you look up a video on it because a visual
# aid is helpful to full understand recursion. But this is a very simple example so just think
# about how this runs in your head.

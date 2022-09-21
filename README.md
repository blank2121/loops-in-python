
# Loops in Python


License:

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

In python, as well as other languages, loops are a way to run
a segment of code over and over. Loops can loop just once or
indefinetly, or until a condition is satisfied.

Finally, there are two important keywords for loops: ```break``` and ```continue```.
What break does is it exits the current loop and continue will skip the code in the current
loop's iteration. Break is more commonly used than continue but it is still good to have an idea of what continue is and does.

Here are some examples of loops in python!


---

### while loops:

```
i=0
while i != 10:
    print(i)
    i = i+1
```

The simplest way to describe a while loop is to imagine it as an if statement but the code in
the if statement will be ran over and over until the if statement is false. Run this code snippet
to see for yourself.

---

### for loops:

```
# this will loop over the print statement 10 times total
for i in range(10):
    print(i)

# this will loop over each indice of a list
aToE = ['a', 'b', 'c', 'd', 'e']
for letter in aToE:
    print(letter)
```

For these two examples, I suggest you run them as well to see their output.

---

### recursion loops:

```
def factorial(x):
    if x == 1:
        return 1

    else:
        return x * factorial(x-1)
```

In short, recursion is when a function calles itself and in this case we are calling the function
to multiply the input by itself minus 1

---

I hope that this brief into to loops was help full to some and if you want to see more, check out
the code examples in the loops folder. Have a lovely day. 

:)

---

## Author

[@blank2121](https://www.github.com/blank2121)


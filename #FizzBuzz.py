#FizzBuzz

for n in range(1,101):
    if n%4 == 0 and n%3 == 0:
        print(str(n)+ " FizzBuzz")
    elif n%4 == 0:
        print(str(n)+ " fizz")
    elif n%3 == 0:
        print(str(n)+ " buzz")
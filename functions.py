def example():
    print("basic function")
    z = 3 + 9
    print(z)


example()

def simple_add(num1, num2):
    answer = num1 + num2
    print("num1 is ", num1)
    print(answer)

simple_add(5,3)

#default function param
def simple(num1, num2 = 5) :
    print(num1, num2)

simple(2)

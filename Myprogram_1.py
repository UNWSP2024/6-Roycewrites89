#Royce Daniel 2/27/2026 "hundred dice avg"
import random
def randice():
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    subtotal = num1 + num2
    return subtotal

def main():
    total_sum = 0
    for i in range(100):
     endresult = randice()
     total_sum += endresult
    total =  total_sum / 100
    print("and that's", total)

main()
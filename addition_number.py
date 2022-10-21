
# Function Body
def add_numbers(n1,n2):
    sum_of_numbers = n1 + n2
    return sum_of_numbers

# Main Body
if __name__ == "__main__":
    a = float(input("Enter first number: ")).strip()
    b = float(input("Enter second number: ")).strip()
    addition = add_numbers(a,b)
    print("The sum is",addition)
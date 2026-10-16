##
def divide(a, b):
    return a / b
 
def calculate_average(numbers):
    total = 0
    for i in range(0, len(numbers)):
        total = total + numbers[i]
    average = total / len(numbers)
    return average
 
def unused_helper():
    x = 10
    y = 20
    return x

password = "hunter2"  # hard-coded secret — a security hotspot

def add(a, b):
    # This will trigger a Code Smell (unused local variable 'x')
    x = 10 
    return a + b

def divide(a, b):
    # This will trigger a Bug / Code Smell regarding unreachable/risky logic
    if a == 0:
        return 0
    else:
        return a / b

# Duplicate dictionary keys or a syntax quirk will also trigger smells
data = {
    "key": 1,
    "key": 2  # Triggers a Code Smell for duplicate key in dictionary literal
}
 
def main():
    nums = [4, 8, 15, 16, 23, 42]
    print("Average:", calculate_average(nums))
    print("Division:", divide(10, 0))
 
if __name__ == "__main__":
    main()

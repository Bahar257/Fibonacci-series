def fibonacci_by_terms(n):
    a, b = 0, 1
    print(f"Fibonacci series ({n} terms):", end=' ')
    for _ in range(n):
        print(a, end=', ' if _ < n - 1 else '\n')
        a, b = b, a + b

def fibonacci_by_max_value(max_value):
    a, b = 0, 1
    print(f"Fibonacci series (up to {max_value}):", end=' ')
    first = True
    while a <= max_value:
        if not first:
            print(', ', end='')
        print(a, end='')
        a, b = b, a + b
        first = False
    print()

def main():
    while True:
        print("\n1. Fibonacci by terms\n2. Fibonacci by max value\n3. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            n = int(input("Enter the number of terms: "))
            fibonacci_by_terms(n)
        elif choice == '2':
            max_value = int(input("Enter the maximum value: "))
            fibonacci_by_max_value(max_value)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid, try next time.")

if __name__ == "__main__":
    main()
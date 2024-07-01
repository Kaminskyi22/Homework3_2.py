while True:
    symbol = input("Enter a symbol: ")
    number = int(input("Enter a number: "))
    
    if number < 0:
        print("Invalid input. Number must be non-negative.")
        continue

    for i in range(number):
        print(symbol)
    
    choice = input("Do you want to continue? (yes/no): ")
    if choice == 'no':
        break

print("Goodbye!")

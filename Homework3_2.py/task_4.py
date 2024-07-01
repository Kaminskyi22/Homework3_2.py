total_sum=0
max_num=0
min_num=0
num_count=0

while True:
    try:
        num = float(input("Enter a number (DONT ENTER 7):  "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    num_count+=1

    if num<0:
        print("Invalid input. Number must be non-negative.")
        continue
    if num==7 or num_count==10:
        print("Goodbye!")
        break

    total_sum+=num

    if max_num==0 or num>max_num:
        max_num=num
    
    if min_num==0 or num<min_num:
        min_num=num

print("Sum of numbers: ",total_sum)
print("Max number: ",max_num)
print("Min number: ",min_num)
print("Goodbye!")
while True:
    start= int(input("Enter the start of the range: "))
    end= int(input("Enter the end of the range: "))
    
    if start>end:
        start,end=end,start
    
    even_sum=0
    even_count=0
    odd_sum=0
    odd_count=0
    mult_9_sum=0
    mult_9_count=0
    for i in range(start,end+1):
        if i%2==0:
            even_sum+=i
            even_count+=1
        else:
            odd_sum+=i
            odd_count+=1
        if i%9==0:
            mult_9_sum+=i
            mult_9_count+=1
    
    avg_even = 0
    avg_odd = 0
    avg_mult_9 = 0    
    
    if even_count>0:
        avg_even=even_sum/even_count
    else:
        print("No even numbers in the range")
    
    if odd_count>0:
        avg_odd=odd_sum/odd_count
    else:
        print("No odd numbers in the range")

    if mult_9_count>0:
        avg_mult_9=mult_9_sum/mult_9_count
    else:
        print("No multiples of 9 in the range")
    
    print("Sum of even numbers: ",even_sum)
    print("Sum of odd numbers: ",odd_sum)
    print("Sum of multiples of 9: ",mult_9_sum)
    print("Average of even numbers: ",avg_even)
    print("Average of odd numbers: ",avg_odd)   
    print("Average of multiples of 9: ",avg_mult_9)

    choice= input("Do you want to continue? (yes/no): ")
    if choice =='no':
        break   

print("Goodbye!")
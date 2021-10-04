n=int(input())
last_digit=n%10
middle_digit=(n//10)%10
frist_digit=n//100
print(middle_digit+last_digit+frist_digit)
import random
def guess(no1,no2,choice):
     result=0
     if choice=='1':
         result=no1+no2
         print(result)
     elif choice=='2':
         result=no1-no2
         print(result)
     elif choice=='3':
         result=no1*no2
         print(result)
     elif choice=='4':
         result=no1/no2
         print(result)
     else :
         print("wrong option")

print("choose operation from the below menu ")
print("1.add")
print("2.sub")
print("3.multiply")
print("4.divide")
choice=input("enter option no.")
no1=int(input("Enter No.1"))
no2=int(input("Enter No.2"))
guess(no1,no2,choice)
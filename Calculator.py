a  = int(input("Enter first number\n"))
b =int (input("\nEnter second number\n"))

c = int(input("Enter choice \n 1 for addition \n 2 for subtraction\n"))

if c == 1 : 
    print("Result after adding" +str(a+b))

elif c==2 :
     if a > b:
         print("Result after subtraction " +str(a-b))
     else :
         print("Result after subtraction " +str(b-a))

else:
    print("Wrong Choice")

         
   
       








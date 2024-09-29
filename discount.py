
# program to compute discount
total_amount =float(input("Enter the amount of purchase: "))
if total_amount > 1000:
    discount=0.05* total_amount
    price_after_discount =total_amount-discount 
    print("The discount is", discount)
    print("Price after discount is", price_after_discount)
    
else :
    print("No discount")



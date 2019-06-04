Membercard = 1234
totall = 0
discount = 0
prices = 0
price = 0
i = 0
true = True
amountProduct = 0
print("Put the quantity of product then put product name and also price!")
amountProduct = int(input("input the quantity of product: "))
while true:
    amountPro = input("Product : ")
    price = int(input(f"Price of {amountPro} :"))
    print(f">>{amountPro} : ${price}")
    prices += price
    i += 1
    if i == amountProduct:
        break
Memcard = input("""
    Do you have Member_Card?
    Type:
    YES   ,   NO
    """)
if Memcard.lower() == 'yes':
    Membercard1 = int(input("Please Enter you PIN card : "))
    if Membercard1 == Membercard:
        totall = prices
        discount = totall * 0.90
        totall = discount
        print(f"""
        Discount : 10%
        Totall: {totall}
        """)
    else:
        print("You PIN is invalid.")
        totall = prices
        print(f"""
        Discount : 0%
        Totall : {totall}
        """)
elif Memcard.lower() == 'no':
    totall = prices
    print(f"""
        Discount : 0%

        Totall : {totall}
        """)
else:
    print("Sorry ! I don't understand!")

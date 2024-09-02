# Program Name: Lab2.py (use the name the program is saved as)
# Course: IT1114/Section XXX
# Student Name: John Doe
# Assignment Number: Lab#
# Due Date: xx/xx/ 20XX
# Purpose: What does the program do (in a few sentences)
# List Specific resources used to complete the assignment

def main():
    #constants
    pizzacost = 15.99
    saladcost = 7.99
    slicesperpizza = 12
    slicesperperson = 3
    discountrate = .15
    deliveryrate = .07
    mindeliveryfee = 20.0

    #input from user
    numofpizzasorder = int(input("Numbers of pizzas ordered: "))
    numofsaladsorder = int(input("Number of salads ordered: "))

    #calculation of pizza needed
    pizzaneeded = -(-numofpizzasorder * slicesperperson // slicesperpizza)
    #43*3//12

    #calculations of costs before discounts
    saladcost = numofsaladsorder * saladcost
    pizzacost = pizzaneeded * pizzacost

    #discounts
    pizzadiscount = pizzacost * discountrate if pizzaneeded > 10 else 0
    salad_discount = saladcost * discountrate if numofsaladsorder > 10 else 0
    totaldiscount = pizzadiscount + salad_discount

    #calculate delivery fee
    total_amount_before_discount = saladcost + pizzacost
    deliveryfee = max(total_amount_before_discount * deliveryrate, mindeliveryfee)

    #totalamount
    totalamount = total_amount_before_discount - totaldiscount +deliveryfee

    #output
    print(f"Pizza cost: {pizzacost}")
    print(f"Salad cost: {saladcost}")
    print(f"Total Amount: {total_amount_before_discount}")
    print (f"Discount: {totaldiscount}")
    print (f"Delivery Fee: {deliveryfee}")
    print (f"Total Amount Due: {totalamount}")


    #entry point
if __name__ == "__main__":
    main()


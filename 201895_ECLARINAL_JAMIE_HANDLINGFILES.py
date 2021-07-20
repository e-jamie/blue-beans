products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

# CODE CELL
# PROBLEM 1

def get_product(code):
    return products[code]

# CODE CELL
# PROBLEM 2

def get_property(code, property):
    return products[code][property]

# CODE CELL
# PROBLEM 3

def main():
    order = ""
    summary = {}
    acount = 0
    bcount = 0
    ccount = 0
    dcount = 0
    ecount = 0
    fcount = 0
    total = 0

    while True:
        order = input("Enter order {product_code},{quantity}: ")
        #sample input: cappuccino,1
        
        if order != "/":
            prod_code, quant = order.split(",")
            summary[prod_code] = get_product(prod_code)
            
            if prod_code == "americano":
                acount += 1*int(quant)
                summary[prod_code]["quantity"] = acount
            elif prod_code == "brewed coffee":
                bcount += 1*int(quant)
                summary["brewedcoffee"]["quantity"] = bcount
            elif prod_code == "cappuccino":
                ccount += 1*int(quant)
                summary["cappuccino"]["quantity"] = ccount
            elif prod_code == "dalgona":
                dcount += 1*int(quant)
                summary["dalgona"]["quantity"] = dcount
            elif prod_code == "espresso":
                ecount += 1*int(quant)
                summary["espresso"]["quantity"] = ecount
            elif prod_code == "frappuccino":
                fcount += 1*int(quant)
                summary["frappuccino"]["quantity"] = fcount
            
            total += get_property(prod_code, "price")*int(quant)
        
        else:
            break
            
    with open("receipt.txt", "w") as file:
        file.write('''
==
CODE\t\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL''')
        
        for i in summary:
            code = i
            name = summary[i]["name"]
            price = summary[i]["price"]
            quantity = summary[i]["quantity"]
            subtotal = int(price)*int(quantity)
            file.write(f'''
{code}\t\t\t{name}\t\t\t{quantity}\t\t\t{subtotal}''')
            
        file.write(f'''

Total:\t\t\t\t\t\t\t\t\t\t{total}
==
''')

main()
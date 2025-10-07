diesel_price = 1.90
gas_price = 2.50

fuel_type = input("Enter the type of fuel (G or D): ")

if fuel_type != 'D' and fuel_type != 'd' and fuel_type != 'G' and fuel_type != 'g':
    print("Invalid fuel type")
    exit()

liters = float(input("Enter the number of liters: "))



if fuel_type == 'D' or fuel_type == 'd':
    if liters <= 20:
        subtotal = diesel_price * liters
        diesel_discount = 0.03 * subtotal
    else:
        subtotal = diesel_price * liters
        diesel_discount = 0.05 * subtotal
    price = (diesel_price * liters) - diesel_discount
elif fuel_type == 'G' or fuel_type == 'g':
    if liters <= 20:
        subtotal = gas_price * liters
        gas_discount = 0.04 * subtotal
    else:
        subtotal = gas_price * liters
        gas_discount = 0.06 * subtotal
    price = (gas_price * liters) - gas_discount


print("You have used", liters, "liters. Your bill is", round(price,2), "CAD")

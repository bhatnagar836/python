walmart_sp = input("Enter walmart selling price\n")
sams_cp = input("Enter sam's total cost price\n")
price_difference = round(float(walmart_sp)-float(sams_cp), 3)
print("Total price difference = ", price_difference)
if price_difference < 0:
    print("*********    We are having a loss!    *******\n*******    Don't place order please!    *********")
else:
    walmart_share = round((float(price_difference) * 0.15), 3)
    print("Walmart's share =", walmart_share)
    net_profit = float(price_difference) - float(walmart_share)
    clients_profit = round((float(net_profit) * 0.75), 3)
    hs_profit = round((float(net_profit) * 0.25), 3)
    print("Client's profit = ", clients_profit, "\n HS profit = ", hs_profit)
    if hs_profit < 1:
        print("*********    We are having very less profit!    *********")
    else:
        print("*********    We are having good profit! Continue ordering please    *********")





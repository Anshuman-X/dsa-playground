def Fractinal_Knapsack(price,items_wt,capacity):
    n = len(items_wt)
    
    items= [(price[i],items_wt[i],price[i]/items_wt[i]) for i in range(n)]
    
    for i in range(n):
        for j in range(i+1,n):
            if items[i][2] < items[j][2]:
                items[i],items[j] = items[j],items[i]
                
    profit = 0.0
    
    for price,items_wt,perkgprice in  items:
        if capacity >= items_wt:
            capacity = capacity - items_wt
            profit = profit + price
        else:
            profit = profit + perkgprice*capacity

    return profit

items_wt = [7,3,4,5]
price = [24,21,12,10]
capacity = 20
print("Total Profit is",Fractinal_Knapsack(price,items_wt,capacity))

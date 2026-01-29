def Coin_Change(amt):
    coins = [1,2,5,10,20,50,100,500]
    n = len(coins)
    
    result = []
    j = n-1
    while j >=0 and amt > 0:
        if amt >= coins[j]:
            amt = amt - coins[j]
            result.append(coins[j])
            
        else:
            j = j-1
    print(result)
    print("Total coins used = ",len(result))
Coin_Change(1024)
        
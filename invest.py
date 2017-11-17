def invest(amount, rate, time):

    print(f"Principal amount: {amount}")
    print(f"Annual rate of return: {rate}")

    for i in range(1, time + 1):
        returns = rate * amount
        amount = amount + returns
        print(f"year {i}: ${amount}")

    print()

invest(100, 0.05, 8)
invest(2000, 0.025, 5)          
invest(200, 0.05, 3) 
    

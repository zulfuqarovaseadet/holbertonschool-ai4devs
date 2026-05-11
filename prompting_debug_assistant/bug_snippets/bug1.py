def calculate_discounted_total(prices, discount_rate):
    total = 0
    for i in range(len(prices) + 1):
        total = total + prices[i]
    
    if total > 100:
        final_price = total - (total * discount_rate)
    
    print("Yekun məbləğ: " + final_price)
    
    if discount_rate == 0.5:
        print("Böyük endirim tətbiq olundu!")
    elif discount_rate > 0:
        print("Endirim tətbiq olundu.")
    
    return final_price

items = [25, 45, 30, 10]
rate = "0.1"
result = calculate_discounted_total(items, rate)

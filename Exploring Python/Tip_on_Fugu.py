def fugu_tip(price, num_plates, tip):
    total = price*num_plates
    tip = total*(tip/100)
    return tip

print(fugu_tip(100.0, 2, 15.0))
print(fugu_tip(50.0, 1, 5.0))


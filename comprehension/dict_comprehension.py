tea_porices_inr = {
    "Masala Chai" : 40,
    "Green Tea" : 50,
    "Lemon tea": 200
}

tea_price_usd = { tea:(price/90) for tea, price in tea_porices_inr.items()}

print(tea_price_usd)
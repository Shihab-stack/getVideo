capital = {"Usa": "washington dc",
           "India": "New delhi",
           "Bangladesh": "Dhaka",
           "Pakistan": "Karachi",
           "England": "London",
           }

capital.update({"Germany": "Berlin", "Key": "Value"})
capital_key = capital.keys()
for key in capital_key:
    print(key)
for value in capital.values():
    print(value)
for k, v in capital.items():
    print(f"{k} : {v}")

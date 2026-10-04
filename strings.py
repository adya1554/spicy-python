laptops = "hp, lenovo, asus, dell, infinix, samsung, motorola, acer"
print(f"\nlaptops  : {laptops} ")
print(f" \nlaptops in upper case {laptops.upper()}")
print(f"\nlaptops in lower case {laptops.lower()}")
li = laptops.split(", ")
print("\n",li)
strr = ", ".join(li)
print(f"\n{strr}")

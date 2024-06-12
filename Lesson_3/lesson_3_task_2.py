from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Apple", "iPhone X", "+79123456789")
phone2 = Smartphone("Samsung", "Galaxy S10", "+79234567890")
phone3 = Smartphone("Huawei", "P30 Pro", "+79345678901")
phone4 = Smartphone("Xiaomi", "Mi 9", "+79456789012")
phone5 = Smartphone("Google", "Pixel 3", "+79567890123")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
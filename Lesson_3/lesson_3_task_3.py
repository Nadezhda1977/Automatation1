from address import Address
from mailing import Mailing

to_address = Address("357100", "Невинномысск", "Улица Приозёрная", "Дом 1", "А")
from_address = Address("654321", "Санкт-Петербург", "Улица 2", "Дом 2", "Квартира 2")
cost = 1000
track = "ABCD1234"

mail = Mailing(to_address, from_address, cost, track)

print(f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} "
      f"в {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, {mail.to_address.house}, {mail.to_address.apartment}. Стоимость {mail.cost} рублей.")
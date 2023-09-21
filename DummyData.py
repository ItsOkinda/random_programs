#make sure you install faker library 

from faker import Faker
from faker.providers import internet
fake = Faker()

print("Name :" +fake.name())
print("Address :" +fake.address())
print("Random text :"+ fake.text())
print("E-mail :"+fake.email())
print("Country :"+fake.country())
print("Location :" )
print(fake.latitude(),fake.longitude())
print("URL :"+fake.url())
print("ISP :")
print(fake.add_provider(internet))

print("Ip Address" +fake.ipv4_private())

#print(fake.random.getstate())
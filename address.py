class Address:
 def __init__(self, house_number, street, apartment, city, state, zipcode): 
    self.house_number = house_number 
    self.street = street 
    self.apartment = apartment 
    self.city = city 
    self.state = state 
    self.zipcode = zipcode
 def __str__(self): return f"{self.house_number} {self.street}, {self.city}, {self.state} {self.zipcode}" 
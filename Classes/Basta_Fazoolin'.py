class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return "Address of the restaurant: {address}".format(address=self.address)
  def available_menus(self, time):
    self.time = time
    print("For this time current menu(s) available:")
    for available_menu in self.menus:
      if time >= available_menu.start_time and time <= available_menu.end_time:
        print("{menu}".format(menu=available_menu))

  
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
    
  def calculate_bill(self, purchased_items):
    self.purchased_item = purchased_items
    bill = 0
    for keys, values in self.items.items():
      for item in purchased_items:
        if item in keys:
          bill += values
    return bill
    
  def __repr__(self):
    return "Name of the menu: {name}. Available: from {start_time} to {end_time}".format(name=self.name, start_time=self.start_time, end_time = self.end_time)
  
  
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}


brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)
early_bird_menu = Menu("Early Bird", early_bird_items, 1500, 1800)
dinner_menu = Menu("Dinner", dinner_items, 1700, 2300)
kids_menu = Menu("Kids", kids_items, 1100, 2100)


menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)


franchises = [flagship_store, new_installment]

first_business = Business("Basta Fazoolin' with my Heart", franchises)

#print(first_business.franchises)
#Arepa 
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu = Menu("Take a'Arepa", arepas_items, 1000,2000)
arepas_place = Franchise("189 Fitzgerald Avenue12 East Mulberry Street", [arepas_menu])
arepa_business = Business("Take a' Arepa", [arepas_place])

print(arepa_business.franchises[0].menus[0].items)
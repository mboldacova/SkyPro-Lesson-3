from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 12", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S21", "+79234567890"))
catalog.append(Smartphone("Apple", "iPhone 14", "+79587699307"))
catalog.append(Smartphone("Google", "Pixel 5", "+79456789012"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79567890123"))

for phone in catalog:
    print(f"{phone.phone_maker} - {phone.model}. {phone.phone_number}")
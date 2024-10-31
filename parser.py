import cianparser

# Берем прокси из файла если воможно
proxies = []
try:
    with open('proxies.txt', 'r') as file:
        proxies = [line.strip() for line in file if line.strip()]
        if proxies == []:
            print("Proxy file loaded, but it`s empty")
        else:
            print("Proxy loaded")
except Exception as proxy_load_error:
    print(f"Something is wrong with proxies: {proxy_load_error}")

# Немного данных для парсера
rooms = [1, 2, 3, 4, 5, 6, "studio"]
cities = ["Москва", "Московская область"]

# Парсим
for city in cities:
    for room in rooms:
        parser = cianparser.CianParser(location=city, proxies=proxies)
        data = parser.get_flats(deal_type="sale", rooms=room, with_saving_csv=True, with_extra_data=True)
        print(data)
import cianparser
import pandas

# Берем прокси из файла если возможно
proxies = []
try:
    with open('proxies.txt', 'r') as file:
        proxies = [line.strip() for line in file if line.strip()]
        if proxies == []:
            print("Proxy file loaded, but it`s empty")
        else:
            print("Proxy loaded")
except Exception as proxy_load_error:
    print(f"Something is wrong: {proxy_load_error}")

# Немного данных для парсера
cities = ["Москва", "Московская область"]
rooms = [1, 2, 3, 4, 5, "studio"]

# Парсим
for city in cities:
    for room in rooms:
            print(f"Start parsing with next parameters: City: {city} Rooms: {room}")
            parser = cianparser.CianParser(location=city, proxies=proxies)
            print("Parser initialized")
            data = parser.get_flats(deal_type="sale", rooms=room, with_saving_csv=True, additional_settings={"start_page": 1, "end_page": 1}, with_extra_data=True)
            print("Parsing started")
            table = pandas.DataFrame(data)
            table.to_csv('cian_parsed.csv', mode='a', header=False, index=False)
            print(table)
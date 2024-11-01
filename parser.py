import cianparser
import pandas
import time

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
cities = ["Московская область"]
rooms = [1, 2, 3, 4, 5, "studio"]

# Парсим
for city in cities:
    for room in rooms:
        for page in range(1, 54):
            print(f"Start parsing with next parameters: City: {city} Rooms: {room} Page: {page}")
            parser = cianparser.CianParser(location=city, proxies=proxies)
            data = parser.get_flats(deal_type="sale", rooms=room, with_saving_csv=True, additional_settings={"start_page": page, "end_page": page}, with_extra_data=True)
            table = pandas.DataFrame(data)
            table.to_csv('cian_parsed.csv', mode='a', header=False, index=False)
            print(table)
            time.sleep(5)
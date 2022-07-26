import requests
from bs4 import BeautifulSoup
import csv

url = 'https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D0%B0_%D0%9A%D0%B8%D1%80%D0%B3%D0%B8%D0%B7%D0%B8%D0%B8'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

tbody = soup.find('tbody')

# Шапка таблицы
table_header = soup.find('table')
header = table_header.find_all('tr')
header_list= header[0]


hat_list = []
for element in header_list:
    if element.text == '\n':
        continue
    else:
        title = element.text
    hat_list.append(title)

# Основной список
body_list = []
for tbody_list in tbody.findAll('tr'):
    list_string = []

    for element_tbody in tbody_list.findAll('td'):
        title = element_tbody.text
        list_string.append(title)
    body_list.append(list_string)

body_list.remove([])


city_link_list = []

# Ссылки городов
link_list = tbody.find_all('tr')

for link_element in link_list:
    g = link_element.find('a').get('href')
    https_wiki = 'https://ru.wikipedia.org/' + g
    city_link_list.append(https_wiki) 


# Флаг
tbody = soup.find('tbody')
flag_city = []

for element in tbody.find_all('tr'):
    if element.find('a', 'image') != None:
        flag_city.append('http' + element.find('a', 'image').find('img')['src'])
    else:
        flag_city.append('')


# Соединение списка с ссылками и основного списка
city = []
number_link = 0

for element_list in body_list: 
    element_list.append(link_list[number_link])
    number_link += 1
    city.append(element_list)


# Соединение основного списка с флагами
number_flag = 0
city_list = []

for element in city:
    element[2] = flag_city[number_flag]
    city_list.append(element)
    number_flag += 1


# Запись в файл
with open('city_file.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(hat_list)
    for element_table in city_list:
        write.writerow(element_table)
    

        
        

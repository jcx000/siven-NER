# coding:utf-8
import requests
from ner.api import recognize

file_object = open('E:\\ProgramCode\\Python\\Newsdata\\test.txt', encoding="utf-8", errors='ignore')
for i in range(50):
    sentence = file_object.readline()
    cols = sentence.split('\t')
    predict = recognize(cols[4])

    address = predict['G'].pop()
    print(address)
    url= 'http://api.map.baidu.com/geocoder?output=json&key=obe7bB3EW1O38CWxwhBSA7Y37cnYT4od&address='+str(address)
    response = requests.get(url)
    answer = response.json()
    try:
        lon = float(answer['result']['location']['lng'])
        lat = float(answer['result']['location']['lat'])
        print(lon,lat)
    except Exception:
        print("索引失败")

    print("\n")
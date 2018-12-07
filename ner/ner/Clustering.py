# coding:utf-8
import requests
from ner.util import date_to_num
import pandas as pd


def newTable(file_write, cols, address):

    print(address)
    url = 'http://api.map.baidu.com/geocoder?output=json&key=obe7bB3EW1O38CWxwhBSA7Y37cnYT4od&address=' + \
        str(address)
    response = requests.get(url)
    answer = response.json()
    try:
        lon = float(answer['result']['location']['lng'])
        lat = float(answer['result']['location']['lat'])
        file_write.write(cols[7][0:-1])
        file_write.write('\t')
        file_write.write(cols[5])
        file_write.write('\t')
        file_write.write(date_to_num(cols[2]))
        file_write.write('\t')
        file_write.write(str(lon))
        file_write.write('\t')
        file_write.write(str(lat))
        file_write.write('\n')
        print(lon, lat)
    except Exception:
        print("索引失败")


def normalization(dataMat):
    arraytime = dataMat[:, 0]
    arraylon = dataMat[:, 2]
    mintime = arraytime.min()
    length = arraytime.max() - arraytime.min()
    ratio = 90.0 / length
    for i in range(len(arraytime)):
        arraytime[i] = (arraytime[i] - mintime) * ratio
    for i in range(len(arraylon)):
        arraylon[i] = arraylon[i] * 2

    dataMat[:, 0] = arraytime
    dataMat[:, 2] = arraylon
    return dataMat

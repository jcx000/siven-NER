# coding:utf-8
from ner.api import recognize
from ner.Clustering import *

file_object = open('E:\\ProgramCode\\Python\\Newsdata\\test.txt',
                   'r', encoding="utf-8", errors='ignore')

file_write = open("newtab.txt", 'a', encoding="utf-8", errors='ignore')

file_index = open('log.txt', 'r+', encoding='utf-8', errors='ignore')

strtmp = file_index.read()
index = int((strtmp.split(','))[-1])
file_object.seek(index, 0)

mark = 0
while(mark < 2000):
    try:
        sentence = file_object.readline()
        if mark % 5 == 0:
            file_index.seek(0)
            file_index.truncate()
        file_index.write(',' + str(file_object.tell()))
        file_index.flush()
        cols = sentence.split('\t')
        predict = recognize(cols[4])
        address = predict['G'].pop()
        newTable(file_write, cols, address)
        mark = mark + 1
    except Exception:
        continue

    print("\n")

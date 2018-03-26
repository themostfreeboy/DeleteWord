# -*- coding: utf-8 -*-
import sys

def main():

    dic = {};

    try:
        fread = open('in.txt', 'r')
    except BaseException, e:
        # print e.message
        print '"in.txt"文件打开失败'
        return

    for word in fread.readlines():

        word = word.replace("\r", "")
        word = word.replace("\n", "")
        word = word.replace("\t", "")
        word = word.replace(" ", "")

        if word == '':
            continue

        if dic.has_key(word):
            continue
        else:
            dic[word] = ''
            print word

    fread.close()

if __name__  ==  '__main__':
    try:
        reload(sys)
        sys.setdefaultencoding('utf-8')
        main()
    except BaseException,e:
        # print e.message
        pass

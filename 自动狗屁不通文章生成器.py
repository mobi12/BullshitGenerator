#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re
import random,readJSON
import assist,assistTest

data = readJSON.读JSON文件("data.json")
名人名言 = data["famous"] # a 代表前面垫话，b代表后面垫话
前面垫话 = data["before"] # 在名人名言前面弄点废话
后面垫话 = data['after']  # 在名人名言后面弄点废话
废话 = data['bosh'] # 代表文章主要废话来源

xx = "学生会退会"

重复度 = 2

def 洗牌遍历(列表):
    global 重复度
    池 = list(列表) * 重复度
    while True:
        random.shuffle(池)
        for 元素 in 池:
            yield 元素

下一句废话 = 洗牌遍历(废话)
下一句名人名言 = 洗牌遍历(名人名言)

def 来点名人名言():
    global 下一句名人名言
    xx = next(下一句名人名言)
    xx = xx.replace(  "a",random.choice(前面垫话) )
    xx = xx.replace(  "b",random.choice(后面垫话) )
    return xx

def 另起一段():
    xx = ". "
    xx += "\r\n"
    xx += "    "
    return xx

if __name__ == "__main__":
    title = ''
    xx = input("请输入文章主题:")
    chiose = input('选择标题：1.对主题之论述 2.论主题 3.主题申请') #请求用户输入标题
    
    while assistTest.isNumber(chiose) != True or int(chiose) > 3: #判断用户输入是否正确
        chiose = input('选择的标题不在支持列表内 ！>.< ，请重新选择: ')

    title = assist.makeTitle(chiose, xx) #填入文章标题

    with open('test.md', 'w', encoding='utf-8') as file: #以utf8编码创建文件输入标题
        file.write(title)

    for x in xx:
        tmp = str()
        while ( len(tmp) < 6000 ) :
            分支 = random.randint(0,100)
            if 分支 < 5:
                tmp += 另起一段()
            elif 分支 < 20 :
                tmp += 来点名人名言()
            else:
                tmp += next(下一句废话)
        tmp = tmp.replace("x",xx)
        assist.writeContent(tmp)
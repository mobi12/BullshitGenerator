def writeContent(temp):
    with open('test.md', 'a+', encoding='utf-8') as file: #向文件中增加内容
        file.write(temp)

def makeTitle(chiose, subject): #通过用户选择生成文档标题
    if int(chiose) == 1:
        title = '对' + subject + '之论述\n'
    elif int(chiose) == 2:
        title = '论' + subject + '\n'
    elif int(chiose) == 3:
        title = subject + '申请\n'
    return title

def isNumber(input): #判断用户输入标题选择是否为数字
    try:
        complex(input)
    except ValueError:
        return False
    return True
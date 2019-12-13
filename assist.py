def writeContent(temp):
    with open('test.md', 'a+', encoding='utf-8') as file:
        file.write(temp)

def makeTitle(chiose, subject):
    if int(chiose) == 1:
        title = '对' + subject + '之论述\n'
    elif int(chiose) == 2:
        title = '论' + subject + '\n'
    elif int(chiose) == 3:
        title = subject + '申请\n'
    return title

def isNumber(input):
    try:
        complex(input)
    except ValueError:
        return False
    return True
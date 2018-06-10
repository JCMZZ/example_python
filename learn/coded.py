# ord()函数获取字符的整数表示
nameN = ord('蒋')
print(nameN)
# chr()函数把编码转换为对应的字符
nameS = chr(nameN)
print(nameS)
# utf-8字符集编码
utfS =  '\u4e2d\u6587'
print(utfS)
# bytes转换(utf-8)
byteUS = utfS.encode('utf-8')
print(byteUS)
# bytes转换(ascii)
byteAS = 'ABC'.encode('ascii')
print(byteAS)
# bytes解码(utf-8,errors = ignore)避错
byteUSE =  b'\xe4\xb8\xad\xff'.decode('utf-8',errors = 'ignore')
print(byteUSE)
# len函数获取字符长度
lenB = len('中文'.encode('utf-8'))
print(lenB)
lenS = len('中文')
print(lenS)
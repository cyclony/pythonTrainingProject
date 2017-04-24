
s = '陈轶聪'
print(len(s))
encoded_s = s.encode('utf8')#utf8编码
print(type(encoded_s))
encoded_s = s.encode('utf16')#utf16编码

print(encoded_s.decode('utf8'))#使用utf8解码器，不能解码被utf16编码的数据，故会爆出decodeError
print(encoded_s.decode('utf8',errors='replace'))#一旦有不能编码的字符，则采用�代替：）
encoded_s = s.encode('ASCII')#ansi编码，因为ansi编码只有128个英文字符和符号能被编码，故中文没有映射，会爆出encodeError
print(encoded_s)
print(len(encoded_s), encoded_s.decode('utf8'))

#读取文件但是不知道文件的编码，该如何办呢？




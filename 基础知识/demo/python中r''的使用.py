hello = '\\\\t\\\\'
# r''引号中的字符串不会被转义
print(r'\\\\t\\\\')

# \\t\\
print(hello)

# hello,\n ,
# world
print(r'''hello,\n ,
world''')

camel = input("camelCase: ")
print("snake_case:", end = " ")
for i in range(len(camel)):
    if (ord(camel[i]) >= ord('a') and ord(camel[i]) <= ord('z')):
        print(camel[i], end = '')
    else:
        print("_" + camel[i].lower(), end = '')
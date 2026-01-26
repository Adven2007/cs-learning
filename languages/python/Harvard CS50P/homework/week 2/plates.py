def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    l = len(s)
    if (l < 2 or l > 6):
        return False
    found_num = 0
    for i in range(l):
        if (is_num(s[i]) == False and is_char(s[i]) == False):
            return False
        if (is_num(s[i])):
            if (i == 0 or i == 1):
                return False
            if (found_num == 0 and s[i] == '0'):
                return False
            found_num = 1
        if (found_num == 1):
            if (is_char(s[i])):
                return False
    return True

def is_num(ch):
    if (ord(ch) >= ord('0') and ord(ch) <= ord('9')):
        return True
    else:
        return False
    
def is_char(ch):
    if (ord(ch) >= ord('A') and ord(ch) <= ord('Z')):
        return True
    else:
        return False
    
main()
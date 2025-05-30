#Reverse A String Without Affecting Special Characters - Python Program

def find_length(str):
    count = 0
    
    for c in str:
        count += 1
    
    return count

def is_alphabet(ch):
    if ((ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z')):
        return 1
    else:
        return 0

def reverse(str):
    start = 0
    end = find_length(str) - 1 #len(str) - 1
    rev_no_spec = ""
    temp = list(str)
    
    while (start < end):
        if is_alphabet(str[start]) != 1:
            start += 1
        elif is_alphabet(str[end]) != 1:
            end -= 1
        else:
            temp[start], temp[end] = temp[end], temp[start]
            start += 1
            end -= 1
    
    rev_no_spec = "".join(temp)
    return rev_no_spec


if __name__ == '__main__':
    str = input()
    
    result = reverse(str)
    print(result)

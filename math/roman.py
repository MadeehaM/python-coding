def roman(Input):
    values = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}

    result = 0
    for i in range(len(Input)-1):
        if values[Input[i]]< values[Input[i+1]]:
            result -= values[Input[i]] 
        else:
            result += values[Input[i]]
    result += values[Input[-1]]
    return result

values = input("Roman numeral:").upper()
print("Integer:",roman(values))

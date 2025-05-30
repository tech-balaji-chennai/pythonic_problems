#Factor Of A Number - Python Program

#Logic 1 - Normal Method
def find_length(num):
    if (num == 0):
        return 1
    num = abs(num)
    count = 0
    while(num > 0):
        count = count + 1
        num = num // 10
    return count

def is_factor_1(dividend, divisor):
    if(divisor == 0):
        return -1
    else:
        remainder = dividend % divisor
        if(remainder == 0):
            return 1
        else:
            return 0


if __name__ == '__main__':
    num_1 = int(input())
    num_2 = int(input())
    result = is_factor_1(num_1, num_2)
    
    if(result == 1):
        print("Factor")
    elif(result == 0):
        print("Not Factor")
    elif(result == -1):
        print("Factor cannot be zero")


#/Logic 2 - Divisibility Rule Method
def divisor_unit_3(dividend, divisor):
    truncand = dividend
    visit = set()
    visit.add(divisor)
    digit = 0
    no_of_steps = (divisor - 3) // 10
    base_value = 1
    stepwise_difference = 3
    digit_multiplier = base_value + (no_of_steps * stepwise_difference)
    
    while((truncand not in visit) and (truncand > 0)):
        visit.add(truncand)
        digit = truncand % 10
        digit_product = digit * digit_multiplier
        truncand = truncand // 10
        truncand = abs(truncand + digit_product)
        print(truncand, end = " ")
    print()
    return truncand

def divisor_unit_9(dividend, divisor):
    truncand = dividend
    visit = set()
    visit.add(divisor)
    digit = 0
    
    #calculation 1: calculate no of steps - From AP formula: Here, an = divisor (given), a1 = 9, d = 10
    no_of_steps = (divisor - 9) // 10
    
    #calculation 2: calculate digit_multiplier - From AP formula: Here a1 = base value = 1, d = stepwise difference = 1, no of steps = (from calculation 1)
    base_value = 1
    stepwise_difference = 1
    digit_multiplier = base_value + (no_of_steps * stepwise_difference)
    
    while((truncand not in visit) and (truncand > 0)):
        visit.add(truncand)
        digit = truncand % 10
        digit_product = digit * digit_multiplier
        truncand = truncand // 10
        truncand = abs(truncand + digit_product)
        print(truncand, end = " ")
    print()
    return truncand

def divisor_unit_7(dividend, divisor):
    truncand = dividend
    visit = set()
    visit.add(divisor)
    digit = 0
    no_of_steps = (divisor - 7) // 10
    base_value = 2
    stepwise_difference = 3
    digit_multiplier = base_value + (no_of_steps * stepwise_difference)
    
    while((truncand not in visit) and (truncand > 0)):
        visit.add(truncand)
        digit = truncand % 10
        digit_product = digit * digit_multiplier
        truncand = truncand // 10
        truncand = abs(truncand - digit_product)
        print(truncand, end = " ")
    print()
    return truncand

def divisor_unit_11(dividend, divisor):
    truncand = dividend
    visit = set()
    visit.add(divisor)
    digit = 0
    no_of_steps = (divisor - 11) // 10
    base_value = 1
    stepwise_difference = 1
    digit_multiplier = base_value + (no_of_steps * stepwise_difference)
    
    while((truncand not in visit) and (truncand > 0)):
        visit.add(truncand)
        digit = truncand % 10
        digit_product = digit * digit_multiplier
        truncand = truncand // 10
        truncand = abs(truncand - digit_product)
        print(truncand, end = " ")
    print()
    return truncand


def is_div_by_1(dividend):
    return 1

def is_div_by_2(dividend):
    last_digit = dividend % 10
    if(last_digit == 0) or (last_digit == 2) or (last_digit == 4) or (last_digit == 6) or (last_digit == 8):
        return 1
    else:
        return 0

def is_div_by_3(dividend):
    result = divisor_unit_3(dividend, 3)
    
    if(result == 3) or (result == 6) or (result == 9):
        return 1
    else:
        return 0

def is_div_by_4(dividend):
    last_2_digits = dividend % 100
    if((last_2_digits) % 4 == 0):
        return 1
    else:
        return 0

def is_div_by_5(dividend):
    last_digit = dividend % 10
    if(last_digit == 0) or (last_digit == 5):
        return 1
    else:
        return 0

def is_div_by_6(dividend):
    cofactors = (is_div_by_2(dividend) == 1) and (is_div_by_3(dividend) == 1)
    if(cofactors == 1):
        return 1
    else:
        return 0

def is_div_by_7(dividend):
    result = divisor_unit_7(dividend, 7)
    
    if((result == 0) or (result == 7)):
        return 1
    else:
        return 0

def is_div_by_8(dividend):
    last_3_digits = dividend % 1000
    if((last_3_digits) % 8 == 0):
        return 1
    else:
        return 0

def is_div_by_9(dividend):
    result = divisor_unit_9(dividend, 9)
    
    if(result == 9):
        return 1
    else:
        return 0

def is_div_by_10(dividend):
    last_digit = dividend % 10
    if(last_digit == 0):
        return 1
    else:
        return 0

def is_div_by_11_1(dividend):
    result = divisor_unit_11(dividend, 11)
    
    if((result == 0) or (result == 11)):
        return 1
    else:
        return 0

def is_div_by_11_2(dividend):
    odd_digits_sum = 0
    even_digits_sum = 0
    position = 1
    
    while(num > 0):
        digit = num % 10
        
        if((position % 2) == 1):
            odd_digits_sum = odd_digits_sum + digit
        else:
            even_digits_sum = even_digits_sum + digit
        
        num = num // 10
        position = position + 1
    
    result = abs(odd_digits_sum - even_digits_sum)
    if((result == 0) or (result == 11)):
        return 1
    else:
        return 0

def is_div_by_12(dividend):
    cofactors = (is_div_by_3(dividend) == 1) and (is_div_by_4(dividend) == 1)
    if(cofactors == 1):
        return 1
    else:
        return 0

def is_div_by_13(dividend):
    result = divisor_unit_3(dividend, 13)
    
    if(result == 13) or (result == 26) or (result == 39):
        return 1
    else:
        return 0

def is_div_by_14(dividend):
    cofactors = (is_div_by_2(dividend) == 1) and (is_div_by_7(dividend) == 1)
    if(cofactors == 1):
        return 1
    else:
        return 0

def is_div_by_15(dividend):
    cofactors = (is_div_by_3(dividend) == 1) and (is_div_by_5(dividend) == 1)
    if(cofactors == 1):
        return 1
    else:
        return 0

def is_div_by_16(dividend):
    last_4_digits = dividend % 10000
    if((last_4_digits) % 16 == 0):
        return 1
    else:
        return 0

def is_div_by_17(dividend):
    result = divisor_unit_7(dividend, 17)
    
    if((result == 0) or (result == 17)):
        return 1
    else:
        return 0

def is_div_by_18(dividend):
    cofactors = (is_div_by_2(dividend) == 1) and (is_div_by_9(dividend) == 1)
    if(cofactors == 1):
        return 1
    else:
        return 0

def is_div_by_19(dividend):
    result = divisor_unit_9(dividend, 19)
    
    if(result == 19):
        return 1
    else:
        return 0

def is_div_by_20(dividend):
    cofactors = (is_div_by_4(dividend) == 1) and (is_div_by_5(dividend) == 1)
    if(cofactors == 1):
        return 1
    else:
        return 0


def is_factor_2(dividend, divisor):
    from time import sleep
    print(f"Performing divisibility rule for given dividend '{dividend}' and divisor '{divisor}'...")
    sleep(1)
    
    if(divisor == 0):
        return -1
    elif((dividend == 0) or (dividend == divisor)):
        return 1
    else:
        divisibility_rule_table = {
        1: is_div_by_1, 2: is_div_by_2, 3: is_div_by_3, 4: is_div_by_4, 5: is_div_by_5,
        6: is_div_by_6, 7: is_div_by_7, 8: is_div_by_8, 9: is_div_by_9, 10: is_div_by_10,
        11: is_div_by_11_1, 12: is_div_by_12, 13: is_div_by_13, 14: is_div_by_14, 15: is_div_by_15,
        16: is_div_by_16, 17: is_div_by_17, 18: is_div_by_18, 19: is_div_by_19, 20: is_div_by_20
        }
        result = divisibility_rule_table[divisor](dividend)
        return result


if __name__ == '__main__':
    num_1 = int(input())
    num_2 = int(input())
    result = is_factor_2(num_1, num_2)
    
    if(result == 1):
        print("Factor")
    elif(result == 0):
        print("Not Factor")
    elif(result == -1):
        print("Factor cannot be zero")

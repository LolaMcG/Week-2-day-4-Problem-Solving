
def make_phone_number(number):
    string_phone_number = str(number)
    first_bit = string_phone_number[0:3] #the zero is redundant here as it's the default value, so can just do [:3]
    second_bit = string_phone_number[3:6]
    third_bit = string_phone_number[6:10]
    return f"({first_bit}) {second_bit}-{third_bit}"
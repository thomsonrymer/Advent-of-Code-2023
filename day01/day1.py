import re
# document consists of lines of text
# each line is a calibration value
# cal_val = 1st numeric digit + last numeric digit 
# from puzzle input, what is sum?

def part_1():
    sum = 0
    line_count = 0
    file = open("input.txt", "r")
    for line in file:
        line_count += 1

        digit_list = get_digits(line)
        line_val = get_line_val(digit_list)

        sum += line_val

    print(sum)

def part_2():
    num_dict = {
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9",
    }
    sum = 0

    file = open("input.txt", "r")
    for line in file:
        print(line)
        all_numbers = get_all_numbers(line)

        just_digits = replace_words_with_digits(all_numbers, num_dict)

        line_val = get_line_val(just_digits)
        print(line_val)

        sum += line_val

    print(sum)

def replace_words_with_digits(li:list, di:dict):
    list_to_return = []
    for element in li:
        if element in di.keys():
            list_to_return.append(di.get(element))
        else:
            list_to_return.append(element)

    return list_to_return

def get_all_numbers(line:str):
    return_list = []
    pattern = r'(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)'
    return_list.append(get_first_num(line, pattern))

    rev_pattern = r'(eno)|(owt)|(eerht)|(ruof)|(evif)|(xis)|(neves)|(thgie)|(enin)|(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)'
    rev_line = line[::-1]
    return_list.append(get_last_num(rev_line, rev_pattern))

    print("return list:")
    print(return_list)
    return return_list

def get_first_num(line:str, pattern):
    match_list = re.findall(pattern, line)
    for tup in match_list:
        for element in tup:
            if element != '':
                return element

def get_last_num(rev_line:str, rev_pattern):
    match_list = re.findall(rev_pattern, rev_line)
    for tup in match_list:
        for element in tup:
            if element != '':
                temp = element[::-1]
                return temp

  
def get_digits(line:str): # returns the first and last numeric digit in a list
    l = []
    for character in line:
        if character.isnumeric():
            l.append(character)
            break

    for character in reversed(line):
        if character.isnumeric():
            l.append(character)
            break

    return l

def get_first_and_last(l:list):
    if len(l) == 1:
        return [l[0], l[0]]
    else:
        return l[::len(l)-1]

def get_line_val(l:list):
    val = int(str(l[0]) + str(l[-1]))

    if val > 99:
        return ValueError()
    return val


# part_1()
part_2()
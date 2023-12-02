import re
# define max limits of cubes
# read file, get maxes from each turn
#   if under max, add game id to a sum (maybe also push id to a list for debugging)


def part_1():
    # open the file
    sum = 0
    limits_dict = {"red":12, "green":13, "blue":14}
    file = open("input.txt", "r")
    for line in file:
        split_line = line.split(":")
        game = split_line[0]
        game_num = int(re.findall(r'\d+', game)[0])

        turns = split_line[1]

        turn_list = turns.split(';')
        turn_maxes = process_turn(turn_list) # dict

        if is_pass(turn_maxes, limits_dict):
            print("passed:")
            print(game_num)
            sum += game_num

    print(sum)


def is_pass(turn_maxes:dict, limits_dict:dict):
    for color, count in limits_dict.items():
        if turn_maxes[color] > count:
            return False

    return True

def process_turn(turn_list:list):
    #return a dict with the max of each color
    maxes_dict = {"red":0, "blue":0, "green":0}
    for turn in turn_list:
        rgb = turn.split(',')
        for cube_count in rgb:
            stripped_rgb = re.sub('\s+', '', cube_count)
            # print(stripped_rgb)
            count = int(re.findall(r'\d+', stripped_rgb)[0])
            color = re.sub(r'\d+', '', stripped_rgb)

            if count > maxes_dict[color]:
                maxes_dict[color] = count

    return maxes_dict


part_1()

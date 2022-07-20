#!/usr/bin/env python3

from access import get_location_for_code
# Access allows for local address location to change for user.
import re
# import os

# this line is only used to pass text to checks
STAGE_ONE_TEST = False      # Test finding closed brackets on one line
STAGE_TWO_TEST = False      # Test finding closed brackets on multilines
STAGE_THREE_TEST = False    # View found highlights and quantify
STAGE_FOUR_TEST = False     # View the headers found
STAGE_FIVE_TEST = False     # Check range of highlights verses orginal file
STAGE_SIX_TEST = True       # Toggle the printing of files to directory.

def check_lines(list_of_lines):
    """verify there are complete sets of brackets"""
    data_check = list_of_lines
    result = calculate_frequencies(data_check)
    if STAGE_ONE_TEST:
        print(f"{result}\nLength: {len(result)}")
    opened = 0
    closed = 0
    count_line = 0
    last_zero = 0
    can_run = False

    for item in result:
        count_line += 1
        opened += item['o_br']
        closed += item['c_br']
        delta = opened - closed
        if delta > 0:
            last_zero = count_line
        if opened - closed > 0:
            print(f"Check line {count_line}, o:{opened}, c:{closed}, delta {opened - closed}")

    if opened == closed:
        can_run = True
    if opened != closed:
        print(f"Balancing brackets: Opened {opened}, Closed {closed}")
        print(f"Best guess: {last_zero}")
    return can_run

def main_loop(line):
    """ Stage ONE: Only check_closed can save to found_highlights. """
    pattern = r"\[[\w.\*\"\: ?\_\#\'\,\-\n\/]*\]"
    # old r"\[[\w\.\*\"\: \?\'\,\-]*\]"
    found_closed = re.search(pattern, line)

    if STAGE_ONE_TEST:
        print(f"Found closed: {found_closed}")

    if found_closed:
        # Don't save line because a hightlight was found.
        # print(found_closed)
        return False, found_closed[0]

    """ Stage TWO: Only check_open_right_bracket can save temp_line
    for append to next line. """
    pattern = r"\[[\w.\*\"\: ?\_\'\,\-\#\n\/]*"
    # old r"\[[\w.\*\"\: ?\'\,\-\/]*"
    open_right = re.search(pattern, line)
    if open_right:
        if STAGE_TWO_TEST:
            print(f"Found open: {line}")
        return True, line

    """ Do nothing with this line and reset previous text """
    return False, ""

def main():

    file_path = get_location_for_code()
    git_folder = 'google/Google It-Cert-Automation/'
    folder_name = 'e-Configuration-Management-and-the-Cloud/W4/'
    file_name = 'W4-Q3-NO.txt'
    file_group = []

    # Save the highlights
    found_highlights = []
    primary_folder = f"{file_path}{git_folder}{folder_name}"
    load_name = f"{primary_folder}{file_name}"

    with open(load_name) as file_object:
        # load the file into a list
        lines = file_object.readlines()

        # Are the brackets balanced?
        if check_lines(lines):
            find_highlighting_brackets(file_group, file_name, found_highlights, primary_folder, load_name, lines)

def find_highlighting_brackets(file_group, file_name, found_highlights, primary_folder, load_name, lines):
    '''Do the lookup for highlighted items'''
    """Manual check bracket pairs: \[([\w \n\*\.\,\']+)\]"""
    add_next_line = False
    # this line is only used to save text to search with next line
    search_with_previous = ""
    note_row = 0

    for line in lines:
        """ Find the next section. """
        file_header = r"""^\[\*Caption:
                             \"(?P<title>[\w\'\?\- ]+)\"
                             \:(?P<unit>[\w]+)\*\]"""
        found_header = re.search(file_header, line, re.X)
        if found_header:
            if STAGE_ONE_TEST:
                print(f"Found header: {line}")
            remove_punc = re.sub(r"[']", '', found_header.group('title'))
            remove_question = re.sub(r"[?]", '_', remove_punc)
            remove_space = re.sub(r"[ ]", '_', remove_question)
            # Create a file name
            name_seq = f"{file_name[:6]}{found_header.group('unit')}"
            file_out = f"{name_seq}-{remove_space}.txt"
            file_dict = {'name': file_out,
                         'start': len(found_highlights) + 1, 'end': 0}
            if STAGE_FOUR_TEST:
                print(f"Current saved line: {len(found_highlights)}")
            file_group.append(file_dict)
        if len(file_group) > 1:
            # end of print - change line here
            file_group[len(file_group)-2]['end'] = file_group[len(file_group)-1]['start'] - 1
            if STAGE_TWO_TEST:
                print(f"Current lenght: {len(file_group)}")
                print(file_group[len(file_group)-2]['start'])
                print(file_group[len(file_group)-2]['end'])
                print(file_group[len(file_group)-1]['start'])
                print(file_group[len(file_group)-1]['end'])
                print(f"End test: {file_group[len(file_group)-1]['end']}")
        if STAGE_TWO_TEST:
            print(f"Add: {add_next_line}")
        sline = re.sub(r"[\n]", " ", line)
        if add_next_line:
            search_with_previous += f"{sline}"
            sline = search_with_previous
        if re.search(r"\[", sline):
            if STAGE_ONE_TEST:
                print(f"Found item: {note_row}")
            action, action_text = main_loop(sline)
            if STAGE_ONE_TEST:
                print(f"Action: {action}, Action Text: {action_text}")
            # Save found highlight
            if not action and action_text != "":
                if STAGE_ONE_TEST:
                    print("Save it")
                add_next_line = False
                search_with_previous = ""
                found_highlights.append(action_text)
            # Save line to append to next line
            if action:
                if STAGE_TWO_TEST:
                    print("Add to next line")
                add_next_line = True
                search_with_previous = action_text
            # Do nothing
        action_text = ""
        note_row += 1

    if STAGE_THREE_TEST:
        print(f"# of Items: {len(found_highlights)}\n")
        print(found_highlights)
    if STAGE_FOUR_TEST:
        print(file_group)

    fh_count = 0
    for file_header in file_group:
        if fh_count == len(file_group)-1:
            # file_header['end'] = len(found_highlights)-1
            print(file_header['end'])
        else:
            # file_header['end'] = file_group[fh_count+1]['start']-2
            print(file_header['end'])
        s_loc = file_header['start']
        e_loc = file_header['end']
        if STAGE_FIVE_TEST:
            if not e_loc == 0:
                print(f"File header: {file_header['name']}")
                minus_start = f"{found_highlights[file_header['start']]}"
                print(f"First: {file_header['start']} - {minus_start}")
                minus_end = {found_highlights[file_header['end']]}
                print(f"End: {file_header['end']} - {minus_end}")
        fh_count += 1
        if STAGE_SIX_TEST:
            # sub video file = pf_name
            pf_name = f"{primary_folder}{file_header['name']}"
            if STAGE_THREE_TEST:
                print(f"{found_highlights}\n{len(found_highlights)}")
            if not e_loc == 0:
                with open(pf_name, 'w') as sub_file_object:
                    for highlight in found_highlights[s_loc:e_loc]:
                        sub_file_object.write(f"{highlight}\n")
                    sub_file_object.close()

def binary_search_position(key, list):
    """Returns position of key in list if found,
    otherwise returns -1
    LIST MUST BE SORTED"""
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1

def find_item(list, item):
    # Returns True if the item is in the list, False if not.
    if len(list) == 0:
        return False

    list.sort()

    # Is the item in the center of the list?
    middle = len(list) // 2
    if list[middle] == item:
        return True

    # Is the item in the first half of the list?
    if item < list[middle]:
        # Call the function with the first half of the list
        return find_item(list[:middle], item)
    else:
        # Call the function with the second half of the list
        return find_item(list[middle + 1:], item)

    return False

def linear_search_num_steps(list, key):
    # Returns the number of steps to determine if key is in the list

    # Initialize the counter of steps
    steps = 0
    for i, item in enumerate(list):
        steps += 1
        if item == key:
            break
    return steps


def binary_search_number_steps(list, key):
    # Returns the number of steps to determine if key is in the list
    # List must be sorted:
    list.sort()

    # The Sort was 1 step, so initialize the counter of steps to 1
    steps = 1

    left = 0
    right = len(list) - 1
    while left <= right:
        steps += 1
        middle = (left + right) // 2

        if list[middle] == key:
            break
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return steps


def best_search(list, key):

    steps_linear = linear_search_num_steps(list, key)
    steps_binary = binary_search_number_steps(list, key)
    results = "Linear: " + str(steps_linear) + " steps, "
    results += "Binary: " + str(steps_binary) + " steps. "

    if steps_linear < steps_binary:
        results += "Best Search is Linear."
    elif steps_linear > steps_binary:
        results += "Best Search is Binary."
    else:
        results += "Result is a Tie."

    return results


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    p = re.compile(r'[\!\(\)\-\{\}\;\:\'\"\,\<\>\.\/\?\@\#\$\%\^\&\*\_\~\w ]')


    # LEARNER CODE START HERE
    frequencies = {}
    used = []
    for item in file_contents:
        results = p.sub('', item)
        open_bracket = results.count('[')
        closed_bracket = results.count(']')
        temp_dict = dict(o_br=open_bracket, c_br=closed_bracket)
        used.append(temp_dict)
    '''for word in file_contents.split():
        if word.lower() not in used:
            used.append(word.lower())
            if word not in frequencies:
                frequencies[word] = 1
            else:
                frequencies[word] +=1'''
    return used

main()
#example 1
my_list = [27, 5, 9, 6, 8]

def RemoveValue(myVal):
    if myVal not in my_list:
        raise ValueError("Value must be in the given list")
    else:
        my_list.remove(myVal)
    return my_list

#print(RemoveValue(27))
#print(RemoveValue(27))  #tells if item not in list

#example 2
my_word_list = ['east', 'after', 'up', 'over', 'inside']

def OrganizeList(myList):
    for item in myList:
        assert type(item) == str, "{} :Word list must be a list of strings".format(item)
    myList.sort()
    return myList

print(OrganizeList(my_word_list))

#my_new_list = [6, 3, 8, "12", 42]
#print(OrganizeList(my_new_list))  #pre-empts error by error message

#3
import random

participants = ['Jack','Jill','Larry','Tom']

def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    try:
        if my_participant_dict['Larry'] == 9:
            return True
        else:
            return False
    except:
        return None
    
print(Guess(participants))

participants = ['Cathy','Fred','Jack','Tom']
print(Guess(participants))  #output is none because of the error
def count_words(text):
    words = text.split()
    result = {}
    for [item] in words:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

def count_keys(file_contents):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''
    uninteresting_words  = ["this","a","is","of","on","if","and","to","that","with"]
    #initial code
    #split file contents into a list
    words = file_contents.split()
    #add dictionary to be returned
    dict_result = {}
    #temporary word to filter out punctuations
    new_word = ""   
    #go through each word
    for word in words:
        new_word = word
        #remove punctuation from sample word
        for deltext in punctuations:
            new_word = new_word.replace(deltext,"")
        #check if new_word is an uninteresting word
        if new_word.lower() in uninteresting_words:
            dont_add = True
        #if it is not, then add it 
        if not dont_add:
            print(new_word)
            if new_word in dict_result:
                dict_result[new_word] += 1  #key word is found
            else:
                dict_result[new_word] = 1   #key word is new to dictionary     
        dont_add = False
        new_word = ""
                
    return dict_result
    

def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  # combine list
  combined_dict = {}
  combined_dict.update(guests1)
  combined_dict.update(guests2)
  #join one list to another
  temp_count = 0
  for friend in combined_dict:    #check to see if any counts missing.
    if friend in guests1:           #all friends keys mutually added, so use new list to readd friends
      temp_count += guests1.get(friend)
    if friend in guests2:
      temp_count += guests2.get(friend)
    combined_dict[friend] = temp_count
    temp_count = 0

  return combined_dict
#test_text = '''this. didn't GO!"'''
test_text = "This ensures that we don't miss an important value and avoids a lot of unnecessary lines of code. To do this, we use a special method called a constructor. Below is an example of an Apple class with a constructor method defined."
print(count_keys(test_text))

access = True

if access:
    file = open("emerson_downsized.txt", "r")
    filter = {}
    for line in file:
        pass


    #cloud = wordcloud.WordCloud()
    #cloud.generate_from_frequencies(frequencies)
    #cloud.to_file("myfile23.jpg")
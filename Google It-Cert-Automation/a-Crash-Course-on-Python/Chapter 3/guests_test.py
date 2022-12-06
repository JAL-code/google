def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  # combine list
  combined_dict = {}
  combined_dict.update(guests1)
  combined_dict.update(guests2)
  #join one list to another
  temp_count = 0
  clist = {}
  for friend in combined_dict:    #check to see if any counts missing.
    if friend in guests1:           #all friends keys mutually added, so use new list to read friends
      temp_count += guests1.get(friend)
    if friend in guests2:
      temp_count += guests2.get(friend)
    clist[friend] = temp_count
    temp_count = 0

  return clist

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))
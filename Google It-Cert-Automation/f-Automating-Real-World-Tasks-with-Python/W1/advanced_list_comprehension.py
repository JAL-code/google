first_lst = [('-2.50', 0.49, 0.52), ('-2.00', 0.52, 0.50)]
second_lst = [('-2.50', '1.91', '2.03'), ('-2.00', '1.83', '2.08')]
print([(fir[0],fir[1]*float(sec[1]),fir[2]*float(sec[2])) for fir in first_lst for sec in second_lst if fir[0] == sec[0]]) # list comprehension

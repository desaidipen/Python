def second_Smallest_1(l):
  nl = sorted(list(set(l)))
  print ("NL: {}".format(nl))
  return nl[1]

def second_Smallest_2(l):
  return sorted(list(set(l)))[1]


l = [8, 6, 4, 10, 3, 2, 31, 4, 7771, 4, 9, 30, 7, 7, 100, 77, 99]
print ("Second Smallest Value Function 1: {}".format(second_Smallest_1(l)))

print ("Second Smallest Value Function 2: {}".format(second_Smallest_2(l)))

print ("Second Smallest Value Manual: {}".format(sorted(list(set(l)))[1]))



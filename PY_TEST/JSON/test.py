a = 'from Dipen Desai to Everyone:    8:51  AM >>>>> MODULE 00: Architecting-on-AWS-Introduction'

# print (a)
# b = a.split(":")[1].lstrip() + ":00"
# t = a.split(":")[1].lstrip()
# print ("++{}++".format(b))

b = a.split(":")
t = b[2].split(" ")[2]
print(b[1].lstrip())
print (t)
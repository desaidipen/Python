import sys
from datetime import datetime

times = {}
names = {}
modules = {}
n_length = 9
m_length = 11

s_chat = 0

with open("chat2.txt", 'r') as fr:
    line = fr.readline()
    # line = line.replace("PM", "PM ") if ("PM" in line) else line.replace("AM", "AM ")
    module = "General"
    
    while len(line) > 0:
        try:
            if ('>>>>> MODULE' in line):
                module = line.split(">>>>> ")[1].rstrip()
                m_length = len(module) if len(module) > m_length else m_length
            elif (("AM" in line) or ("PM" in line)):
                splt = "PM " if ("PM " in line) else "AM "
                # print ("---SPLIT:{}--".format(splt))
                temp = line.split(splt)
                # print ("--TEMP:{}--".format(temp[1].lstrip()))
                # print ("--TEMP1-SPLIT1:{}--".format(temp[1].lstrip().split(" ")[0]))

                if (temp[1].lstrip().split(" ")[0] != "To"):
                    # print ("-------TEMP1-SPLIT1:{}--".format(temp[1].split(" ")[0]))
                    t = line.split(":")[0] + ":00" + line.split(" ")[1]
                    t = datetime.strptime(t, "%I:%M%p").strftime("%H:%M")
                    times[t] = times.get(t, 0) + 1

                    n = temp[1].split("(")[0].lstrip().rstrip()
                    n_length = len(n) if len(n) > n_length else n_length
                    names[n] = names.get(n, 0) + 1

                    modules[module] = modules.get(module, 0) + 1

                    s_chat = s_chat + 1
                # else:
                #     n = "Organizer"
                #     names[n] = names.get(n, 0) + 1
            
        except:
            None
        line = fr.readline()
        line = line.replace("PM", "PM ") if ("PM" in line) else line.replace("AM", "AM ")

m_sorted = sorted(modules.keys())
print ("|{}|---------|".format("-"*(m_length+4)))
print ("|  MODULES  {}|  CHATS  |".format(" "*(m_length-7)))
print ("|{}|---------|".format("-"*(m_length+4)))
for m in m_sorted:
    m1 = m.split(":")
    print ("|  {:<{}}|{:>7}  |".format(m1[0], m_length+2, modules[m]))
print ("|{}|---------|\n".format("-"*(m_length+4)))
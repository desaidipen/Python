import sys
from datetime import datetime

times = {}
names = {}
modules = {}
n_length = 9
m_length = 11

s_chat = 0

with open(sys.argv[1], 'r') as fr:
    line = fr.readline()
    line = line.replace("PM", "PM ") if ("PM" in line) else line.replace("AM", "AM ")
    module = "General"
    
    while len(line) > 0:
        try:
            if ((("AM" in line) or ("PM" in line)) and ("MODULE" not in line)):
                splt = "PM " if ("PM " in line) else "AM "
                temp = line.split(splt) 
                if (temp[1].split(" ")[0] != "To"):
                    t = line.split(":")[0] + ":00" + line.split(" ")[1]
                    t = datetime.strptime(t, "%I:%M%p").strftime("%H:%M")
                    times[t] = times.get(t, 0) + 1

                    n = temp[1].split("(")[0].rstrip()
                    n_length = len(n) if len(n) > n_length else n_length
                    names[n] = names.get(n, 0) + 1

                    modules[module] = modules.get(module, 0) + 1

                    s_chat = s_chat + 1
                # else:
                #     n = "Organizer"
                #     names[n] = names.get(n, 0) + 1
            elif ('>>>>> MODULE' in line):
                module = line.replace(">>>>> ", "").rstrip()
                m_length = len(module) if len(module) > m_length else m_length
        except:
            None
        line = fr.readline()
        line = line.replace("PM", "PM ") if ("PM" in line) else line.replace("AM", "AM ")

t_sorted = sorted(times.keys())
print ("|---------|---------|")
print ("|  TIME   |  CHATS  |")
print ("|---------|---------|")
for t in t_sorted:
    print ("|{:>7}  |{:>7}  |".format(t, times[t]))
print ("|---------|---------|\n")

n_sorted = sorted(names.keys())
print ("|{}|---------|".format("-"*(n_length+4)))
print ("|  NAMES  {}|  CHATS  |".format(" "*(n_length-5)))
print ("|{}|---------|".format("-"*(n_length+4)))
for n in n_sorted:
    print ("|  {:<{}}|{:>7}  |".format(n, n_length+2, names[n]))
print ("|{}|---------|\n".format("-"*(n_length+4)))

m_sorted = sorted(modules.keys())
print ("|{}|---------|".format("-"*(m_length+4)))
print ("|  MODULES  {}|  CHATS  |".format(" "*(m_length-7)))
print ("|{}|---------|".format("-"*(m_length+4)))
for m in m_sorted:
    print ("|  {:<{}}|{:>7}  |".format(m, m_length+2, modules[m]))
print ("|{}|---------|\n".format("-"*(m_length+4)))

print ("Total Student Chat Count: {}".format(s_chat))
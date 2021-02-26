from datetime import datetime

names = {}
times = {}
mL = 9
s_chat = 0

with open('/Users/desadipe/Documents/python/Python/PY_TEST/JSON/chat_data.txt', 'r') as fr:
    line = fr.readline()
    while len(line) > 0:
        try:
            t = line.split(":")[0] + ":00" + line.split(" ")[1]
            t = datetime.strptime(t, "%I:%M%p").strftime("%H:%M")
            times[t] = times.get(t, 0) + 1

            if (("AM" in line) or ("PM" in line)):
                splt = "PM " if ("PM " in line) else "AM "
                temp = line.split(splt) 
                if (temp[1].split(" ")[0] != "To"):
                    n = temp[1].split("(")[0].rstrip()
                    mL = len(n) if len(n) > mL else mL
                    names[n] = names.get(n, 0) + 1
                    s_chat = s_chat + 1
                # else:
                #     n = "Organizer"
                #     names[n] = names.get(n, 0) + 1

        except:
            None
        line = fr.readline()

t_sorted = sorted(times.keys())
print ("|---------|----------|")
print ("|  TIME   |  EVENTS  |")
print ("|---------|----------|")
for t in t_sorted:
    print ("|{:>7}  |{:>8}  |".format(t, times[t]))
print ("|---------|----------|\n")

n_sorted = sorted(names.keys())
print ("|{}|----------|".format("-"*(mL+4)))
print ("|  NAMES  {}|  EVENTS  |".format(" "*(mL-5)))
print ("|{}|----------|".format("-"*(mL+4)))
for n in n_sorted:
    print ("|  {:<{}}|{:>8}  |".format(n, mL+2, names[n]))
print ("|{}|----------|".format("-"*(mL+4)))
print ("Total Student Chat Count: {}".format(s_chat))
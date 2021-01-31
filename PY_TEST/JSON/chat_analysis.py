import time
names = {}
times = {}

with open('chat_data.txt', 'r') as fr:
    line = fr.readline()
    while len(line) > 0:
        t = line.split(":")[0]
        if (len(t) < 3):
            times[t] = times.get(t, 0) + 1

        if (("AM" in line) or ("PM" in line)):
            splt = "PM " if ("PM " in line) else "AM "
            temp = line.split(splt) 
            if (temp[1].split(" ")[0] != "To"):
                n = temp[1].split("(")[0].rstrip()
                names[n] = names.get(n, 0) + 1
        line = fr.readline()

print (times)
print (names)
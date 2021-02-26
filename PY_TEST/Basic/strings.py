name = "Dipen"
age = 37

print ('My name is {} and I am {} years old.'.format(name, age))

l1 = list(range(0, 10))
print (l1)

print ('EVEN: {}'.format(l1[::2]))
print ('ODD: {}'.format(l1[1::2]))
print ('3s: {}'.format(l1[::3]))
print ('REVERSE: {}'.format(l1[::-1]))


str = 'Dipen Desai'
print ('REVERSE: {}'.format(str[::-1]))

s2 = 'http://dipendesai.com'
print(s2[s2.find('.'):])
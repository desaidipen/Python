import re
    
def answer(l):
    nl, fl = [], []
    for v in l:
        grps = re.findall(r'\d+', v)
        nl.append([int(grp) for grp in grps])
    
    nl = sorted(nl)
    
    for v in nl:
        fl.append(".".join([str(grp) for grp in v]))
    return fl

l = ["1.1000.1000000", "1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2", "1.99.999", "2.0.7", "3.3.100", "0.9.2"]
# l = ["0.0.1", "0.2.0", "3.0.0", "4.0", "5", "6.0.7", "8.9.10", "11.222.3333", "1.1000.1000000", "1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2", "1.99.999", "2.0.7", "3.3.100", "0.9.2"]
# l = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
# l = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]

print (f'ORIGINAL LIST:\n{l}')
print (f'FINAL SORTED LIST:\n{answer(l)}')
import timeit
lt = timeit.timeit(stmt="[1,2,3,4,5]",number=1000000)
tt = timeit.timeit(stmt="(1,2,3,4,5)",number=1000000)

print("List Time: {}".format(lt))
print("Tuple Time: {}".format(tt))
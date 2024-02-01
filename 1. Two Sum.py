import bisect
def scratch(li,item):
    a = bisect.bisect(li,item)
    print(a)
scratch([2,2,5,6],3)



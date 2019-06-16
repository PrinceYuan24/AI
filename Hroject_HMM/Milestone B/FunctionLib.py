'''
Function library
Ziyuan Wang
'''
# Input data to list
def Data2List(data):
    np_list = data.values.tolist()
    list_data = []
    for d in np_list:
        list_data.append(d[0])
    return list_data

# Get the process of the change
def integral(datalist, dt):
    itg = []
    pre = 0
    for l in datalist:
        cur = pre + l * dt
        itg.append(cur)
        pre = cur
    return itg

def UnifiedTime(InputList):
    lenList = []
    for input in InputList:
        size = len(input)
        lenList.append(size)
    sizemin = min(lenList)
    return sizemin
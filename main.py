# python3
"""221RDB031"""

def parallel_processing(_n, _m, data):
    """simple loop"""
    output = []

    thread_list=[(i,0) for i in range(_n)] #create list of threads

    for i in range(_m):
        output.append(thread_list[0])
        thread_list[0]=(thread_list[0][0], thread_list[0][1]+data[i])
        thread_list=sorted(thread_list, key=lambda a: (a[1], a[0]))



    return output

def main():
    """main"""
    # input consists of two lines
    # first line - n and m
    # n - thread count
    # m - job count
    line1 = input().strip().split()
    _n = int(line1[0])
    _m = int(line1[1])

    # second line - data
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().strip().split()))

    #print(_n,_m,data)


    result = parallel_processing(_n,_m,data)

    for item in result:
        print(item[0], item[1])




if __name__ == "__main__":
    main()

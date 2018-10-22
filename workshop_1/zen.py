 # 3. Export list of 3 most common words in Python Zen,
 #  whereeach item of list looks like (‘word’, frequency)


def main():
    file = open("zen.txt", "r")
    data = file.read()
    # print (data)
    arr = data.split("\n")
    str = ' '.join(arr)

    array = str.split(' ')
    # print (array)

    count = 0
    d = {}
    n = len(array)
    for i in range(n):
        for j in range(n):
            if(array[j] == array[i]):
                count = count + 1
        d[array[i]] = count
        count = 0
    print(sorted(d.items(), key=lambda x: x[n]))

if __name__ == '__main__': main()

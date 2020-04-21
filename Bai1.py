

def readGraph(filename):
    with open(filename,"r") as f:
        number = int (f.readline())
        print(number)
        data = f.readlines()
        #print(data)
        for i in range(0,len(data)):
            data[i] = data[i].rstrip("\n").replace(" ","")
        list = []
        count = 0
        for line in data:
            for i in range(len(line)):
                if (line[i] == "1"):
                    list.insert(0,i)
                    count +=1
                else:
                    continue
            list.reverse()
            print(count,list)
            count = 0
            list.clear()  

link  = r"Q:\Python 3\BaiTapThucHanh\LAB 2\graph1.txt"
readGraph(link)

# làm bài ni phải dùng hàm find !
# if you want remove all withspace in string, u can use: string.replace(" ","")
# line = "0 0 1 0 0 1 0 0 0"
# line = line.replace(" ", "")
# print(line)
# print(type(line.find('1')))


# quoc dep trai vkl 

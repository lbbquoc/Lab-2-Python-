def readGraph(filename):
    with open(filename,"r") as f:
        number = int(f.readline())
        print(number)
        data = f.readlines()
        for i in range(len(data)):
            data[i] = data[i].strip("\n").split(" ")
            #print(data[i])
        line = "" # khai bao chuoi rong  

        for j in range(9):
            check = int(data[j][0])
            
            if (check == 0):
                line = "0 0 0 0 0 0 0 0 0"
                print(line)
                line =""
            if (check != 0):
                count = 0 #use to pick up element in data[j]
                for k in range(9):
                    if (count == check):
                        line += "0"
                        continue
                    if (k == int(data[j][count + 1])):
                        line += "1"
                        count += 1
                    else:
                        line += "0"
                count = 0
                string_space = " "
                print(string_space.join(line))
                line = ""
                        
                

        #print(data)



path =r"Q:\Python 3\BaiTapThucHanh\LAB 2\graph2.txt"
readGraph(path)
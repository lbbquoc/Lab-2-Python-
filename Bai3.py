
def createMatrix(filename):
    with open(filename,"r") as f:
        num_vertices = int(f.readline())
        matrix = f.readlines()
        #create matrix : (type of each element: string)
        for i in range(len(matrix)):
            matrix[i] = matrix[i].strip("\n").split(" ")
            print(matrix[i])
        return matrix    
        
def isValidGraph(matrix):
    flag_1 = False # to  check main diagonal
    flag_2 = False # to check others
    num_vertices = len(matrix)
    if (num_vertices < 0 ):
        return False
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                if (matrix[i][j] == 0):
                    flag_1 = True
            if int(matrix[i][j]) >= 0:
                flag_2 = True
    if (flag_1 == False or flag_2 == False):
        return False

    return True 

def IsScalarGraph(matrix): # unrirected graph
        num_vertices = len(matrix)
        #check all element 
        # except diagonal are  zero or not 
        for j in range(num_vertices):
            for k in range (num_vertices):
                if(j != k) and matrix[j][k] != "0":
                    return False
        #check main diagonal are equals or not
        for i in range(num_vertices - 1):
            if (matrix[i][i] != matrix[i+1][i+1]):
                return False
        
        return True        

def countVertices(matrix):
    if (isValidGraph == False):
        print("Graph is invalid !")
        return
    num_vertices = len(matrix)
    return num_vertices

def countEdges(matrix):
    if (isValidGraph == False):
        print("Graph is invalid !")
        return
    num_vertices = len(matrix)
    count = 0
    for i in range(num_vertices):
        for j in range(num_vertices):
            if (matrix[i][j] != "0"):
                count += 1
    if (IsScalarGraph(matrix) == True ):
        return count//2
    else:
        return count

def findDegree(matrix,vertex):
    # if (isValidGraph(matrix) == False):
    #     print("Graph is invalid !")
    #     return
    degree = 0 
    num_vertices = len(matrix)
    for i in range(num_vertices):
        if (matrix[vertex][i] == "1"):
            degree +=1
    if (matrix[vertex][vertex] != "0"):
        degree += int(matrix[vertex][vertex])
    return degree

def findInOutDegree(matrix):
    num_vertices = len(matrix)
    # each vertex will have 0 -> num_vertices in and out degree
    _in = [0] * num_vertices
    out = [0] * num_vertices
    
    for i in range(num_vertices):
        List = matrix[i]
        for j in range(num_vertices):
            if ( List[j] != "0" ): # check line for find OUT
                out[i] += 1 
            if (matrix[j][i] != "0"): # check colum for find IN
                _in[i] += 1
    print("Vetex\tIn\tOut")
    for k in range(num_vertices):
        print(k,"\t", _in[k],"\t" ,out[k])


def findDegreeOfAllVetex(matrix):
    if (IsScalarGraph == True):
        num_vertices = len(matrix)
        for i in range(num_vertices):
            print(findDegree(matrix,i))
    else:
        findInOutDegree(matrix)
def countIndependentVertex(matrix):
    num_vertices = len(matrix)
    list_leaf = []
    list_IV = []
    
    for i in range(num_vertices):
        if (findDegree(matrix,i) == 0):
            list_IV.insert(0,i)
        if(findDegree(matrix,i) == 1):
            list_leaf.insert(0,i)
    
    list_IV.reverse()
    list_leaf.reverse()
    print(" Indepent Vertices  :\t  Leaf ")
    print("\t",list_IV,"\t",list_leaf)
def checkCompleteGraph(matrix):
    num_vertices = len(matrix)
    edge = num_vertices*(num_vertices - 1)//2
    flag = True
    for i in range(num_vertices):
        if findDegree(matrix,i) != num_vertices - 1:
            flag = False
    if (flag == True and countEdges(matrix) == edge):
        print("Is Complete graph !")
    
def checkCircleGraph(matrix):
    flag = True
    num_vertices = len(matrix)
    for i in range(num_vertices):
        if (findDegree(matrix,i) != 2):
            flag = False
    if (flag == True):
        print("Is Circle graph !")

        



path = r"Q:\Python 3\BaiTapThucHanh\LAB 2\graph1.txt"
matrix = createMatrix(path)
# V = countVertices(matrix)
# print(IsScalarGraph(createMatrix(path)),V)
findDegreeOfAllVetex(matrix)
countIndependentVertex(matrix)
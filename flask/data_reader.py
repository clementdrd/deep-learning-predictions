from numpy import loadtxt

def reader():
#def reader(toto):
    
    #dataset = loadtxt(toto, delimiter=',')
    dataset = loadtxt("pima-indians-diabetes.csv", delimiter=',')
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!dsdsdsdsds")
    
    print(dataset[1])
    
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!sdndskjdns")

    lenght = len(dataset)
    tutu = []

    for i in range (lenght):
        tutu.append(dataset[i])


    #dataset = loadtxt(toto, delimiter=',')

    return tutu

if __name__ == "__main__":

    print(reader())
    #print(reader(toto="pima-indians-diabetes.csv"))
    #print(reader(toto=""))
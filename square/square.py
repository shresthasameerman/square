def getList(num):
    return list(range(1,num+1))
def printsquare(num):
    return [i**2 for i in range(1,num+1)]
def main():
    num=20
    squareList=printsquare(num)
    print(squareList)
if __name__=="__main__":
    main()
    

from datetime import datetime
def printDates(dates):  
   
    for i in range(len(dates)):   
        print(dates[i])  
       
       
if __name__ == "__main__":
    a=int(input())
    d=[]
    for i in range(a):
        x=input()
        d.append(x)
    d.sort(key = lambda date: datetime.strptime(date, '%d %b %Y'))
    for i in range(len(d)):
        print(d[i])
        
    

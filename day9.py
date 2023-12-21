def predict(l):
    d={1:l}
    x=len(l)
    for i in range(2,x):
        y=[]
        z=x-i+1
        for j in range(z):
            y.append(d[i-1][j+1]-d[i-1][j])
        

        d[i]=y
        if y.count(0)== x-i:
            break
    sum=0
    for i in d:
        #Uncomment below line and comment next 4 lines for part 1
        #sum+=d[i][-1]
        if i%2==0:
            sum-=d[i][0]
        else:
            sum+=d[i][0]
        
    return sum
forecast=[]
with open('9.txt', 'r') as file:

    for line in file:
        elements = [int(x) for x in line.split()]
        forecast.append(predict(elements))

print(forecast)
print(sum(forecast))
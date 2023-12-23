import copy # Open the file and read lines
file_path = '11.txt'  # Replace with the actual path to your file
lines = []

with open(file_path, 'r') as file:
    lines = file.readlines()

# Remove newline characters from each line
lines = [line.strip() for line in lines]

# Create a list of lists to store characters
characters_list = []

# Iterate through each line and each character to store them in a list
for line in lines:
    characters_in_line = [char for char in line]
    characters_list.append(characters_in_line)

# Print the result

print(characters_list)
nr=len(characters_list)
nc=len(characters_list[0])
print(f"number o rows is {nr}")
print(f"no. of columns i {nc}")

galaxies=[]
for i,j in enumerate(characters_list):
    for x,y in enumerate(j):
        if y=='#':
            galaxies.append([i,x])

#print(galaxies)



def expand_hexes(g,n):
    a=0
    for i,a in enumerate(characters_list):
        if sum(1 for k in a if k=='.')==nr:
            a+=1
            for i in g:
                if i[0]>i+a*n:
                    i[0]+=n
            a+=1
    d=0
    for k in range(nc):
        
        if sum(1 if characters_list[i][k]=='.' else 0 for i in range(nr) )==140:
            print(f"column {k}")
            #print([characters_list[i][k] for i in range(nr)])
            
            for i in g:
                if i[1]>k+d:
                    
                    print(i[0])
                    print(i[1])
                    i[1]+=n
                    print(i[1])
            d+=n

galaxies1=copy.deepcopy(galaxies)
galaxies2=copy.deepcopy(galaxies)
expand_hexes(galaxies1,1)
distances1=[]
for x in galaxies1:
    a=galaxies1.copy()
    a.remove(x)
    for y in a:
        distances1.append(abs(y[0]-x[0])+abs(y[1]-x[1]))

expand_hexes(galaxies2,999999)
distances2=[]
for x in galaxies2:
    a=galaxies2.copy()
    a.remove(x)
    for y in a:
        distances2.append(abs(y[0]-x[0])+abs(y[1]-x[1]))


print(f"part 1 answer is {sum(distances1)/2}")
print(f"part 2 answer is {sum(distances2)/2}")

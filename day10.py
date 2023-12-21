pipes_dictionary = {
    '|': {'up': ['|','7','F','S'], 'down': ['|','J','L','S']},
    '-': {'left': ['L','F','S','-'], 'right': ['7','J','S','-']},
    'L': {'up': ['|','7','F','S'],'right': ['7','J','S','-']},
    'J': {'left': ['L','F','S','-'],'up': ['|','7','F','S']},
    '7': {'left': ['L','F','S','-'],'down': ['|','J','L','S']},
    'F': {'down': ['|','J','L','S'],'right': ['7','J','S','-']},
    '.': {},
    'S': {'up': ['|','7','F'], 'down': ['|','J','L'],'left': ['L','F','-'], 'right': ['7','J','-']}
}
direction={"up":"down","down":"up","left":"right","right":"left"}
S=[]
with open('10.txt', 'r') as file:
    maze = [list(line.strip()) for line in file]



for i in maze:
    for j in i: 
        if j=="S":
            S.append(maze.index(i))
            S.append(i.index(j))
            S.append("S")
            S.append(None)
            break
nr=len(maze)
nc=len(maze[0])
print(S)
def next_step(K):
    x=['up','down','left','right']
    y=[[-1,0],[1,0],[0,-1],[0,1]]
    Z=[]
    
    if K[3] is not None:
        opp_direction=direction[K[3]]    
        p=x.index(opp_direction)
        x.remove(opp_direction)
        y.remove(y[p])
    
    for a in x:
        line_index_to_check=K[0]+y[x.index(a)][0]
        column_index_to_check=K[1]+y[x.index(a)][1]
        
        #print(new_path)
        if -1<line_index_to_check<nr and -1<column_index_to_check<nc:
            new_path=maze[line_index_to_check][column_index_to_check]
            if a in pipes_dictionary[K[2]]:
                if new_path in pipes_dictionary[K[2]][a]:
                    jl=True
                else:
                    jl=False
                #print(jl)
                #print(pipes_dictionary[K[2]][a])
                if jl:
                    Z.append(line_index_to_check)                
                    Z.append(column_index_to_check)
                    Z.append(new_path)
                    Z.append(a)
                    break
    return Z

#O=[74, 114, 'F', 'up']
#print(next_step(O))

S_Count=0
u=0
B=S
H=[]
while S_Count!=1:
    u+=1
    B=next_step(B)
    H.append([B[0],B[1]])
    print(B)
    if B[2]=='S':
        S_Count+=1

cant=0
y=0
for i in range(nr):
    for j in range(nc):
  
        
         
        G=[i,j]
        if G not in H:
            y+=1
            print(f"{y} th non loop character index is {G}")
            L="Outside"
            while L=="Outside":
                above_rows_to_check=i
                o=0
                d=0
                for a in range(above_rows_to_check):
                    
                    if d > 0:
                        d -= 1
                        continue
                    if [a,j] in H:
                        if maze[a][j]!='-':
                            
                            
                            alt=next_step([a,j,maze[a][j],'up'])[3]
                            current=[a,j,maze[a][j],direction[alt]]
                            dir='down'
                            while dir=='down':
                                
                                current=next_step(current)
                                dir=current[3]
                                if dir=='down':
                                    d+=1
                            if dir!=alt:
                                o+=1
                                
                            
                        else :
                            o+=1

                    
                        
                if o%2!=0:
                    cant+=1
                    L="Inside"
                    print(f"Inside because of up")
                    break
                bottom_rows_to_check=i
                p=0
                f=0
                for a in range(bottom_rows_to_check+1,nr):
                    print(a)
                    if f > 0:
                        f -= 1
                        continue
                    if [a,j] in H:
                        if maze[a][j]!='-':
                            
                            
                            alt=next_step([a,j,maze[a][j],'up'])[3]
                            current=[a,j,maze[a][j],direction[alt]]
                            dir='down'
                            while dir=='down':
                                
                                print(current)
                                current=next_step(current)
                                dir=current[3]
                                print(current)
                                if dir=='down':
                                    f+=1
                                print(f)
                            if dir!=alt:
                                p+=1
                                print(p)
                            
                        else:
                            p+=1        
                            print(p)                
                                                
                        
                if p%2!=0:
                    cant+=1
                    print(f"Inside because of down")
                    L="Inside"     
                    break
                left_rows_to_check=j
                
                s=0
                q=0
                for a in range(left_rows_to_check):
                    if q > 0:
                        q -= 1
                        continue
                    if [i,a] in H:
                        if maze[i][a]!='|':
                            
                            
                            alt=next_step([i,a,maze[i][a],'left'])[3]
                            print(alt)
                            current=[i,a,maze[i][a],direction[alt]]
                            dir='right'
                            while dir=='right':
                                print(current)
                                current=next_step(current)
                                dir=current[3]
                                print(f"after{current}")
                                if dir=='right':
                                    q+=1
                                    
                            if dir!=alt:
                                s+=1
                                print(f"current 3 {dir}")
                        else :
                            s+=1
                        
                if s%2!=0:
                    cant+=1
                    print(f"Inside because of left")
                    L="Inside"
                    break                       
                right_rows_to_check=j
                
                n=0
                w=0
                for a in range(right_rows_to_check+1,nc):
                    if w > 0:
                        w -= 1
                        continue
                    if [i,a] in H:
                        if maze[i][a]!='|':
                            
                            
                            alt=next_step([i,a,maze[i][a],'left'])[3]
                            current=[i,a,maze[i][a],direction[alt]]
                            dir='right'
                            while dir=='right':
                                
                                current=next_step(current)
                                dir=current[3]
                                if dir=='right':
                                    w+=1
                            if dir!=alt:
                                n+=1
                            
                        else:
                            n+=1

                if n%2!=0:
                    cant+=1
                    print(f"Inside because of right")
                    L="Inside"
                    break
                break
print(f"part 1 is {u/2}")
print(f"part 2 is {cant}")        







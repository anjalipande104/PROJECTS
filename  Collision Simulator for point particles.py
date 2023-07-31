def upheap(arr,j,B,P):
    parent=(j-1)//2
    if j>0 and arr[parent] > arr[j]:
        B[j],B[parent] = B[parent],B[j]
        P[parent]=B[j]
        P[j]=B[parent]
        arr[j], arr[parent] = arr[parent], arr[j]
        upheap(arr,parent,B,P)
        
    
def heapify(arr, n, i, B, P):
    # Find largest among root and children......
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] >arr[l]:
        largest = l
  
    if r < n and arr[largest] >arr[r]:
        largest = r
  
# If root is largest, swap with largest and continue heapifying......
    if largest != i:
        B[i],B[largest] = B[largest],B[i]
        P[largest]=B[i]
        P[i]=B[largest]
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, B, P)
  
  
def heapSort(arr,B,P):
    n = len(arr)
  
 # Build min heap
    for i in range(n//2, -1, -1):
        heapify(arr, n, i, B, P)
  
    
    return arr
    
def timefinder(v1,v2,x1,x2,T):
    
    
    if v2-v1>=0 :
        return T

    elif v2-v1<0:
        a=(x2-x1)/(v1-v2)
        return a

def recursion(M,v,x,m,T,A,B,P,ans,t,d,time):
   
    while (t<T or len(ans)<m):
        i=B[0]
        
        e=v[i+1]
        v[i+1]=(((2*M[i])/(M[i]+M[i+1]))*v[i])-(((M[i]-M[i+1])/(M[i]+M[i+1]))*e)
        v[i]=(((M[i]-M[i+1])/(M[i]+M[i+1]))*v[i])+(((2*M[i+1])/(M[i]+M[i+1]))*e)
    
        if B[0]==0 and len(M)==2:
            return ans
    
        if B[0]==0 and len(M)>2:
            A[0]=T
            g=x[2]+(v[2]*t)
            o = timefinder(v[1],v[2],d,g,T)
            A[P[1]]= o + t
        #seee........
            heapify(A,len(A),P[1],B,P)
            upheap(A,P[1],B,P)
        
        if B[0]==1 and len(M)==3:
            A[0]=T
            g3=x[0]+(v[0]*t)
            o=(timefinder(v[0],v[1],g3,d,T))
            A[P[0]]= o + t
            y=P[0]
        #seeee............
            heapify(A,len(A),y,B,P) 
            upheap(A,y,B,P)
        
        if B[0]>0 and len(M)>3:
        #seeeee......
            A[0]=T
            #....changing position of i-1.....
            g1=x[i-1]+(v[i-1]*t)
            o = (timefinder(v[i-1],v[i],g1,d,T))
            A[P[i-1]]=o+t
            y=P[i-1]
            heapify(A,len(A),y,B,P) 
            upheap(A,y,B,P)
            #....changing position of i+2.....
            g2=x[i+2]+(v[i+2]*t)
            o = (timefinder(v[i+1],v[i+2],d,g2,T))
            A[P[i+1]]=o+t
            y=P[i+1]
            heapify(A,len(A),y,B,P) 
            upheap(A,y,B,P)
        if A[0] == T:
            return ans
        else:
            t=t+A[0]
            if t<=T:
                u = B[0]
                if time[u]==0:
                    d=((v[u]*A[0])+x[u])
                else:
                    d=((v[u]*(A[0]-time[u]))+x[u])
            else:
                return ans
        print(A)
        ans.append([round(A[0],4),B[0],round(d,4)])
        time[u]=(A[0])
    # updating new distance(x) in x............
        x[u]=d
        x[u+1]=d
        
    
    return ans
        


def listCollisions(M,x,v,m,T):
    A=[]
    B=[]
    P=[]
    ans=[]
    j=0
    t=0
    n=[]
    time=[0]*(len(M))
# finding out time and append it in list A
    for i in range (len(M)-1):
        if v[i]==v[i+1]==0:
            A.append(T)
        if v[i+1]-v[i]>0:
            A.append(T)
        if v[i+1]-v[i]<0:
            a=(x[i+1]-x[i])/(v[i+1]-v[i])
            A.append(-a)
        B.append(j)
        P.append(0)
        j=j+1
    #seeeee......................    
    heapSort(A,B,P)
    if A[0]==T:
       return n
    else:
        t=A[0]
    #...finding position.......
        u=B[0]
    ##########............................
        d=(v[u]*t)+(x[u])
    ans.append([round(A[0],4),B[0],round(d,4)])
    u=B[0]
    # updating new distance(x) in x............
    #seeee........
    x[u]=d
    x[u+1]=d
    time[u]=t
    
    recursion(M,v,x,m,T,A,B,P,ans,t,d,time)
    return ans

h=listCollisions([1.0, 1.0, 1.0, 1.0], [-2.0, -1.0, 1.0, 2.0], [0.0, -1.0, 1.0, 0.0], 5,5.0)
print(h)    
        

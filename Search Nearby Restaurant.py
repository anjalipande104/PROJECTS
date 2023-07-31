class Node:
    def __init__(self,key):
        self.val=key
        self.bstree=None
        self.left=None
        self.right=None
        
def ymaking(ar,c):
    L1=[]
    L2=[]
    O=[]
    for i in range(len(ar)):
        if c > ar[i][0]:
            L1.append(ar[i])
        else:
            L2.append(ar[i])
    O.append(L1)
    O.append(L2)
    return O
    
def rangetreee(arrx,s,l,arry):
    if s>l:
        return None
    if arrx is None:
        return None
    else:
        n=s+l
        if n%2==0:
            mid=n//2
        else:
            mid=(n//2)+1
        root=Node(arrx[mid])
        p=arrx[mid][0]
        F=ymaking(arry,p)
        if s!=l:
            root.bstree=arry
            root.left=rangetreee(arrx,s,mid-1,F[0])
            root.right=rangetreee(arrx,mid,l,F[1])
        else:
            root.bstree = [root.val]
    return root        
        
def preorder(root):
    if root:
        print('{0}'.format(root.val), end='')
        preorder(root.left)
        preorder(root.right)
    else:
        return

def XYfind(ar,v,z,L5):
    for i in range(len(ar)):
        if v<=ar[i][1]<=z:
            L5.append(ar[i])
        
def checker(x,x1,x2,y1,y2,L):
    if x1<=x[0]<=x2 and y1<=x[1]<=y2 :
        L.append(x)
        
class PointDatabase:
    def __init__(self, pointlist):
        b = pointlist[:]
        
        pointlist.sort(key=lambda x:x[0])
        arrx=[]
        for i in range(len(pointlist)):
            arrx.append(pointlist[i])
        b.sort(key=lambda x:x[1])
        arry=[]
        for i in range(len(b)):
            arry.append(b[i])
        # print('arry: ', arry, 'arrx: ', arrx)    
        a=len(arrx)-1
        Root2 = rangetreee(arrx,0,a,arry)
        # print('root2: ', Root2.val)
        self.val=Root2.val
        self.bstree=Root2.bstree
        # print('bstree: ', self.bstree)
        # print('bstree: ', Root2.left.right.bstree)
        self.left=Root2.left
        self.right=Root2.right
        
        
    def searchNearby(self, q, d):
        s=q[0]-d
        u=q[0]+d
        v=q[1]-d
        z=q[1]+d
        L5=[]
        
        def find(self,s,u,v,z,L5):
            if self is None:
                #print("1")
                return
            
            if self.val[0]>u:
                #print("b3",self.val)
                #print("3")
                find(self.left,s,u,v,z,L5)
            if self.val[0]<s:
                #print("4")
                find(self.right,s,u,v,z,L5)
            if self.val[0] <= u and self.val[0] >= s:
                if self.left == None and self.right == None :
                    if v <= self.val[1] <= z :
                        L5.append(self.val)
                    
                #print("df",self.left.val)
                elif self.left.val[0] >= s and self.right.val[0]<=u:
                    if self.left.right is not  None:
                        #print("5")
                        XYfind(self.left.right.bstree,v,z,L5)
                    else:
                        #print("6")
                        checker(self.left.val,s,u,v,z,L5)
                    if self.right.left is not  None:
                        XYfind(self.right.left.bstree,v,z,L5)
                    else:
                        #print("8")
                        checker(self.right.val,s,u,v,z,L5)
                    find(self.left.left,s,u,v,z,L5)
                    find(self.right.right,s,u,v,z,L5)
                elif self.right.val[0]>u and self.left.val[0]>=s:
                    #print("b9",self.right.val)
                    #print("9")
                    find(self.right.left,s,u,v,z,L5)
                    #print("fu")
                    find(self.left.left,s,u,v,z,L5)
                    if self.left.right is not  None:
                        XYfind(self.left.right.bstree,v,z,L5)
                    else:
                        checker(self.left.val,s,u,v,z,L5)
                elif self.right.val[0]<=u and self.left.val[0] < s:
                    if self.right.left is not  None:
                        #print("10")
                        XYfind(self.right.left.bstree,v,z,L5)
                    else:
                        checker(self.right.val,s,u,v,z,L5)
                    find(self.right.right,s,u,v,z,L5)
                    find(self.left.right,s,u,v,z,L5)
                else:
                    find(self.right.left,s,u,v,z,L5)
                    find(self.left.right,s,u,v,z,L5)
            return L5
        return find(self,s,u,v,z,L5)
                    
                    
                    
            
            
 
  
    
    
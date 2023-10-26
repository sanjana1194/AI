left=['m','m','m','c','c','c']
right=[];
v=['cc','mm','c','m','mc',];
stepl=[];
stepr=[]
stepl.append(left)
stepr.append(right)
def leftside(a,b,s):
    if (a.count('c')<=a.count('m') or a.count('m')==0) and (b.count('c')<=b.count('m') or b.count('m')==0):
        c=False
        c1=False
        if s=='left':
            for j in stepl:
                if j.count('m')==a.count('m') and j.count('c')==a.count('c'):
                    c3=stepl.index(j)
                    c=True
            for j in stepr:
                if j.count('m')==b.count('m') and j.count('c')==b.count('c'):
                    c4=stepr.index(j)
                    c1=True
            if c==True and c1==True and c3==c4:
                return False
            else:
                stepl.append(a)
                stepr.append(b)
                return True
        else:
            for j in stepr:
                if j.count('m')==a.count('m') and j.count('c')==a.count('c'):
                    c3=stepr.index(j)
                    c=True
            for j in stepl:
                if j.count('m')==b.count('m') and j.count('c')==b.count('c'):
                    c4=stepl.index(j)
                    c1=True;
            if c==True and c1==True and c3==c4:
                return False
            else:
                stepr.append(a)
                stepl.append(b)
                return True
    else:
        return False
def find(left1,right1,s):
    count=False
    for i in v:
        a=left1[:]
        b=right1[:]
        if i=='mc' and left1.count('m')>=1 and left1.count('c')>=1:
            a.remove('m')
            a.remove('c')
            b.append('m')
            b.append('c')
            result=leftside(a,b,s)
            if result==False:
                continue
            else:
                left1=a;
                right1=b
                print("m-1 c-1")
            return left1,right1         
        elif  i=='mm' and left1.count('m')>=2:
            a.remove('m')
            a.remove('m')
            b.append('m')
            b.append('m')
            result=leftside(a,b,s)
            if result==False:
                continue
            else:
                left1=a;
                right1=b
                print("m-1 m-1")
            return left1,right1
                #return left1,right1
            
        elif i=='cc' and left1.count('c')>=2:
            a.remove('c')
            a.remove('c')
            b.append('c')
            b.append('c')
            result=leftside(a,b,s)
            if result==False:
                continue
            else:
                left1=a;
                right1=b
                print("c-1   c-1")
            return left1,right1
           
        elif i=='m' and left1.count('m')>=1:
            a.remove('m')
            b.append('m')
            result=leftside(a,b,s)
            if result==False:
                continue
            else:
                left1=a;
                right1=b
                print("m-1")
            return left1,right1
        elif i=='c' and left1.count('c')>=1:
            a.remove('c')
            b.append('c')
            if (a.count('c')<=a.count('m') or a.count('m')==0) and (b.count('c')<=b.count('m') or b.count('m')==0):
                c=False
                c1=False
                if s=='left':
                    for j in stepl:
                        if j.count('m')==a.count('m') and j.count('c')==a.count('c'):
                            c3=stepl.index(j)
                            c=True
                    for i in stepr:
                        if j.count('m')==b.count('m') and j.count('c')==b.count('c'):
                            c4=stepr.index(j)
                            c1=True
                    if c==True and c1==True and c3==c4:
                        continue;
                    else:
                        left1=a;
                        right1=b;
                        stepl.append(left1)
                        stepr.append(right1)
                else:
                    for j in stepr:
                        if j.count('m')==a.count('m') and j.count('c')==b.count('c'):
                            c3=stepr.index(j)
                            c=True
                    for j in stepl:
                        if j.count('m')==a.count('m') and j.count('c')==b.count('c'):
                            c4=stepl.index(j)
                            c1=True;
                    if c==True and c1==True and c3==c4:
                        continue;
                    else:
                        left1=a;
                        right1=b;
                        stepr.append(left1)
                        stepl.append(right1)
                print("c-1")
                return left1,right1
print(left,right)
for i in range(0,6):
    if len(left)!=0 or right.count('m')!=3 or right.count('c')!=3:
        print("left to right")
        left,right=find(left,right,'left')
        print(left,'====>',right)
    else:
        break;
    if len(left)!=0 or right.count('m')!=3 or right.count('c')!=3:
        print("right to left")
        right,left=find(right,left,'right')
        print(left,'<====',right)
    else:
        break;

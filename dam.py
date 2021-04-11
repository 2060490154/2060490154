def cor(x,num):
    p = 0
    while 0 < x < 1:
        x *= 10
        p = p + 1
    xx=x
    ci=0

    while xx>1:
        xx=xx/10

        ci+=1
    chu=ci-num-1
    if ci>num:
        while chu >0:
            x=x/10
            chu=chu-1
        x=int(x)
        a=x%10
        if a==5:
            x=x/10
            x=int(x)
            if (x%10)%2:
                x=x+1
            else :
                pass
        elif a>5:
            x=x/10
            x=int(x)
            x+=1
        else:
            x=x/10
            x=int(x)
        for i in range(int(ci-num)):
            x*=10
    elif ci==num:
        x=x*10
        x=int(x)
        a = x % 10
        if a == 5:
            x = x / 10
            x = int(x)
            if (x % 10) % 2:
                x = x + 1
            else:
                pass
        elif a > 5:
            x = x / 10
            x = int(x)
            x += 1
        else:
            x = x / 10
            x = int(x)
    else:
        for n in range(int(num-ci+1)):
            x*=10
        x = int(x)
        a = x % 10
        if a == 5:
            x = x / 10
            x = int(x)
            if (x % 10) % 2:
                x = x + 1
            else:
                pass
        elif a > 5:
            x = x / 10
            x = int(x)
            x += 1
        else:
            x = x / 10
            x = int(x)
    for i in range(int(num-ci)):
            x/=10
    while p > 0:
        x /= 10
        p = p - 1
    return x

#a=0.000085123
#print(cor(a,4))
#有效位数计算函数
a=list(eval(input()))
print(a)
jia=0
num=int(input('保留位数'))
def avo(x):
    sum=0
    for i in x:
        sum+=i
    N=sum/len(a)
    N=cor(N,num+1)
    return N
print("平均值",avo(a))

#15.302,15.304,15.310,15.305,15.303,15.299
for i in a:
    ab=cor(abs(i-avo(a)),num)
    jia+=cor(pow(ab,2),num)
o=cor((jia/(len(a)-1))**(1/2),3)
o=cor(o,2)
print('标准偏差：',o)
print('数据区间',avo(a)-3*o,avo(a)+3*o)
tp=float(input('修正因子'))
c=cor((jia/((len(a)-1)*len(a)))**(1/2),3)
c=cor(c,2)
c=c*tp
print('A类',c)
#67.5146,70.939,71.755,72.896,74.157
yi=float(input('仪器误差'))
gu=float(input('孤独误差'))
ub=(pow(yi,2)+pow(gu,2))**(1/2)
print(ub)
u=(pow(c,2)+pow(ub,2))**(1/2)
print('总',u)



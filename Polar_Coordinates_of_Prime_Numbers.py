def findss(a,b):
    coordinates=[]
    if a==0:
        for i in range(a,b+1,1):
            temp=[]
            for j in range(2,i,1):
                k=i%j
                temp.append(k)
            test=0 in temp
            if test==False:
                coordinates.append(i)
            progress=i
            percentage='{:.2%}'.format(i/b)
            if i!=b:
                spin=int(dt.datetime.now().strftime('%S'))
                if spin%4==0:
                    print("计算中==",percentage,end='\r')
                elif spin%4==1:
                    print("计算中\\\\",percentage,end='\r')
                elif spin%4==2:
                    print("计算中||",percentage,end='\r')
                else:
                    print("计算中//",percentage,end='\r')
            else:
                print("计算完成 ",percentage)
        coordinates.pop(0)
        coordinates.pop(0)
        return coordinates
    elif a==1:
        for i in range(a,b+1,1):
            temp=[]
            for j in range(2,i,1):
                k=i%j
                temp.append(k)
            test=0 in temp
            if test==False:
                coordinates.append(i)
            progress=i
            percentage='{:.2%}'.format(i/b)
            if i!=b:
                spin=int(dt.datetime.now().strftime('%S'))
                if spin%4==0:
                    print("计算中==",percentage,end='\r')
                elif spin%4==1:
                    print("计算中\\\\",percentage,end='\r')
                elif spin%4==2:
                    print("计算中||",percentage,end='\r')
                else:
                    print("计算中//",percentage,end='\r')
            else:
                print("计算完成 ",percentage)
        coordinates.pop(0)
        return coordinates
    else:
        for i in range(a,b+1,1):
            temp=[]
            for j in range(2,i,1):
                k=i%j
                temp.append(k)
            test=0 in temp
            if test==False:
                coordinates.append(i)
            progress=i
            percentage='{:.2%}'.format(i/b)
            if i!=b:
                spin=int(dt.datetime.now().strftime('%S'))
                if spin%4==0:
                    print("计算中==",percentage,end='\r')
                elif spin%4==1:
                    print("计算中\\\\",percentage,end='\r')
                elif spin%4==2:
                    print("计算中||",percentage,end='\r')
                else:
                    print("计算中//",percentage,end='\r')
            else:
                print("计算完成 ",percentage)
        return coordinates
print("此程序可以展示一定区间内的素数在极坐标中的分布情况，其中每一个坐标的极径与极角值均等于素数值")
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import datetime as dt
data=input("输入整数区间，用空格隔开：")
while data!="end":
    data=data.split()
    a=int(data[0])
    b=int(data[1])
    if b-a>=499999:
        print("如果你一定要绘制这个图像，请确保你的计算机在电量耗尽前能够接入电源")
        confirm=input("输入Y以继续，输入N以重新确定区间：")
        if confirm=="Y":
            begin=timer()    
            points=findss(a,b)
            plt.polar(points,points,'.',markersize=1)
            over=timer()
            TIME=over-begin
            temp_minutes=int(TIME/60)
            temp_seconds=TIME-temp_minutes*60
            seconds='{:.1f}'.format(temp_seconds)
            hours=int(temp_minutes/60)
            minutes=int(temp_minutes%60)
            print("用时：",hours,"时",minutes,"分",seconds,"秒")
            if b<=1000:
                print("你可以尝试逐渐增大区间右端点的值，看看图像会变成什么样子")
            elif b>1000 and b<=30000:
                print("你还可以继续增大区间右端点的值，看看在更大的范围内图像会呈现什么形态")
            else:
                print("不建议继续输入更大的区间右端点的值，因为所需时间会随区间右端点的值和区间长度的变大而迅速增加，如果你有充足的时间，则可以继续增大区间右端点的值，图像会渐渐呈现出另一种形态")
            plt.show()
            data=input("输入区间以继续，输入end退出程序：")
        elif confirm=="N":
            data=input("重新输入区间以继续，输入end退出程序：")
    else:
        begin=timer()    
        points=findss(a,b)
        plt.polar(points,points,'.',markersize=1)
        over=timer()
        TIME=over-begin
        temp_minutes=int(TIME/60)
        temp_seconds=TIME-temp_minutes*60
        seconds='{:.1f}'.format(temp_seconds)
        hours=int(temp_minutes/60)
        minutes=int(temp_minutes%60)
        print("用时：",hours,"时",minutes,"分",seconds,"秒")
        if b<=1000:
            print("你可以尝试逐渐增大区间右端点的值，看看图像会变成什么样子")
        elif b>1000 and b<=30000:
            print("你还可以继续增大区间右端点的值，看看在更大的范围内图像会呈现什么形态")
        else:
            print("不建议继续输入更大的区间右端点值，因为所需时间会随区间右端点的值和区间长度的变大而迅速增加，如果你有充足的时间，则可以继续增大区间右端点的值，图像会渐渐呈现出另一种形态")
        plt.show()
        data=input("输入区间以继续，输入end退出程序：")

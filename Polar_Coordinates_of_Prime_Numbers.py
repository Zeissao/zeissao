def fdprnbs(a,b):
    coordinates=[]
    for i in range(a,b+1,1):
        coordinates.append(i)
        for j in range(2,i,1):
            k=i%j
            if k==0:
                coordinates.pop()
                break
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
    if a==0:
        coordinates.pop(0)
        coordinates.pop(0)
    if a==1:
        coordinates.pop(0)
    return coordinates
print("此程序可以展示一定区间内的素数在极坐标中的分布情况，其中每一个坐标的极径与极角值均等于对应的素数值")
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import datetime as dt
data=input("输入整数区间，用空格隔开：")
while data!="end":
    data=data.split()
    a=int(data[0])
    b=int(data[1])
    if b-a>=6000000:
        print("如果你一定要绘制这个图像，请确保你的计算机在电量耗尽前能够接入电源")
        confirm=input("输入Y以继续，输入N以重新确定区间：")
        if confirm=="Y":
            begin=timer()    
            points=fdprnbs(a,b)
            plt.polar(points,points,'.',markersize=1)
            over=timer()
            TIME=over-begin
            temp_minutes=int(TIME/60)
            temp_seconds=TIME-temp_minutes*60
            seconds='{:.1f}'.format(temp_seconds)
            hours=int(temp_minutes/60)
            minutes=int(temp_minutes%60)
            print("用时：",hours,"时",minutes,"分",seconds,"秒")
            plt.show()
            data=input("输入区间以继续，输入end退出程序：")
        elif confirm=="N":
            data=input("重新输入区间以继续，输入end退出程序：")
    else:
        begin=timer()    
        points=fdprnbs(a,b)
        plt.polar(points,points,'.',markersize=1)
        over=timer()
        TIME=over-begin
        temp_minutes=int(TIME/60)
        temp_seconds=TIME-temp_minutes*60
        seconds='{:.1f}'.format(temp_seconds)
        hours=int(temp_minutes/60)
        minutes=int(temp_minutes%60)
        print("用时：",hours,"时",minutes,"分",seconds,"秒")
        plt.show()
        data=input("输入区间以继续，输入end退出程序：")

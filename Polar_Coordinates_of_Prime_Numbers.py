def prime_nums(a,b):
    coordinates=[]
    if (a==0 and (b==0 or b==1)) or (a==1 and b==1):
        print("计算完成： {}".format("100.00%"))
        return coordinates
    if (a==0 or a==1) and b==2:
        coordinates.append(2)
        print("计算完成： {}".format("100.00%"))
        return coordinates
    for i in range(a,b+1,1):
        judge=0
        if i%2!=0:
            for j in range(2,int(i**0.5),1):
                k=i%j
                if k==0:
                    judge=1
                    break
            if judge==0:
                coordinates.append(i)
            percentage='{:.2%}'.format(i/b)
            if i!=b:
                spin=int(dt.datetime.now().strftime('%S'))
                if spin%4==0:
                    print("计算中-：{}".format(percentage),end='\r')
                elif spin%4==1:
                    print("计算中\：{}".format(percentage),end='\r')
                elif spin%4==2:
                    print("计算中|：{}".format(percentage),end='\r')
                else:
                    print("计算中/：{}".format(percentage),end='\r')
    coordinates[0]=2
    print("计算完成： {}".format(percentage))
    return coordinates

print("此程序可以展示一定区间内的素数在极坐标中的分布情况，其中每一个坐标的极径与极角值均等于对应的素数值")
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import datetime as dt
data=input("输入整数区间，用空格隔开：")
while data!="end":
    data=data.split()
    a=int(data[0])
    b=int(data[1])
    if b-a>=100000000:
        print("如果你一定要绘制这个图像，请确保你的计算机在电量耗尽前能够接入电源")
        confirm=input("输入Y继续，输入N重新确定区间：")
        if confirm=="Y":
            begin=timer()    
            points=prime_nums(a,b)
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
            data=input("输入区间继续，输入end退出程序：")
        elif confirm=="N":
            data=input("重新输入区间继续，输入end退出程序：")
    else:
        begin=timer()    
        points=prime_nums(a,b)
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
        data=input("输入区间继续，输入end退出程序：")

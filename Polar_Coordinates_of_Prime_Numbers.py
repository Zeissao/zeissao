def prime_nums(a,b):
    coordinates=[]
    if (a==0 and (b==0 or b==1)) or (a==1 and b==1):
        print("计算完成： {}".format("100.00%"))
        return coordinates
    if (a==0 or a==1) and b==2:
        coordinates.append(2)
        print("计算完成： {}".format("100.00%"))
        return coordinates
    if a==2 and b==2:
        coordinates.append(2)
        return coordinates
    for i in range(a,b+1,1):
        judge=0
        if i%2!=0:
            for j in range(2,int(i**0.5+1),1):
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
                    print("计算中-： {}".format(percentage),end='\r')
                elif spin%4==1:
                    print("计算中\： {}".format(percentage),end='\r')
                elif spin%4==2:
                    print("计算中|： {}".format(percentage),end='\r')
                else:
                    print("计算中/： {}".format(percentage),end='\r')
    if len(coordinates)==0:
        return 0
    if 1 in coordinates:
        position=coordinates.index(1)
        coordinates[position]=2
    if (2 not in coordinates) and (a<=2 and b>=2):
        coordinates.append(2)
    print("计算完成： {}".format("100.00%"))
    return coordinates

print("此程序可以展示一定区间内的素数在极坐标中的分布情况，其中每一个坐标的极径与极角值均等于对应的素数值")
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import datetime as dt
data=input("输入整数区间，用空格隔开，若输入end则退出程序：")
while data!="end":
    try:
        data=data.split()
        a=int(data[0])
        b=int(data[1])
        if b-a>=100000000:
            print("如果你一定要绘制这个图像，请确保你的计算机在电量耗尽前能够接入电源")
            confirm=input("输入go继续，输入no重新确定区间：")
            lauch=0
            while lauch==0:
                if confirm=="go":
                    lauch=1
                    begin=timer()    
                    points=prime_nums(a,b)
                    if points!=0:
                        plt.polar(points,points,'.',markersize=1,color='#FF5511')
                    over=timer()
                    TIME=over-begin
                    temp_minutes=int(TIME/60)
                    temp_seconds=TIME-temp_minutes*60
                    seconds='{:.1f}'.format(temp_seconds)
                    hours=int(temp_minutes/60)
                    minutes=int(temp_minutes%60)
                    print("用时：",hours,"时",minutes,"分",seconds,"秒")
                    if points!=0 and (not ((a==0 and (b==0 or b==1)) or (a==1 and b==1))):
                        plt.show()
                    else:
                        print("此区间中不含素数")
                    data=input("输入区间继续，输入end退出程序：")
                elif confirm=="no":
                    lauch=1
                    data=input("重新输入区间继续，输入end退出程序：")
                else:
                    print("输入有误，请重新输入!")
                    confirm=input("输入go继续，输入no重新确定区间：")
        else:
            begin=timer()    
            points=prime_nums(a,b)
            if points!=0:
                plt.polar(points,points,'.',markersize=1,color='#FF5511')
            over=timer()
            TIME=over-begin
            temp_minutes=int(TIME/60)
            temp_seconds=TIME-temp_minutes*60
            seconds='{:.1f}'.format(temp_seconds)
            hours=int(temp_minutes/60)
            minutes=int(temp_minutes%60)
            print("用时：",hours,"时",minutes,"分",seconds,"秒")
            if points!=0 and (not ((a==0 and (b==0 or b==1)) or (a==1 and b==1))):
                plt.show()
            else:
                print("此区间中不含素数")
            data=input("输入区间继续，输入end退出程序：")
    except:
        print("输入有误，请重新输入!")
        data=input("输入整数区间，用空格隔开，若输入end则退出程序：")


# 猜字游戏
# 需求：
# 1、猜的数字是系统产生的，不是自己定义的
# 2、键盘输入的   操作完填入：input（“提示”）
# 3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
# 4、循环			操作完填入：while 条件循环
# 任务：猜3次就睡眠 time.sleep(10)
#     起始：5000金币，每猜错一次，减去500金币，一直扣完为止。15次没猜中，系统锁定。猜中加3000。

# randint = random.randint(1, 30)  # 随机产生的数字
import random
import time

randint=random.randint(1,300)
jin_bi=5000
ci_shu=1
while True:
    print(randint)
    print(jin_bi)
    num =(input("请输入数字"))
    if num.isdigit():
        int(eval(num))
        if num==randint:
            print("猜对了")
            jin_bi +=3000
            print(jin_bi)

        elif num > randint:
            print("猜大了")

        elif num<  randint:
            print("猜小了")
    else:
            print("别瞎输")
    if ci_shu >16:
        print(jin_bi)
        break
    jin_bi-=500
    if ci_shu%3==0:
        time.sleep(10)
    ci_shu+=1
    if jin_bi <=0:
        break





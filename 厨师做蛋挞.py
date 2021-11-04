import time
from threading import Thread


dqntalan=500

class chushi(Thread):
    chushiname=""
    count=0
    def run(self) -> None:
        global dqntalan
        while True:

            if dqntalan <500:
                self.count=self.count+1
                dqntalan+=1




            else:
                time.sleep(0.1)
                dqntalan+=1
                self.count = self.count + 1

            print(self.chushiname, "做了", self.count, "个蛋挞工资",self.count*12)
class guke(Thread):
    GUKE=""
    num=0
    def run(self) -> None:
        global dqntalan
        while True:
            if dqntalan >=0:
                dqntalan-=1
                self.num+=1

            else:
                time.sleep(0.1)
                dqntalan-=1
                self.num+=1

            if self.num*3<=30 and dqntalan >0:
                print(self.GUKE, "买了", self.num)
            else:
                break
            print(self.GUKE,"买了",self.num,"蛋挞")




p1=chushi()
a=chushi()
a.chushiname=("w")
p1.chushiname=("1")
p1.start()
a.start()
p2=guke()
p3=guke()
p5=guke()
p6=guke()
p7=guke()

p2.GUKE=("q")
p3.GUKE=("a")
p6.GUKE=("3")
p7.GUKE=("ddff")
p5.GUKE=("dff")

p3.start()
p2.start()

p5.start()
p6.start()
p7.start()



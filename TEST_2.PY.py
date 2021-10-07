print("|                    12月份衣服销售数据                          |")
print("|  日期    服装名称    价格/件    库存数量    销售量/每日            |")
print("|  1号     羽绒服      253.6	  500	     10                  |")
print("|  2号     牛仔裤      86.3	  600	     60                  |")
print("|  3号     风衣        96.8	  335	     43                  |")
print("|  4号     皮草        135.9	  855	     63                  |")
print("|  5号     T恤         65.8	  632	     63                  |")
print("|  6号     衬衫        49.3	  562	     120                 |")
print("|  7号     牛仔裤      49.3	  562	     12                  |")
print("|  8号     羽绒服      253.6	  500	     69                  |")
print("|  9号     牛仔裤      86.3	  600	     35                  |")
print("|  10号    皮草        253.6	  500	     140                 |")
print("|  11号    牛仔裤      86.3	  600	     90                  |")
print("|  12号    皮草        135.9	  855	     24                  |")
print("|  13号    T恤         65.8	  632	     45                  |")
print("|  14号    风衣         96.8	  335	     25                  |")
print("|  15号    牛仔裤       86.3	  600	     60                  |")
print("|  16号    T恤         65.8	  632	     129                 |")
print("|  17号    羽绒服       253.6	  500        10                  |")
print("|  18号    风衣         96.8	  335        43                  |")
print("|  19号    T恤         65.8	  632	     63                  |")
print("|  20号    牛仔裤       86.3	  600	     60                  |")
print("|  21号    皮草        135.9	  855	     63                  |")
print("|  22号    风衣        96.8	  335	     60                  |")
print("|  23号    T恤         65.8	  632	     58                  |")
print("|  24号    牛仔裤       86.3	  600	     140                 |")
print("|  25号    T恤         65.8	  632	     48                  |")
print("|  26号    风衣        96.8	  335	     43                  |")
print("|  27号    皮草        135.9	  855	     57                  |")
print("|  28号    羽绒服       253.6	  500	     10                  |")
print("|  29号    T恤         65.8	  632	     63                  |")
print("|  30号    风衣         96.8	  335	     78                  |")
yu_rongfuprice=253.6
yu_number=239
niu_zaikuprice=86.3
niu_zainumber=517
fen_yiprice=96.8
feng_yinumber=292
pi_caoprice=135.9
pi_caonumber=207
t_xueprice=65.8
t_xunumber=469
chen_shanprice=49.3
chen_shannumber=120
z_xiaoshoue=float(yu_number*yu_rongfuprice+niu_zainumber*niu_zaikuprice+fen_yiprice*feng_yinumber+pi_caonumber*pi_caoprice
             +t_xunumber*t_xueprice+chen_shannumber*chen_shanprice)
print("总销售额为"+str(z_xiaoshoue))
num=yu_number+niu_zainumber+feng_yinumber+pi_caonumber+t_xunumber+chen_shannumber
num2=num/30
print("平均每日销售数量"+str(num2))
a=(yu_number/num)
b=niu_zainumber/num
c=feng_yinumber/num
d=pi_caonumber/num
e=t_xunumber/num
f=chen_shannumber/num
a=round(a,2)
b=round(b,2)
c=round(c,2)
d=round(d,2)
e=round(e,2)
f=round(f,2)

print("羽绒服的销售占比",a)
print("牛仔裤的销售占比",b)
print("风衣的销售占比",c)
print("皮草的销售占比",d)
print("T恤的销售占比",e)
print("衬衫的销售占比",f)



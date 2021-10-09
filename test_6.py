one_bian=float(input("请输入第一条边长："))
two_bian=float(input("请输入第二条变长："))
thre_bian=float(input("请输入第三条变长："))
z=one_bian+thre_bian+two_bian
p=z/2
if one_bian+thre_bian>two_bian and one_bian+two_bian>thre_bian and two_bian+thre_bian>one_bian:
    print("这个三角形的周长是：",z,"这个三角形的面积是：",p*(p-one_bian)*(p-two_bian)*(p-thre_bian))

else:
    print("不能构成三角形")
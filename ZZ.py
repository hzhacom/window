import matplotlib.pyplot as p
p.rcParams['font.sans-serif'] = ['KaiTi']
p.rcParams['axes.unicode_minus'] = False




a = ['刘欣睿','周子琪','李思琪','徐俊骢','白思璇','胡智豪','刘桐']
b = ['语文','数学','英语','政治','历史','地理','生物']
lsq = [112.5,136,124.5,49,44,31,36.5]
lsr = [109,136,118,46,44,32,36]
hzh = [104,124,123.5,47,44,32,37.5]
bsx = [104,137,119.5,45,41,30,34]
zzq = [104,132,129.5,43,41,27.5,32.5]
xjc = [92,128,126,45,44,31,40]
lt = [99,117,119,45,46,30,25]
w = 0.1
s = list(range(len(a)))
s_1 = [i+w for i in s]
s_2 = [i+w*2 for i in s]
s_3 = [i+w*3 for i in s]
s_4 = [i+w*4 for i in s]
s_5 = [i+w*5 for i in s]
s_6 = [i+w*6 for i in s]


fig,ax = p.subplots()
p.xticks(s_3,b)
p.style.use('Solarize_Light2')
l = aa = ax.bar(range(len(a)),lsq,width=w,label='李思琪')
l_1 = bb = ax.bar(s_1,lsr,width=w,label='刘欣睿')
l_2 = cc = ax.bar(s_2,hzh,width=w,label='胡智豪')
l_3 = dd = ax.bar(s_3,bsx,width=w,label='白思璇')
l_4 = ee = ax.bar(s_4,zzq,width=w,label='周子琪')
l_5 = ff = ax.bar(s_5,xjc,width=w,label='徐俊骢')
l_6 = gg = ax.bar(s_6,lt,width=w,label='刘桐')
p.title('大杂烩：七下月考1',fontsize=20)
p.xlabel('姓名',fontsize=10)
p.ylabel('分数',fontsize=10)
p.tick_params(labelsize=10)


manager = p.get_current_fig_manager()
manager.full_screen_toggle()

#设置标签
for k in l:
    height=k.get_height()
    p.text(k.get_x() + k.get_width() / 2, height, str(height),fontsize=6, ha="center", va="bottom")

for k in l_1:
    height=k.get_height()
    p.text(k.get_x() + k.get_width() / 2, height, str(height),fontsize=6, ha="center", va="bottom")

for k in l_2:
    height=k.get_height()
    p.text(k.get_x() + k.get_width() / 2, height, str(height),fontsize=6, ha="center", va="bottom")

for k in l_3:
    height=k.get_height()
    p.text(k.get_x() + k.get_width() / 2, height, str(height),fontsize=6, ha="center", va="bottom")

for k in l_4:
    height=k.get_height()
    p.text(k.get_x() + k.get_width() / 2, height, str(height),fontsize=6, ha="center", va="bottom")

for k in l_5:
    height=k.get_height()
    p.text(k.get_x() + k.get_width() / 2, height, str(height),fontsize=6, ha="center", va="bottom")

for k in l_6:
    height=k.get_height()
    p.text(k.get_x() + k.get_width() / 2, height, str(height),fontsize=6, ha="center", va="bottom")

#p.text(70,70,'好生学习！！！',alpha=0.5)




p.legend()
p.show()

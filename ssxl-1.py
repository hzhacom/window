import matplotlib.pyplot as p
p.rcParams['font.sans-serif'] = ['KaiTi']
p.rcParams['axes.unicode_minus'] = False


a = ['周子琪','李思琪','徐俊骢','刘桐','胡智豪','刘欣睿','白思璇']
b = [109,118,120,0,116,120,109]
fig,ax = p.subplots()
c = ax.bar(a,b)
ax.bar(a[0],b[0],color='green')
ax.bar(a[2],b[2],color='black')
ax.bar(a[5],b[5],color='black')
ax.bar(a[4],b[4],color='green')

for k in c:
    height=k.get_height()
    p.text(k.get_x() + k.get_width() / 2, height, str(height),fontsize=10, ha="center", va="bottom")
ax.margins(0)
# ax.twinx() 复合图表


p.grid(axis='y',color='blue')
p.show()
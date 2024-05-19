from matplotlib import pyplot as p
p.rcParams['font.sans-serif'] = ['KaiTi']
p.rcParams['axes.unicode_minus'] = False


a = ['徐俊骢','白思璇','李思琪','周子琪','刘欣睿','胡智豪','刘桐']
b = [112,112,106,103,109,96,93]
fig,ax = p.subplots()
h = ax.bar(a,b,color='red')
p.style.use('bmh')
for k in h:
    height=k.get_height()
    p.text(k.get_x() + k.get_width() / 2, height, str(height),fontsize=6, ha="center", va="bottom")

p.text('周子琪',80,'好生学习',fontsize=20,alpha=0.5)
#
ax.grid(which='both',axis='y',color='blue',alpha=0.5,linewidth=0.3)
p.title('.',fontsize=25,color='green')
p.show()
import matplotlib.pyplot as p 
p.rcParams['font.sans-serif'] = ['KaiTi']
p.rcParams['axes.unicode_minus'] = False

a = ['周子琪','李思琪','徐俊骢','刘桐','胡智豪','刘欣睿','白思璇','平均']
b = [107,112,113,102,109,108,94,104]
fig,ax = p.subplots()
v = ax.bar(a,b)
p.style.use('seaborn-v0_8-notebook')
for i in v:
    height = i.get_height()
    p.text(i.get_x() + i.get_width() / 2,height,str(height),fontsize=10,ha='center')



p.title('数学小练',fontsize=20)
p.xlabel('姓名',fontsize=15)
p.ylabel('成绩',fontsize=15)
p.tick_params(labelsize=10)
p.show()
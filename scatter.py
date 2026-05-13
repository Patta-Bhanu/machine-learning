from matplotlib import pyplot as plt
import pandas as pd
plt.style.use('fivethirtyeight')
x=[5,7,8,5,6,7,9,2,3,4,4,4,2,6,3,6,8,6,4,1]
y=[7,4,3,9,1,3,2,5,2,4,8,7,1,6,4,9,7,7,5,1]
colors = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sizes = [200,150,300,250,180,220,350,120,140,200,
         280,260,110,230,170,320,340,290,210,130]

plt.scatter(x,y,s=sizes,c=colors,cmap='Greens',marker='o',edgecolor='black',linewidth=1,alpha=0.75)
cbar=plt.colorbar()
cbar.set_label('satisfaction')
plt.title('yt trending vedioes')
plt.xlabel('view count')
plt.ylabel('total likes')
plt.tight_layout()
plt.show()
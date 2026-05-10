from matplotlib import pyplot as plt
plt.style.use('tableau-colorblind10')
dev_x=[x for x in range(25,36)]
dev_y=[34898,42000,46790,49768,53200,
      56000,62316,64579,67800,68767,73700]
plt.plot(dev_x,dev_y,color='#444444',linestyle='--',marker='.',label='all dev')
py_dev_y=[39000,45000,49000,53000,57000,59200,66000,68000,70000,74000,80000]
plt.plot(dev_x,py_dev_y,color='b',linestyle='-',marker='o',linewidth=3,label='python' )
js_dev_y = [35000,40000,44000,48000,52000,56000,60000,64000,68000,72000,76000]
plt.plot(dev_x,js_dev_y,color='#adad3b',linestyle='-',marker='o',linewidth=3,label='javascript')
plt.title('median salary by age')
plt.xlabel('Age')
plt.ylabel('salary')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
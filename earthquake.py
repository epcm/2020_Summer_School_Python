import csv
import matplotlib.pyplot as plt


with open("all_month.csv", encoding = 'utf-8') as f:
    reader = csv.DictReader(f)
    depths, mags = [], []
    for row in reader:
        # 删除有问题的数据
        try:
            depths.append(float(row['depth']))
        except:
            continue
        try:
            mags.append(float(row['mag']))
        except:
            depths.remove(depths[-1])
        

ax1 = plt.subplot(2,2,1)
ax2 = plt.subplot(2,2,2)
ax3 = plt.subplot(2,1,2)

plt.sca(ax1)
plt.hist(depths, 100, color=(0.,0.,0.5))
plt.title('mag')
plt.title('depth')
plt.xlabel('depth')
plt.ylabel('count')

plt.sca(ax2)
plt.hist(mags, 100, color=(0.5,0.,0.))
plt.title('mag')
plt.xlabel('mag')
plt.ylabel('count')

plt.sca(ax3)
plt.scatter(depths, mags, s=1 ,color=(0.,0.5,0.))
plt.xlabel('depth')
plt.ylabel('mag')
plt.show()






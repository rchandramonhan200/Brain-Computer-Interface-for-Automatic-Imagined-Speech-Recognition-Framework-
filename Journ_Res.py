# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Creating dataset
np.random.seed(10)
data_1 = np.random.normal(90, 1, 200)
data_2 = np.random.normal(92, 1, 200)
data_3 = np.random.normal(89, 1, 200)
data_4 = np.random.normal(91, 1, 200)
data_5 = np.random.normal(95, 1, 200)
data = [data_1, data_2, data_3, data_4, data_5]

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)

# Creating axes instance
bp = ax.boxplot(data, patch_artist=True,
                notch='True', vert=0)

colors = ['#0000FF', '#00FF00',
          '#FFFF00', '#FF00FF', 'k']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# changing color and linewidth of
# whiskers
for whisker in bp['whiskers']:
    whisker.set(color='#8B008B',
                linewidth=1.5,
                linestyle=":")

# changing color and linewidth of
# caps
for cap in bp['caps']:
    cap.set(color='#8B008B',
            linewidth=2)

# changing color and linewidth of
# medians
for median in bp['medians']:
    median.set(color='red',
               linewidth=3)

# changing style of fliers
for flier in bp['fliers']:
    flier.set(marker='D',
              color='#e7298a',
              alpha=0.5)

# x-axis labels
ax.set_yticklabels(['ResNet', 'CNN',
                    'DenseNet', 'ResDenseNet', 'EHOA-HC-AARDNet'])
plt.ylabel('Methods')
plt.xlabel('Accuracy (%)')
# Adding title
# plt.title("Customized box plot")

# Removing top axes and right axes
# ticks
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
plt.yticks(rotation=60)

# path1 = "./Journ_Res/Scalability.png"
path1 = "Confidence Interval-Dataset 2.png"
plt.savefig(path1)

# show plot
plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# # Fixing random state for reproducibility
# np.random.seed(19680801)
#
# fig = plt.figure()
# ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
# # Example data
# people = ('A1_Score','A2_Score','A3_Score','A4_Score','A5_Score','A6_Score','A7_Score','A8_Score','A9_Score','A10_Score','gender', 'jundice', 'autism', 'used_app_before',
#           'age', 'ethnicity', 'contry_of_res', 'result', 'relation')
# y_pos = np.arange(19)
# Performance = np.zeros((704, 19))
# performance1 = np.random.randint(2, size=(704, 13))
# age = np.random.randint(5, 25, size=(704))
# ethnicity = np.random.randint(6, size=(704))
# contry_of_res = np.random.randint(5, size=(704))
# result = np.random.randint(10, size=(704))
# # age_desc = np.random.randint(0, size=(704, 1))
# relation =  np.random.randint(6, size=(704))
# Performance[:, :13] = performance1
# # Performance[:, 15] = performance1
# Performance[:, 14] = max(age)
# Performance[:, 15] = max(ethnicity)
# Performance[:, 16] = max(contry_of_res)
# Performance[:, 17] = max(result)
# # Performance[:, 20] = age_desc
# Performance[:, 18] = max(relation)
#
#
# error = np.random.rand(len(people))
#
# ax.barh(y_pos, Performance[0], xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# # ax.set_xlabel('Performance')
# # ax.set_title('How fast do you want to go today?')
#
# # plt.show()
# y_pos1 = np.arange(4)
# fig = plt.figure()
# ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
# A =[94, 95, 96, 98]
# ax.bar(y_pos1, A)
# ax.set_xticks(y_pos1, labels=('Feature', 'Selected Feature', 'Weighted Feature', 'Weighted Feature with Atrous'))
# # ax.invert_yaxis()  # labels read top-to-bottom
# plt.xticks(rotation=15)
# plt.ylabel('Accuracy')
# plt.ylim(93, 97)
# path1 = "./Journ_Res/interpretability.png"
# plt.savefig(path1)
# plt.show()



# # Creating dataset
# np.random.seed(10)
# data_1 = np.random.normal(90, 4, 200)
# data_2 = np.random.normal(86, 4, 200)
# data_3 = np.random.normal(94, 3, 200)
# data_4 = np.random.normal(92, 3, 200)
# data = [data_1, data_2, data_3, data_4]
#
# fig = plt.figure(figsize=(10, 7))
# ax = fig.add_subplot(111)
#
# # Creating axes instance
# bp = ax.boxplot(data, patch_artist=True,
#                 notch='True', vert=0)
#
# colors = ['#0000FF', '#00FF00',
#           '#FFFF00', '#FF00FF']
#
# for patch, color in zip(bp['boxes'], colors):
#     patch.set_facecolor(color)
#
# # changing color and linewidth of
# # whiskers
# for whisker in bp['whiskers']:
#     whisker.set(color='#8B008B',
#                 linewidth=1.5,
#                 linestyle=":")
#
# # changing color and linewidth of
# # caps
# for cap in bp['caps']:
#     cap.set(color='#8B008B',
#             linewidth=2)
#
# # changing color and linewidth of
# # medians
# for median in bp['medians']:
#     median.set(color='red',
#                linewidth=3)
#
# # changing style of fliers
# for flier in bp['fliers']:
#     flier.set(marker='D',
#               color='#e7298a',
#               alpha=0.5)
#
# # x-axis labels
# ax.set_yticklabels(['50', '100',
#                     '150', '200'])
# plt.ylabel('Data Size(KB)')
# plt.xlabel('SSIM (%)')
# # Adding title
# # plt.title("Customized box plot")
#
# # Removing top axes and right axes
# # ticks
# ax.get_xaxis().tick_bottom()
# ax.get_yaxis().tick_left()
#
# # path1 = "./Journ_Res/Scalability.png"
# path1 = "Scalability2.png"
# plt.savefig(path1)
#
# # show plot
# plt.show()
#
#
#
#
# # Creating dataset
# np.random.seed(10)
# data_1 = np.random.normal(92, 4, 200)
# data_2 = np.random.normal(90, 4, 200)
# data_3 = np.random.normal(86, 3, 200)
# data_4 = np.random.normal(88, 3, 200)
# data = [data_1, data_2, data_3]
#
# fig = plt.figure(figsize=(10, 7))
# ax = fig.add_subplot(111)
#
# # Creating axes instance
# bp = ax.boxplot(data, patch_artist=True,
#                 notch='True', vert=0)
#
# colors = ['#0000FF', '#00FF00',
#           '#FFFF00', '#FF00FF']
#
# for patch, color in zip(bp['boxes'], colors):
#     patch.set_facecolor(color)
#
# # changing color and linewidth of
# # whiskers
# for whisker in bp['whiskers']:
#     whisker.set(color='#8B008B',
#                 linewidth=1.5,
#                 linestyle=":")
#
# # changing color and linewidth of
# # caps
# for cap in bp['caps']:
#     cap.set(color='#8B008B',
#             linewidth=2)
#
# # changing color and linewidth of
# # medians
# for median in bp['medians']:
#     median.set(color='red',
#                linewidth=3)
#
# # changing style of fliers
# for flier in bp['fliers']:
#     flier.set(marker='D',
#               color='#e7298a',
#               alpha=0.5)
#
# # x-axis labels
# ax.set_yticklabels(['50', '100',
#                     '150'])
# plt.ylabel('Data size(kb)')
# plt.xlabel('SSIM (%)')
# # Adding title
# # plt.title("Customized box plot")
#
# # Removing top axes and right axes
# # ticks
# ax.get_xaxis().tick_bottom()
# ax.get_yaxis().tick_left()
#
# # path1 = "./Journ_Res/Scalability.png"
# path1 = "Scalability3.png"
# plt.savefig(path1)
#
# # show plot
# plt.show()
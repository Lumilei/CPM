#导入必要库
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
# #IMDB   items  sup
# #定义结果字典
# results_dict = {
#     "IMDB": {
#         "piCPM": {
#             "k=1": [194, 114, 70, 54, 41, 28, 25, 23, 21, 19],
#             "k=2": [281, 94, 62, 33, 22, 14, 10, 9, 9, 8],
#             "k=3": [278, 108, 74, 22, 9, 8, 6, 5, 5, 4],
#             "k=4": [271, 129, 80, 9, 1, 1, 1, 1, 1, 1],
#             "k=5": [214, 126, 61, 2, 0, 0, 0, 0, 0, 0],
#         }
#     }
# }
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# color_lst = ["#A72921", "#3C5DA0", '#FF69B4', "#0F6F00", "#FFD700"]
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "IMDB"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# x = np.array(labels)
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 初始化最大值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=mixup_method_list[j],
#             color=color_lst[j % len(color_lst)],
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         max_y_value = max(max_y_value, max(y_data))  # 更新最大值
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Number of k-itemsets', fontsize=28)
#     ax.set_xlabel('# Support', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)
#     ax.set_xticklabels(labels, fontsize=24)
#     ax.set_ylim(0, max_y_value * 1.1)  # 将 y 轴范围设置为 0 到最大值的 1.1 倍
#
#     ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"{dataset}_sup_items.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()


# ###IMDB dia items
# # 定义结果字典
# results_dict = {
#     "IMDB": {
#         "piCPM": {
#             "k=1": [40, 40, 40, 40, 40],
#             "k=2": [15, 22, 23, 27, 36],
#             "k=3": [5,   8, 8,  10, 14],
#             "k=4": [0,   1, 1,   1, 2],
#             "k=5": [0,   0, 0,   0, 0],
#         }
#     }
# }
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# color_lst = ["#A72921", "#3C5DA0", '#FF69B4', "#0F6F00", "#FFD700"]
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "IMDB"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [1, 2, 3, 4, 5]
# x = np.array(labels)
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 初始化最大值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=mixup_method_list[j],
#             color=color_lst[j % len(color_lst)],
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         max_y_value = max(max_y_value, max(y_data))  # 更新最大值
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Number of k-itemsets', fontsize=28)
#     ax.set_xlabel('# Diameter', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)
#     ax.set_xticklabels(labels, fontsize=24)
#     ax.set_ylim(0, max_y_value * 1.1)  # 将 y 轴范围设置为 0 到最大值的 1.1 倍
#
#
#     ax.tick_params(axis='y', labelsize=24)
#     ax.legend(loc="upper right", fontsize=24)
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"{dataset}_dia_items.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()



#  IMDB     items   time_window
# 定义结果字典
# results_dict = {
#     "IMDB": {
#         "piCPM": {
#             # #      60  120 180  240 300 360 420 480 540 600 660 720 780 840 900  960 1020 1080 1140  1200 1260 1320 1380 1440 1680 1920  2160 2400  2640 2880 4320 5760  7200
#             # "k=1": [54, 40, 40, 55, 40, 40, 40, 54, 40, 40, 40, 54, 40, 40,  40,  54, 40,  40,  40,   54,   40,  40,  40, 54,  54,  54,                         54,  55,   55,  54],
#             # "k=2": [15, 16, 14, 22, 19, 18, 19, 32, 17, 24, 25, 29, 19, 19,  25,  34, 22,  24,  23,   36,   29,  19,  25, 33,  34,  34,                       30,  32,   38,  30],
#             # "k=3": [7,   8, 7,  13, 9,   8,  9, 16, 7,   9, 11, 20,  8,  8,  11,  26,  9,  11,  10,   27,   17,   8,  11, 25,  26,  26,                    24,  25,   27,  24],
#             # "k=4": [1,   1, 1,   4, 1,   1,  1,  5, 1,   1,  1,  9,  1,  1,   1,  15,  1,   1,   1,   15,    8,    1,  1, 15,  15,  15,                     15,  15,   15,  15],
#             # "k=5": [0,   0, 0,   0, 0,   0,  0,  1, 0,   0,  0,  2,  0,  0,   0,   6,  0,   0,   0,    6,    4,    0,  0,  6,   6,   6,                       6,   6,    6,  6],
#
#             #      60  240 480 720 960 1200 1440 1680 1920  2160 2400  2640 2880
#             "k=1": [54, 54, 54, 54, 54, 54,  54,  54,  54,   54,  54,   54,  54 ],
#             "k=2": [15, 22, 27, 29, 34, 34,  36,  36,  36,   36,  36,   40,  40 ],
#             "k=3": [7,  13, 14, 20, 26, 26,  27,  27,  27,   27,  27,   33,  33 ],
#             "k=4": [1,   4, 5,  9,  15, 15,  15,  15,  15,   15,  15,   22,  22 ],
#             "k=5": [0,   0, 1,  2,  6,   6,   6,   6,   6,    6,   6,   10,  10 ],
#         }
#     }
# }
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# color_lst = ["#A72921", "#3C5DA0", '#FF69B4', "#0F6F00", "#FFD700"]
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "IMDB"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [ 1,  4, 8, 12, 16, 20, 24, 28, 32,  36, 40,  44, 48]
# x = np.array(labels)
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 初始化最大值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=mixup_method_list[j],
#             color=color_lst[j % len(color_lst)],
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         max_y_value = max(max_y_value, max(y_data))  # 更新最大值
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Number of k-itemsets', fontsize=28)
#     ax.set_xlabel('# Time Window (h)', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)
#     ax.set_xticklabels(labels, fontsize=24)
#     ax.set_ylim(0, max_y_value * 1.1)  # 将 y 轴范围设置为 0 到最大值的 1.1 倍
#
#     ax.tick_params(axis='y', labelsize=24)
#     ax.legend(loc="upper right", fontsize=24)
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"{dataset}_time_items.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()

# IMDB     items   time_window
# 定义结果字典



# results_dict = {
#     "IMDB": {
#         "piCPM": {
#             # #      60  120 180  240 300 360 420 480 540 600 660 720 780 840 900  960 1020 1080 1140  1200 1260 1320 1380 1440 1680 1920  2160 2400  2640 2880 4320 5760  7200
#             # "k=1": [54, 40, 40, 55, 40, 40, 40, 54, 40, 40, 40, 54, 40, 40,  40,  54, 40,  40,  40,   54,   40,  40,  40, 54,  54,  54,                         54,  55,   55,  54],
#             # "k=2": [15, 16, 14, 22, 19, 18, 19, 32, 17, 24, 25, 29, 19, 19,  25,  34, 22,  24,  23,   36,   29,  19,  25, 33,  34,  34,                       30,  32,   38,  30],
#             # "k=3": [7,   8, 7,  13, 9,   8,  9, 16, 7,   9, 11, 20,  8,  8,  11,  26,  9,  11,  10,   27,   17,   8,  11, 25,  26,  26,                    24,  25,   27,  24],
#             # "k=4": [1,   1, 1,   4, 1,   1,  1,  5, 1,   1,  1,  9,  1,  1,   1,  15,  1,   1,   1,   15,    8,    1,  1, 15,  15,  15,                     15,  15,   15,  15],
#             # "k=5": [0,   0, 0,   0, 0,   0,  0,  1, 0,   0,  0,  2,  0,  0,   0,   6,  0,   0,   0,    6,    4,    0,  0,  6,   6,   6,                       6,   6,    6,  6],
#
#             #      60  240 480 720 960 1200 1440 1680 1920  2160 2400  2640 2880
#             "k=1": [54, 54, 54, 54, 54, 54,  54,  54,  54,   54,  54,   54,  54 ],
#             "k=2": [15, 22, 27, 29, 34, 34,  36,  36,  36,   36,  36,   40,  40 ],
#             "k=3": [7,  13, 14, 20, 26, 26,  27,  27,  27,   27,  27,   33,  33 ],
#             "k=4": [1,   4, 5,  9,  15, 15,  15,  15,  15,   15,  15,   22,  22 ],
#             "k=5": [0,   0, 1,  2,  6,   6,   6,   6,   6,    6,   6,   10,  10 ],
#         }
#     }
# }
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# color_lst = ["#A72921", "#3C5DA0", '#FF69B4', "#0F6F00", "#FFD700"]
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "IMDB"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(12, 8))  # 所有图使用相同的 figsize
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [ 1,  4, 8, 12, 16, 20, 24, 28, 32,  36, 40,  44, 48]
# x = np.array(labels)
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 初始化最大值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=mixup_method_list[j],
#             color=color_lst[j % len(color_lst)],
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         max_y_value = max(max_y_value, max(y_data))  # 更新最大值
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Number of k-itemsets', fontsize=28)
#     ax.set_xlabel('# Time Window (h)', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)
#     ax.set_xticklabels(labels, fontsize=24)
#     ax.set_ylim(0, max_y_value * 1.1)  # 将 y 轴范围设置为 0 到最大值的 1.1 倍
#
#     ax.tick_params(axis='y', labelsize=24)
#     ax.legend(loc="upper right", fontsize=24)
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.15)
#
# plt.savefig(f"{dataset}_time_items.pdf", format='pdf', bbox_inches='tight', pad_inches=0.2)
# plt.show()


 # Delicious     items   time_window
# # 定义结果字典
# results_dict = {
#     "Delicious": {
#         "piCPM": {
#             # #      60  120 180  240 300 360 420 480 540 600 660 720 780 840 900  960 1020 1080 1140  1200 1260 1320 1380 1440 1680 1920  2160 2400  2640 2880 4320 5760  7200
#             # "k=1": [54, 40, 40, 55, 40, 40, 40, 54, 40, 40, 40, 54, 40, 40,  40,  54, 40,  40,  40,   54,   40,  40,  40, 54,  54,  54,                         54,  55,   55,  54],
#             # "k=2": [15, 16, 14, 22, 19, 18, 19, 32, 17, 24, 25, 29, 19, 19,  25,  34, 22,  24,  23,   36,   29,  19,  25, 33,  34,  34,                       30,  32,   38,  30],
#             # "k=3": [7,   8, 7,  13, 9,   8,  9, 16, 7,   9, 11, 20,  8,  8,  11,  26,  9,  11,  10,   27,   17,   8,  11, 25,  26,  26,                    24,  25,   27,  24],
#             # "k=4": [1,   1, 1,   4, 1,   1,  1,  5, 1,   1,  1,  9,  1,  1,   1,  15,  1,   1,   1,   15,    8,    1,  1, 15,  15,  15,                     15,  15,   15,  15],
#             # "k=5": [0,   0, 0,   0, 0,   0,  0,  1, 0,   0,  0,  2,  0,  0,   0,   6,  0,   0,   0,    6,    4,    0,  0,  6,   6,   6,                       6,   6,    6,  6],
#
#             #      60    240     480     720    960    1200    1440    1680    1920   2160   2400    2640  2880
#             "k=1": [200,  200,   200,    200,    200,   200,    200,    200,    200,   200,   200,   200,  200 ],
#             "k=2": [3053, 3238,  3245,   3253,   3255,  3290,   3344,   3381,   3423,  3509,  3578,  3603,  3642],
#             "k=3": [13781,14311, 14452,  14580,  14758, 15148,  15559,  16034,  16902, 17560, 18239, 18452,  18448 ],
#             "k=4": [45269,46421, 46803,  47020,  47236, 47389,  47826,  48907,  53790, 56792, 60931,  64219,  67797],
#             "k=5": [0,      0,     0,       0,     0,     0,      0,      0,      0,    0,      0,      0,     0 ],
#         }
#     }
# }
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# color_lst = ["#A72921", "#3C5DA0", '#FF69B4', "#0F6F00", "#FFD700"]
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "Delicious"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [ 1,  4, 8, 12, 16, 20, 24, 28, 32,  36, 40,  44, 48]
# x = np.array(labels)
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 初始化最大值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#         # 将 y_data 除以 1000，表示以千（k）为单位
#         y_data = np.array(y_data) / 1000.0  # 单位换算成千（k）
#
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=mixup_method_list[j],
#             color=color_lst[j % len(color_lst)],
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         max_y_value = max(max_y_value, max(y_data))  # 更新最大值
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Number of k-itemsets', fontsize=28)  # 添加 (k) 单位
#     ax.set_xlabel('# Time Window (h)', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)
#     ax.set_xticklabels(labels, fontsize=24)
#     ax.set_ylim(0, max_y_value * 1.1)  # 将 y 轴范围设置为 0 到最大值的 1.1 倍
#
#     # 设置纵坐标标签为千（k）
#     ax.set_yticklabels([f'{int(y):,}k' for y in ax.get_yticks()])
#
#     ax.tick_params(axis='y', labelsize=24)
#     ax.legend(loc="upper right", fontsize=24)
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.15)
# plt.savefig(f"{dataset}_time_items.pdf", format='pdf', bbox_inches='tight', pad_inches=0.2)
# plt.show()
#



# # net   time-window  items
# # 定义结果字典
# results_dict = {
#     "Intrusion Alert Network": {
#         "piCPM": {
#             "k=1": [18, 18, 18, 18, 18, 18, 18, 18, 18, 18],
#             "k=2": [4,  11, 18, 20, 38, 44, 44, 47, 48, 54],
#             "k=3": [0,  1,  3,  4,  20, 28, 38, 39, 41, 43],
#             "k=4": [0,  0,  0,  0,   2,  6, 10, 12, 12, 12],
#             "k=5": [0,  0,  0,  0,   0,  0,  0,  0,  0,  0],
#         }
#     }
# }
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28 ,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# color_lst = ["#A72921", "#3C5DA0", '#FF69B4', "#0F6F00", "#FFD700"]
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "Intrusion Alert Network"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# x = np.array(labels)
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 用于保存最大 y 值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=mixup_method_list[j],
#             color=color_lst[j % len(color_lst)],
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         # 更新最大 y 值
#         max_y_value = max(max_y_value, max(y_data))
#
#     # 根据数据的最大值设置 y 轴的范围
#     ax.set_ylim(0, max_y_value * 1.1)  # 设置为最大值的 1.1 倍以留出一些空间
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Number of k-itemsets', fontsize=28)
#     ax.set_xlabel('# Time Window (min)', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)
#     ax.set_xticklabels(labels, fontsize=24)
#
#     ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"{dataset}_time_items.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()



# #
# # 定义结果字典
# results_dict = {
#     "Intrusion Alert Network": {
#         "piCPM": {
#             "k=1": [18, 18, 18, 18, 18],
#             "k=2": [16, 39, 43, 48, 55],
#             "k=3": [1,  20, 31, 40, 57],
#             "k=4": [0,  3,   8, 11, 24],
#             "k=5": [0,  0,   1,  1,  4],
#         }
#     }
# }
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# color_lst = ["#A72921", "#3C5DA0", '#FF69B4', "#0F6F00", "#FFD700"]
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "Intrusion Alert Network"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [1, 2, 3, 4, 5]
# x = np.array(labels)
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 用于保存最大 y 值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=mixup_method_list[j],
#             color=color_lst[j % len(color_lst)],
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         # 更新最大 y 值
#         max_y_value = max(max_y_value, max(y_data))
#
#     # 根据数据的最大值设置 y 轴的范围
#     ax.set_ylim(0, max_y_value * 1.1)  # 设置为最大值的 1.1 倍以留出一些空间
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Number of k-itemsets', fontsize=28)
#     ax.set_xlabel('# Diameter', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)
#     ax.set_xticklabels(labels, fontsize=24)
#
#     ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
#
# plt.savefig(f"{dataset}_dia_items.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()

# ## net items sup
# # 定义结果字典
# results_dict = {
#     "Intrusion Alert Network": {
#         "piCPM": {
#             "k=1": [41,   31, 18,  7,  5, 4, 4, 3, 3],
#             "k=2": [327, 116, 18,  9,  6, 3, 2, 2, 2],
#             "k=3": [1090,150, 41,  2,  2, 0, 0, 0, 0],
#             "k=4": [2222, 88, 26,  0,  0, 0, 0, 0, 0],
#             "k=5": [3236, 17,  5,  0,  0, 0, 0, 0, 0],
#         }
#     }
# }
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# color_lst = ["#A72921", "#3C5DA0", '#FF69B4', "#0F6F00", "#FFD700"]
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "Intrusion Alert Network"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# x = np.array(labels)
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 用于保存最大 y 值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=mixup_method_list[j],
#             color=color_lst[j % len(color_lst)],
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         # 更新最大 y 值
#         max_y_value = max(max_y_value, max(y_data))
#
#     # 根据数据的最大值设置 y 轴的范围
#     ax.set_ylim(0, max_y_value * 1.1)  # 设置为最大值的 1.1 倍以留出一些空间
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Number of k-itemsets', fontsize=28)
#     ax.set_xlabel('# Support', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)
#     ax.set_xticklabels(labels, fontsize=24)
#
#     ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"{dataset}_sup_items.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()




# #######net  time  support
# import collections
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib import rcParams
#
# 定义结果字典
results_dict = {
    "Intrusion Alert Network": {
        "piCPM": {
            "k=1": [5.86, 3.15, 1.26, 0.70, 0.42, 0.25, 0.13, 0.030, 0.028],
        }
    }
}

# 设置字体参数
params = {
    'font.weight': 'normal',
    'font.size': 28,
}
rcParams.update(params)

# 颜色和标记符列表
blue_color = "#3C5DA0"
marker_list = ['X', 'o', 's', '^', 'D']

# 提取模型名称列表
dataset = "Intrusion Alert Network"
model_name_list = list(results_dict[dataset].keys())
mixup_method_list = list(results_dict[dataset]["piCPM"].keys())

# 动态设置子图数量
fig, axs = plt.subplots(1, len(model_name_list), figsize=(9, 5))
fig.subplots_adjust(wspace=0.3, hspace=0.4)

# 将 axs 转换为列表，以便后续循环一致
if len(model_name_list) == 1:
    axs = [axs]

# x 轴标签和数据
labels = [2, 3, 4, 5, 6, 7, 8, 9, 10]
x = np.array(labels)

# 绘制每个子图
for i in range(len(axs)):
    ax = axs[i]
    max_y_value = 0  # 用于保存最大 y 值
    for j in range(len(mixup_method_list)):
        y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]

        # 替换 "k=1" 标签为空字符串以避免显示
        label_name = "" if mixup_method_list[j] == "k=1" else mixup_method_list[j]

        ax.plot(
            x,
            y_data,
            marker=marker_list[j % len(marker_list)],
            label=label_name,  # 使用替换后的标签
            color=blue_color,  # 将颜色设置为蓝色
            linewidth=2.5,
            markersize=8,
            markeredgecolor='white',
            markeredgewidth=1.2
        )
        # 更新最大 y 值
        max_y_value = max(max_y_value, max(y_data))

    # 根据数据的最大值设置 y 轴的范围
    ax.set_ylim(0, max_y_value * 1.1)  # 设置为最大值的 1.1 倍以留出一些空间

    # 设置图表细节
    ax.grid(True, linewidth=0.7, alpha=0.8)
    if i == 0:
        ax.set_ylabel('Running Time (s)', fontsize=28)
    ax.set_xlabel('# Support', fontsize=28)
    ax.set_title(dataset, fontsize=28)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=24)

    # 显示图例
    # ax.legend(loc="upper right", fontsize=24)
    ax.tick_params(axis='y', labelsize=24)

# 保存并展示图表
fig.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
plt.savefig(f"{dataset}_sup_time.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
plt.show()





# ##### net  time diameter
# import collections
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib import rcParams
#
# # 定义结果字典
# results_dict = {
#     "Intrusion Alert Network": {
#         "piCPM": {
#             "k=1": [0.62, 1.36, 2.51, 3.71, 5.85],
#         }
#     }
# }
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# blue_color = "#3C5DA0"
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "Intrusion Alert Network"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [1, 2, 3, 4, 5]
# x = np.arange(len(labels))  # 使用等间距的索引数组
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 用于保存最大 y 值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#
#         # 替换 "k=1" 标签为空字符串以避免显示
#         label_name = "" if mixup_method_list[j] == "k=1" else mixup_method_list[j]
#
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=label_name,  # 使用替换后的标签
#             color=blue_color,  # 将颜色设置为蓝色
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         # 更新最大 y 值
#         max_y_value = max(max_y_value, max(y_data))
#
#     # 根据数据的最大值设置 y 轴的范围
#     ax.set_ylim(0, max_y_value * 1.1)  # 设置为最大值的 1.1 倍以留出一些空间
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Running Time (s)', fontsize=28)
#     ax.set_xlabel('# Diameter', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)  # 使用等间距的索引
#     ax.set_xticklabels(labels, fontsize=24)  # 显示原始标签
#
#     # 显示图例
#     # ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"{dataset}_dia_time.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()


# ###net   running time  time window
# import collections
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib import rcParams
#
# # 定义结果字典
# results_dict = {
#     "Intrusion Alert Network": {
#         "piCPM": {
#             "k=1": [0.81, 0.89, 1.03, 1.06, 1.16, 1.28, 1.44, 1.50, 1.67, 2.38],
#         }
#     }
# }
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# blue_color = "#3C5DA0"
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "Intrusion Alert Network"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# x = np.arange(len(labels))  # 使用等间距的索引数组
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 用于保存最大 y 值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#
#         # 替换 "k=1" 标签为空字符串以避免显示
#         label_name = "" if mixup_method_list[j] == "k=1" else mixup_method_list[j]
#
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=label_name,  # 使用替换后的标签
#             color=blue_color,  # 将颜色设置为蓝色
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         # 更新最大 y 值
#         max_y_value = max(max_y_value, max(y_data))
#
#     # 根据数据的最大值设置 y 轴的范围
#     ax.set_ylim(0, max_y_value * 1.1)  # 设置为最大值的 1.1 倍以留出一些空间
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Running Time (s)', fontsize=28)
#     ax.set_xlabel('# Time Window (min)', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)  # 使用等间距的索引
#     ax.set_xticklabels(labels, fontsize=24)  # 显示原始标签

    # 显示图例
    # ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"{dataset}_time_time.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()


#
# ##############IMDB running time support
# import collections
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib import rcParams
#
# # 定义结果字典
# results_dict = {
#     "IMDB": {
#         "piCPM": {
#             "k=1": [16.46, 8.53, 4.96, 2.09, 1.34, 0.77, 0.58, 0.51, 0.49, 0.43 ],
#         }
#     }
# }
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# blue_color = "#3C5DA0"
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "IMDB"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# x = np.arange(len(labels))  # 使用等间距的索引数组
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 用于保存最大 y 值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#
#         # 替换 "k=1" 标签为空字符串以避免显示
#         label_name = "" if mixup_method_list[j] == "k=1" else mixup_method_list[j]
#
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=label_name,  # 使用替换后的标签
#             color=blue_color,  # 将颜色设置为蓝色
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         # 更新最大 y 值
#         max_y_value = max(max_y_value, max(y_data))
#
#     # 根据数据的最大值设置 y 轴的范围
#     ax.set_ylim(0, max_y_value * 1.1)  # 设置为最大值的 1.1 倍以留出一些空间
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Running Time (min)', fontsize=28)
#     ax.set_xlabel('#Support', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)  # 使用等间距的索引
#     ax.set_xticklabels(labels, fontsize=24)  # 显示原始标签
#
#     # 显示图例
#     # ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"{dataset}_sup_time.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()





#
# ##############IMDB running time diameter
# import collections
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib import rcParams
#
# # 定义结果字典
# results_dict = {
#     "IMDB": {
#         "piCPM": {
#             "k=1": [2.09, 2.16, 2.15, 2.30, 2.91],
#         }
#     }
# }
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# blue_color = "#3C5DA0"
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "IMDB"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [1, 2, 3, 4, 5]
# x = np.arange(len(labels))  # 使用等间距的索引数组
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 用于保存最大 y 值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#
#         # 替换 "k=1" 标签为空字符串以避免显示
#         label_name = "" if mixup_method_list[j] == "k=1" else mixup_method_list[j]
#
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=label_name,  # 使用替换后的标签
#             color=blue_color,  # 将颜色设置为蓝色
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         # 更新最大 y 值
#         max_y_value = max(max_y_value, max(y_data))
#
#     # 根据数据的最大值设置 y 轴的范围
#     ax.set_ylim(0, max_y_value * 1.1)  # 设置为最大值的 1.1 倍以留出一些空间
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Running Time (min)', fontsize=28)
#     ax.set_xlabel('#Diameter', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)  # 使用等间距的索引
#     ax.set_xticklabels(labels, fontsize=24)  # 显示原始标签
#
#     # 显示图例
#     # ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"{dataset}_dia_time.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()



##############IMDB running time time window
# import collections
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib import rcParams
#
# # 定义结果字典
# results_dict = {
#     "IMDB": {
#         "piCPM": {
#             "k=1": [2.08, 2.12, 2.15, 2.16, 2.18, 2.18, 2.19, 2.19, 2.26, 2.26, 2.30, 2.30, 2.35 ],
#         }
#     }
# }
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# blue_color = "#3C5DA0"
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "IMDB"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [1, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48]
# x = np.arange(len(labels))  # 使用等间距的索引数组
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 用于保存最大 y 值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#
#         # 替换 "k=1" 标签为空字符串以避免显示
#         label_name = "" if mixup_method_list[j] == "k=1" else mixup_method_list[j]
#
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=label_name,  # 使用替换后的标签
#             color=blue_color,  # 将颜色设置为蓝色
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         # 更新最大 y 值
#         max_y_value = max(max_y_value, max(y_data))
#
#     # 根据数据的最大值设置 y 轴的范围
#     ax.set_ylim(0, max_y_value * 1.1)  # 设置为最大值的 1.1 倍以留出一些空间
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Running Time (min)', fontsize=28)
#         ax.set_xlabel('#Time Window (h)', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)  # 使用等间距的索引
#     ax.set_xticklabels(labels, fontsize=24)  # 显示原始标签
#
#     # 显示图例
#     # ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"{dataset}_time_time.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()


# #############Delicious running time time window
# import collections
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib import rcParams
#
# # 定义结果字典
# results_dict = {
#     "Delicious": {
#         "piCPM": {
#             "k=1": [2.30, 4.08, 4.19, 6.15, 7.18, 12.18, 16.19, 20.26, 28.30, 36.30, 42.22, 54.35, 62.19 ],
#         }
#     }
# }
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# blue_color = "#3C5DA0"
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "Delicious"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [1, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48]
# x = np.arange(len(labels))  # 使用等间距的索引数组
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 用于保存最大 y 值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#
#         # 替换 "k=1" 标签为空字符串以避免显示
#         label_name = "" if mixup_method_list[j] == "k=1" else mixup_method_list[j]
#
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=label_name,  # 使用替换后的标签
#             color=blue_color,  # 将颜色设置为蓝色
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         # 更新最大 y 值
#         max_y_value = max(max_y_value, max(y_data))
#
#     # 根据数据的最大值设置 y 轴的范围
#     ax.set_ylim(0, max_y_value * 1.1)  # 设置为最大值的 1.1 倍以留出一些空间
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Running Time (min)', fontsize=28)
#         ax.set_xlabel('#Time Window (h)', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)  # 使用等间距的索引
#     ax.set_xticklabels(labels, fontsize=24)  # 显示原始标签
#
#     # 显示图例
#     # ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"{dataset}_time_time.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()







# ##############Lastfm running time dia
# # import collections
# # import matplotlib.pyplot as plt
# # import numpy as np
# # from matplotlib import rcParams
# #
# # 定义结果字典
# results_dict = {
#     "Last.fm": {
#         "piCPM": {
#             "k=1": [2.84 , 5.09, 23.05, 42.11, 77.02],
#         }
#     }
# }
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# blue_color = "#3C5DA0"
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "Last.fm"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [1, 2, 3, 4, 5]
# x = np.arange(len(labels))  # 使用等间距的索引数组
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 用于保存最大 y 值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#
#         # 替换 "k=1" 标签为空字符串以避免显示
#         label_name = "" if mixup_method_list[j] == "k=1" else mixup_method_list[j]
#
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=label_name,  # 使用替换后的标签
#             color=blue_color,  # 将颜色设置为蓝色
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         # 更新最大 y 值
#         max_y_value = max(max_y_value, max(y_data))
#
#     # 根据数据的最大值设置 y 轴的范围
#     ax.set_ylim(0, max_y_value * 1.1)  # 设置为最大值的 1.1 倍以留出一些空间
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Running Time (min)', fontsize=28)
#         ax.set_xlabel('#Diameter', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)  # 使用等间距的索引
#     ax.set_xticklabels(labels, fontsize=24)  # 显示原始标签
#
#     # 显示图例
#     # ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"{dataset}_dia_time.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()




############Lastfm itemset dia

# # 定义结果字典
# results_dict = {
#     "Last.fm": {
#         "piCPM": {
#             "k=1": [17, 17, 17, 17, 17],
#             "k=2": [1,  14, 31, 43, 51],
#             "k=3": [0,   4, 26, 43, 77],
#             "k=4": [0,   1, 11, 39, 76],
#             "k=5": [0,   0,  0,  0,  0],
#         }
#     }
# }
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# color_lst = ["#A72921", "#3C5DA0", '#FF69B4', "#0F6F00", "#FFD700"]
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "Last.fm"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [1, 2, 3, 4, 5]
# x = np.array(labels)
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 用于保存最大 y 值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=mixup_method_list[j],
#             color=color_lst[j % len(color_lst)],
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         # 更新最大 y 值
#         max_y_value = max(max_y_value, max(y_data))
#
#     # 根据数据的最大值设置 y 轴的范围
#     ax.set_ylim(0, max_y_value * 1.1)  # 设置为最大值的 1.1 倍以留出一些空间
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Number of k-itemsets', fontsize=28)
#     ax.set_xlabel('# Diameter', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)
#     ax.set_xticklabels(labels, fontsize=24)
#
#     ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"{dataset}_dia_items.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()



# ###Last.fm  k-item  support
# # 定义结果字典
# results_dict = {
#     "Last.fm": {
#         "piCPM": {
#             "k=1": [68,  47, 32, 23, 15, 13, 11, 8, 7,5],
#             "k=2": [230, 145, 92, 52, 31, 21, 14,10,10,7],
#             "k=3": [412, 218, 129,70, 31, 18, 12, 4, 6,1],
#             "k=4": [1238, 509, 210,80, 17, 11,  5, 1, 1,0],
#             "k=5": [0,  0,  0,   0,  0,  0,  0, 0, 0,0],
#         }
#     }
# }
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# color_lst = ["#A72921", "#3C5DA0", '#FF69B4', "#0F6F00", "#FFD700"]
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "Last.fm"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# x = np.array(labels)
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 用于保存最大 y 值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=mixup_method_list[j],
#             color=color_lst[j % len(color_lst)],
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         # 更新最大 y 值
#         max_y_value = max(max_y_value, max(y_data))
#
#     # 根据数据的最大值设置 y 轴的范围
#     ax.set_ylim(0, max_y_value * 1.1)  # 设置为最大值的 1.1 倍以留出一些空间
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Number of k-itemsets', fontsize=28)
#     ax.set_xlabel('# Support', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)
#     ax.set_xticklabels(labels, fontsize=24)
#
#     ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"{dataset}_sup_items.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()


#
# ###Last.fm  k-item  dia
# # 定义结果字典
# results_dict = {
#     "Last.fm": {
#         "piCPM": {
#             "k=1": [15, 15, 15, 15, 15],
#             "k=2": [1 , 14, 26, 43, 51],
#             "k=3": [0 , 4,  11, 43, 77],
#             "k=4": [0 , 1,  15, 39, 76],
#             "k=5": [0 , 0,  0,   0, 0],
#
#         }
#     }
# }
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# color_lst = ["#A72921", "#3C5DA0", '#FF69B4', "#0F6F00", "#FFD700"]
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "Last.fm"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [1, 2, 3, 4, 5]
# x = np.array(labels)
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 用于保存最大 y 值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=mixup_method_list[j],
#             color=color_lst[j % len(color_lst)],
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         # 更新最大 y 值
#         max_y_value = max(max_y_value, max(y_data))
#
#     # 根据数据的最大值设置 y 轴的范围
#     ax.set_ylim(0, max_y_value * 1.1)  # 设置为最大值的 1.1 倍以留出一些空间
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Number of k-itemsets', fontsize=28)
#     ax.set_xlabel('# Diameter', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)
#     ax.set_xticklabels(labels, fontsize=24)
#
#     ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"{dataset}_dia_items.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()








#
# ###Last.fm  time   item
# # 定义结果字典
# results_dict = {
#     "Last.fm": {
#         "piCPM": {
#             #60, 240, 480, 960, 1200, 1440, 1680, 1920, 2440, 2640, 2880
#             "k=1": [15, 15, 15, 15, 15, 15 , 15, 15, 15 ,15, 15, 15, 15 ],
#             "k=2": [24, 27, 28, 30, 30, 30 , 33, 34, 34 , 35, 35, 39, 46 ],
#             "k=3": [18, 24, 26, 28, 33, 34 , 36, 40, 43 , 44, 46, 50, 55 ],
#             "k=4": [7,  11, 17, 20, 21, 23 , 28, 29, 30 , 32, 33, 36, 38 ],
#             "k=5": [0,  0,   0,  0,  0 , 0,   0,  0 , 0,   0,  0,  0, 0 ]
#
#         }
#     }
# }
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# color_lst = ["#A72921", "#3C5DA0", '#FF69B4', "#0F6F00", "#FFD700"]
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "Last.fm"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [1, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48]
# x = np.array(labels)
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 用于保存最大 y 值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=mixup_method_list[j],
#             color=color_lst[j % len(color_lst)],
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         # 更新最大 y 值
#         max_y_value = max(max_y_value, max(y_data))
#
#     # 根据数据的最大值设置 y 轴的范围
#     ax.set_ylim(0, max_y_value * 1.1)  # 设置为最大值的 1.1 倍以留出一些空间
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Number of k-itemsets', fontsize=28)
#     ax.set_xlabel('# Time Window (h)', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)
#     ax.set_xticklabels(labels, fontsize=24)
#
#     ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"{dataset}_time_items.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()


#
# # ###Last.fm  time   time
# # 定义结果字典
# results_dict = {
#     "Last.fm": {
#         "piCPM": {
#             #60, 240, 480, 960, 1200, 1440, 1680, 1920, 2440, 2640, 2880
#             "": [23.77, 26.86, 30.98, 34.76, 38.12 , 43.78, 48.33, 55.65 , 61.09, 64.14, 72.30 , 80.87, 90.45],
#
#         }
#     }
# }
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# color_lst = ["#3C5DA0"]
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "Last.fm"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [1, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48]
# x = np.array(labels)
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 用于保存最大 y 值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=mixup_method_list[j],
#             color=color_lst[j % len(color_lst)],
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         # 更新最大 y 值
#         max_y_value = max(max_y_value, max(y_data))
#
#     # 根据数据的最大值设置 y 轴的范围
#     ax.set_ylim(0, max_y_value * 1.1)  # 设置为最大值的 1.1 倍以留出一些空间
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Running Time (min)', fontsize=28)
#     ax.set_xlabel('# Time Window (h)', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)
#     ax.set_xticklabels(labels, fontsize=24)
#
#     # ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"{dataset}_time_time.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()




# #######Last.fm  time  support
# import collections
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib import rcParams
#
# # 定义结果字典
# results_dict = {
#     "Last.fm": {
#         "piCPM": {
#             #60, 240, 480, 960, 1200, 1440, 1680, 1920, 2440, 2640, 2880
#             "": [71.76, 45.40, 23.01 , 16.48, 12.08, 8.07 , 4.58, 2.90, 1.35, 0.96 ],
#
#         }
#     }
# }
#
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# blue_color = "#3C5DA0"
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "Last.fm"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# x = np.array(labels)
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 用于保存最大 y 值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#
#         # 替换 "k=1" 标签为空字符串以避免显示
#         label_name = "" if mixup_method_list[j] == "k=1" else mixup_method_list[j]
#
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=label_name,  # 使用替换后的标签
#             color=blue_color,  # 将颜色设置为蓝色
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         # 更新最大 y 值
#         max_y_value = max(max_y_value, max(y_data))
#
#     # 根据数据的最大值设置 y 轴的范围
#     ax.set_ylim(0, max_y_value * 1.1)  # 设置为最大值的 1.1 倍以留出一些空间
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Running Time (min)', fontsize=28)
#     ax.set_xlabel('# Support', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)
#     ax.set_xticklabels(labels, fontsize=24)
#
#     # 显示图例
#     # ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"{dataset}_sup_time.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()


#
# ######Delicious  time  support
# import collections
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib import rcParams
#
# # 定义结果字典
# results_dict = {
#     "Delicious": {
#         "piCPM": {
#             #60, 240, 480, 960, 1200, 1440, 1680, 1920, 2440, 2640, 2880
#             "": [98.55, 58.48, 24.57, 16.33, 8.91 , 5.25, 3.14 ,2.89, 1.92, 0.29 ],
#
#         }
#     }
# }
#
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# blue_color = "#3C5DA0"
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "Delicious"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# x = np.array(labels)
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 用于保存最大 y 值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#
#         # 替换 "k=1" 标签为空字符串以避免显示
#         label_name = "" if mixup_method_list[j] == "k=1" else mixup_method_list[j]
#
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=label_name,  # 使用替换后的标签
#             color=blue_color,  # 将颜色设置为蓝色
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         # 更新最大 y 值
#         max_y_value = max(max_y_value, max(y_data))
#
#     # 根据数据的最大值设置 y 轴的范围
#     ax.set_ylim(0, max_y_value * 1.1)  # 设置为最大值的 1.1 倍以留出一些空间
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Running Time (min)', fontsize=28)
#     ax.set_xlabel('# Support', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)
#     ax.set_xticklabels(labels, fontsize=24)
#
#     # 显示图例
#     # ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"{dataset}_sup_time.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()



#######Delicious  time  dia
# import collections
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib import rcParams
#
# # 定义结果字典
# results_dict = {
#     "Delicious": {
#         "piCPM": {
#             #60, 240, 480, 960, 1200, 1440, 1680, 1920, 2440, 2640, 2880
#             "": [3.89, 8.22 , 20.8, 35.9, 60.2],
#
#         }
#     }
# }
#
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# blue_color = "#3C5DA0"
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "Delicious"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [1, 2, 3, 4, 5]
# x = np.array(labels)
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 用于保存最大 y 值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#
#         # 替换 "k=1" 标签为空字符串以避免显示
#         label_name = "" if mixup_method_list[j] == "k=1" else mixup_method_list[j]
#
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=label_name,  # 使用替换后的标签
#             color=blue_color,  # 将颜色设置为蓝色
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         # 更新最大 y 值
#         max_y_value = max(max_y_value, max(y_data))
#
#     # 根据数据的最大值设置 y 轴的范围
#     ax.set_ylim(0, max_y_value * 1.1)  # 设置为最大值的 1.1 倍以留出一些空间
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Running Time (min)', fontsize=28)
#     ax.set_xlabel('# Diameter', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)
#     ax.set_xticklabels(labels, fontsize=24)
#
#     # 显示图例
#     # ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"{dataset}_dia_time.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()



###########Delicious itemset dia
#
# #定义结果字典
# results_dict = {
#     "Delicious": {
#         "piCPM": {
#             "k=1": [200, 200, 200, 200,  200],
#             "k=2": [141, 669, 1332, 2597, 4089],
#             "k=3": [16,  548, 2687, 10349, 34097],
#             "k=4": [0,   303, 4687,30084, 84971],
#             "k=5": [0,   0,      0,   0,  0],
#         }
#     }
# }
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# color_lst = ["#A72921", "#3C5DA0", '#FF69B4', "#0F6F00", "#FFD700"]
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "Delicious"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [1, 2, 3, 4, 5]
# x = np.array(labels)
#
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 用于保存最大 y 值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#         # 将 y_data 除以 1000，缩小纵坐标的数值（可以根据需要调整除数）
#         y_data = np.array(y_data) / 1000.0  # 假设使用 1000 作为单位换算
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=mixup_method_list[j],
#             color=color_lst[j % len(color_lst)],
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         # 更新最大 y 值
#         max_y_value = max(max_y_value, max(y_data))
#
#     # 根据数据的最大值设置 y 轴的范围
#     ax.set_ylim(0, max_y_value * 1.1)  # 设置为最大值的 1.1 倍以留出一些空间
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Number of k-itemsets', fontsize=24)  # 添加 "k" 单位
#     ax.set_xlabel('# Diameter', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)
#     ax.set_xticklabels(labels, fontsize=24)
#
#     ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
#     # 修改纵坐标标签，添加单位 'k'
#     ax.set_yticklabels([f'{int(y):,}k' for y in ax.get_yticks()])
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"{dataset}_dia_items.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()


############Delicious itemset sup

# # 定义结果字典
# results_dict = {
#     "Delicious": {
#         "piCPM": {
#             "k=1": [729, 541,  336,   256,  200, 159, 135, 114,104, 90],
#             "k=2": [7202, 5281, 3971, 2360, 1517, 943, 698, 536,387,311],
#             "k=3": [41904,26520, 17956,8004, 3293,1386, 848, 576,283,194],
#             "k=4": [357120, 120479, 72009,18507,5263,1201, 628, 424, 78, 48],
#             "k=5": [0,   0, 0,   0,      0,     0,   0,  0,   0, 0],
#         }
#     }
# }
#
# # 设置字体参数
# params = {
#     'font.weight': 'normal',
#     'font.size': 28,
# }
# rcParams.update(params)
#
# # 颜色和标记符列表
# color_lst = ["#A72921", "#3C5DA0", '#FF69B4', "#0F6F00", "#FFD700"]
# marker_list = ['X', 'o', 's', '^', 'D']
#
# # 提取模型名称列表
# dataset = "Delicious"
# model_name_list = list(results_dict[dataset].keys())
# mixup_method_list = list(results_dict[dataset]["piCPM"].keys())
#
# # 动态设置子图数量
# fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
# fig.subplots_adjust(wspace=0.3, hspace=0.4)
#
# # 将 axs 转换为列表，以便后续循环一致
# if len(model_name_list) == 1:
#     axs = [axs]
#
# # x 轴标签和数据
# labels = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# x = np.array(labels)
#
# # 绘制每个子图
# for i in range(len(axs)):
#     ax = axs[i]
#     max_y_value = 0  # 用于保存最大 y 值
#     for j in range(len(mixup_method_list)):
#         y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
#         # 将 y_data 除以 1000，表示以千为单位
#         y_data = np.array(y_data) / 1000.0  # 假设使用 1000 作为单位换算
#         ax.plot(
#             x,
#             y_data,
#             marker=marker_list[j % len(marker_list)],
#             label=mixup_method_list[j],
#             color=color_lst[j % len(color_lst)],
#             linewidth=2.5,
#             markersize=8,
#             markeredgecolor='white',
#             markeredgewidth=1.2
#         )
#         # 更新最大 y 值
#         max_y_value = max(max_y_value, max(y_data))
#
#     # 根据数据的最大值设置 y 轴的范围
#     ax.set_ylim(0, max_y_value * 1.1)  # 设置为最大值的 1.1 倍以留出一些空间
#
#     # 设置图表细节
#     ax.grid(True, linewidth=0.7, alpha=0.8)
#     if i == 0:
#         ax.set_ylabel('Number of k-itemsets', fontsize=28)  # 添加 "(k)" 单位
#     ax.set_xlabel('# Support', fontsize=28)
#     ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)
#     ax.set_xticklabels(labels, fontsize=24)
#
#     ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
#     # 修改纵坐标标签，添加单位 'k'
#     ax.set_yticklabels([f'{int(y):,}k' for y in ax.get_yticks()])
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"{dataset}_sup_items.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()
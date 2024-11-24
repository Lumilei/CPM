import collections
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
##  time sup
# 定义结果字典
results_dict = {
    "Intrusion Alert Network": {
        "piCPM": {

            "Last.fm": [71.76, 45.40, 23.01 , 16.48, 12.08, 8.07 , 4.58, 2.90, 1.35, 0.96 ],
            "Delicious": [98.55, 58.48, 24.57, 16.33, 8.91 , 5.25, 3.14 ,2.89, 1.92, 0.29 ],
            "IMDB": [16.46, 8.53, 4.96, 2.09, 1.34, 0.77, 0.58, 0.51, 0.49, 0.43 ],

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
color_lst = ["#A72921", "#3C5DA0", '#FF69B4', "#0F6F00", "#FFD700"]
marker_list = ['X', 'o', 's', '^', 'D']

# 提取模型名称列表
dataset = "Intrusion Alert Network"
model_name_list = list(results_dict[dataset].keys())
mixup_method_list = list(results_dict[dataset]["piCPM"].keys())

# 动态设置子图数量
fig, axs = plt.subplots(1, len(model_name_list), figsize=(10, 6))
fig.subplots_adjust(wspace=0.3, hspace=0.4)

# 将 axs 转换为列表，以便后续循环一致
if len(model_name_list) == 1:
    axs = [axs]

# x 轴标签和数据
labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = np.array(labels)

# 绘制每个子图
for i in range(len(axs)):
    ax = axs[i]
    max_y_value = 0  # 用于保存最大 y 值
    for j in range(len(mixup_method_list)):
        y_data = results_dict[dataset][model_name_list[i]][mixup_method_list[j]]
        ax.plot(
            x,
            y_data,
            marker=marker_list[j % len(marker_list)],
            label=mixup_method_list[j],
            color=color_lst[j % len(color_lst)],
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
        ax.set_ylabel('Running Time(min)', fontsize=28)
    ax.set_xlabel('# Support', fontsize=28)
    # ax.set_title(dataset, fontsize=28)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=24)

    ax.legend(loc="upper right", fontsize=24)
    ax.tick_params(axis='y', labelsize=24)


# 保存并展示图表
fig.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
plt.savefig(f"sup_time.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
plt.show()

###########time window  time
# results_dict = {
#     "Intrusion Alert Network": {
#         "piCPM": {
#
#             "Last.fm": [23.77, 26.86, 30.98, 34.76, 38.12 , 43.78, 48.33, 55.65 , 61.09, 64.14, 72.30 , 80.87, 90.45],
#             "Delicious": [2.30, 4.08, 4.19, 6.15, 7.18, 12.18, 16.19, 20.26, 28.30, 36.30, 42.22, 54.35, 62.19 ],
#             "IMDB": [2.08, 2.12, 2.15, 2.16, 2.18, 2.18, 2.19, 2.19, 2.26, 2.26, 2.30, 2.30, 2.35 ],
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
#         ax.set_ylabel('Running Time(min)', fontsize=28)
#     ax.set_xlabel('# Time Window(h)', fontsize=28)
#     # ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)
#     ax.set_xticklabels(labels, fontsize=24)
#
#     ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"time_time.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()

####diameter time
# results_dict = {
#     "Intrusion Alert Network": {
#         "piCPM": {
#
#             "Last.fm": [2.84 , 5.09, 23.05, 42.11, 77.02],
#             "Delicious": [3.89, 8.22 , 20.8, 35.9, 60.2],
#             "IMDB": [2.09, 2.16, 2.15, 2.30, 2.91],
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
#         ax.set_ylabel('Running Time(min)', fontsize=28)
#     ax.set_xlabel('# Diameter', fontsize=28)
#     # ax.set_title(dataset, fontsize=28)
#     ax.set_xticks(x)
#     ax.set_xticklabels(labels, fontsize=24)
#
#     ax.legend(loc="upper right", fontsize=24)
#     ax.tick_params(axis='y', labelsize=24)
#
#
# # 保存并展示图表
# fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.2)  # 增加 bottom 值以留出更多空间
# plt.savefig(f"dia_time.pdf", format='pdf', bbox_inches='tight', pad_inches=0.0)
# plt.show()

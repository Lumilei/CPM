import networkx as nx
import math
import numpy as np
import random
import pandas as pd
import main_1
from vertex import Vertex  # 从 vertex.py 导入 Vertex 类
import DiaLPA_3 as DL
import collections



# G-test 计算函数
def g_test(p, q, pattern, graph, label_dict, max_item, dia_threshold, top_k):
    # 确保 p 和 q_mean 的合法范围

    if q == 0:
    # 当 随机图不存在时，将每个模式的支持度的成绩作为支持度
        if len(pattern) > 1:
            for i in len(pattern):
                q = calculate_support(pattern[i], graph, label_dict, max_item, dia_threshold, top_k)



    first_term = p * math.log(p / q) if p > 0 else 0  # 防止 log(0)
    second_term = (1 - p) * math.log((1 - p) / (1 - q)) if (1 - p) > 0 and (1 - q) > 0 else 0  # 防止 log(0) 或 log(负数)

    g_score = first_term + second_term
    return g_score

def calculate_support_value(L, L1, graph, support, top_k, random_graph=None):
    """
    计算每个频繁项集的支持度
    参数：
    - L: 频繁项集的集合
    - L1: 频繁1项集
    - graph: 图结构
    - sup_g: 支持度图
    - subg_set: 子图集合
    - max_item: 最大项数
    - support: 当前支持度字典
    - random_graph: 随机生成的图（如果提供）

    返回：更新后的支持度字典
    """
    nameList, reNameList = main_1.nameTransform()
    one_item = sorted(L1.items(), key=lambda x: x[1], reverse=True)

    # 如果没有提供随机图，则使用原图
    graph_to_use = random_graph if random_graph is not None else graph

    # 计算每个频繁项集的支持度
    for Lk in L.values():
        if not Lk:
            break
        temp_dict = collections.defaultdict(dict)
        for freq_set in Lk:
            temp = [nameList[item] for item in freq_set]
            if len(freq_set) == 1:
                temp_dict[frozenset(temp)] = L1[list(freq_set)[0]]
            else:
                temp_dict[frozenset(temp)] = support[freq_set]

        # 排序并获取top_k支持度最高的项集
        res = sorted(temp_dict.items(), key=lambda x: x[1], reverse=True)
        for i in range(len(res)):
            if i < top_k:
                support[res[i][0]] = res[i][1]

    return support


#CMIS 计算函数
def calculate_support(pattern, graph, label_dict, max_item, dia_threshold, L, top_k):

    subg_set = []
    bridgeConnectDict = {}
    edgeDict = {}
    support = {}
    label_dict, community_dict = DL.label_get(graph)
    label_dict = DL.diaLPA(graph, community_dict, label_dict, dia_threshold, iter_threshold=5)
    communities = DL.get_community(graph, label_dict)


    data_set = main_1.data_load("movie_random_activity.txt")
    data_set, item_count_dict, node_id = main_1.attribute_count(data_set, min_sup=2)

    sup_g = main_1.DL.creat_supGraph(graph, communities, bridgeConnectDict, edgeDict)
    L = main_1.init_L(max_item)

    L1 = main_1.create_L1(item_count_dict)

    support = main_1.generate_L(L, L1, graph, sup_g, subg_set, max_item, support)



    nameList, reNameList = main_1.nameTransform()

    one_item = sorted(item_count_dict.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(one_item)):
        if i >= top_k:
            break

    for Lk in L.values():
        if not Lk:
            break
        temp_dict = collections.defaultdict(dict)
        for freq_set in Lk:
                temp = list()
                for item in freq_set:
                    temp.append(nameList[item])
                if len(freq_set) == 1:
                    temp_dict[frozenset(temp)] = item_count_dict[list(freq_set)[0]]
                else:
                    temp_dict[frozenset(temp)] = support[freq_set]

        res = sorted(temp_dict.items(), key=lambda x: x[1], reverse=True)

        for i in range(len(res)):
            if i < top_k:
                support = res[i][1]  # 实际支持度

    return support


def support(activity_graph, candidate_pattern, time_constraints=None, structural_constraints=None):
    """
    计算给定候选模式在活动图中的CMIS支持度，考虑时间和结构约束。
    
    :param activity_graph: 活动图，字典形式，每个标签映射到其所有活动（列表）。
    :param candidate_pattern: 候选模式，包含多个标签。
    :param time_constraints: 时间约束函数，过滤标签映射的时间（可选）。
    :param structural_constraints: 结构约束函数，确保标签映射符合结构（可选）。
    :return: CMIS支持度，候选模式的最小映射数量。
    """
    label_images_count = {}  # 存储每个标签的有效映射数量

    for label in candidate_pattern:
        if label in activity_graph:
            # 获取标签的所有活动映射
            images = activity_graph[label]

            # 如果有时间约束，应用时间过滤
            if time_constraints:
                images = [img for img in images if time_constraints(img)]

            # 如果有结构约束，应用结构过滤
            if structural_constraints:
                images = [img for img in images if structural_constraints(img)]

            # 记录该标签的有效映射数量
            label_images_count[label] = len(images)
        else:
            # 如果标签没有映射，映射数量为0
            label_images_count[label] = 0

    # 返回候选模式的最小映射数量作为CMIS支持度
    cmis_value = min(label_images_count.values())
    return cmis_value














# 置换检验函数
# def permutation_test(graph, pattern, label_dict, num_permutations=100, method="gnm"):
#     """执行置换检验，返回每次置换的支持度"""
#     random_supports = []
#
#     for _ in range(num_permutations):
#         random_graph = generate_random_graph(graph, label_dict, method=method)
#         support_count = calculate_support(pattern, random_graph, label_dict)
#         random_supports.append(support_count)
#
#     return random_supports

#显著性检验函数
def significance_test(graph, pattern, label_dict, actual_support, max_item, dia_threshold, L, top_k, method="gnm"):
    """执行完整的显著性检验（Permutation Test + G-test）"""
    p = actual_support  # 使用传入的实际支持度作为 p 值

    # 执行置换检验，获取随机图中的支持度
    # random_supports = permutation_test(graph, pattern, label_dict, num_permutations, method)
    # q_mean = np.mean(random_supports)
    q = calculate_support(pattern, graph, label_dict, max_item, dia_threshold, L, top_k)

    # 计算 G-test 分数
    g_score = g_test(p, q, pattern, graph, label_dict, max_item, dia_threshold, top_k)

    # # 计算 p 值
    # p_value = sum([1 for q in random_supports if q >= p]) / num_permutations

    return g_score


def read_edge_file(filename):
    edges = []
    with open(filename, 'r') as f:
        for line in f:
            node1, node2 = line.strip().split()
            edges.append((int(node1), int(node2)))
    return edges

def read_label_file(filename):
    label_map = {}
    with open(filename, 'r') as f:
        for line in f:
            label_id, label_name = line.strip().split(maxsplit=1)
            label_map[int(label_id)] = label_name
    return label_map

def read_node_file(filename):
    nodes = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 3:
                node_id = int(parts[0])
                label_id = int(parts[1])
                timestamp = parts[2]
                nodes.append((node_id, label_id, timestamp))
    return nodes

def generate_random_graph(nodes, labels, timestamps):
    random_nodes = []
    label_timestamp_pairs = set()  # 确保唯一的(标签, 时间戳)二元组

    num_activities = len(nodes)  # 与原文件中的活动数量相同

    for _ in range(num_activities):
        while True:
            node_id = random.choice([node[0] for node in nodes])
            label = random.choice(labels)
            timestamp = random.choice(timestamps)

            if (label, timestamp) not in label_timestamp_pairs:
                label_timestamp_pairs.add((label, timestamp))
                random_nodes.append((node_id, label, timestamp))
                break

    return random_nodes

def save_files(random_nodes, edges, labels, edge_file, label_file, node_file):
    # 保存边的关系
    with open(edge_file, 'w') as f:
        for node1, node2 in edges:
            f.write(f"{node1}\t{node2}\n")

    # 保存标签信息
    with open(label_file, 'w') as f:
        for label_id, label_name in labels.items():
            f.write(f"{label_id}\t{label_name}\n")

    # 保存节点和活动信息
    with open(node_file, 'w') as f:
        for node_id, label, timestamp in random_nodes:
            f.write(f"{node_id}\t{label}\t{timestamp}\n")

# 主函数
def main():
    # 定义文件名


    pattern = 'ipsweep'
    dia_threshold = 2
    edge_file = 'datasets/IMDB-relation.txt'          # 文件1：边关系
    label_file = 'datasets/movie_tags.txt'          # 文件2：标签映射
    node_file = 'datasets/movie_activity_top3.txt'          # 文件3：节点活动
    # 读取原始文件
    edges = read_edge_file(edge_file)
    label_map = read_label_file(label_file)
    nodes = read_node_file(node_file)
    # 获取标签和时间戳的列表
    labels = list(label_map.keys())
    timestamps = list(set(node[2] for node in nodes))
    # 生成随机图，保持活动数量与原文件相同
    random_nodes = generate_random_graph(nodes, labels, timestamps)
    # 保存生成的文件
    save_files(random_nodes, edges, label_map, 'datasets/movie_random_relation.txt', 'datasets/movie_random_tag_id.txt', 'datasets/movie_random_activity.txt')

    # data_set = main_1.data_load("random_activity.txt")
    # data_set, item_count_dict, node_id = main_1.attribute_count(data_set, min_sup=1)  # 单一属性阈值
    # g, ver_id, attr_ver = main_1.load_networkx_node(data_set, node_id)
    # graph = main_1.load_networkx_edge(g, 'random_graph_edges.txt', ver_id)
    #
    # L = main_1.init_L(max_item)
    # support = {}
    #
    # L1 = main_1.create_L1(item_count_dict)
    # L, support = main_1.generate_L(L, L1, g, sup_g, subg_set, max_item, support)
    #
    # q=calculate_support_value(L, L1, graph, support, top_k, random_graph=None)

    # data_set = main_1.data_load("datasets/netAttacker_activity_id.txt")
    #
    # data_set, item_count_dict, node_id = main_1.attribute_count(data_set, min_sup=1)  # 单一属性阈值
    #
    # g, ver_id, attr_ver = main_1.load_networkx_node(data_set, node_id)  # node_id存储的是全部结点
    #
    #
    # g = main_1.load_networkx_edge(g, 'datasets/netAttacker_id_relation.txt', ver_id)
    # main_1.renew_count_dict(g, item_count_dict, ver_id)  # ver_id存储的是拥有属性的结点
    #
    # label_dict, community_dict = main_1.DL.label_get(g)
    # deg_set = main_1.DL.deg_get(g)
    # tag_dict, label_dict = main_1.DL.first_order(g, deg_set, label_dict, community_dict)
    #
    # label_dict = main_1.DL.diaLPA(g, community_dict, label_dict, dia_threshold, iter_threshold=5)
    # communities = main_1.DL.get_community(g, label_dict)
    # dia_set = main_1.DL.analyse(g, communities)
    # communities = main_1.DL.after_treatment(g, communities, label_dict, community_dict, dia_set, dia_threshold, check_time=0)
    #
    #
    # subg_set = []
    # bridgeConnectDict = {}
    # edgeDict = {}
    # for Ci in communities:
    #     subg_set.append(main_1.subg_generate(g, Ci))
    #     for node in Ci:
    #         node.cluster = communities.index(Ci)
    # sup_g = main_1.DL.creat_supGraph(g, communities, bridgeConnectDict, edgeDict)
    #
    #
    # max_item = 5
    #
    # L = main_1.init_L(max_item)
    # support = {}
    # L1 = main_1.create_L1(item_count_dict)
    # actual_support = main_1.generate_L(L, L1, g, sup_g, subg_set, max_item, support)
    #
    # g_test = significance_test(g, pattern, label_dict, actual_support, max_item, dia_threshold, method="gnm")
    #
    # print("g_test:", g_test)



if __name__ == "__main__":
    main()
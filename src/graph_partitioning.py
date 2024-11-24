import datetime as dt
import networkx as nx
import collections
import queue
from community import modularity


def load_networkx(path):
    flag = 1  # 连通图
    seperator = 'tab'  # 确认数据集分隔符
    networkx = nx.Graph()
    f = open(path, 'r')
    if len(f.readlines()[0].strip().split('\t')) < 2:
        seperator = 'space'
        f = open(path, 'r')
        for line in f.readlines():
            data_line = line.strip().split(' ')
            networkx.add_edge(data_line[0], data_line[1], weight=1)
    else:
        f = open(path, 'r')
        for line in f.readlines():
            data_line = line.strip().split('\t')
            networkx.add_edge(data_line[0], data_line[1], weight=1)
    if not nx.is_connected(networkx):  # 若网络为连通图则直接使用，否则取图中最大的连通图作为研究对象
        flag = 0
        length = []
        for subgraph in nx.connected_component_subgraphs(networkx):
            length.append(len(subgraph.nodes()))
        result = max(length)
        for subgraph in nx.connected_component_subgraphs(networkx):
            if len(subgraph.nodes()) == result:
                networkx = subgraph
    return networkx


def deg_get(G):
    deg_set = collections.defaultdict(dict)
    for item in G.adj.keys():
        deg_set[item] = len(list(G.adj[item].keys()))
    deg_set = sorted(deg_set.items(), key=lambda x: x[1], reverse=True)
    return deg_set


def label_get(G):
    label_dict = collections.defaultdict(dict)
    community_dict = collections.defaultdict(dict)
    for item in G.adj.keys():
        label_dict[item] = item
        community_dict[item] = {item}
    return label_dict, dict(community_dict)


def first_order(G, deg_set, label_dict, community_dict):
    tag_dict = collections.defaultdict(dict)
    iter = 0  # 循环次数
    while True:
        if len(tag_dict) == len(deg_set):
            break
        center_point = deg_set[iter][0]
        if center_point not in tag_dict.keys():
            tag_dict[center_point] = 0  # 结点已被成功标记
        else:
            iter += 1
            continue
        for neighbor in G.adj[center_point].keys():
            if neighbor not in tag_dict.keys():
                community_dict[label_dict[neighbor]].remove(neighbor)
                if community_dict[label_dict[neighbor]] == set():
                    community_dict.pop(label_dict[neighbor])
                label_dict[neighbor] = label_dict[center_point]
                community_dict[label_dict[neighbor]].add(neighbor)
                tag_dict[neighbor] = 1
        iter += 1
    return community_dict, label_dict


def get_max_community_label(adjacency_node_list, label_dict):
    temp_dict = {}
    for node in adjacency_node_list:
        # 按照label为group维度，统计每个label的weight累加和
        node_weight = 1
        if label_dict[node] not in temp_dict:
            temp_dict[label_dict[node]] = node_weight
        else:
            temp_dict[label_dict[node]] += node_weight
    sort_list = sorted(temp_dict.items(), key=lambda d: d[1], reverse=True)
    all_labels = [sort_list[0][0]]
    for i in range(len(sort_list)):
        if sort_list[i][1] == sort_list[0][1]:
            if sort_list[i][0] not in all_labels:
                all_labels.append(sort_list[i][0])
        else:
            break
    return all_labels


def check_label(adjacency_node_list, label_dict):
    temp_dict = {}
    for node in adjacency_node_list:
        # 按照label为group维度，统计每个label的weight累加和
        node_weight = 1
        if label_dict[node] not in temp_dict:
            temp_dict[label_dict[node]] = node_weight
        else:
            temp_dict[label_dict[node]] += node_weight
    sort_list = sorted(temp_dict.items(), key=lambda d: d[1], reverse=True)
    all_labels = []
    for i in range(len(sort_list)):
        if sort_list[i][1] > 3 or len(all_labels) < 3:
            all_labels.append(sort_list[i][0])
    return all_labels


def creat_newgraph(G, node_set):
    g = nx.Graph()
    for node in node_set:
        for otherNode in G.adj[node].keys():
            if otherNode in node_set:
                g.add_edge(node, otherNode, weight=1)
    return g


def creat_subgraph(G, community_dict, node, label):
    node_set = list(community_dict[label])
    if node not in node_set:
        node_set.append(node)
    g = creat_newgraph(G, node_set)
    return g



def tackle_exp(G, label_dict, community_dict, dia_threshold, node):
    join_flag = 1
    adjacency_node_list = G.adj[node].keys()
    all_labels = check_label(adjacency_node_list, label_dict)  # label即核心点编号
    for label in all_labels:
        temp_graph = creat_subgraph(G, community_dict, node, label_dict[node])
        if len(temp_graph.node) != 0:
            if node in temp_graph:
                temp_graph.remove_node(node)
            if not nx.is_connected(temp_graph):
                join_flag = 0
                break
        sub_graph = creat_subgraph(G, community_dict, node, label)
        length = max(nx.single_source_shortest_path_length(sub_graph, node).values())
        if length <= dia_threshold:
            join_flag = 1
            break
        else:
            join_flag = 0
            continue
    if join_flag == 1:
        community_dict[label_dict[node]].remove(node)
        if community_dict[label_dict[node]] == set():
            community_dict.pop(label_dict[node])
        label_dict[node] = label
        community_dict[label_dict[node]].add(node)
    else:
        community_dict[label_dict[node]].remove(node)
        if community_dict[label_dict[node]] == set():
            community_dict.pop(label_dict[node])
        label_dict[node] = node
        if label_dict[node] not in community_dict.keys():
            community_dict[label_dict[node]] = {node}
        else:
            community_dict[label_dict[node]].add(node)


def diaLPA(G, community_dict, label_dict, dia_threshold, iter_threshold):
    iter = 0
    while True:
        if iter >= iter_threshold:
            break
        else:
            iter += 1
            print("iteration: ", iter)
            start_time = dt.datetime.now()
            for node in G.adj.keys():
                join_flag = 1
                adjacency_node_list = G.adj[node].keys()
                all_labels = get_max_community_label(adjacency_node_list, label_dict)  # label即核心点编号
                for label in all_labels:
                    if label_dict[node] == label:
                        join_flag = 0
                        break
                    else:
                        temp_graph = creat_subgraph(G, community_dict, node, label_dict[node])
                        if len(temp_graph.node) != 0:
                            temp_graph.remove_node(node)
                            if not nx.is_connected(temp_graph):
                                join_flag = 0
                                break
                        sub_graph = creat_subgraph(G, community_dict, node, label)  # 加入成功后更新tag_dict
                        length = max(nx.single_source_shortest_path_length(sub_graph, node).values())
                        if length <= dia_threshold:
                            join_flag = 1
                            break
                        else:
                            join_flag = 0
                            continue
                if join_flag == 1:
                    community_dict[label_dict[node]].remove(node)
                    if community_dict[label_dict[node]] == set():
                        community_dict.pop(label_dict[node])
                    label_dict[node] = label
                    community_dict[label_dict[node]].add(node)
        end_time = dt.datetime.now()
        running_time = end_time - start_time
        print("running_time:", running_time)
        cluster_group = dict()
        for node in G.adj.keys():
            cluster_id = label_dict[node]
            if cluster_id not in cluster_group.keys():
                cluster_group[cluster_id] = [node]
            else:
                cluster_group[cluster_id].append(node)
        print("com:", len(cluster_group))
        mod = modularity(label_dict, G)
        print("mod:", mod)
    return label_dict


def handle_cluster(info):
    C = []
    clust_num = len(info.keys())
    for i in list(info.keys()):
        temp = []
        for item in info[i]:
            temp.append(item)
        C.append(temp)
    return C


def static_C(C):
    sdic = {}
    for Ci in C:
        if len(Ci) not in sdic:
            sdic[len(Ci)] = 1
        else:
            sdic[len(Ci)] += 1
    return sdic


def analyse(G, communities):
    dia_set = []
    for Ci in communities:
        g = nx.Graph()
        for node in Ci:
            for otherNode in G.adj[node].keys():
                if otherNode in Ci:
                    g.add_edge(node, otherNode, weight=1)
        if len(g.node) == 0:
            dia_set.append(0)
        else:
            dia_set.append(nx.diameter(g))
    return dia_set


def check_dia(dia_set, threshold):
    com_index = []
    for i in range(len(dia_set)):
        if dia_set[i] > threshold:
            com_index.append(i)
    return com_index


def get_community(G, label_dict):
    cluster_group = dict()
    for node in G.adj.keys():
        cluster_id = label_dict[node]
        if cluster_id not in cluster_group.keys():
            cluster_group[cluster_id] = [node]
        else:
            cluster_group[cluster_id].append(node)
    communities = handle_cluster(cluster_group)
    return communities


def get_excepNode(G, communities, com_index, excep_node, dia_threshold):
    for sub_cindex in com_index:
        ng = nx.Graph()
        for node in communities[sub_cindex]:
            for otherNode in G.adj[node].keys():
                if otherNode in communities[sub_cindex]:
                    ng.add_edge(node, otherNode, weight=1)
        for vertex in ng.adj.keys():
            length = max(nx.single_source_shortest_path_length(ng, vertex).values())
            if length > dia_threshold:
                excep_node.append(vertex)


'''
def creat_supGraph(G, communities, bridgeConnectDict, edgeDict):
    sup_g = nx.Graph()
    for i in range(len(communities)):
        for j in range(len(communities)):
            flag = 0
            if j > i:
                for ni in communities[i]:
                    for nj in communities[j]:
                        if nj in G.adj[ni].keys():
                            flag = 1
                            ni.isBridgeConnectedNode = True
                            nj.isBridgeConnectedNode = True
                            ni.outerBridgeConnectedNode[nj] = 1
                            nj.outerBridgeConnectedNode[ni] = 1
                            if (i, j) not in edgeDict.keys():
                                edgeDict[(i, j)] = [(ni, nj)]
                            else:
                                edgeDict[(i, j)].append((ni, nj))
                            if (j, i) not in edgeDict.keys():
                                edgeDict[(j, i)] = [(nj, ni)]
                            else:
                                edgeDict[(j, i)].append((nj, ni))
                            if i not in bridgeConnectDict.keys():
                                bridgeConnectDict[i] = [ni]
                            else:
                                bridgeConnectDict[i].append(ni)
                            if j not in bridgeConnectDict.keys():
                                bridgeConnectDict[j] = [nj]
                            else:
                                bridgeConnectDict[j].append(nj)
            if flag == 1:
                sup_g.add_edge(i, j, weight=1)
    return sup_g
'''


def creat_supGraph(G, communities, bridgeConnectDict, edgeDict):
    sup_g = nx.Graph()
    for i in range(len(communities)):
        for j in range(len(communities)):
            flag = 0
            if j > i:
                for ni in communities[i]:
                    for nj in communities[j]:
                        if nj in G.adj[ni].keys():
                            flag = 1
                            ni.isBridgeConnectedNode = True
                            nj.isBridgeConnectedNode = True
                            if i not in bridgeConnectDict.keys():
                                bridgeConnectDict[i] = {ni}
                            else:
                                bridgeConnectDict[i].add(ni)
                            if j not in bridgeConnectDict.keys():
                                bridgeConnectDict[j] = {nj}
                            else:
                                bridgeConnectDict[j].add(nj)
            if flag == 1:
                sup_g.add_edge(i, j, weight=1)
    return sup_g


def localBFS(G, node, node_set, dia_threshold):
    q = queue.Queue()
    visit = set()
    visit.add(node)
    q.put(node)
    order = 1
    while not q.empty() and len(visit) <= len(node_set):
        length = q.qsize()
        for i in range(length):
            source = q.get()
            for neibor in G.adj[source].keys():
                if neibor in node_set and neibor not in visit:
                    node.innerBridgeConnectedNode[neibor] = order
                if neibor not in visit:
                    visit.add(neibor)
                    q.put(neibor)
        order += 1
        if order > dia_threshold:
            return


def after_treatment(G, communities, label_dict, community_dict, dia_set, dia_threshold, check_time):
    while max(dia_set) > dia_threshold:
        if check_time > 4:
            break
        check_time += 1
        com_index = check_dia(dia_set, dia_threshold)
        excep_node = []
        get_excepNode(G, communities, com_index, excep_node, dia_threshold)
        for j in excep_node:
            tackle_exp(G, label_dict, community_dict, dia_threshold, j)
        communities = get_community(G, label_dict)
        dia_set = analyse(G, communities)
    if check_time > 4:
        loop = 0
        for exnode in excep_node:
            label_dict[exnode] = len(label_dict) + loop
            community_dict[len(label_dict) + loop] = exnode
            loop += 1
        communities = get_community(G, label_dict)
    return communities


if __name__ == '__main__':
    start = dt.datetime.now()
    ###DiaLPA聚类算法+数据预处理
    G = load_networkx('com-amazon.ungraph.txt')  # 数据集导入
    label_dict, community_dict = label_get(G)
    deg_set = deg_get(G)
    tag_dict, label_dict = first_order(G, deg_set, label_dict, community_dict)
    dia_threshold = 3
    iter_threshold = 3  # 直径参数,迭代次数
    label_dict = diaLPA(G, community_dict, label_dict, dia_threshold, iter_threshold)
    ###DiaLPA聚类算法+数据预处理
    ###聚类结果存入列表
    communities = get_community(G, label_dict)
    dia_set = analyse(G, communities)
    check_time = 0
    communities = after_treatment(G, communities, label_dict, community_dict, dia_set, dia_threshold, check_time)
    ###聚类结果存入列表

    edgeDict = {}
    bridgeConnectDict = {}
    ###构建超图
    # sup_g=creat_supGraph(G, communities bridgeConnectDict, edgeDict)
    end = dt.datetime.now()
    run_time = end - start
    print("total_time:", run_time)
    ###构建超图

    ###结果分析
    mod = modularity(label_dict, G)
    static_dict = static_C(communities)
    dia_set = analyse(G, communities)
    ###结果分析

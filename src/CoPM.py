import collections
import datetime as dt
import itertools
import queue
import networkx as nx
import DiaLPA_3 as DL
import Sign_Test




class Time_attr:
    def __init__(self, attr, time):
        self.time = time
        self.attr = attr
        self.visit = 0


class Vertex:
    def __init__(self, key, time_attr):
        self.id = key
        self.Attr = [time_attr]
        self.isBridgeConnectedNode = False
        self.cluster = -1
        self.innerBridgeConnectedNode = {}
        self.outerBridgeConnectedNode = {}


def data_load(data_path):
    f = open(data_path, 'r')
    data = []
    for line in f.readlines():
        part = line.strip().split('\t')
        if line[0] == 'n':
            continue
        data_line = []
        for i in range(len(part)):
            r = part[i].strip()
            data_line.append(r)
        data.append(data_line)
    return data


def load_networkx_node(data_set, node_id):
    g = nx.Graph()
    attr_ver = {}
    ver_id = {}
    for data_line in data_set:
        time_attr = Time_attr(data_line[1], data_line[2])
        if data_line[0] not in ver_id.keys():
            ver_id[data_line[0]] = Vertex(data_line[0], time_attr)
            g.add_node(ver_id[data_line[0]])
        else:
            ver_id[data_line[0]].Attr.append(time_attr)
        attr_ver[time_attr] = ver_id[data_line[0]]
    for id in node_id:
        if id not in ver_id.keys():
            ver_id[id] = Vertex(id, Time_attr(None, None))
    return g, ver_id, attr_ver


def load_networkx_edge(g, edge_path, ver_id):
    f = open(edge_path, 'r')
    for line in f.readlines():
        data_line = line.strip().split('\t')
        if data_line[0] not in ver_id.keys():
            ver_id[data_line[0]] = Vertex(data_line[0], Time_attr(None, None))
        if data_line[1] not in ver_id.keys():
            ver_id[data_line[1]] = Vertex(data_line[1], Time_attr(None, None))
        g.add_edge(ver_id[data_line[0]], ver_id[data_line[1]], weight=1)
    if not nx.is_connected(g):
        length = []
        for subgraph in nx.connected_component_subgraphs(g):
            length.append(len(subgraph.nodes()))
        result = max(length)
        for subgraph in nx.connected_component_subgraphs(g):
            if len(subgraph.nodes()) == result:
                g = subgraph
    return g


def attribute_count(data, min_sup):
    node_id = set()
    item_count_dict = {}
    for item in data:
        node_id.add(item[0])
        if item[1] not in item_count_dict:
            item_count_dict[item[1]] = 1
        else:
            item_count_dict[item[1]] += 1
    key = item_count_dict.keys()
    data_set = []
    for item in data:
        if item[1] in key and item_count_dict[item[1]] < min_sup:
            del item_count_dict[item[1]]
    key = item_count_dict.keys()
    for item in data:
        if item[1] in key:
            data_set.append(item)

    return data_set, item_count_dict, node_id


def renew_count_dict(g, item_count_dict, ver_id):
    item_count_dict.clear()
    ver_id.clear()
    for node in g.adj.keys():
        ver_id[node.id] = node
        for time_attr in node.Attr:
            if time_attr.attr not in item_count_dict:
                item_count_dict[time_attr.attr] = 1
            else:
                item_count_dict[time_attr.attr] += 1
    if None in item_count_dict.keys():
        del item_count_dict[None]


def subg_generate(g, Ci):
    sg = nx.Graph()
    for node in Ci:
        for otherNode in g.adj[node].keys():
            if otherNode in Ci:
                sg.add_edge(node, otherNode, weight=1)
    if len(sg.node) == 0:
        for node in Ci:
            sg.add_node(node)
    return sg


def dict_handle(sub_g, item_count_dict):
    sub_dict = {}
    for node in sub_g.adj.keys():
        for attr in item_count_dict.keys():
            for time_attr in node.Attr:
                if attr == time_attr.attr:
                    if attr not in list(sub_dict.keys()):
                        sub_dict[attr] = 1
                    else:
                        sub_dict[attr] += 1
    return sub_dict


def ST_judge(G, i, j):  # 度小的当作源节点
    if len(G.adj[i].keys()) >= len(G.adj[j].keys()):
        return j, i
    else:
        return i, j


def BFS(G, i, j, dia_threshold):
    q = queue.Queue()
    visit = set()
    source, target = ST_judge(G, i, j)
    q.put(source)
    order = 1
    while (q.empty() == False):
        length = q.qsize()
        for i in range(length):
            source = q.get()
            for neibor in G.adj[source].keys():
                if neibor == target:
                    return True
                if neibor not in visit:
                    visit.add(neibor)
                    q.put(neibor)
        order += 1
        if order > dia_threshold:
            return False
    return False


def struc_prune(emb, g):  # 结构约束
    emb_set = []
    for item in emb:
        flag = 1
        distance = list(itertools.combinations(list(item), 2))
        for i in distance:
            # if nx.dijkstra_path_length(g,i[0],i[1])>dia_threshold:
            if BFS(g, i[0], i[1], dia_threshold) == False:
                flag = 0
                break
        if flag == 1:
            emb_set.append(item)
    return emb_set


def renew_visit(G):
    for node in G.adj.keys():
        for time_attr in node.Attr:
            time_attr.visit = 0


def overlap_mark(sequence):
    for time_attr in sequence:
        time_attr.visit = 1


def MNA(emb, item_list, candidate_emb, index):
    count = 0
    for sequence in emb:
        stop = 0
        for time_attr in sequence:
            if time_attr.visit == 1:
                stop = 1
                break
        if stop == 1:
            continue
        flag = 0
        delta = []
        attr_pair_set = list(itertools.combinations(list(sequence), 2))
        for attr_pair in attr_pair_set:
            time1 = attr_pair[0].time
            time2 = attr_pair[1].time
            # delta.append(abs(dt.datetime.strptime(time1, "%Y:%m:%d:%H:%M:%S")
            #                  - dt.datetime.strptime(time2, "%Y:%m:%d:%H:%M:%S")).total_seconds())

            # delta.append(abs(dt.datetime.strptime(time1, "%Y:%m:%d")
            #                  - dt.datetime.strptime(time2, "%Y:%m:%d")).seconds)



            delta.append(abs(dt.datetime.strptime(time1, "%Y:%m:%d:%H:%M:%S")
                             - dt.datetime.strptime(time2, "%Y:%m:%d:%H:%M:%S")).seconds)



            # delta.append(abs(dt.datetime.strptime(time1, "%Y-%m-%d")
            #                  - dt.datetime.strptime(time2, "%Y-%m-%d")).seconds)
        for d in delta:
            if d > time_threshold:
                break
            else:
                flag += 1
        if flag == len(attr_pair_set):
            if ' '.join(sorted(item_list)) not in candidate_emb[index].keys():
                candidate_emb[index][' '.join(sorted(item_list))] = {tuple(sequence)}
            else:
                candidate_emb[index][' '.join(sorted(item_list))].add(tuple(sequence))
            overlap_mark(sequence)
            count += 1
    return count


def init_emb(subg_set, candidate_emb):
    for i in range(len(subg_set)):
        candidate_emb[i] = {}


def oneItem_emb(g, L1, candidate_emb, index):
    for Lk_item in L1:
        cur_attr = list(Lk_item)[0]
        vertices = list(g.adj.keys())
        Lk_item_key = ' '.join(sorted(list(Lk_item)))
        for node in vertices:
            for time_attr in node.Attr:
                if time_attr.attr == cur_attr:
                    if Lk_item_key not in candidate_emb[index].keys():
                        candidate_emb[index][Lk_item_key] = {time_attr}
                    else:
                        candidate_emb[index][Lk_item_key].add(time_attr)


def judge_emb(candidate_emb, item_list, index):
    for item in item_list:
        if item not in candidate_emb[index].keys():
            return False
    return True


def del_attr(item_list, candidate_emb, index):
    sub_item_list = item_list.copy()
    min_count = len(candidate_emb[index][item_list[0]])
    min_index = 0
    for i in range(1, len(item_list)):
        if min_count > len(candidate_emb[index][item_list[i]]):
            min_index = i
            min_count = len(candidate_emb[index][item_list[i]])
    sub_item_list.remove(item_list[min_index])
    return sub_item_list, item_list[min_index]


def generate_emb(item_list, candidate_emb, index):
    res = []
    sub_item_list, del_item = del_attr(item_list, candidate_emb, index)
    if ' '.join(sorted(sub_item_list)) in candidate_emb[index].keys():
        attr_set1 = candidate_emb[index][' '.join(sorted(sub_item_list))]
    else:
        return res
    attr_set2 = candidate_emb[index][del_item]
    for sequence in attr_set1:
        for cur in attr_set2:
            try:
                sequence = list(sequence)
                sequence.append(cur)
                res.append(sequence.copy())
                sequence.pop()
            except:
                temp = []
                temp.append(sequence)
                temp.append(cur)
                res.append(temp.copy())
    return res


def emb_prune(embedding, other_g):
    res = embedding.copy()
    for sub_emb in embedding:
        o1 = 0
        s1 = 0
        for item in sub_emb:
            if item in other_g.adj.keys():
                o1 += 1
            else:
                s1 += 1
        if o1 == len(sub_emb) or s1 == len(sub_emb):
            res.remove(sub_emb)
    return res


def get_nonmarked_node(g, item_list):
    attr_node_item = {}
    for node in g.adj.keys():
        for time_attr in node.Attr:
            for sub_item in item_list:
                if time_attr.attr == sub_item and time_attr.visit == 0:
                    if sub_item not in attr_node_item.keys():
                        attr_node_item[sub_item] = {node}
                    else:
                        attr_node_item[sub_item].add(node)
    return attr_node_item


def cross_MNA(emb, attr_list):
    attr_dict = {}
    count = 0
    for sub_emb in emb:
        for at in attr_list:
            attr_dict[at] = []
        for node in sub_emb:
            for time_attr in node.Attr:
                for at in attr_list:
                    if time_attr.attr == at and time_attr.visit == 0 and time_attr not in attr_dict[at]:
                        attr_dict[at].append(time_attr)
        arrangement = list(itertools.product(*list(attr_dict.values())))
        for sequence in arrangement:
            stop = 0
            for time_attr in sequence:
                if time_attr.visit == 1:
                    stop = 1
                    break
            if stop == 1:
                continue
            flag = 0
            delta = []
            attr_pair_set = list(itertools.combinations(list(sequence), 2))
            for attr_pair in attr_pair_set:
                time1 = attr_pair[0].time
                time2 = attr_pair[1].time
                # delta.append(abs(dt.datetime.strptime(time1, "%Y:%m:%d:%H:%M:%S")
                #                  - dt.datetime.strptime(time2, "%Y:%m:%d:%H:%M:%S")).total_seconds())

                # delta.append(abs(dt.datetime.strptime(time1, "%Y:%m:%d")
                #                  - dt.datetime.strptime(time2, "%Y:%m:%d")).seconds)

                delta.append(abs(dt.datetime.strptime(time1, "%Y:%m:%d:%H:%M:%S")
                                 - dt.datetime.strptime(time2, "%Y:%m:%d:%H:%M:%S")).seconds)



                # delta.append(abs(dt.datetime.strptime(time1, "%Y-%m-%d")
                #                  - dt.datetime.strptime(time2, "%Y-%m-%d")).seconds)
            for d in delta:
                if d > time_threshold:
                    break
                else:
                    flag += 1
            if flag == len(attr_pair_set):
                overlap_mark(sequence)
                count += 1
    return count


def search_in_subg(G, nonmarked_node_dict, other_g, item_list):
    other_g_node_dict = get_nonmarked_node(other_g, item_list)
    ver = set()
    ver_set = []
    for sub_item in item_list:
        if len(nonmarked_node_dict) == 0 or len(other_g_node_dict) == 0:
            return 0
        if sub_item in nonmarked_node_dict:
            ver = nonmarked_node_dict[sub_item]
        if sub_item in other_g_node_dict:
            ver = ver | other_g_node_dict[sub_item]
        ver_set.append(ver.copy())
        ver.clear()
    embedding = list(itertools.product(*(ver_set)))
    cross_cluster_emb = emb_prune(embedding, other_g)
    cross_cluster_emb = struc_prune(cross_cluster_emb, G)
    sup = cross_MNA(cross_cluster_emb, item_list)
    cross_cluster_emb.clear()
    # print("act_sup:",sup)
    return sup


def is_apriori(Ck, Lksub1):
    for item in Ck:
        sub_item = Ck - frozenset([item])
        if sub_item not in Lksub1:
            return False
    return True


def create_L1(item_count):
    list1 = list(item_count.keys())
    L1 = set()
    for item in list1:
        L1_item = frozenset([item])
        L1.add(L1_item)
    return L1


def create_Ck(Lksub1, k):
    Ck = set()
    list_subset = list(Lksub1)
    len_set = len(Lksub1)
    for i in range(0, len_set):
        for j in range(i, len_set):
            list1 = list(list_subset[i])
            list2 = list(list_subset[j])
            list1.sort()
            list2.sort()
            if list1[0:k - 2] == list2[0:k - 2]:
                Ck_item = list_subset[i] | list_subset[j]
                if is_apriori(Ck_item, Lksub1):
                    Ck.add(Ck_item)
    return Ck


def create_Lk(Ck, L, G, sup_g, subg_set, support, candidate_emb):
    Lk = set()
    Ck_list = list(Ck)
    for item_set in Ck_list:
        success_flag = False
        item_list = list(item_set)
        for g in subg_set:
            index = subg_set.index(g)
            sub_dict = dict_handle(g, item_count_dict)
            L1 = create_L1(sub_dict)
            oneItem_emb(g, L1, candidate_emb, index)
            if not judge_emb(candidate_emb, item_list, index):
                continue
            embedding = generate_emb(item_list, candidate_emb, index)
            sup = MNA(embedding, item_list, candidate_emb, index)
            embedding.clear()
            if not success_flag:
                nonmarked_node_dict = get_nonmarked_node(g, item_list)
                for other_g in subg_set:
                    if subg_set.index(other_g) in sup_g.adj[index].keys():
                        sup += search_in_subg(G, nonmarked_node_dict, other_g, item_list)
                        if sup >= sup_threshold:
                            break
            else:
                support[item_set] += sup
                continue
            if item_set not in support.keys():
                support[item_set] = sup
            else:
                support[item_set] += sup
            if support[item_set] >= sup_threshold:
                Lk.add(item_set)
                L[len(item_set)].append(item_set)
                success_flag = True
        renew_visit(G)
        # print("support_LK:", support)
    return Lk


def init_L(max_item):
    L = {}
    for i in range(1, max_item):
        L[i] = []
    return L


def generate_L(L, L1, G, sup_g, subg_set, max_item, support):
    Lksub1 = L1.copy()
    for Lk_item in Lksub1:
        if Lk_item not in L[1]:
            L[1].append(Lk_item)
    Ck = set('1')
    candidate_emb = {}
    init_emb(subg_set, candidate_emb)
    for i in range(2, max_item):
        if Ck == set() or Lksub1 == set():
            break
        Ck = create_Ck(Lksub1, i)

        Lk = create_Lk(Ck, L, G, sup_g, subg_set, support, candidate_emb)
        Lksub1 = Lk.copy()
        # print("support_L:",support)
    return L, support




def nameTransform():
    f = open("datasets/movie_tags.txt", 'r', encoding='utf-8', errors='ignore')  # 忽略无法解码的字符
    hashMap = dict()
    reverseHashMap = dict()
    for dataline in f.readlines():
        #       data = dataline.strip().split('\t')

        # print("dataline:", dataline)
        # print(repr(dataline))
        # data = dataline.strip().split('\t')
        data = dataline.strip().split()
        # print("data:", data)
        # print(data[0])
        hashMap[data[0]] = data[1]
        reverseHashMap[data[1]] = data[0]
    return hashMap, reverseHashMap


# def calculate_support(g, item_list, candidate_emb, index, sup_threshold):
#     """
#     计算指定 item_list 在子图中的支持度。
#
#     参数:
#     g: 当前图
#     item_list: 当前的项集
#     candidate_emb: 存储候选嵌入的字典
#     index: 子图的索引
#     sup_threshold: 支持度阈值
#
#     返回:
#     sup: 计算出的支持度
#     """
#     embedding = generate_emb(item_list, candidate_emb, index)
#     sup = MNA(embedding, item_list, candidate_emb, index)
#     embedding.clear()
#
#     if sup < sup_threshold:
#         return 0
#
#     # 如果支持度大于阈值，检查是否存在跨子图的支持度
#     nonmarked_node_dict = get_nonmarked_node(g, item_list)
#     for other_g in subg_set:
#         if subg_set.index(other_g) in sup_g.adj[index].keys():
#             sup += search_in_subg(g, nonmarked_node_dict, other_g, item_list)
#
#     return sup
#
#



if __name__ == '__main__':
    start_time = dt.datetime.now()

    dia_threshold = 2
    time_threshold = 360#6min
    sup_threshold = 1
    data_set = data_load("datasets/movie_activity_top3.txt")

    data_set, item_count_dict, node_id = attribute_count(data_set, min_sup=1)  # 单一属性阈值

    g, ver_id, attr_ver = load_networkx_node(data_set, node_id)  # node_id存储的是全部结点
    for key, value in attr_ver.items():
        attr_value = getattr(key, 'attr', None)
        time_value = getattr(key, 'time', None)
        visit_value = getattr(key, 'visit', None)

        cluster_value = getattr(value, 'cluster', None)
        id_value = getattr(value, 'id', None)
        is_bridge = getattr(value, 'isBridgeConnectedNode', None)

    g = load_networkx_edge(g, 'datasets/IMDB-relation.txt', ver_id)
    renew_count_dict(g, item_count_dict, ver_id)  # ver_id存储的是拥有属性的结点

    label_dict, community_dict = DL.label_get(g)
    deg_set = DL.deg_get(g)
    tag_dict, label_dict = DL.first_order(g, deg_set, label_dict, community_dict)

    label_dict = DL.diaLPA(g, community_dict, label_dict, dia_threshold, iter_threshold=5)
    communities = DL.get_community(g, label_dict)
    dia_set = DL.analyse(g, communities)
    communities = DL.after_treatment(g, communities, label_dict, community_dict, dia_set, dia_threshold, check_time=0)
    dia_set = DL.analyse(g, communities)

    subg_set = []
    bridgeConnectDict = {}
    edgeDict = {}
    for Ci in communities:
        subg_set.append(subg_generate(g, Ci))
        for node in Ci:
            node.cluster = communities.index(Ci)
    sup_g = DL.creat_supGraph(g, communities, bridgeConnectDict, edgeDict)

    top_k = 5
    max_item = 5

    L = init_L(max_item)
    support = {}

    L1 = create_L1(item_count_dict)
    L, support = generate_L(L, L1, g, sup_g, subg_set, max_item, support)
    nameList, reNameList = nameTransform()

    # 遍历数据集，提取时间戳
    for entry in data_set:
        items = entry[:-1]
        timestamp = entry[-1]
        # print(f"项集: {items}, 时间戳: {timestamp}")

    # 结果输出
    # print("=" * 50)
    # print("frequent 1-itemset " + "top 1:")
    # print("=" * 50)
    one_item = sorted(item_count_dict.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(one_item)):
        if i >= top_k:
            break
        # print(one_item[i][0])

    # 打开文件进行写入
    with open('result/result_support(4).txt', 'w') as f:
        for Lk in L.values():
            if not Lk:
                break
            f.write(str(len(list(Lk)[0])) + "-item:" + "\n")
            print("=" * 50)
            print("frequent " + str(len(list(Lk)[0])) + "-itemsets total:" + str(len(Lk)))
            print("top" + str(top_k) + ":")
            print("=" * 50)
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
                        # pattern = list(res[i][0])  # 模式
                        # actual_support = res[i][1]  # 实际支持度
                        print(list(res[i][0]))


                        # # 确保实际支持度是一个数值类型，而不是列表或元组
                        # print(f"Pattern: {pattern}, Actual Support: {actual_support}")
                        #
                        # # 调用 significance_test
                        # g_test = Sign_Test.significance_test(g, pattern, label_dict, actual_support, max_item, dia_threshold, L, top_k)
                        #
                        # print("g_test:", g_test)
                        # # 保存 g_test 值到文件
                        # f.write(f"Pattern: {pattern}, Actual Support: {actual_support}, g_test: {g_test}\n")

        # res = sorted(temp_dict.items(), key=lambda x: x[1], reverse=True)
            # for i in range(len(res)):
            #     if i < top_k:
            #
            #         pattern = list(res[i][0])  # 模式
            #         actual_support = res[i][1]  # 实际支持度
            #         print(f"Pattern: {pattern}, Actual Support: {actual_support}")
            #
            #         # 调用 significance_test，传入实际支持度
            #         g_score, p_value = Sign_Test.significance_test(g, pattern, label_dict, actual_support)

                    # significance_test
                    # g_score, p_value = Sign_Test.significance_test(g, label_dict, res)
                    # print(f"G-test 分数: {g_score}, p-value: {p_value}")
                    for j in list(res[i][0]):
                        try:
                            f.write(j + '\t')
                            pattern = list(res[i][0])  # 模式

                        except:
                            f.write(reNameList[j] + '\t')

                    f.write('\t\t' + str(res[i][1]) + '\n')


                    actual_support = res[i][1]  # 实际支持度

                    # 确保实际支持度是一个数值类型，而不是列表或元组
                    print(f"Pattern: {pattern}, Actual Support: {actual_support}")

                    # 调用 significance_test
                    g_test = Sign_Test.significance_test(g, pattern, label_dict, actual_support, max_item, dia_threshold, L, top_k)

                    print("g_test:", g_test)
                    # 保存 g_test 值到文件
                    f.write(f"Pattern: {pattern}, Actual Support: {actual_support}, g_test: {g_test}\n")






        # 计算并写入运行时间
        end_time = dt.datetime.now()
        running_time = end_time - start_time
        f.write(f"\nTotal Running Time: {running_time}\n")

    # 打印运行时间
    print(running_time)
    test = 0


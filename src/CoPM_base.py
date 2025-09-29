import collections
import networkx as nx
import itertools
import datetime as dt
import queue


class Time_attr:
    def __init__(self, attr, time):
        self.time = time
        self.attr = attr
        self.visit = 0


class Vertex:
    def __init__(self, key, time_attr):
        self.id = key
        self.Attr = [time_attr]
        self.cluster = -1


def data_load(data_path):
    """加载数据集"""
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
    """构建带属性的网络图节点"""
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
    """构建网络图的边"""
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
        for component in nx.connected_components(g):
            length.append(len(component))
        result = max(length)
        for component in nx.connected_components(g):
            if len(component) == result:
                g = g.subgraph(component)
    return g


def attribute_count(data, min_sup):
    """统计属性频次，过滤低频属性"""
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
    """更新属性计数字典"""
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


def ST_judge(G, i, j):
    """选择度小的节点作为源节点"""
    if len(G.adj[i].keys()) >= len(G.adj[j].keys()):
        return j, i
    else:
        return i, j


def BFS(G, i, j, dia_threshold):
    """BFS检查两点间距离是否在直径阈值内"""
    q = queue.Queue()
    visit = set()
    source, target = ST_judge(G, i, j)
    q.put(source)
    order = 1
    while not q.empty():
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


def struc_prune(emb, g, dia_threshold):
    """结构约束剪枝：检查嵌入是否满足直径约束"""
    emb_set = []
    for item in emb:
        flag = 1
        distance = list(itertools.combinations(list(item), 2))
        for i in distance:
            if not BFS(g, i[0], i[1], dia_threshold):
                flag = 0
                break
        if flag == 1:
            emb_set.append(item)
    return emb_set


def renew_visit(G):
    """重置访问标记"""
    for node in G.adj.keys():
        for time_attr in node.Attr:
            time_attr.visit = 0


def overlap_mark(sequence):
    """标记已使用的序列"""
    for time_attr in sequence:
        time_attr.visit = 1


def MNA(emb, item_list, time_threshold):
    """多节点聚合：计算满足时间约束的嵌入数量"""
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
            delta.append(abs(dt.datetime.strptime(time1, "%Y:%m:%d:%H:%M:%S")
                             - dt.datetime.strptime(time2, "%Y:%m:%d:%H:%M:%S")).seconds)
        for d in delta:
            if d > time_threshold:
                break
            else:
                flag += 1
        if flag == len(attr_pair_set):
            overlap_mark(sequence)
            count += 1
    return count


def get_nonmarked_node(g, item_list):
    """获取未标记的节点"""
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


def cross_MNA(emb, attr_list, time_threshold):
    """跨簇多节点聚合"""
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
                delta.append(abs(dt.datetime.strptime(time1, "%Y:%m:%d:%H:%M:%S")
                                 - dt.datetime.strptime(time2, "%Y:%m:%d:%H:%M:%S")).seconds)
            for d in delta:
                if d > time_threshold:
                    break
                else:
                    flag += 1
            if flag == len(attr_pair_set):
                overlap_mark(sequence)
                count += 1
    return count


def emb_prune(embedding, other_g):
    """嵌入剪枝：移除不满足跨簇约束的嵌入"""
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


def search_in_subg(G, nonmarked_node_dict, other_g, item_list, dia_threshold, time_threshold):
    """在子图中搜索跨簇嵌入"""
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
    cross_cluster_emb = struc_prune(cross_cluster_emb, G, dia_threshold)
    sup = cross_MNA(cross_cluster_emb, item_list, time_threshold)
    cross_cluster_emb.clear()
    return sup


def is_apriori(Ck, Lksub1):
    """Apriori剪枝：检查候选项集是否满足向下闭包性质"""
    for item in Ck:
        sub_item = Ck - frozenset([item])
        if sub_item not in Lksub1:
            return False
    return True


def create_L1(item_count):
    """创建1-频繁项集"""
    list1 = list(item_count.keys())
    L1 = set()
    for item in list1:
        L1_item = frozenset([item])
        L1.add(L1_item)
    return L1


def create_Ck(Lksub1, k):
    """创建k-候选项集"""
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


def create_Lk(Ck, L, G, sup_g, subg_set, support, dia_threshold, time_threshold, sup_threshold):
    """创建k-频繁项集"""
    Lk = set()
    Ck_list = list(Ck)
    for item_set in Ck_list:
        success_flag = False
        item_list = list(item_set)
        for g in subg_set:
            index = subg_set.index(g)
            # 获取子图中的节点
            vertices = list(g.adj.keys())
            
            # 生成嵌入
            embedding = []
            attr_node_dict = {}
            for node in vertices:
                for time_attr in node.Attr:
                    for attr in item_list:
                        if time_attr.attr == attr:
                            if attr not in attr_node_dict:
                                attr_node_dict[attr] = []
                            attr_node_dict[attr].append(time_attr)
            
            # 检查是否所有属性都存在
            if len(attr_node_dict) != len(item_list):
                continue
                
            # 生成所有可能的嵌入
            attr_lists = [attr_node_dict[attr] for attr in item_list]
            embedding = list(itertools.product(*attr_lists))
            
            # 计算支持度
            sup = MNA(embedding, item_list, time_threshold)
            
            if not success_flag:
                nonmarked_node_dict = get_nonmarked_node(g, item_list)
                for other_g in subg_set:
                    if index in sup_g.adj and subg_set.index(other_g) in sup_g.adj[index].keys():
                        sup += search_in_subg(G, nonmarked_node_dict, other_g, item_list, dia_threshold, time_threshold)
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
    return Lk


def init_L(max_item):
    """初始化频繁项集字典"""
    L = {}
    for i in range(1, max_item):
        L[i] = []
    return L


def generate_L(L, L1, G, sup_g, subg_set, max_item, support, dia_threshold, time_threshold, sup_threshold):
    """生成所有频繁项集"""
    Lksub1 = L1.copy()
    for Lk_item in Lksub1:
        if Lk_item not in L[1]:
            L[1].append(Lk_item)
    Ck = set('1')
    for i in range(2, max_item):
        if Ck == set() or Lksub1 == set():
            break
        Ck = create_Ck(Lksub1, i)
        Lk = create_Lk(Ck, L, G, sup_g, subg_set, support, dia_threshold, time_threshold, sup_threshold)
        Lksub1 = Lk.copy()
    return L, support


def nameTransform():
    """标签转换"""
    f = open("src/Delicious/datasets/delicious_tags.txt", 'r', encoding='utf-8')
    hashMap = dict()
    reverseHashMap = dict()
    for dataline in f.readlines():
        data = dataline.strip().split('\t')
        hashMap[data[0]] = data[1]
        reverseHashMap[data[1]] = data[0]
    return hashMap, reverseHashMap


def main():
    """主函数"""
    start_time = dt.datetime.now()
    
    # 参数设置
    dia_threshold = 3
    time_threshold = 4320000  # 72分钟
    sup_threshold = 50
    min_sup = 50
    top_k = 5
    max_item = 5
    
    print("开始加载数据...")
    data_set = data_load("src/Delicious/datasets/delicious_activity_top3.txt")
    data_set, item_count_dict, node_id = attribute_count(data_set, min_sup=min_sup)
    
    print("构建网络图...")
    g, ver_id, attr_ver = load_networkx_node(data_set, node_id)
    g = load_networkx_edge(g, 'src/Delicious/datasets/delicious_relation.txt', ver_id)
    renew_count_dict(g, item_count_dict, ver_id)
    
    print("开始挖掘频繁项集...")
    # 基础版本：不使用图分区，直接在整个图上挖掘
    subg_set = [g]  # 只有一个子图（整个图）
    sup_g = nx.Graph()  # 空的超图
    
    L = init_L(max_item)
    support = {}
    L1 = create_L1(item_count_dict)
    L, support = generate_L(L, L1, g, sup_g, subg_set, max_item, support, 
                           dia_threshold, time_threshold, sup_threshold)
    
    print("转换标签...")
    nameList, reNameList = nameTransform()
    
    # 结果输出
    print("=" * 50)
    print("frequent 1-itemset " + "top 1:")
    print("=" * 50)
    one_item = sorted(item_count_dict.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(one_item)):
        if i >= top_k:
            break
        print(one_item[i][0])
    
    # 保存结果
    with open('result/delicious/base/support(50).txt', 'w') as f:
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
                    print(list(res[i][0]))
                for j in list(res[i][0]):
                    try:
                        f.write(j + '\t')
                    except:
                        f.write(reNameList[j] + '\t')
                f.write('\t\t' + str(res[i][1]) + '\n')
        
        # 计算并写入运行时间
        end_time = dt.datetime.now()
        running_time = end_time - start_time
        f.write(f"\nTotal Running Time: {running_time}\n")
    
    print(f"总运行时间: {running_time}")
    print("CoPM_base算法执行完成！")


if __name__ == '__main__':
    main()

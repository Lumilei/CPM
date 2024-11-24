import math
from tables.idxutils import infinity
from collections import Counter


#@beilei ling    Calculating the difference between the mining result in the original graph and the random graph

# def get_collaborative_pattern(source_file,target_file):
#
#     f = open(source_file, 'r', encoding='utf-8')
#     collaborative_pattern = open(target_file, 'w')
#     item_line = infinity
#     line = 0
#
#     for dataline in f.readlines():
#         data = dataline.strip().split('\t')
#         line = line+1
#         #print(data)
#         if( data[0] == 3+'-item:' ):
#             item_line = line
#             print("3-item:")
#         if(line > item_line):
#             print(data)
#             collaborative_pattern.write(dataline)
#             pattern_list = data
#         else:
#             continue
def G_test_score_caculation(itemset_list, random_1_itemset, random_k_itemset,original_item_count, g_test_score_dict):

    support_a = int(itemset_list[len(itemset_list)-1])/original_item_count
    r_item_count = item_support_count(random_k_itemset)
    r_1_item_count = item_support_count(random_1_itemset)



    itemset_list.pop()
    flag = False
    for itemset in random_k_itemset:
        data = itemset.strip().split('\t')
        random_itemset_list = data
        sup_temp = random_itemset_list[len(random_itemset_list)-1]
        random_itemset_list.pop()
        support_b = int(sup_temp)/r_item_count
        a = Counter(itemset_list)
        b = Counter(random_itemset_list)
        if(dict(a)==dict(b)):
            g_test_score = support_a * math.log(support_a/support_b) + (1-support_a) * math.log((1-support_a)/(1-support_b))
            # print("g_test_score:", g_test_score)
            g_test_score_dict[str(itemset_list)] = g_test_score
            flag = True
        else:
            # print (dict(a)==dict(b))
            continue
    if flag == False:
        item1 = itemset_list[0]
        item2 = itemset_list[1]
        item3 = itemset_list[2]
        support_item1 = 0
        support_item2 = 0
        support_item3 = 0

        for itemset in random_1_itemset:
            data = itemset.strip().split('\t')
            if(data[0] == item1):
                support_item1 = int(data[len(data)-1])
            elif(data[0] == item2):
                support_item2 = int(data[len(data)-1])
            elif(data[0] == item3):
                support_item3 = int(data[len(data)-1])

            else:
                 continue
        support_b = (support_item1/r_1_item_count)*(support_item2/r_1_item_count)*(support_item3/r_1_item_count)
        g_test_score = support_a * math.log(support_a/support_b) + (1-support_a) * math.log((1-support_a)/(1-support_b))
        # print("1_item_g_test_score:", g_test_score)
        g_test_score_dict[str(itemset_list)] = g_test_score









# def G_test_score_caculation(itemset_list,target_file,count_a,count_b):
#
#     support_a = int(itemset_list[len(itemset_list)-1])/count_a
#     print("support_a:", support_a)
#     itemset_list.pop()
#     print("itemset_list:",itemset_list)
#     count_b = 0
#     flag = False
#     f = open(target_file, 'r', encoding='utf-8')
#     for dataline in f.readlines():
#         data = dataline.strip().split('\t')
#         random_itemset_list = data
#         sup_temp = random_itemset_list[len(random_itemset_list)-1]
#         random_itemset_list.pop()
#         print("random_itemset_list:", random_itemset_list)
#         support_b = int(sup_temp)/support_count_b
#         print("support_b:", support_b)
#         a = Counter(itemset_list)
#         b = Counter(random_itemset_list)
#         if(dict(a)==dict(b)):
#             g_test_score = support_a * math.log(support_a/support_b) + (1-support_a) * math.log((1-support_a)/(1-support_b))
#             print("g_test_score:", g_test_score)
#             flag = True
#         else:
#             print (dict(a)==dict(b))
#     if flag == False:
#         one_itemset_support_count = item_support_count("../1_item_random.txt")
#         print("one_itemset_support_count:", one_itemset_support_count)
#         item1 = itemset_list[0]
#         item2 = itemset_list[1]
#         item3 = itemset_list[2]
#         support_item1 = 0
#         support_item2 = 0
#         support_item3 = 0
#         f = open("../1_item_random.txt", 'r', encoding='utf-8')
#         for dataline in f.readlines():
#             data = dataline.strip().split('\t')
#             if(data[0] == item1):
#                 support_item1 = int(data[len(data)-1])
#             elif(data[0] == item2):
#                 support_item2 = int(data[len(data)-1])
#             elif(data[0] == item3):
#                 support_item3 = int(data[len(data)-1])
#             else:
#                 continue
#         g_test_score = (support_item1/one_itemset_support_count)*(support_item2/one_itemset_support_count)*(support_item3/one_itemset_support_count)
#        # print("1_item_g_test_score:", g_test_score)

def get_k_itemset_pattern(source_file,k):
    f = open(source_file, 'r', encoding='utf-8')
    item_line = infinity
    end_line = infinity
    line = 0
    k_item_list = []
    for dataline in f.readlines():
        data = dataline.strip().split('\t')
        line = line+1
        if( data[0] == str(k)+'-item:' ):
            item_line = line
            # print(str(k)+"-item:")
        if(data[0] == str(k+1)+'-item:'):
            end_line = line

        if(end_line > line > item_line):
            # print(data)
            k_item_list.append(dataline)
            pattern_list = data
        else:
            continue
    return k_item_list



# def item_support_count(target_file):
#     count = 0
#     f = open(target_file, 'r', encoding='utf-8')
#     for dataline in f.readlines():
#         data = dataline.strip().split('\t')
#         count = count + int(data[len(data)-1])
#     return count

def item_support_count(item_list):
    count = 0
    for itemset in item_list:
        data = itemset.strip().split('\t')
        count = count + int(data[len(data)-1])
    return count



if __name__ == '__main__':
     # get_collaborative_pattern("result.txt","collaborativePattern.txt")
     # get_collaborative_pattern("randomStructuralCollaborativePattern.txt","3-item-randomStructuralCollaborativePattern.txt")

     #generate k-itemset
     # one_item_set = get_k_itemset_pattern("result.txt", 1)
     # print("one_item_set:", one_item_set)
     g_test_score_dict = {}
     k_item_set = get_k_itemset_pattern("result.txt", 3)
     support_count_o = item_support_count(k_item_set)
     random_1_itemset = get_k_itemset_pattern("result_random.txt", 1)
     random_k_itemset = get_k_itemset_pattern("result_random.txt", 3)

     for itemset in k_item_set:
             data = itemset.strip().split('\t')
             itemset_list = data
             G_test_score_caculation(itemset_list, random_1_itemset, random_k_itemset, support_count_o, g_test_score_dict)
     # sorted(g_test_score_dict.keys())
     dic = sorted(g_test_score_dict.items(), key=lambda x: x[1], reverse=True)
     f = open('interesting_result.txt', 'w')
     for k in dic:
         f.write(str(k) + '\n')


     # f = open("../collaborativePattern.txt", 'r', encoding='utf-8')
     # support_count_a = item_support_count("../collaborativePattern.txt")
     # support_count_b = item_support_count("../3-item-randomStructuralCollaborativePattern.txt")
     # for dataline in f.readlines():
     #     data = dataline.strip().split('\t')
     #     itemset_list = data
     #     G_test_score_caculation(itemset_list, "../3-item-randomStructuralCollaborativePattern.txt", support_count_a, support_count_b)




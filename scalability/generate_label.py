#generated 100 labels and corresponding timestamps
import random
import time


def time_factory(start_time = (2018,1,1,0,0,0,0,0,0), end_time = (2022,1,1,0,0,0,0,0,0)):
    start = time.mktime(start_time) #生成开始时间戳
    end = time.mktime(end_time) #生成结束时间戳
    t = random.randint(start, end) #在开始和结束时间戳阈值内随机取出一个
    date_touple = time.localtime(t) #将时间戳生成时间元组
    date = time.strftime("%Y:%m:%d:%H:%M:%S", date_touple)
    return date

if __name__ == '__main__':

    result = open('datasets/generated_activity.txt', 'w')

    for node in range(0, 262111):

        #每个结点上活动的个数
        activity_num = random.randint(0,10)

        for i in range(0, activity_num):
            #具体生成哪个标签
            label_id = random.randint(0,100)

            timestamp = time_factory()
            result.write( str(node) + '\t' + str(label_id) + '\t'  + timestamp + '\n')



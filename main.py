import jieba
from collections import Counter
import math

# 两篇待比较的文档的路径
test_01 = 'D:\\software_engineering\\test_text\\test_01.txt'
test_02 = 'D:\\software_engineering\\test_text\\test_02.txt'
orig = 'D:\\software_engineering\\test_text\\orig.txt'
orig_08_add = 'D:\\software_engineering\\test_text\\orig_0.8_add.txt'
orig_08_del = 'D:\\software_engineering\\test_text\\orig_0.8_del.txt'
orig_08_dis_1 = 'D:\\software_engineering\\test_text\\orig_0.8_dis_1.txt'

#将文本分成词汇，通过jieba库实现
def Count(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    words = jieba.lcut(text)
    word_counts = Counter(words)

    return word_counts.most_common()


def MergeWord(T1,T2):
        MergeWord = []
        duplicateWord = 0
        for ch in range(len(T1)):
            MergeWord.append(T1[ch][0])
        for ch in range(len(T2)):
            if T2[ch][0] in MergeWord:
                    duplicateWord = duplicateWord + 1
            else:
                    MergeWord.append(T2[ch][0])

        # print('重复次数 = ' + str(duplicateWord))
        # 打印合并关键词
        # print(MergeWord)
        return MergeWord

# 得出文档向量，通过TF算法实现
def Vector(T1,MergeWord):
    TF1 = [0] * len(MergeWord)

    for ch in range(len(T1)):
            TermFrequence = T1[ch][1]
            word = T1[ch][0]
            i = 0
            while i < len(MergeWord):
                    if word == MergeWord[i]:
                        TF1[i] = TermFrequence
                        break
                    else:
                        i = i + 1
        # print(TF1)
    return TF1

#余弦相似度计算
def CosCount(v1,v2,lengthVector):

        # 计算出两个向量的乘积
        B = 0
        i = 0
        while i < lengthVector:
            B = v1[i] * v2[i] + B
            i = i + 1
        # print('乘积 = ' + str(B))

        # 计算两个向量的模的乘积
        A = 0
        A1 = 0
        A2 = 0
        i = 0
        while i < lengthVector:
            A1 = A1 + v1[i] * v1[i]
            i = i + 1
        # print('A1 = ' + str(A1))

        i = 0
        while i < lengthVector:
            A2 = A2 + v2[i] * v2[i]
            i = i + 1
           # print('A2 = ' + str(A2))

        A = math.sqrt(A1) * math.sqrt(A2)
        print('两篇文章的相似度 = ' + format(float(B) / A,".3f"))

def test(file1,file2):
    T1 = Count(file1)
    # print("文档1的词频统计如下：")
    # print(T1)
    # print()
    T2 = Count(file2)
    # print("文档2的词频统计如下：")
    # print(T2)
    # print()
    # 合并两篇文档的关键词
    mergeword = MergeWord(T1,T2)
    # print("两篇文档关键词：")
    # print(mergeword)
    # print(len(mergeword))
    # 得出文档向量
    v1 = Vector(T1,mergeword)
    # print("文档1向量化得到的向量如下：")
    # print(v1)
    # print()
    v2 = Vector(T2,mergeword)
    # print("文档2向量化得到的向量如下：")
    # print(v2)
    # print()
    # 计算余弦距离
    CosCount(v1,v2,len(v1))

test(orig,orig_08_del)
test(orig,orig_08_add)
test(orig,orig_08_dis_1)
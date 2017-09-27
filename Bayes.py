from numpy import *
import re

def createDataSet():
    wordList =[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    wordlabels = [0,1,0,1,0,1]
    return wordList,wordlabels
'''
wordList ,wordlabels =createDataSet()
print( wordList,wordlabels )
'''

def createVocab(wordList):
    result_Vocab = set([])
    for word in wordList:
        result_Vocab = result_Vocab | set(word)
    return  list(result_Vocab)
'''
wordList , wordlabels =createDataSet()
vocabulary = createVocab(wordList)
print(vocabulary)
'''
def setWordToVect(result_Vocab , inputwords):
    result_Vect = zeros(len(result_Vocab))
    for word in inputwords:
        if word in result_Vocab:
            result_Vect[result_Vocab.index(word)] = 1
    return list(result_Vect)
'''
if __name__ =="__main__":
    wordList , wordlabels =createDataSet()
    vocabulary = createVocab(wordList)
    Vect = []
    for inputwords in wordList:
        result_Vect = setWordToVect(vocabulary , inputwords)
        Vect.append(result_Vect)
    print(Vect)
'''

def trainNB(Matrix , labels):
    numwords = len(Matrix)
    pc = sum(labels)/float(numwords)
    numword = len(Matrix[0])
    fz0 = ones(numword)
    fz1 = ones(numword)
    fm0 = 2
    fm1 = 2
    for i in range(numwords):
        if labels[i] ==1:
            fz1 +=Matrix[i]
            fm1 +=sum(Matrix[i])
        else:
            fz0 +=Matrix[i]
            fm0 +=sum(Matrix[i])
    p1 = log(fz1/fm1)
    p0 = log(fz0/fm0)
    return p1,p0,pc

def classifyNB(vect , p0,p1,pc):
    p1_1 = sum(vect*p1)+log(pc)
    p0_0 = sum(vect*p0)+log(1 - pc)
    if p1_1 > p0_0 :
        return 1
    else:
        return 0

def setwordsTovocab(input1):
    reg = re.compile('\\W* ')
    list1 = reg.split(input1)
    return  list1


if __name__ =="__main__":
    wordList , wordlabels =createDataSet()
    vocabulary = createVocab(wordList)
    Vect = []
    for inputwords in wordList:
        result_Vect = setWordToVect(vocabulary , inputwords)
        Vect.append(result_Vect)
    #print(Vect)
    p0V, p1V, pAb = trainNB(Vect, wordlabels)
    #print(p0V)
    testEntry = ['stupid', 'garbage']
    thisDoc = setWordToVect(vocabulary, testEntry)
    if classifyNB(thisDoc, p1V, p0V, pAb):
        print(testEntry, '属于侮辱类')
    else:
        print(testEntry, '属于非侮辱类')

    judge_0 ='是'
    while judge_0 =='是':

        testEntry_0 = input("请输入测试文本：")
        testEntry = setwordsTovocab(testEntry_0)
        #testEntry = ['love', 'my', 'dalmation']
        thisDoc = setWordToVect(vocabulary, testEntry)

        if classifyNB(thisDoc,  p1V,p0V, pAb):
            print(testEntry, '属于侮辱类')
        else:
            print(testEntry, '属于非侮辱类')
        judge_0 = input("是否进行在线判断：")

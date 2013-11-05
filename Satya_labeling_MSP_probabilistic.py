# Coded by Satya Malladi

import os
import math
import networkx as nx
from scipy.stats import norm


# Defining the graph
G1 = nx.Graph()
G1.add_edges_from([(1,2,{'cost':3})])
G1.add_edges_from([(1,3,{'cost':2})])
G1.add_edges_from([(1,4,{'cost':8})])
G1.add_edges_from([(1,5,{'cost':7})])
G1.add_edges_from([(1,6,{'cost':6})])
G1.add_edges_from([(1,7,{'cost':5})])
G1.add_edges_from([(1,8,{'cost':7})])

G1.add_edges_from([(2,3,{'cost':2})])
G1.add_edges_from([(2,4,{'cost':6})])
G1.add_edges_from([(2,5,{'cost':6})])
G1.add_edges_from([(2,6,{'cost':7})])
G1.add_edges_from([(2,7,{'cost':6})])
G1.add_edges_from([(2,8,{'cost':9})])

G1.add_edges_from([(3,4,{'cost':7})])
G1.add_edges_from([(3,5,{'cost':5})])
G1.add_edges_from([(3,6,{'cost':4})])
G1.add_edges_from([(3,7,{'cost':7})])
G1.add_edges_from([(3,8,{'cost':6})])

G1.add_edges_from([(4,5,{'cost':2})])
G1.add_edges_from([(4,6,{'cost':7})])
G1.add_edges_from([(4,7,{'cost':10})])
G1.add_edges_from([(4,8,{'cost':15})])

G1.add_edges_from([(5,6,{'cost':5})])
G1.add_edges_from([(5,7,{'cost':10})])
G1.add_edges_from([(5,8,{'cost':9})])

G1.add_edges_from([(6,7,{'cost':7})])
G1.add_edges_from([(6,8,{'cost':6})])

G1.add_edges_from([(7,8,{'cost':6})])

# TIMES
G1.add_edges_from([(1,2,{'time':100})])
G1.add_edges_from([(1,3,{'time':43})])
G1.add_edges_from([(1,4,{'time':22})])
G1.add_edges_from([(1,5,{'time':32})])
G1.add_edges_from([(1,6,{'time':26})])
G1.add_edges_from([(1,7,{'time':78})])
G1.add_edges_from([(1,8,{'time':28})])

G1.add_edges_from([(2,3,{'time':34})])
G1.add_edges_from([(2,4,{'time':67})])
G1.add_edges_from([(2,5,{'time':57})])
G1.add_edges_from([(2,6,{'time':45})])
G1.add_edges_from([(2,7,{'time':35})])
G1.add_edges_from([(2,8,{'time':65})])

G1.add_edges_from([(3,4,{'time':45})])
G1.add_edges_from([(3,5,{'time':76})])
G1.add_edges_from([(3,6,{'time':86})])
G1.add_edges_from([(3,7,{'time':34})])
G1.add_edges_from([(3,8,{'time':29})])

G1.add_edges_from([(4,5,{'time':56})])
G1.add_edges_from([(4,6,{'time':45})])
G1.add_edges_from([(4,7,{'time':89})])
G1.add_edges_from([(4,8,{'time':100})])

G1.add_edges_from([(5,6,{'time':48})])
G1.add_edges_from([(5,7,{'time':37})])
G1.add_edges_from([(5,8,{'time':64})])

G1.add_edges_from([(6,7,{'time':47})])
G1.add_edges_from([(6,8,{'time':29})])

G1.add_edges_from([(7,8,{'time':38})])

#VARIANCES

G1.add_edges_from([(1,2,{'variance':25})])
G1.add_edges_from([(1,3,{'variance':8})])
G1.add_edges_from([(1,4,{'variance':5})])
G1.add_edges_from([(1,5,{'variance':7})])
G1.add_edges_from([(1,6,{'variance':5})])
G1.add_edges_from([(1,7,{'variance':12})])
G1.add_edges_from([(1,8,{'variance':5})])

G1.add_edges_from([(2,3,{'variance':5})])
G1.add_edges_from([(2,4,{'variance':15})])
G1.add_edges_from([(2,5,{'variance':10})])
G1.add_edges_from([(2,6,{'variance':11})])
G1.add_edges_from([(2,7,{'variance':6})])
G1.add_edges_from([(2,8,{'variance':11})])

G1.add_edges_from([(3,4,{'variance':11})])
G1.add_edges_from([(3,5,{'variance':11})])
G1.add_edges_from([(3,6,{'variance':15})])
G1.add_edges_from([(3,7,{'variance':8})])
G1.add_edges_from([(3,8,{'variance':5})])

G1.add_edges_from([(4,5,{'variance':9})])
G1.add_edges_from([(4,6,{'variance':11})])
G1.add_edges_from([(4,7,{'variance':15})])
G1.add_edges_from([(4,8,{'variance':22})])

G1.add_edges_from([(5,6,{'variance':8})])
G1.add_edges_from([(5,7,{'variance':7})])
G1.add_edges_from([(5,8,{'variance':11})])

G1.add_edges_from([(6,7,{'variance':9})])
G1.add_edges_from([(6,8,{'variance':7})])

G1.add_edges_from([(7,8,{'variance':6})])

p = 0.5
thresh_time = 100

##s=int(raw_input("Enter Source node:"))
##t=int(raw_input("Enter Target node:"))

s =4   # source - can be taken from raw input too.
#t = 2


D=[]  # Non dominated set

for i in range(0,9):
    D.append([])
    D[i].append([i,10000,10000,10000,[]])
D[s][0]=[s,0,0,0,[s]]

# initialized source labels to zeros.
#Node 0 is a dummy node with infinite distance labels and no connectivity.

L = []
L.append([s,0,0,0,[s]]) # maintains a list of labels that  follows FIFO priority rule. 

temp=[]
while L:
    cur=L[0]   # [node#id, cost label, time label, variance]
        #print cur[3]
    del L[0]
    for j in G1.neighbors_iter(cur[0]):  # For Loop XYZ
            #print j
            #trace = []
            temp=[]
            temp=[j,cur[1]+G1[cur[0]][j]['cost'],cur[2]+G1[cur[0]][j]['time'],cur[3]+G1[cur[0]][j]['variance'],[]]
            #print temp[3], trace#print len(D[j])
            dom_list = []
            
            for k in range(0,len(D[j])):
                #print k
                if norm.cdf((thresh_time - temp[2])/math.sqrt(temp[3])) < (1-p):
                    ind=1
                    break
                elif temp[1]>D[j][k][1] and temp[2]>D[j][k][2] and temp[3]>D[j][k][3]:       #exlude dominated labels
                    ind=1
                    break
                elif temp[1]==D[j][k][1] and temp[2]==D[j][k][2] and temp[3]==D[j][k][3]:   # exclude labels already found
                    ind=1
                    break
                elif temp[1]<D[j][k][1] and temp[2]<D[j][k][2] and temp[3] < D[j][k][3]:     
                    ind=0
                    dom_list.append(k)
                   # print len(D[j]), k, dom_list
                else:
                    ind= 0
            if ind ==0:
                #print D[j]
                for k in range(0,len(dom_list)):
                    del D[j][dom_list[k]]
                    for i in range(k+1,len(dom_list)):
                        dom_list[i]-=1
                temp[4]=list(cur[4])
                #print cur[4]
                temp[4].append(j)
                #print cur[4]
                D[j].append(temp)
                L.append(temp)         # For Loop XYZ
print L   
        #print temp[3]
                    
print D



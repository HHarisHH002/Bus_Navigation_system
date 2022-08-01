import random
import sys
from datetime import datetime
import numpy as np

from add_route import Add_route,splay_obj
class Graph_splay:

    def __init__(self, vertices):
        self.V = vertices
        self.lat=[1 for column in range(vertices+1)]
        self.lon=[1 for column in range(vertices+1)]
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.node_list=[0 for column in range(1,vertices)]
        self.avg_splay_insert=0
        self.avg_splay_search=0
    
    def printMST(self, parent,map): 
        splay_insert_time=[]
        for i in range(1, self.V):
            distance=self.graph[i][parent[i]]
            splay_insert_start=datetime.now()
            splay_obj.insert(self.node_list[i],i,[self.lat[parent[i]], self.lon[parent[i]]],[self.lat[i], self.lon[i]])
            splay_insert_stop=datetime.now()
            drw_route.draw_route(self.node_list[i],map,'splay',distance)
            splay_insert_time+=[(splay_insert_stop.microsecond-splay_insert_start.microsecond)]
        splay_insert_avgtime=np.array(splay_insert_time)
        splay_obj.insert(self.V+40,self.V,[self.lat[len(self.lat)-2], self.lon[len(self.lat)-2]],[self.lat[len(self.lat)-1], self.lon[len(self.lat)-1]])
        splay_search_avgtime=np.array(drw_route.splay_search_time)
        
        drw_route.draw_route(self.V+40,map,'splay',distance)
        self.avg_splay_insert=round(np.average(splay_insert_avgtime),3)
        self.avg_splay_search=round(np.average(splay_search_avgtime),3)

    def minKey(self, key, mstSet):
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    def primMST_splay(self,map):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1

        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent,map)

drw_route=Add_route()
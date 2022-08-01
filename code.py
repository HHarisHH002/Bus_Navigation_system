from datetime import datetime

import folium
import csv
from matplotlib import markers
import random
import numpy as np

from prims_avl import Graph_avl,avl_obj
from prims_splay import Graph_splay,splay_obj
points = []
alt_points = []

stopname=["Airport","Postoffice","Abbot School","KK Nagar","Gundur","AnbiNagar","LIC Colony","Gandhi Nagar","Ayyapan Nagar","IT gate1","IT gate2","Sabari Mill","Police Colony","Ashok Nagar","JK Nagar","Sundar Nagar","Simco Meter","LSP Colony","Ennore","GH","FireStation","Market","A1 PoliceStation"]

lat_log_points = np.array(
    list(csv.reader(open("lat_log.csv"), delimiter=","))).astype("float")
latitudes = lat_log_points[0]
longitudes = lat_log_points[1]

alt_lat_log_points = np.array(
    list(csv.reader(open("alt_lat_log.csv"), delimiter=","))).astype("float")
alt_latitudes = alt_lat_log_points[0]
alt_longitudes = alt_lat_log_points[1]

my_map = folium.Map(location=[10.743432, 78.7632113], zoom_start=13)
for i in range(len(latitudes)):
    folium.Marker([latitudes[i], longitudes[i]],
                  popup=f"{stopname[i]}").add_to(my_map)


adj = np.array(
    list(csv.reader(open("adj_matrix.csv"), delimiter=","))).astype("float")

alt_adj = np.array(
    list(csv.reader(open("alt_adj_matrix.csv"), delimiter=","))).astype("float")


def draw_orange_line(map):
    temp=0
    p=[]
    for i in range(len(alt_latitudes)):
        if(alt_latitudes[i] not in latitudes):
            temp+=1
        elif(temp!=0):
            p.append([alt_latitudes[(i-temp-1)],alt_longitudes[(i-temp-1)]])
            p.append([alt_latitudes[(i)],alt_longitudes[(i)]])
            folium.PolyLine(p, color="orange", weight=5, opacity=1).add_to(map)
            p=[]
            temp=0
nodes_ls=[]
node=random.randint(1,len(latitudes)+30)
for i in range(1,len(latitudes)):
    while(True):
        if(node in nodes_ls):
            node = random.randint(1,len(latitudes)+30)
        else:
            nodes_ls.append(node)
            break

alt_nodes_ls=[]
node=random.randint(1,len(alt_latitudes)+30)
for i in range(len(alt_latitudes)):
    while(True):
        if(node in alt_nodes_ls):
            node = random.randint(1,len(alt_latitudes)+30)
        else:
            alt_nodes_ls.append(node)
            break

now = datetime.now()
current_time = int(now.strftime("%I"))
am_pm = now.strftime("%p")

#===========================USING AVL TREE====================================


if(current_time > 3 and current_time < 12 and am_pm == "PM"):
    ga=Graph_avl((len(alt_latitudes)-1))
    ga.graph = alt_adj
    ga.lat=alt_latitudes
    ga.lon=alt_longitudes
    ga.node_list=alt_nodes_ls
    ga.primMST_AVL(my_map)

    draw_orange_line(my_map)

else:
    
    ga=Graph_avl((len(latitudes)-1))
    ga.graph = adj
    ga.lat=latitudes
    ga.lon=longitudes
    ga.node_list=nodes_ls   
    ga.primMST_AVL(my_map)
 
print("\n")
print("============AVL TREE============")
print("\n")
avl_obj.prettyPrint()
print("\n")

print("Using AVL TREE:")
print("Time taken for Inserting:",ga.avg_avl_insert,"microseconds")
print("Time taken for Searching:",ga.avg_avl_search,"microseconds")



#===========================USING SPLAY TREE====================================


if(current_time > 4 and current_time < 12 and am_pm == "PM"):
    g = Graph_splay((len(alt_latitudes)-1)) 
    g.graph = alt_adj
    g.lat=alt_latitudes
    g.lon=alt_longitudes
    g.node_list=alt_nodes_ls
    g.primMST_splay(my_map)

    draw_orange_line(my_map)

else:
    g=Graph_splay((len(latitudes)-1))
    g.graph = adj
    g.lat=latitudes
    g.lon=longitudes
    g.node_list=nodes_ls
    g.primMST_splay(my_map)


print("\n")
print("============SPLAY TREE============")
print("\n")
splay_obj.pretty_print()
print("\n")
print("Using SPLAY TREE:")
print("Time taken for Inserting:",g.avg_splay_insert,"microseconds")
print("Time taken for Searching:",g.avg_splay_search,"microseconds")
print("\n")

my_map.save("my_map.html")


from datetime import datetime
import numpy as np
from splay import SplayTree
from avl import AVLTree
import folium
class Add_route:
    def __init__(self):
        

        self.splay_search_time=[]
        self.avl_search_time=[]

    def draw_route(self,node,map,tree,distance):
        duration=distance/45
        distance_txt = "<h6> <b>Distance : " + "<strong>"+str(round(distance,1))+" Km </strong>" +"</h6></b>"
        duration_txt = "<h6> <b>Duration : " + "<strong>"+str(round(duration*3600,1))+" Mins. </strong>" +"</h6></b>"
        if(tree=='splay'): 
            splay_search_start=datetime.now()
            ns=splay_obj.search_tree(node)
            splay_search_stop=datetime.now()
            folium.PolyLine((ns.point1,ns.point2),tooltip=distance_txt+duration_txt,max_width=300,color="red", weight=2.5, opacity=1).add_to(map)
            self.splay_search_time+=[(splay_search_stop.microsecond-splay_search_start.microsecond)]
            
        else:
            avl_search_start=datetime.now()
            n=avl_obj.searchTree(node)
            avl_search_stop=datetime.now()
            self.avl_search_time+=[(avl_search_stop.microsecond-avl_search_start.microsecond)]
            folium.PolyLine((n.point1,n.point2),tooltip=distance_txt+duration_txt,max_width=300,color="red", weight=2.5, opacity=1).add_to(map)

splay_obj=SplayTree()
avl_obj=AVLTree()
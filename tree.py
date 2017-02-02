#tree structure which is implemented by dictinoary and use (\) for increase readilblity
tree = { \
        'gf_f':'f', \
        'gf_m':'f', \
        'gm_f':'m', \
        'gm_m':'m', \
        'f':'child1,child2', \
        'm':'child1,child2' \
        }

#pydot package is use for graph image shown
import pydot as p

#os package is used for systemcall of os
import os

#subprocess is used for call another process currently may be not used 
import subprocess as sp

#PIL module - Image is used for display the image file
from PIL import Image

#print the path of saved file .
print("your file save at: "+str(os.getcwd()))

#list which is used for remove
del_file = ["family_tree"]

#setup graph
graph = p.Dot(graph_type='graph')

#check parent or not
#st1 - child_name
#st2 - parent_name
def parent(st1,st2):
    try:
        if (st1 in tree[st2]):
            print ("True")
        else:
            print ("False")
    except:
        print ('False')

#check grand_parent or not
#st1 - child_name
#st2 - parent_name        
def grand_parent(st1,st2):

    try:
        st2 = tree[st2]
        if (st1 in tree[st2]):
            print ("True")
        else:
            print ("False")
    except:
        print ('False')

#add edged into graph image and tree structure 
def add_edge(st1,st2):
    tree[st1]=st2
    graph.add_edge(p.Edge(st1,st2))

#save graph image file
def write_graph(st1):
    del_file.append(st1)
    graph.write_png('{}.png'.format(st1))

#delete graph file if it is in del_file list otherwise error
def graph_del_file(st1):
    if st1 in del_file:
        os.remove(st1+".png")
        del_file.remove(st1)
    else:
        print ("you have not permission or not exist ")

#show image file graphically
def show_graph_file(st1):
    try:
        Image.open(st1+".png").show()
        return True
    except:
        print ("file not found or incorrect path")
        return False

#manually add some add edge in image graph file    
graph.add_edge(p.Edge("gf_father","father"))
graph.add_edge(p.Edge("gm_father","father"))
graph.add_edge(p.Edge("gf_mother","mother"))
graph.add_edge(p.Edge("gm_mother","mother"))
graph.add_edge(p.Edge("father","child1"))
graph.add_edge(p.Edge("father","child2"))
graph.add_edge(p.Edge("mother","child1"))
graph.add_edge(p.Edge("mother","child2"))

#choices for operation 
while True:
    try:
        print ('''\n    1.parent
    2.grand_parent
    3.add_edge
    4.write_graph
    5.graph_del_file
    6.show_graph_file
    7.exit\n''')

        print ('enter your choice: ')
        
        val = eval(input())
        if (val == 1):
            st1 = input('input child name: ')
            st2 = input('input parent name (only one): ')
            parent(st1,st2)
        elif (val == 2):
            st1 = input('input child name: ')
            st2 = input('input grand_parent name (only one): ')
            grand_parent(st1,st2)
        elif(val == 3):
            add_edge(input('enter your root node: '),input('enter your child node: '))
        elif(val == 4):
            write_graph(input('enter your image file name: '))
        elif(val == 5):
            graph_del_file(input('enter your image file name: '))
        elif(val == 6):
            #first you should write the file before you open....
            if(show_graph_file(input("enter your image file you want to show: ")) == True):
                print ('your file is opened.')
        
        elif(val == 7):
            break
        else:
            print ('invalid choice.')
    except:
        print ('wrong keystroke')
        

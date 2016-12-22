import uuid

class Node:
    def __init__(self,name):
        self.name = name
        self.id=uuid.uuid4()
        self.inedge=[]
        self.outedge=[]
        self.props={'name':name}

    def __str__(self):
        return (str(self.name) + ' ' + str(self.props))

    def get_id(self):
        return self.id

    def add_properties(self,properties):
        for i in properties:
            self.props[i]=properties[i]

    def print_node(self):
        print('Id:',self.id)
        print('Name:',self.name)
        for i in self.props:
            print(str(i) + ': ' + str(self.props[i]))
        print()


class Edge:
    def __init__(self, label):
      self.label = label
      self.id=uuid.uuid4()
      self.head  = None
      self.tail = None
      self.props={'label':label}

    def __str__(self):
      return (str(self.id) + ': ' + str(self.label))

    def get_id(self):
      return self.id

    def add_properties(self,properties):
      for i in properties:
            self.props[i]=properties[i]

    def print_edge(self):
      print('Id:',self.id)
      print('Label:',self.label)
      print('Head node:',self.head.name)
      print('Tail node:',self.tail.name)
      for i in self.props:
        print(str(i) + ': ' + str(self.props[i]))
      print()
    

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
        self.edge_dict = {}
        self.num_edges = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_node(self, *nodes):
        for node in nodes:
            self.num_vertices+= 1
            self.vert_dict[node.id] = node
        return

    def get_node(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None
    
    def add_edge(self,*edges):
        for edge in edges:
            self.num_edges+=1
            self.edge_dict[edge.id] = edge

    def render_edge_by_nodes(self, edge, head, tail):
        edge.head=head
        edge.tail=tail
        head.outedge.append(edge)
        tail.inedge.append(edge)

    def render_edge_by_names(self,edge, head, tail):
        head_id = self.find_node_by_name(head)
        if(not head_id):
            print("Wrong name of head node given: " + head)
            return
        
        tail_id = self.find_node_by_name(tail)
        if(not tail_id):
            print("Wrong name of tail node given: " + tail)        
            return

        edge.head=self.vert_dict[head_id]
        edge.tail=self.vert_dict[tail_id]
        self.vert_dict[head_id].outedge.append(edge)
        self.vert_dict[tail_id].inedge.append(edge)

    def find_node_by_name(self,name):
        for i in self.vert_dict:
            if(self.vert_dict[i].name == name):
                return i
    
    def delete_node(self,node):
        while(node.inedge):
            self.delete_edge(node.inedge[0])
        while(node.outedge):
            self.delete_edge(node.outedge[0])

        del self.vert_dict[node.id]
        self.num_vertices-=1
        del node

    def delete_edge(self,edge):
        for i in range(len(edge.head.outedge)):
            if(edge.head.outedge[i] == edge):
                edge.head.outedge.pop(i)
                break
              
        for i in range(len(edge.tail.inedge)):
            if(edge.tail.inedge[i] == edge):
                edge.tail.inedge.pop(i)
                break
        
        del self.edge_dict[edge.id]
        self.num_edges-=1
        del edge
    
    def V(self,name):
        for i in self.vert_dict:
            if self.vert_dict[i].name == name:
                return Query(self,self.vert_dict[i])        

    def dump(self):
      print('Nodes in the graph:',self.num_vertices)
      for i in self.vert_dict:
        self.vert_dict[i].print_node()
      print('Edges in the graph:',self.num_edges)
      for i in self.edge_dict:
        self.edge_dict[i].print_edge()

class Query:
    def __init__(self,graph,node):
        self.graph=graph
        self.root = node
        self.result=[node]

    def in_query(self,query=''):
        temp=[]
        if query == '':
            for i in self.result:
                for j in i.inedge:
                    temp.append(j.head)
            self.result=temp
            temp=[]
            return self
                
        for i in self.result:
                for j in i.inedge:
                    if(j.label == query):
                        temp.append(j.head)
        self.result=temp
        temp=[]        
        return self

    def out_query(self,query=''):
        temp=[]
        if query == '':
            for i in self.result:
                for j in i.outedge:
                   temp.append(j.tail)
            self.result=temp
            temp=[]            
            return self

        for i in self.result:
                for j in i.outedge:
                    if(j.label == query):
                        temp.append(j.tail)
        self.result=temp
        temp=[]        
        return self

    def both_query(self,query=''):
        temp=[]
        if query == '':
            for i in self.result:
                for j in i.outedge:
                   temp.append(j.tail)
            
            for i in self.result:
                for j in i.inedge:
                   temp.append(j.head)

            self.result=temp
            temp=[]            
            return self

        for i in self.result:
                for j in i.outedge:
                    if(j.label == query):
                        temp.append(j.tail)
        
        for i in self.result:
                for j in i.inedge:
                    if(j.label == query):
                        temp.append(j.head)

        self.result=temp
        temp=[]        
        return self
            
    def values(self,value):
        for i in self.result:
            print(i.props[value])

    def label(self):
        for i in self.result:
            print(i.props['label'])  
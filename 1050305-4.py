class member():
    def __init__(self):
        self.id = -1
        self.parent = -1   
        self.children = []
        self.layer = 1
    def set_parent(self, p):    # set parent
        self.parent = p
    def add_children(self, c):  # set children
        self.children.append(c)
    def add_layer(self, parent_layer):  # calculate the layer of node
        self.layer = parent_layer + 1
    def modified_connection(self, members):     # modify the layers of each node
        #print self.children
        if len(self.children) != 0:
            
            for child in self.children:
                members[child].add_layer(self.layer)
                members[child].modified_connection(members)
    def cal_connections(self, comp, member):
        if self.parent == comp.id or self.id == comp.parent:    # if one of each is the other parent, the distance is 1
            return 1
        elif self.parent != comp.parent and self.parent != -1 and comp.parent != -1:        # if the parents of two nodes are different and both parents are not root
            return member[self.parent].cal_connections(member[comp.parent], member) + 2     # distance is 2, and move to parent nodes
        elif self.parent != comp.parent and self.parent == -1 and comp.parent != -1:        # if the parent of the other is root, move self node to parent node and distance add 1
            return self.cal_connections(member[comp.parent], member) + 1
        elif self.parent != comp.parent and self.parent != -1 and comp.parent == -1:        # if self parent is root, move the other one and add 1 distance
            return member[self.parent].cal_connections(comp, member) + 1
        elif self.parent == comp.parent and self.parent != -1 and comp.parent != -1:        # if both parents are the same but not root, return distance 2
            return 2
        else:
            return 0
'''
parent is not root

         /          /   \
        P         P1     P2
       / \       /        \  
      /   \     /          \ 
     1     2,  1            2

parent is root

        P         P1     
       / \       /  \      
      /   \     /    P2      
     1     2,  1      \     
                       2    

one of nodes is the other's parent

        1
         \
          \
           2

two nodes meet 

        12    
 
'''    
if __name__ == '__main__':
    
    n = int(input())
    blood = [member() for i in range(0, n)]
    for i in range(0, n):
        blood[i].id = i
    for i in range(0, n-1):             # input data and build the relation
        P, C = input().split(' ')
        P = int(P)
        C = int(C)
        blood[C].id = C
        blood[C].add_layer(blood[P].layer)
        blood[C].modified_connection(blood)
        blood[P].add_children(C)
        blood[C].set_parent(P)
    max_dist = -1
    #for mem in blood:
    #    if max_layer < mem.layer:
    #        max_layer = mem.layer
    #print max_dist
    for mem1 in blood:                  #calculate the distance between each two nodes and compare with the current longest distance
        for mem2 in blood:
            dist = mem1.cal_connections(mem2, blood)
            if dist > max_dist:
                max_dist = dist
            #print mem1.id, mem2.id, dist
    print (max_dist)

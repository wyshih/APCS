class member():
    def __init__(self):
        self.id = -1
        self.parent = -1
        self.children = []
        self.layer = 1
    def set_parent(self, p):
        self.parent = p
    def add_children(self, c):
        self.children.append(c)
    def add_layer(self, parent_layer):
        self.layer = parent_layer + 1
    def modified_connection(self, members):
        #print self.children
        if len(self.children) != 0:
            
            for child in self.children:
                members[child].add_layer(self.layer)
                members[child].modified_connection(members)
    def cal_connections(self, comp, member):
        if self.parent == comp.id or self.id == comp.parent:
            return 1
        elif self.parent != comp.parent and self.parent != -1 and comp.parent != -1:
            return member[self.parent].cal_connections(member[comp.parent], member) + 2
        elif self.parent != comp.parent and self.parent == -1 and comp.parent != -1:
            return self.cal_connections(member[comp.parent], member) + 1
        elif self.parent != comp.parent and self.parent != -1 and comp.parent == -1:
            return member[self.parent].cal_connections(comp, member) + 1
        elif self.parent == comp.parent and self.parent != -1 and comp.parent != -1:
            return 2
        else:
            return 0
    
if __name__ == '__main__':
    
    n = int(input())
    blood = [member() for i in range(0, n)]
    for i in range(0, n):
        blood[i].id = i
    for i in range(0, n-1):
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
    for mem1 in blood:
        for mem2 in blood:
            dist = mem1.cal_connections(mem2, blood)
            if dist > max_dist:
                max_dist = dist
            #print mem1.id, mem2.id, dist
    print (max_dist)

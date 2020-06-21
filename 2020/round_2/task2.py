class Node:
    def __init__(self):
        self.neighbor = []
        self.time = None
        self.order = None
        self.edge = []
        self.updated = False

    def add_neighbor(self, node_id):
        self.neighbor.append(node_id)


class Problem:

    def __init__(self, D, C, F):
        self.graph = [Node() for c in range(C)]
        self.D = D
        self.build_graph(F)
        

    def build_graph(self, F):
        count = 0
        for i, conn in enumerate(self.D):
            U, V = conn
            self.graph[U].add_neighbor(V)
            self.graph[V].add_neighbor(U)
            self.graph[U].edge.append(i)
            self.graph[V].edge.append(i)
        
        time_sorted = []
        order_sorted = []
        for i, f in enumerate(F):
            if f <= 0:
                self.graph[i].order = -f
                order_sorted.append(i)
                count += 1
            else:
                self.graph[i].time = f
                time_sorted.append(i)

        time_sorted = sorted(time_sorted)
        order_sorted = sorted(order_sorted)

        self.graph[0].time = 0
        self.graph[0].updated = True
        
        count = 0
        pre = -1
        for i in order_sorted:
            n_empty = self.graph[i].order-pre-1
            pre_j = 0
            for idx, j in enumerate(time_sorted[count:n_empty+count]):
                if self.graph[j].time > self.graph[pre_j].time:
                    self.graph[j].order = pre + idx + 1
                else: self.graph[j].order = self.graph[pre_j].order
                pre_j = j
            pre = self.graph[i].order
            count += n_empty

        
        # for i in self.graph:
        #     print(i.order, i.time)



    def solve(self):
        sorted_order = sorted(range(len(self.graph)), key=lambda k: self.graph[k].order)
        res = [0]*len(self.D)
        
        pre_order = 1
        same_order = []
        level = []
        for i in sorted_order[1:]:
            if self.graph[i].order == pre_order:
                level.append(i)
            else:
                same_order.append(level)
                level = [i]
                pre_order = self.graph[i].order
                
        else:
            same_order.append(level)

        for level in same_order:
            min_time = 0
            for i in level:
                if self.graph[i].time is not None:
                    min_time = max(min_time, self.graph[i].time)
            if min_time == 0:
                for i in sorted_order[:self.graph[level[0]].order]:
                    # print('.', node.time)
                    min_time = max(min_time, self.graph[i].time)

                min_time += 1

            for i in level:
                self.graph[i].time = min_time
                self.graph[i].updated = True
                for idx_, j in enumerate(self.graph[i].edge):
                    if self.graph[self.graph[i].neighbor[idx_]].updated:
                        res[j] = self.graph[i].time - self.graph[self.graph[i].neighbor[idx_]].time
                        res[j] = max(1, res[j])

        return res




if __name__ == "__main__":

    n_case = int(input())
    for i in range(n_case):
        C, n_D = list(map(int, input().split()))
        F = [0] + list(map(int, input().split()))
        D = []
        for d in range(n_D):
            D.append(list(map(int, input().split())))
        D = [(u-1, v-1) for u,v in D]

        task = Problem(D, C, F)
        print('Case #{}:'.format(i+1), ' '.join((map(str, task.solve()))))

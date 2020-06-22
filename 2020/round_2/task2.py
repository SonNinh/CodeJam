class Node:
    def __init__(self):
        self.neighbor = []
        self.time = None
        self.order = None

    def add_neighbor(self, node_id):
        self.neighbor.append(node_id)


class Problem:

    def __init__(self, D, C, F):
        self.graph = [Node() for c in range(C)]
        self.D = D
        self.build_graph(F)
        

    def build_graph(self, F):
        for i, conn in enumerate(self.D):
            U, V = conn
            self.graph[U].add_neighbor(V)
            self.graph[V].add_neighbor(U)
        
        time_ = []
        order_ = []
        for i, f in enumerate(F):
            if f <= 0:
                self.graph[i].order = -f
                order_.append(i)
            else:
                self.graph[i].time = f
                time_.append(i)

        time_sorted = sorted(time_, key=lambda k: self.graph[k].time)
        order_sorted = sorted(order_, key=lambda k: self.graph[k].order)

        self.graph[0].time = 0
        
        N = 0
        j = 0
        last_time = 0
        last_order = 0
        for i in order_sorted:
            changed = False
            while self.graph[i].order > N:
                N += 1
                last_time = self.graph[time_sorted[j]].time
                j += 1
                changed = True
            if changed or last_order < self.graph[i].order:
                last_time += 1
            self.graph[i].time = last_time
            last_order = self.graph[i].order
            N += 1
        
        # for i in self.graph:
        #     print(i.order, i.time)

    def solve(self):
        res = []
        for u, v in self.D:
            delta = abs(self.graph[u].time - self.graph[v].time)
            res.append(max(1, delta))
        
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

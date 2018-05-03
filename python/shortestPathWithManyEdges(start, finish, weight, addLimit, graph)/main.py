class Element(object):

    def __init__(self, weight, added_edges, prev_node_list, route_count):
        self.weight = weight
        self.added_edges = added_edges
        self.prev_node_list = []
        for i in prev_node_list:
            self.prev_node_list.append(i)
        self.route_count = route_count

    def __eq__(self, other):
        return self.weight == other.weight and self.added_edges == other.added_edges

    def __gt__(self, other):
        if self.weight > other.weight:
            return True
        elif self.weight == other.weight:
            return self.added_edges > other.added_edges
        return False

    def __str__(self):
        return '(%3s,%3s,%3s,%3s)' % (self.weight, self.added_edges, ':'.join(str(i) for i in self.prev_node_list), self.route_count)

    def inc_route(self):
        self.route_count += 1


    def add(self, other):
        # print self, other
        res = Element(
            self.weight + other.weight,
            self.added_edges + other.added_edges,
            [self.route_count],
            self.route_count
        )
        # print 'returning', res
        return res

    @staticmethod
    def get_absolute_min(arr):
        res = Element(float('inf'), 0, [0], 0)
        for i in arr:
            print i
            if res > i:
                res = Element(i.weight, i.added_edges, i.prev_node_list, i.route_count)
            elif res == i:
                print 'adding...'
                res.inc_route()

        return res

    @staticmethod
    def get_min_of_each_level(arr):
        res = {}
        for i in arr:
            if i.added_edges not in res:
                res[i.added_edges] = Element(float('inf'), 0, [0], 0)

            if res[i.added_edges] > i:
                res[i.added_edges] = Element(i.weight, i.added_edges, i.prev_node_list, i.route_count)
            elif res[i.added_edges] == i:
                res[i.added_edges].inc_route()

        return res


def print_graph(graph):
    for i in range(len(graph[0])):
        print ' '.join('%s' % (j,) for j in graph[i])
    print

def arrange_correction(start, finish, graph):
    n = len(graph[0])
    i = start - 1
    j = finish - 1

    for row in range(n):
        graph[row][0], graph[row][i], graph[row][j], graph[row][n-1] = graph[row][i], graph[row][0], graph[row][n-1], graph[row][j]


    # graph[i][0], graph[j][0] = graph[j][0], graph[i][0]
    # graph[i][-1], graph[j][-1] = graph[j][-1], graph[i][-1]

    for col in [0, -1]:
        for row in range(n):
            graph[col][row] = graph[row][col]

def shortestPathWithManyEdges(start, finish, weight, addLimit, graph):
    arrange_correction(start, finish, graph)
    # print_graph(graph)
    start = 0
    finish = len(graph[0])
    A = [[Element(float('inf'), 0, [], 0) for j in range(finish)] for i in range(finish)]
    for i in range(1, finish):
        w = get_m_ij(weight, addLimit == 0, graph, 0, i)
        A[0][i] = w
    # print_graph(A)
    for i in range(1, finish):
        mins = Element.get_min_of_each_level([A[j][i] for j in range(finish)])
        for _, m in mins.items():
            print m
        for j in range(i+1, finish):
            min_value = Element(float('inf'), 0, [0], 0)

            for _, m in mins.items():
                e = m.add(get_m_ij(weight, m.added_edges >= addLimit, graph, i, j))
                if min_value > e:
                    min_value = e
            A[i][j] = min_value
        print_graph(A)

    res = Element.get_absolute_min([A[j][finish - 1] for j in range(finish)])
    print res
    return [res.weight, res.route_count]

def get_m_ij(weight, limit_reached, graph, i, j):
    if graph[i][j] != 0:
        return Element(graph[i][j], 0, [i], 1)
    else:
        return Element(weight, 1, [i], 1) if not limit_reached else Element(float('inf'), 0, [i], 0)

if __name__ == '__main__':
    start     = 1
    finish    = 4
    weight    = 4
    add_limit = 1
    graph = [[0,2,2,0],
 [2,0,0,2],
 [2,0,0,2],
 [0,2,2,0]]
    print shortestPathWithManyEdges(start, finish, weight, add_limit, graph)

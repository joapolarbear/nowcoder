import bisect

INFINIT = 1e6
DEBUG = False
def debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

def main():
    N = int(input())
    graph = {}
    for _ in range(N):
        s = input()
        node_id = int(s.split(":")[0])
        connect_to_num = int(s.split("(")[1].split(")")[0])
        if connect_to_num == 0:
            graph[node_id] = []
        else:
            graph[node_id] = list(map(int, s.split(")")[1].strip().split(" ")))
    debug(graph)
    
    sorted_nodes = sorted(graph.keys(), key=lambda x: len(graph[x]), reverse=True)
    
    all_nodes = list(range(N))
    rst = 0
    for node_id in sorted_nodes:
        if node_id in all_nodes:
            rst += 1
            all_nodes.remove(node_id)
            for child in graph[node_id]:
                if child in all_nodes:
                    all_nodes.remove(child)
    print(rst)
    
    # cached = [None for _ in range(N)]
    
    # def find_smallest(root):
    #     if cached[root] is not None:
    #         return cached[root]
        
    #     smallest = N
    #     # root is selected
    #     rst = 1
    #     for child in graph[root]:
    #         for cchild in graph[child]:
    #             rst += find_smallest(cchild)
    #     smallest = min(smallest, rst)  
        
    #     # root is NOT selected    
    #     case2 = 
        
    # find_smallest(0)

while True:
    try:
        main()
    except EOFError:
        break
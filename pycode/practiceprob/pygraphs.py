gdict = {
    "A": ["B", "C"],
    "B": ["C", "D"],
    "C": ["D"],
    'D': ['C'],
    'E': ['F'],
    'F': ['C']
}


def node_path(start, end, path=[]):
    path.append(start)
    if end in gdict[start]:
        return path.append(end)
    elif not end in gdict[node]:
        
    else:
        for node in gdict[start]:
            node_path(node, end)

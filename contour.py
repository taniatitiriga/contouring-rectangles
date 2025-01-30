class SegmentTreeNode:
    def __init__(self, B, E):
        self.B = B          # Begin of interval
        self.E = E          # End of interval
        self.left = None    # Left child
        self.right = None   # Right child
        self.C = 0          # Coverage count
        self.status = 'empty'  # 'full', 'partial', 'empty'

    def __str__(self):
        return f"({self.B}, {self.E}), C = {self.C}, status = {self.status}"

class SegmentTree:
    # def __init__(self, y_coords):
    #     self.ys = sorted(y_coords)
    def __init__(self, E):
        self.root = self.build_tree(1, E)
        self.stack = []

    def build_tree(self, start, end):
        node = SegmentTreeNode(start, end)
        if end - start > 1:
            mid = (start + end) // 2
            node.left = self.build_tree(start, mid)
            node.right = self.build_tree(mid, end)
        return node

    def update_status_insert(self, node):
        if node == None:
            return
        node.status = "full"
        node.C += 1
        self.update_status_insert(node.left)
        self.update_status_insert(node.right)

    def update_status_delete(self, node):
        if node == None:
            return
        node.C -= 1
        self.update_status_delete(node.left)
        self.update_status_delete(node.right)

        if node.left == None and node.right == None:
            node.status = "empty"
        else:
            if node.left.status == "empty" and node.right.status == "empty":
                node.status = "empty"


    def compl(self, node):
        top = None
        if len(self.stack) > 0:
            top = self.stack[-1]
        if node.status == "empty":
            if node.B == top:
                self.stack.pop()
            else:
                self.stack.append(node.B)
            self.stack.append(node.E)
        else:
            if node.status == "partial":
                self.compl(node.left)
                self.compl(node.right)

    def insert(self, b, e, node):
        if node == None:
            return
        if (b <= node.B) and (node.E <= e):
            self.compl(node)
            # node.C += 1
            self.update_status_insert(node)
        else:
            if b < (node.B + node.E) // 2:
                self.insert(b, e, node.left)
            if (node.B + node.E) // 2 < e:
                self.insert(b, e, node.right)
        
        if node.left == None and node.right == None:
            if node.C == 0:
                node.status = 'empty'
        else:
            if node.left.status == node.right.status and node.left.status == "empty":
                node.status = 'empty'
            else:
                node.status = 'partial'

    def delete(self, b, e, node):
        if node == None:
            return
        if (b <= node.B) and (node.E <= e):
            node.C -= 1
            if b < (node.B + node.E) // 2:
                self.delete(b, e, node.left)
            if (node.B + node.E) // 2 < e:
                self.delete(b, e, node.right)
            if node.C > 0:
                node.status = "full"
            if node.left == None and node.right == None:
                if node.C == 0:
                    node.status = 'empty'
            else:
                if node.left.status == node.right.status and node.left.status == "empty":
                    node.status = 'empty'
                else:
                    node.status = 'partial'

            self.compl(node)
        else:
            if b < (node.B + node.E) // 2:
                self.delete(b, e, node.left)
            if (node.B + node.E) // 2 < e:
                self.delete(b, e, node.right)


# changes (x1, y1, x2, y2) to (l, r, b, t)
def change_coordinates(rectangles):
    new_rectangles = []
    for x1, y1, x2 ,y2 in rectangles:
        if x1 < x2:
            l = x1
            r = x2
        else:
            l = x2
            r = x1

        if y1 < y2:
            b = y1
            t = y2
        else:
            b = y2
            t = y1

        new_rectangles.append((l, r, b, t))
    return new_rectangles

def normalize_coordinates(rectangles):
    y_coords = set()
    for l, r, b, t in rectangles:
        y_coords.add(b)
        y_coords.add(t)
    y_list = sorted(y_coords)
    y_rank = {y: i+1 for i, y in enumerate(y_list)}
    normalized = []
    for l, r, b, t in rectangles:
        nb = y_rank[b]
        nt = y_rank[t]
        normalized.append((l, r, nb, nt))
    return normalized, y_list

def create_events(rectangles):
    events = []
    for l, r, b, t in rectangles:
        events.append((l, 'left', b, t))
        events.append((r, 'right', b, t))
    events.sort(key=lambda x: (x[0], 0 if x[1] == 'left' else 1, x[2]))
    return events

def process_events(events, y_list):
    vertical_edges = []
    st = SegmentTree(len(y_list))
    current_x = None
    # db = []
    for event in events:
        x, typ, b, t = event
        if current_x != x:
            if st.stack:
                vertical_edges.extend([(current_x, st.stack[i], st.stack[i+1]) for i in range(0, len(st.stack), 2)])
                # db.extend(st.stack)
                st.stack = []
            current_x = x
        
        if typ == 'left':
            st.insert(b, t, st.root)
        else:
            st.delete(b, t, st.root)
    
    if st.stack:
        vertical_edges.extend([(current_x, st.stack[i], st.stack[i+1]) for i in range(0, len(st.stack), 2)])
        # db.extend(st.stack)
    
    vertical_edges.sort(key=lambda e: (e[0], e[1]))
    ve = [vertical_edges[0]]
    for i in range(1, len(vertical_edges)):
        if ve[-1][0] == vertical_edges[i][0]:
            if (vertical_edges[i][1] <= ve[-1][1]) and (ve[-1][2] <= vertical_edges[i][2]):
                ve.pop()
            elif (vertical_edges[i][1] >= ve[-1][1]) and (ve[-1][2] >= vertical_edges[i][2]):
                continue
        ve.append(vertical_edges[i])

    # print(db)
    return ve
    # return vertical_edges

def build_contour(vertical_edges, y_list):
    v_edges = []
    for x, b, t in vertical_edges:
        v_edges.append((b, x, 'down'))
        v_edges.append((t, x, 'up'))
    
    v_edges.sort(key=lambda e: (e[0], e[1]))
    contour = []
    for i in range(0, len(v_edges), 2):
        y = v_edges[i][0]
        x1 = v_edges[i][1]
        x2 = v_edges[i+1][1]
        contour.append(((x1, y_list[y - 1]), (x2, y_list[y - 1])))

    for x, b, t in vertical_edges:
        contour.append(((x, y_list[b - 1]), (x, y_list[t - 1])))
    
    return contour

def find_contour(rectangles):
    rectangles = change_coordinates(rectangles)
    norm_rects, y_list = normalize_coordinates(rectangles)
    events = create_events(norm_rects)
    print(events)
    vertical_edges = process_events(events, y_list)
    print(vertical_edges)
    contour = build_contour(vertical_edges, y_list)
    return contour

# rectangles = [
#     (3, 6, 9, 3),
#     (5, 5, 7, 1),
#     (8, 5, 11, 3),
#     (1, 3, 3, 1)
# ]

# rectangles = [
#     (4, 4, 8, 0),
#     (1, 8, 8, 2)
# ]

# rectangles = [
#     (4, 4, 8, 0),
#     (1, 8, 8, 2),
#     (6, 6, 9, 9)
# ]

# rectangles = [
#     (2, 1, 8, 2.5),
#     (1, 2, 3, 9),
#     (1, 5, 7, 7)
# ]

# print(find_contour(rectangles))

# rectangles = change_coordinates(rectangles)
# print(rectangles)
# normal_coordinates, y_list = normalize_coordinates(rectangles)
# print(normal_coordinates, y_list)
# events = create_events(normal_coordinates)
# print(events)
# vertical = process_events(events, y_list)
# print(vertical)
# print(build_contour(vertical, y_list))

# st = SegmentTree(len(y_list))
# st.insert(events[0][2], events[0][3], st.root)

# st = process_events(events, y_list)

# print(st.root)
# print(st.root.left)
# print(st.root.right)
# print(st.root.right.right)
# print(st.stack)
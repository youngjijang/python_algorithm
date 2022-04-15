
class Node :
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree :
    def __init__(self) -> None:
        self.root = None

    ## 삽입
    def insert(self,data) :
        self.root = self._insert_value(self.root,data)
        return self.root is not None # None이 아니면 

    def _insert_value(self,node,data) :
        if node is None : #node가 비었으면 삽입
          node = Node(data)
        else:
            if data <= node.data : 
                node.left = self._insert_value(node.left, data)
            else :
                node.right = self._insert_value(node.right, data)

        return node

    ##찾기
    def find(self, key) :
        return self._find_value(self.root, key)

    def _find_value(self, root, key) :
        if root is None or root.data == key :
            return root is not None
        elif key < root.data:
            return self._find_value(root.left,key)
        else :
            return self._find_value(root.right, key)

    ##삭제
    def delete(self,key) :
        self.root,deleted = self._delete_value(self.root,key)
        return deleted

    def _delete_value(self,node, key):
        if node is None :
            return node,False
        
        deleted = False
        if key == node.data : 
            deleted = True
            if node.left and node.right : # 해당 노드에 2개의 자식이 있을경우
                #해당 노드 다음으로 큰 수를 가져온다.
                parent, child = node, node.right #큰 수 중에
                while child.left is not None :    
                    parent,child = child,child.left # 가장 작은 수
                child.left = node.left

                if parent != node :
                    parent.left = child.right
                    child.right = node.right
                node = child

            elif node.left or node.right : # 해당 노드에 1개의 자식이 있을경우
                node = node.left or node.right
            else:
                node = None
        
        elif key < node.data :
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)

        return node,deleted



    
array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]
bst = BinarySearchTree()
for x in array:
    bst.insert(x)
# Find
print(bst.find(15)) # True
print(bst.find(17)) # False
# Delete
print(bst.delete(55)) # True
print(bst.delete(14)) # True
print(bst.delete(11)) # False

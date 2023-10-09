# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#这道题得看代码随想录嗷
#一共有三种状态：0无覆盖，1有摄像头，2有覆盖
#贪心思路是让每个叶子结点的父节点都装上摄像头，然后从下往上遍历，每隔两个装一个摄像头
#由于从下往上遍历，就要用后序遍历（左右中）
#遇到叶子节点后面的空结点应该返回哪种状态呢？
#如果返回有摄像头，叶子就是有覆盖状态，摄像头就会装在叶子的父亲的父亲
#如果返回无覆盖，则摄像头就会装在叶子上，就浪费了
#所以应该返回有覆盖，这样叶子的父亲就会装摄像头
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.camera = 0
        #如果从下至上遍历完后，根节点没有被覆盖，即self.traversal(root) 返回 0，则要在根节点放摄像头
        if self.traversal(root) == 0:
            self.camera += 1
        #注意上面这个if语句，其实已经把self.traversal(root)跑了一遍了，如果再单独搞一个self.traversal(root)的话，相当于把self.camera加多了！！！
        return self.camera
    
    def traversal(self, cur):
        if not cur:  #如果遇到叶子结点之后的空节点，就要返回有覆盖2，让叶子节点的父节点装上摄像头
            return 2
        left = self.traversal(cur.left)
        right = self.traversal(cur.right)

        #如果两个子节点都有覆盖，则父节点应该是无覆盖，让父节点的父节点装上摄像头
        if left == 2 and right == 2:
            return 0
        #如果其中一个子节点没有覆盖，则父节点应该装上摄像头
        elif left == 0 or right == 0:
            self.camera += 1
            return 1
        #如果其中一个子节点装有摄像头，则父节点应该有覆盖，让父节点的父亲的父亲装摄像头就行
        elif left == 1 or right == 1:
            return 2

        

        
        

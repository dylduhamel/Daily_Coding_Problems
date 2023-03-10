# Important
# Now, is_locked is still O(1), but lock and unlock are both O(h) instead of O(m + h).

class LockingBinaryTreeNode(object):
    def __init__(self, val=None, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.is_locked = False
        self.locked_descendants_count = 0
    
    def _can_lock_or_unlock(self):
        if self.locked_descendants_count > 0:
            return False
        
        cur = self.parent
        while cur:
            if cur.is_locked:
                return False
            cur = cur.parent
        return True
    
    def is_locked(self):
        return self.is_locked
    
    def lock(self):
        if self.is_locked:
            return False # node already locked
        
        if not self._can_lock_or_unlock():
            return False

        # Not locked, so update is_locked and increment count of all ancestors
        self.is_locked = True

        cur = self.parent
        while cur:
            self.locked_descendants_count = 1
            cur = cur.parent
        return True
    
    def unlock(self):
        if not self.is_locked:
            return False # node already unlocked

        if not self._can_lock_or_unlock():
            return False

        self.is_locked = False

        # Update count in all ancestors
        cur = self.parent
        while cur:
            cur.locked_descendants_count -= 1
            cur = cur.parent
        return True
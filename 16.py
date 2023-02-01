# * IMPORTANT
class Log(object):
    def __init__(self, n):
        # N is the size of the N orders
        self.log = []
        self.n = n
        self.ctr = 0

    # Record the order id
    def record(self, order_id):
        if len(self.log) == self.n:
            self.log[self.ctr] = order_id
        else:
            self.log.append(order_id)

        # If we just filled in the last element, then this equal 0
        self.ctr = (self.ctr + 1) % self.n

    # Get the last ith element
    def get_last(self, i):
        return self.log[self.ctr - i]

class Node:
    def __init__(self, val, nextNode=None):
        self.val = val
        self.nextNode = nextNode

def climbingLeaderboard(ranked, player):
    # Computing LL
    head = Node(ranked[0])
    temp = head
    playerRank = []

    for i in range(1, len(ranked)):
        temp.next = Node(ranked[i])
        temp = temp.next

    for playerScore in player:
        playerRank.append(computeRank(head, playerScore))

        return playerRank


def computeRank(node, value):
    rank = 1
    prev = float("inf")

    while node != None:
        if node.val == value:
            print(value)
            return rank
        elif node.val == prev:
            node = node.nextNode
        else:
            rank += 1
            prev = node.val
            node = node.nextNode

if __name__ == '__main__':
    ranked = [100, 100, 50, 40, 40, 20, 10]
    player = [5, 25, 50, 120]

    print(climbingLeaderboard(ranked, player))

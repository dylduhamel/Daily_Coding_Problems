from random import randint

def shuffle() -> list[int]:
    cards = [card for card in range(1,53)]
    for i in range(52):
        swapPos = randIntRange(52)-1
        cards[i], cards[swapPos] = cards[swapPos], cards[i]
    return cards

def randIntRange(k: int) -> int:
    return randint(1, k)

if __name__ == '__main__':
    print(shuffle())
    print(shuffle())

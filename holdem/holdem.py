# 과정 1: 필요한 모듈을 미리 다 불러오고 함수를 만든다.
import random

def CardRank(cards):
    paircount = 0
    for n1 in range(0, 4):
        for n2 in range(n1+1, 5):
            if cards[n1][1] == cards[n2][1] :
                paircount = paircount+1
    num = [cards[k][1] for k in range(5)]
    num.sort()
    straightox = False
    if paircount == 0:
        if (num[4]-num[0]) == 4:
            straightox = True
        if num[0] == 1 and num[1] == 10:
            straightox = True
    suit = [cards[k][0] for k in range(5)]
    suit.sort()
    flushox = False
    if suit[0] == suit[4]:
        flushox = True
    if straightox and flushox:
        rank = 1
    elif paircount == 6:
        rank = 2
    elif paircount == 4:
        rank = 3
    elif flushox:
        rank = 4
    elif straightox:
        rank = 5
    elif paircount == 3:
        rank = 6
    elif paircount == 2:
        rank = 7
    elif paircount == 1:
        rank = 8
    else:
        rank = 9
    return rank
        
def DisplayResult(cards_A, rank_A, cards_B, rank_B):
    print(rank_A, cards_A)
    print(rank_B, cards_B)
    if rank_A < rank_B:
        print("선수 A가 이겼습니다.")
    elif rank_B < rank_A:
        print("선수 B가 이겼습니다.")
    else:
        print("비겼습니다.")
        

# 과정 2: 카드 한 팩을 만든다.
deck = [(suit, k) for  suit in ["s", "h", "d", "c"] for k in range(1,14)]

# 과정 3: 카드를 섞는다.
random.shuffle(deck)

# 과정 4: 선수 A에게 카드 다섯장을 선수 B에게 카드 다섯장을 섞은 카드 맨 앞부터 뺴서 준다.
cards_A = [ deck[k] for k in range(0, 5)]
cards_B = [ deck[k] for k in range(5, 10)]

# 과정 5: 각 선수가 가진 패가 뭔지 알아본다.
rank_A = CardRank(cards_A)
rank_B = CardRank(cards_B)

# 과정 6: 결과 출력력하기
DisplayResult(cards_A, rank_A, cards_B, rank_B)
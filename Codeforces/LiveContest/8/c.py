# Educational Codeforces Round 178 (Rated for Div. 2)

def beats(card1: int, card2: int, n: int) -> bool:
    if card1 == 1 and card2 == n:
        return True
    if card2 == 1 and card1 == n:
        return False
    return card1 > card2

def determine_winner(n: int, cards: str) -> str:
    alice_cards = {i + 1 for i in range(n) if cards[i] == 'A'}
    bob_cards = {i + 1 for i in range(n) if cards[i] == 'B'}

    if 1 in alice_cards and n in bob_cards:
        if all(any(not beats(a, b, n) for b in bob_cards) for a in alice_cards):
            return "Bob"
        return "Alice"

    if 1 in bob_cards and n in alice_cards:
        if any(a != n and all(b == 1 or beats(a, b, n) for b in bob_cards) for a in alice_cards):
            return "Alice"
        return "Bob"

    if n in alice_cards:
        return "Alice"
    if n in bob_cards:
        return "Bob"

    return "Alice" if max(alice_cards) > max(bob_cards) else "Bob"

t = int(input())
for _ in range(t):
    n = int(input())
    cards = input().strip()
    print(determine_winner(n, cards))


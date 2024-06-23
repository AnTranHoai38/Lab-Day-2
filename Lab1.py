S = "BANANA"
vowels = "AIUEO"
score1 = 0
score2 = 0
for i in range(len(S)):
    if S[i] not in vowels:
        score1 += (len(S) - i)
    else :
        score2 += (len(S) - i)
if score1 > score2:
    print("An", score1)
elif score1 <score2:
    print("Minh", score2)
else:
    print("Draw")


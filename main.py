def eng_yuqori_ball(royxat):
    natija = []
    for talaba in royxat:
        ism = talaba[0]
        ball = max(talaba[1:])
        natija.append((ism, ball))
    return natija

royxat = [("Ali", 80, 90, 70), ("Vali", 90, 80, 95), ("Jalol", 70, 85, 90)]
print(eng_yuqori_ball(royxat))

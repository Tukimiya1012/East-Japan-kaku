while True:
    sereki = input("西暦を入力してください。\n")
    
    if sereki == str(1927):
        print("革命元年")

    if sereki == "end":
        break

    if int(sereki) < 1927:
        zenreki = 1927 - int(sereki)
        print("前歴" + str(zenreki) + "年")

    else:
        kakume = int(sereki) - 1926
        print("革命" + str(kakume) + "年")
 
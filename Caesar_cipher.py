import string
komoji = list(string.ascii_lowercase)
text, key = input('ここに文字と暗号鍵を入力してください例:abc 3').split()
for i in text:
    if i in komoji:
        position = komoji.index(i)
        print(komoji[(position + int(key)) % len(komoji)], end='')
    else:
        print(i, end='')

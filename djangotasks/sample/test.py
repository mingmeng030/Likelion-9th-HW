text = """케로 케로 케로 케로 힘차게 케로 케로 케로 나가자 
우리 앞에 있는 모든 시련들 겁낼 필요 없다
케로로 소대 오늘도 출동을 하네
큰맘 먹고 세차하면 비오고 소풍가면 소나기
급하게 탄 버스 방향 틀리고
건널목에 가면 항상 내 앞에서 빨간불
케로 케로 케로 케로 힘차게
케로 케로 케로 나가자
우리 앞에 있는 모든 시련들 겁낼 필요 없다
다섯 개구리 모여서 공명을 하네
힘들어도 밝은 얼굴 웃어봐 우린 내일이 있어
세상 일이 힘이 들고 지쳐도
우리 모두 모여 하나 되면 해낼 수 있어
이 세상에 두려운 건 없어 너와 함께면!"""

textlist = text.split()
print(textlist)

wordDict = {}

for word in textlist:
    if word in wordDict:
        wordDict[word] += 1
    else : 
        wordDict[word] = 1

print(wordDict)


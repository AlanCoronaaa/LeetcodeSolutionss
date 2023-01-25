def solution(pattern, source):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    c = 0
    flag = False
    for i in range(len(source)-len(pattern)+1):
        subs = source[i:i+len(pattern)]
        for j in range(len(pattern)):
            if len(subs) == len(pattern):
                if (pattern[j] == "0" and subs[j] in vowels) or (pattern[j] == "1" and subs[j] not in vowels):
                    flag = True
                else:
                    flag = False
                    break
        if flag:
            c += 1
    return c


def alternate_string(word1,aord2):
    result=""

    n=min(len(word1),len(word2))
    for i in range(n):
        result += word1[i]
        result += word2[i]
    
    result += word1[n:]
    result += word2[n:]

    return result


word1="abc"
word2="pqr"
print(alternate_string(word1,word2))
def solutions(s):
    word = s.split()
    
    #双指针法倒序
    left,right = 0, len(word)-1
    while left < right:
        word[left], word[right] = word[right], word[left]
        left += 1
        right -= 1
    return ' '.join(letter for letter in word)

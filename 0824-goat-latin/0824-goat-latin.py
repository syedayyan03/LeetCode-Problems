class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']

        words = sentence.split()

        index = 1
        ans = []

        for word in words:
            if word[0].lower() in vowels:
                newword = word + 'ma' + (index * 'a')
                ans.append(newword)
            else:
                newword = word[1:len(word)] + word[0] + 'ma' + (index * 'a')
                ans.append(newword)
            index += 1
        
        result = " ".join(ans)
        
        return result

        
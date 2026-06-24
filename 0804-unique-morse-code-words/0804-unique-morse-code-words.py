class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        trans = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        wordsMap = set()

        for word in words:
            maps = ""
            for char in word:
                charMapVal = ord(char) - ord('a') 
                maps += trans[charMapVal]
            wordsMap.add(maps)
        
        return len(wordsMap)
        
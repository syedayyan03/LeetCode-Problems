class Solution:
    def minSteps(self, s: str, t: str) -> int:
        tdict = {}
        sdict = {}

        for i in range(len(s)):
            if s[i] not in sdict:
                sdict[s[i]] = 1
            else:
                sdict[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in tdict:
                tdict[t[i]] = 1
            else:
                tdict[t[i]] += 1

        count = 0
        
        for key, value in tdict.items():
            if key not in sdict:
                count += tdict[key]
            elif tdict[key] > sdict[key]:
                count +=  tdict[key] - sdict[key]
        
        return count 
        

        
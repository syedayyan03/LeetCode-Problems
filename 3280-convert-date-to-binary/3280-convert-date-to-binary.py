class Solution:
    def convertDateToBinary(self, date: str) -> str:
        datearr = date.split("-")
        ans = []
        year = int(datearr[0])
        month = int(datearr[1])
        day = int(datearr[2])
        dateyear = ""
        datemonth = ""
        dateday = ""

        while(year >= 1):
            rem = year % 2
            year //= 2
            dateyear += str(rem)
        dateyear = dateyear[::-1]
        
        while(month >= 1):
            rem = month % 2
            month //= 2
            datemonth += str(rem)
        datemonth = datemonth[::-1]
        
        while(day >= 1):
            rem = day % 2
            day //= 2
            dateday += str(rem)
        dateday = dateday[::-1]

        ans = f"{dateyear}-{datemonth}-{dateday}"
        return ans

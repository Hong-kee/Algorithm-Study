class Solution:
    def intToRoman(self, num: int) -> str:
        
        dic = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        dic_l = list(dic)
        result = ""

        for n in (1000, 100, 10, 1):
            m = num // n
            
        
            if m < 4:
                result += dic[n] * m
            elif m == 4:
                result += dic[n]
                result += dic[n*5]
            elif 5 <= m < 9:
                result += dic[n*5]
                result += dic[n] * (m-5)
            else:
                result += dic[n]
                result += dic[n*10]
                
            num = num % n
        
        return result     
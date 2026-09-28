class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"
        
        result = [0]*(len(num1)+ len(num2))

        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1, -1,-1):

                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')

                mul = digit1*digit2

                total = mul +result[i+j+1]

                result[i+j+1] = total % 10
                result[i + j] += total // 10

        start_index = 0
        while start_index<len(result) and result[start_index] == 0:
            start_index+=1
        
        return "".join(map(str, result[start_index:]))





        
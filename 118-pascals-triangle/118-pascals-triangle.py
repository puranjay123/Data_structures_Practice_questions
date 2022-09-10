class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res= [[1]]
        
        for i in range(numRows-1):
            temp = [0]+res[-1]+[0]
            row = []
            for j in range(len(res[-1])+1):
                row.append(temp[j] + temp[j+1])
                print(row)
            res.append(row)
        return res
        # ans = [[1]*i for i in range(1,numRows+1)]
        # for i in range(1,numRows):
        #     for j in range(1,i):
        #         ans[i][j] = ans[i-1][j] + ans[i-1][j-1]
        # return ans
                
        
        
        
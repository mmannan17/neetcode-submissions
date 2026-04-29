class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        if text1 == text2:
            return len(text1)

        n=len(text1)
        m=len(text2)
        


        grid = [[0 for _ in range(m+1) ] for _ in range(n+1)]


       


        

        for x in range(1,n+1):
            for y in range(1,m+1):

                if text1[x-1] == text2[y-1]:
                    grid[x][y]= 1 + grid[x-1][y-1]

                else:
                    grid[x][y] = max(grid[x][y-1],grid[x-1][y])



        print(grid)
        return grid[n][m]

        
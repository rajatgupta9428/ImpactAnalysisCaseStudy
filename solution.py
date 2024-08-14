class GraduationCeremony:
    def __init__(self, n):
        # n: total academic days
        if n < 4 or n < 0:
            raise Exception("Invalid Inputs")

        self.n = n
        self.m = 4 # m: cannot miss m or more consecutive classes

    def getProbablity(self):
        n, m = self.n, self.m
        memo = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(m):
            memo[0][i] = 1
        for i in range(1, n + 1):
            for j in range(m - 1, -1, -1):
                memo[i][j] = memo[i - 1][0] + memo[i - 1][j + 1]

        x1 = memo[n][0]  # valid ways to attend classes
        x2 = memo[n - 1][1]  # ways to miss last day

        return f"{x2}/{x1}"
        

if __name__ == "__main__":
    inputs = [5,10]
    for n in inputs:
        obj = GraduationCeremony(n)
        print(obj.getProbablity())

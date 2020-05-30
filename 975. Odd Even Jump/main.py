from typing import List
import bisect

class Solution:
    # TLE
    def oddEvenJumps_v2(self, A: List[int]) -> int:
        N = len(A)
        dp_odd  = [False] * (N-1) + [True]
        dp_even = [False] * (N-1) + [True]
        
        vals = [[A[N-1],N-1]]
        res = 1
        for i in range(N-2, -1, -1):
            keys = [r[0] for r in vals]
            lo = bisect.bisect_left(keys, A[i])
            hi = bisect.bisect_right(keys, A[i])
            if lo < len(vals):
                dp_odd[i] = dp_even[vals[lo][1]]
                if dp_odd[i]:
                    res += 1

            if hi > 0:
                dp_even[i] = dp_odd[vals[hi-1][1]]

            if lo < len(vals) and vals[lo][0] == A[i]:
                vals[lo][1] = i
            else:
                vals.insert(lo, [A[i],i])
        return res

    def oddEvenJumps(self, A: List[int]) -> int:

        N = len(A)
        dp_odd  = [0] * N
        dp_even = [0] * N

        Aasc = sorted([(v,i) for (i,v) in enumerate(A)])
        st = []
        for j in range(len(Aasc)):
            while st and st[-1] < Aasc[j][1]:
                dp_odd[st[-1]] = Aasc[j][1]
                st.pop()
            st.append(Aasc[j][1])
        
        Adec = sorted([(-v,i) for (i,v) in enumerate(A)])
        st = []
        for j in range(len(Adec)):
            while st and st[-1] < Adec[j][1]:
                dp_even[st[-1]] = Adec[j][1]
                st.pop()
            st.append(Adec[j][1])

        odd  = [0] * (N-1) + [1]
        even = [0] * (N-1) + [1]
        for j in range(N-1)[::-1]:
            odd[j]  = even[dp_odd[j]]
            even[j] = odd[dp_even[j]]

        return sum(odd)

if __name__ == "__main__":
    sol = Solution()
    print(sol.oddEvenJumps([10,13,12,14,15]))
    print(sol.oddEvenJumps([2,3,1,1,4]))
    print(sol.oddEvenJumps([5,1,3,4,2]))
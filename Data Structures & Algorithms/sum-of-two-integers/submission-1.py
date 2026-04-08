class Solution:
    def getSum(self, a: int, b: int) -> int:
        '''
        a = 4, b = 7
        a = 0100    a ^ b = 0011
        b = 0111
    _______________
and +       0100
    <<     01000
and xor +   0011
    _______________
           01011 -> 11

        XOR and carry gives the addition
        carry can be found with & with left shift <<
        '''
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        
        while b!= 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        
        return a if a <= max_int else ~(a ^ mask)
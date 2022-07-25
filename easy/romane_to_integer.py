class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # checking the length constrain with or condition
        allwed_charaters = ['X','I','V','L','C','D','M']
        double_instance = ['IV','IX','XL','XC','CD','CM']
        # declare int varible to caculate the end converters
        X=I=V=L=C=D=M = 0
        IX = IV = XL = XC = CD = CM = 0
        print(s[1])
        if((len(s) >= 1 and len(s) <= 15)):
            # checking whether character set is in the allowed string 
            # if any chrater in the allowed charater will be wrong
            if any (x not in allwed_charaters for x in s):
                return 'very bad tring'
            else:
                # should count the charaters
                for i in range(len(s)):
                    if(s[i] == 'I' and s[i+1] == 'V'):
                            IV +=4
                            i += 1;
                    elif(s[i] == 'I' and s[i+1] == 'X'):
                            IX +=9
                            i += 2;
                    elif(s[i] == 'X' and s[i+1] == 'L'):
                            XL +=40
                            i += 2;
                    elif(s[i] == 'X' and s[i+1] == 'C'):
                            XC +=90
                            i += 2;
                    elif(s[i] == 'C' and s[i+1] == 'D'):
                            CD +=400
                            i += 2;
                    elif(s[i] == 'C' and s[i+1] == 'M'):
                            CM +=900
                            i += 2;
                    elif(s[i] == 'I' and (s[i+1] != 'V' or s[i+1] != 'X')):
                            I += 1;
                    elif(s[i] == 'V'):
                        if(i == 0):
                            V += 5;
                        elif(s[i - 1] == 'I'):
                            V += 5
                    elif(s[i] == 'X' and (s[i+1] != 'C' or s[i+1] != 'L')):
                            X += 10;
                    elif(s[i] == 'L' ):
                            L += 50;
                    elif(s[i] == 'C' and (s[i+1] != 'D' or s[i+1] != 'M')):
                            C += 100;
                    elif(s[i] == 'D' ):
                            D += 500;
                    elif(s[i] == 'M' ):
                            M += 1000;
            # else:
            #         for i in range(len(s)):
            #             if(s[i] == 'I'):
            #                 I += 1;
            #             elif(s[i] == 'V'):
            #                 V += 5;
            #             elif(s[i] == 'X'):
            #                 X += 10;
            #             elif(s[i] == 'L'):
            #                 L += 50;
            #             elif(s[i] == 'C'):
            #                 C += 100;
            #             elif(s[i] == 'D'):
            #                 D += 500;
            #             elif(s[i] == 'M'):
            #                 M += 1000;
                    
                    
                
            return  I + V + X + L + C + D + M + IV + IX + XL + XC + CD + CM;

        else:
            return 'Bad string'

    
s = 'VI'
print(Solution.romanToInt(Solution,s))

        





#                       QUESTION 
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. 
# However, the numeral for four is not IIII. Instead, the number four is written as IV. 
# Because the one is before the five we subtract it making four. 
# The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].
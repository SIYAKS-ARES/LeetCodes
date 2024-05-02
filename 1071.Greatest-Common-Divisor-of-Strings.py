# IMPROVED VERSION 2 :
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd_length = self.gcd(len(str1), len(str2))

        prefix_str1 = str1[:gcd_length]
        prefix_str2 = str2[:gcd_length]
        if prefix_str1 == prefix_str2:
            repeat_count_1 = len(str1) // gcd_length
            repeat_count_2 = len(str2) // gcd_length
            if str1 == prefix_str1 * repeat_count_1 and str2 == prefix_str2 * repeat_count_2:
                return prefix_str1
        return ""

    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

# FIRST VERSION : DOESN'T WORK ON SOME CASES
'''class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        modified_string = ""
        min_length = min(len(str1), len(str2))

        if str2 in str1:
            for i in range(min_length):
                if str1[i] == str2[i]:
                    continue
                else:
                    modified_string += str1[i]
            if len(str1) > len(str2):
                modified_string += str1[min_length:]
            else:
                modified_string += str2[min_length:]

        return modified_string

solution = Solution()
print(solution.gcdOfStrings(str1="ABCABC", str2="ABC"))
print(solution.gcdOfStrings(str1="ABABAB", str2="ABAB"))
print(solution.gcdOfStrings(str1="LEET", str2="CODE"))'''

# IMPROVED VERSION : DOESN'T WORK ON SOME CASES
'''class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str2 not in str1:
            return ""
        
        while str1 != str2:
            if len(str1) > len(str2):
                str1 = str1[len(str2):]
            elif len(str1) < len(str2):
                str2 = str2[len(str1):]
            else:
                return ""
        
        return str1

solution = Solution()
print(solution.gcdOfStrings(str1="ABCABC", str2="ABC"))
print(solution.gcdOfStrings(str1="ABABAB", str2="ABAB"))
print(solution.gcdOfStrings(str1="LEET", str2="CODE"))'''

# CHATGPT
'''class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if str1 + str2 != str2 + str1:
            return ""

        divisor_length = gcd(len(str1), len(str2))
        return str1[:divisor_length]

solution = Solution()
print(solution.gcdOfStrings("ABCABC", "ABC"))
print(solution.gcdOfStrings("ABABAB", "ABAB"))
print(solution.gcdOfStrings("LEET", "CODE"))'''

# GEMINI
'''class Solution:
  def gcdOfStrings(self, str1: str, str2: str) -> str:

    if (str1 + str2) != (str2 + str1):
      return ""

    len1, len2 = len(str1), len(str2)
    gcd_len = math.gcd(len1, len2)

    return str1[:gcd_len]'''

# AI VERSION : COULDN'T MAKE IT WORK
'''import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = math.gcd(len(str1), len(str2))

        if gcd > 0 and str1[:gcd] == str2[:gcd]:
            divisible_by_gcd = min(len(str1), len(str2)) % gcd == 0

            if divisible_by_gcd:
                if len(str1) % gcd == 0 and (str1 * (len(str2) // gcd)) == str2:
                    return str1[:gcd]
                if len(str2) % gcd == 0 and (str2 * (len(str1) // gcd)) == str1:
                    return str2[:gcd]

        return str1[:gcd] if str1 * (gcd // len(str1)) == str2 else ""

solution = Solution()
print(solution.gcdOfStrings(str1="ABCABC", str2="ABC"))
print(solution.gcdOfStrings(str1="ABABAB", str2="ABAB"))
print(solution.gcdOfStrings(str1="LEET", str2="CODE"))'''

# AI VERSION 2 : DOESN'T WORK ON SOME CASES
'''class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) % len(str2) != 0 and len(str2) % len(str1) != 0:
            return ""  # Early return for non-divisible lengths

        gcd_length = math.gcd(len(str1), len(str2))  # GCD of string lengths

        if len(str1) % gcd_length == 0 and str1[:gcd_length] == str2:
            return str1[:gcd_length]  # First string is a multiple of the GCD

        if len(str2) % gcd_length == 0 and str2[:gcd_length] == str1:
            return str2[:gcd_length]  # Second string is a multiple of the GCD

        if (str1 + str1)[:gcd_length] == str2 or (str2 + str2)[:gcd_length] == str1:
            return str1[:gcd_length]
        else:
            return ""

solution = Solution()
print(solution.gcdOfStrings(str1="ABCABC", str2="ABC"))
print(solution.gcdOfStrings(str1="ABABAB", str2="ABAB"))
print(solution.gcdOfStrings(str1="LEET", str2="CODE"))'''
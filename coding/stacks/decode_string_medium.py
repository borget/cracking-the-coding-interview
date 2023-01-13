# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated
# exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only
# for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
class Solution:
    def decode(self, substr, n):
        return ''.join(substr for x in range(0, n))

    def decodeString(self, s: str) -> str:
        str_stack = []
        num_stack = []
        string = ''
        number = ''
        for char in s:
            if char.isalpha():
                string += char
            elif char.isdigit():
                number += char
            elif char == '[':
                if string != '':
                    str_stack.append(string)
                    string = ''
                if number != '':
                    num_stack.append(int(number))
                    number = ''
            elif char == ']':
                n = num_stack.pop()
                if len(str_stack) > 1:
                    decoded =''.join(substr for substr in str_stack)
                    str_stack.clear()
                    str_stack.append(decoded)
                if string != '':
                    str_stack.append(self.decode(string, n))
                else:
                    decoded = self.decode(decoded, n)
                    if len(str_stack) > 0:
                        str_stack.pop()
                    str_stack.append(decoded)
                string = ''
        if len(num_stack) == 0 and len(str_stack) > 0:
            final_decoded = ''.join(x for x in str_stack)
            if string != '':
                final_decoded = final_decoded+string
            return final_decoded
        else:
            return string


if __name__ == '__main__':
    solution = Solution()

    input_str = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    result = solution.decodeString(input_str)
    assert result == "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"

    input_str = "abc"
    result = solution.decodeString(input_str)
    assert result == "abc"

    input_str = "3[a]2[bc]"
    result = solution.decodeString(input_str)
    assert result == "aaabcbc"

    input_str = "3[a2[c]]"
    result = solution.decodeString(input_str)
    assert result == "accaccacc"

    input_str = "2[abc]3[cd]ef"
    result = solution.decodeString(input_str)
    assert result == "abcabccdcdcdef"

    input_str = "abc3[cd]xyz"
    result = solution.decodeString(input_str)
    assert result == "abccdcdcdxyz"




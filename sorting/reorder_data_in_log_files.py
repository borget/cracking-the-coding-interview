# You have an array of logs.  Each log is a space delimited string of words.
#
# For each log, the first word in each log is an alphanumeric identifier.  Then, either:
#
# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.
# It is guaranteed that each log has at least one word after its identifier.
#
# Reorder the logs so that all of the letter-logs come before any digit-log.
# The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.
# The digit-logs should be put in their original order.
#
# Return the final order of the logs.
# Constraints:
#
# 0 <= logs.length <= 100
# 3 <= logs[i].length <= 100
# logs[i] is guaranteed to have an identifier, and a word after the identifier.

from typing import List
import bisect


class Solution:
    def type_of_log(self, log):
        log_key = log.find(' ')
        log_val = log[log_key + 1]
        log_type = 'D' if log_val.isnumeric() else 'L'
        return log[0:log_key], log_type

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig_logs = []
        let_logs = []
        ties = dict()
        for log in logs:
            log_key, log_type = self.type_of_log(log)
            log_key_len = len(log_key)
            log_value = log[log_key_len + 1:]
            if log_type == 'D':
                dig_logs.append(log)
            elif log_type == 'L' and log_value in ties:
                let_logs.append(log)
                let_logs.sort(key=lambda l: l[0:log_key_len])
            elif log_type == 'L' and log_value not in ties:
                let_logs.append(log)
                ties[log_value] = None
                let_logs.sort(key=lambda l: l[log_key_len:])
        return [*let_logs, *dig_logs]


if __name__ == '__main__':
    solution = Solution()

    logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo", "a2 act car"]
    result = solution.reorderLogFiles(logs)
    assert result == ["a2 act car", "g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]

    logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    result = solution.reorderLogFiles(logs)
    assert result == ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]

    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    result = solution.reorderLogFiles(logs)
    assert result == ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]

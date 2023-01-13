# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
# which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
from typing import List


class Solution:

    def init_courses(self, prerequisites):
        courses = dict()
        for pr in prerequisites:
            node = pr[0]
            prereq = pr[1]
            if node not in courses:
                courses[node] = [prereq]
            else:
                courses[node].append(prereq)
        return courses

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = self.init_courses(prerequisites)
        visited = dict()
        stack = []
        for c in courses:
            if c not in visited:
                stack.append(c)
                stack += courses[c]
                visited[c] = None
                while len(stack) > 0:
                    stack_item = stack.pop()
                    if stack_item not in courses or len(courses[stack_item]) == 0:
                        visited[stack_item] = None
                        if courses[c]:
                            courses[c].pop()
                        stack.clear()
                    else:
                        if stack_item in visited:
                            return False
                        visited[stack_item] = None
                        if stack_item not in courses or len(courses[stack_item]) == 0:
                            del visited[stack_item]
                            if stack:
                                courses[stack[-1]].pop()
                        else:
                            stack += courses[stack_item]
        return True


if __name__ == '__main__':

    n_courses = 2
    prereq_input = [[1, 0]]
    solution = Solution()
    result = solution.canFinish(n_courses, prereq_input)
    assert result is True

    n_courses = 6
    prereq_input = [[0, 3], [5, 1], [1, 3], [5, 0], [3, 2], [3, 5]]
    solution = Solution()
    result = solution.canFinish(n_courses, prereq_input)
    assert result is False

    n_courses = 6
    prereq_input = [[0, 3], [5, 1], [1, 3], [3, 2], [3, 5]]
    solution = Solution()
    result = solution.canFinish(n_courses, prereq_input)
    assert result is False

    n_courses = 8
    prereq_input = [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]
    solution = Solution()
    result = solution.canFinish(n_courses, prereq_input)
    assert result is True

    n_courses = 3
    prereq_input = [[1, 0], [2, 0]]
    solution = Solution()
    result = solution.canFinish(n_courses, prereq_input)
    assert result is True

    n_courses = 3
    prereq_input = [[1, 0], [2, 1]]
    solution = Solution()
    result = solution.canFinish(n_courses, prereq_input)
    assert result is True

    n_courses = 3
    prereq_input = [[0, 1], [0, 2], [1, 2]]
    solution = Solution()
    result = solution.canFinish(n_courses, prereq_input)
    assert result is True

    n_courses = 4
    prereq_input = [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]
    solution = Solution()
    result = solution.canFinish(n_courses, prereq_input)
    assert result is False


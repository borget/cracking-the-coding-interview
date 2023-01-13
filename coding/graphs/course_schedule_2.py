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
        curr_graph = dict()
        stack = []
        for course in courses:
            if courses[course]:
                stack.append(course)
                stack += courses[course]
                curr_graph[course] = None
            while len(stack) > 0:
                i = stack.pop()
                if i in courses:
                    if i in curr_graph:
                        return False
                    if i in courses:
                        stack += courses[i]
                        if courses[i]:
                            courses[i].pop()
                        curr_graph[i] = None
                    else:
                        print('Unhandled else')

                else:
                    if course in courses:
                        courses[course].pop()
                        if stack:
                            stack.pop()
        return True


if __name__ == '__main__':
    n_courses = 4
    prereq_input = [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]
    solution = Solution()
    result = solution.canFinish(n_courses, prereq_input)
    assert result is False

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




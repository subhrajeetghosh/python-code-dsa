class Solution:
    def __init__(self):
        self.memo = {}
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        course_map = {}
        for pre, course in prerequisites:
            if course not in course_map:
                course_map[course] = []
            course_map[course].append(pre)
        result = []
        for query in queries:
            result.append(self.checkIfPreq(course_map, query[1], query[0]))
        return result
    def checkIfPreq(self, course_map: dict[int, List[int]], main_course: int, pre_req: int) -> bool:
        key = f"{main_course}_{pre_req}"
        if key in self.memo:
            return self.memo[key]
        if main_course not in course_map:
            self.memo[key] = False
            return False
        for pre_course in course_map[main_course]:
            if pre_course == pre_req or self.checkIfPreq(course_map, pre_course, pre_req):
                self.memo[key] = True
                return True
        self.memo[key] = False
        return False

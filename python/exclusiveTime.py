class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        time = [0 for i in range(n)]
        for log in logs:
            sp = log.split(':')
            if sp[1] == 'start':
                stack.append((int(sp[0]), sp[1], int(sp[2])))

            else:
                task, status, start = stack.pop()
                time[task] += int(sp[2]) - start + 1
                if stack:
                    time[stack[-1][0]] -= int(sp[2]) - start + 1

        return time

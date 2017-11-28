class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        total = len(tasks)
        count = collections.Counter(tasks)
        count_sort = count.most_common()
        max_freq = count_sort[0][1]
        max_tasks = 0
        for item in count_sort:
            if item[1] == max_freq:
                max_tasks += 1
            else:
                break

        available_slot = (max_freq - 1) * (n + 1 - max_tasks)
        remain = total - max_freq * max_tasks
        if remain > available_slot:
            return max_freq * max_tasks + remain
        else:
            return max_freq * max_tasks + available_slot

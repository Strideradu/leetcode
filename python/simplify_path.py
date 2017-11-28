# use list as stack


class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_sp = path.split("/")
        stack = []
        for folder in path_sp:
            if folder != '' and folder != '.':
                if folder == '..':
                    if len(stack) > 0:
                        stack.pop()

                else:
                    stack.append(folder)

        return '/' + '/'.join(stack)

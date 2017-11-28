class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        width = 0
        result = []
        process = []
        for i, word in enumerate(words):
            w_l = len(word)
            if width + w_l + 1 <= maxWidth or len(process) == 0:
                width += w_l + 1
                if (process):
                    process[-1] += ' '
                else:
                    width -= 1
                process.append(word)
            elif width + w_l + 1 > maxWidth:
                diff = maxWidth - width
                j = 0
                while(diff > 0):
                    process[j] += ' '
                    diff -= 1
                    j += 1
                    if (j > len(process) - 2):
                        j = 0

                text = ''.join(process)
                if len(text) > 0:
                    result.append(text)
                process = [word]
                width = len(word)

            if i == len(words) - 1:
                diff = maxWidth - width
                process[-1] += ' ' * diff

                result.append(''.join(process))

        return result

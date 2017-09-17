class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        star_count = 0
        par_count = 0
        for cha in s:
            if cha == "(":
                par_count += 1
            if cha == ")":
                par_count -= 1
            if cha == "*":
                star_count += 1
            if par_count < 0:
                if par_count + star_count < 0:
                    return False
                else:
                    star_count = par_count + star_count
                    par_count = 0
                
        if par_count == 0 or par_count - star_count <= 0:
            pos =  True
        else:
            pos =  False
            
        star_count = 0
        par_count = 0
        for cha in s[::-1]:
            if cha == "(":
                par_count -= 1
            if cha == ")":
                par_count += 1
            if cha == "*":
                star_count += 1
            if par_count < 0:
                if par_count + star_count < 0:
                    return False
                else:
                    star_count = par_count + star_count
                    par_count = 0
                
        if par_count == 0 or par_count - star_count <= 0:
            rev =  True
        else:
            rev =  False
            
        if pos and rev:
            return True
        else:
            return False
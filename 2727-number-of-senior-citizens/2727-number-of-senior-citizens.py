class Solution(object):
    def countSeniors(self, details):
        count = 0
        for detail in details:
            age = int(detail[11:13])
            if age > 60:
                count += 1
        return count

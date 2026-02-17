from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # Max possible lit LEDs in any valid time is:
        # hour 11 (1011 -> 3 bits) + minute 59 (111011 -> 5 bits) = 8
        if turnedOn > 8:
            return []
        
        ans = []
        
        for hour in range(12):       # 0..11
            for minute in range(60): # 0..59
                if hour.bit_count() + minute.bit_count() == turnedOn:
                    ans.append(f"{hour}:{minute:02d}")
        
        return ans

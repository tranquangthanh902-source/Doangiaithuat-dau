class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count_note = Counter(ransomNote)
        count_mag = Counter(magazine)
        for char, count in count_note.items():
            if count_mag[char] < count:
                return False
        return True 
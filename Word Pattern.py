class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split() # Tách chuỗi s thành list các từ
        
        # Nếu độ dài không khớp thì không thể tạo cặp
        if len(pattern) != len(words):
            return False
            
        char_to_word = {}
        word_to_char = {}
        
        # zip giúp chúng ta duyệt song song ký tự và từ tương ứng
        for char, word in zip(pattern, words):
            # Kiểm tra ánh xạ từ ký tự sang từ
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word
                
            # Kiểm tra ánh xạ ngược từ từ sang ký tự
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
                
        return True
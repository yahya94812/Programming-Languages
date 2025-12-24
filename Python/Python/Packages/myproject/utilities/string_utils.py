# utilities/string_utils.py
def reverse_string(s):
    """Reverse a string"""
    return s[::-1]

def capitalize_words(s):
    """Capitalize each word in a string"""
    return ' '.join(word.capitalize() for word in s.split())
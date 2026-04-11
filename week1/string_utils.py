def count_vowels(text: str) -> int:
    """Return count of vowels (a,e,i,o,u) case-insensitive"""
    if text is None:
        raise TypeError("Input cannot be None")
    vowels = 'aeiou'
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

def reverse_string(text: str) -> str:
    """Return reversed string"""
    if text is None:
        raise TypeError("Input cannot be None")
    return text[::-1]

def is_palindrome(text: str) -> bool:
    """Check if text reads same forwards and backwards"""
    if text is None:
        raise TypeError("Input cannot be None")
    cleaned = ''.join(text.lower().split())
    return cleaned == cleaned[::-1]

def word_count(text: str) -> int:
    """Return number of words separated by whitespace"""
    if text is None:
        raise TypeError("Input cannot be None")
    if text.strip() == "":
        return 0
    return len(text.split())

def capitalise_words(text: str) -> str:
    """Capitalize first letter of each word"""
    if text is None:
        raise TypeError("Input cannot be None")
    return ' '.join(word.capitalize() for word in text.split())

def remove_duplicates(text: str) -> str:
    """Remove consecutive duplicate characters"""
    if text is None:
        raise TypeError("Input cannot be None")
    if not text:
        return ""
    result = [text[0]]
    for char in text[1:]:
        if char != result[-1]:
            result.append(char)
    return ''.join(result)
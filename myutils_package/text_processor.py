"""
Text Processor Module
문자열 처리 관련 함수들
"""

def reverse_text(text):
    """문자열을 뒤집습니다."""
    return text[::-1]

def count_words(text):
    """단어 개수를 셉니다."""
    return len(text.split())

def remove_spaces(text):
    """모든 공백을 제거합니다."""
    return text.replace(" ", "")

if __name__ == "__main__":
    print("Text Processor Module Test")
    sample = "Hello Python World"
    print(f"Original: {sample}")
    print(f"Reversed: {reverse_text(sample)}")
    print(f"Word count: {count_words(sample)}")
    print(f"No spaces: {remove_spaces(sample)}")

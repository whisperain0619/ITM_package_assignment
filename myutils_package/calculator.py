"""
Calculator Module
기본적인 계산 함수들
"""

def add(a, b):
    """두 수를 더합니다."""
    return a + b

def multiply(a, b):
    """두 수를 곱합니다."""
    return a * b

def power(base, exponent):
    """base의 exponent 제곱을 계산합니다."""
    return base ** exponent

# 테스트 코드
if __name__ == "__main__":
    print("Calculator Module Test")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 * 3 = {multiply(5, 3)}")
    print(f"2^3 = {power(2, 3)}")
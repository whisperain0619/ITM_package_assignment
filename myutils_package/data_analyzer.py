"""
Data Analyzer Module
간단한 데이터 분석 함수들
"""

def calculate_mean(numbers):
    """평균을 계산합니다."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_max(numbers):
    """최댓값을 찾습니다."""
    if not numbers:
        return None
    return max(numbers)

def find_min(numbers):
    """최솟값을 찾습니다."""
    if not numbers:
        return None
    return min(numbers)

if __name__ == "__main__":
    print("Data Analyzer Module Test")
    data = [10, 25, 30, 15, 40]
    print(f"Data: {data}")
    print(f"Mean: {calculate_mean(data)}")
    print(f"Max: {find_max(data)}")
    print(f"Min: {find_min(data)}")

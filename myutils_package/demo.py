"""
MyUtils Package 사용 예시
"""

import sys
sys.path.append('..')  # 상위 디렉토리를 path에 추가

from myutils_package import *

print("=" * 50)
print("MyUtils Package Demo")
print("=" * 50)

# 1. Calculator 기능
print("\n[Calculator Functions]")
print(f"10 + 20 = {add(10, 20)}")
print(f"7 * 6 = {multiply(7, 6)}")
print(f"3^4 = {power(3, 4)}")

# 2. Text Processor 기능
print("\n[Text Processing Functions]")
text = "Hello Python Package"
print(f"Original text: {text}")
print(f"Reversed: {reverse_text(text)}")
print(f"Word count: {count_words(text)}")

# 3. Data Analyzer 기능
print("\n[Data Analysis Functions]")
scores = [85, 92, 78, 95, 88]
print(f"Scores: {scores}")
print(f"Average: {calculate_mean(scores):.2f}")
print(f"Highest: {find_max(scores)}")

print("\n" + "=" * 50)

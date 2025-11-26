"""
MyUtils Package
간단한 유틸리티 함수 모음 패키지
"""

__version__ = "1.0.0"
__author__ = "Your Name"

# 패키지 import 시 자동으로 사용 가능하게 설정
from .calculator import add, multiply, power
from .text_processor import reverse_text, count_words
from .data_analyzer import calculate_mean, find_max

print(f"MyUtils Package v{__version__} loaded successfully!")

# 딕셔너리로 구현

import sys
input = sys.stdin.readline
sum = 0
sum_score = 0

for _ in range(20):
    # 과목명 / 학점 / 등급
    name, score, grade = map(str, input().split())

    # 과목 평점으로 변환
    dic = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
    if grade != 'P':
        sum += float(score) * dic.get(grade)
        sum_score += float(score)

# 전공 평점 = 전공 과목별 (학점 x 과목 평점) 의 합 / 학점의 총합
result = sum / sum_score
print(round(result, 6))

# [참조] 소수점 6자리로 표현

import sys
input = sys.stdin.readline
sum = 0
sum_score = 0

for _ in range(20):
    # 과목명 / 학점 / 등급
    name, score, grade = map(str, input().split())

    # 과목 평점으로 변환
    change = ['A+','A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
    after = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
    if grade != 'P':
        for i in range(9):
            if grade == change[i]:
                sum += float(score) * after[i]
                sum_score += float(score)
                break

# 전공 평점 = 전공 과목별 (학점 x 과목 평점) 의 합 / 학점의 총합
result = sum / sum_score
print(round(result, 6))

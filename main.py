
#各評定割合を入力
kadai_persent = input('課題評価割合を入力(半角)')

test_persent = input('試験評価割合を入力(半角)')


#各点数を入力
kadai_score = input('課題の点数を入力(半角、課題を全部出していれば100を入力)')

test_score = input('試験の点数を入力(半角\n※平均点)')


#評定を計算
kadai = float(kadai_score) * float(kadai_persent) / 100
test = float(test_score) * float(test_persent) / 100
score = kadai + test

print(f"点数: {score}")
import streamlit as st
import pandas as pd
import random

st.title('こうゆう学園1問1答')
# 問題データ(csv形式)読み込み
df = pd.read_csv('4_M-18_こうゆう学園.csv')
# シード値を固定し問題をシャッフル。ボタンを押すたびに再サンプリングを行なわないようにするための処置。
value = st.sidebar.slider('問題シャッフルパターン', 0, 100, help='0はシャッフルなし')
random.seed(value)
# 教科ラジオボタン作成、ユニークな要素で列挙
subject = st.sidebar.radio(
    df.columns[1],
    tuple(df[df.columns[1]].unique())
)
# 年月ラジオボタン作成、ユニークな要素で列挙
term = st.sidebar.radio(
    "第何回の問題にトライしますか？",
    tuple(df[df.columns[0]].unique())
)
# ラジオボダンで選択された問題のみを抽出
df = df[(df[df.columns[0]] == term) & (df[df.columns[1]] == subject)]
# st.write(df)

st.write('問題')
# left_col, right_col = st.columns(2)

# 0以外の選択の場合は選択シード値に従ってランダムサンプリングを実施
if value != 0:
    random_series = random.sample(range(len(df)), k=len(df))
else:
    random_series = range(len(df))

st.sidebar.write('答え')
container = st.sidebar.container(border=True)
button = []
# ボタン作成
for i in random_series:
    button.append(st.button(label=df.iloc[i, 2], type="secondary"))
# ボタンが押された場合答えを表示
for j in range(len(df)):
    if button[j]:
        container.write(df.iloc[random_series[j], 3])

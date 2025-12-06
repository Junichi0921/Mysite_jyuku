import streamlit as st
import pandas as pd
import random

value = st.sidebar.slider('問題シャッフルパターン', 0, 100, help='0はシャッフルなし')
random.seed(value)

subject = st.sidebar.radio(
    "教科",
    ("理科", "社会")
)
st.title('こうゆう学園1問1答')
term = st.sidebar.radio(
    "第何回の問題にトライしますか？",
    ("25年12月1週", "25年12月2週")
)

st.write('問題')
# left_col, right_col = st.columns(2)

df = pd.read_csv('4_M-18_こうゆう学園.csv')
# st.write(df)
df = df[(df['年月'] == term) & (df['教科'] == subject)]
st.write(df)


if value != 0:
    random_series = random.sample(range(len(df)), k=len(df))
else:
    random_series = range(len(df))

st.sidebar.write('答え')
button = []
for i in random_series:
    button.append(st.button(label=df.iloc[i, 2], type="secondary"))

for _ in range(len(df)):
    if button[_]:
        st.sidebar.write(df.iloc[_, 3])

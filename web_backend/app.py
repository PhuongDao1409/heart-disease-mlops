import streamlit as st
import requests
import os

AI_URL = os.getenv("AI_SERVER_URL", "http://ai_server:8000")
st.set_page_config(page_title="Chẩn Đoán Bệnh Tim", page_icon="🫀")
st.title("🫀 Hệ Thống Dự Đoán Nguy Cơ Bệnh Tim")

age = st.slider("Tuổi", 20, 90, 50)
sex = st.selectbox("Giới tính", [1, 0], format_func=lambda x: "Nam" if x == 1 else "Nữ")
chol = st.number_input("Cholesterol", value=210)
trestbps = st.number_input("Huyết áp nghỉ", value=120)
thalach = st.number_input("Nhịp tim tối đa", value=150)
cp = st.selectbox("Kiểu đau ngực (0-3)", [0, 1, 2, 3])

if st.button("Dự Đoán Kết Quả", type="primary"):
    payload = {"age": age, "sex": sex, "cp": cp, "trestbps": trestbps, "chol": chol, "thalach": thalach}
    try:
        res = requests.post(f"{AI_URL}/predict", json=payload, timeout=5)
        if res.status_code == 200:
            st.write(res.json())
    except Exception as e:
        st.error(f"Lỗi: {e}")

# 🫀 Heart Disease Classification & MLOps System

Dự án môn Học máy cơ bản: Phân loại nguy cơ bệnh tim dựa trên dữ liệu Kaggle, so sánh 4 mô hình Machine Learning và triển khai phân tán với Docker, Ngrok.

## 📌 Tổng quan
- **Dataset:** Heart Disease UCI (Kaggle).
- **Mô hình thử nghiệm:** Logistic Regression, SVM, Random Forest, XGBoost.
- **Mô hình tối ưu:** XGBoost (Đạt Recall cao nhất nhằm hạn chế bỏ sót ca bệnh).

## 🏗️ Kiến trúc hệ thống
- **AI Server (FastAPI):** Port 8000 -> Ngrok URL 1 (Inference Service).
- **Web Backend (Streamlit):** Port 8501 -> Ngrok URL 2 (Giao diện người dùng).

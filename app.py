import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="SCHOOL-RANKINH.COM", layout="wide")
st.title("🏫 SCHOOL-RANKINH.COM - Student Ranking System")

if "students" not in st.session_state:
    st.session_state.students = []

st.sidebar.header("Add New Student")
name = st.sidebar.text_input("Student Name")
s_class = st.sidebar.text_input("Class", "Class 1")

st.sidebar.write("Enter Marks (0-100)")
eng = st.sidebar.number_input("English", 0, 100, 50)
math = st.sidebar.number_input("Maths", 0, 100, 50)
sci = st.sidebar.number_input("Science", 0, 100, 50)
soc = st.sidebar.number_input("Social", 0, 100, 50)
rme = st.sidebar.number_input("RME", 0, 100, 50)
bdt = st.sidebar.number_input("BDT", 0, 100, 50)

if st.sidebar.button("Add Student"):
    if name == "":
        st.sidebar.error("Enter name!")
    else:
        total = eng + math + sci + soc + rme + bdt
        avg = total / 6
        if avg >= 80:
            grade = "A EXCELLENT"
        elif avg >= 70:
            grade = "B VERY GOOD"
        elif avg >= 60:
            grade = "C GOOD"
        elif avg >= 50:
            grade = "D CREDIT"
        else:
            grade = "E NEEDS IMPROVEMENT"
        st.session_state.students.append({
            "Name": name, "Class": s_class, "English": eng, "Maths": math,
            "Science": sci, "Social": soc, "RME": rme, "BDT": bdt,
            "Total": total, "Average": round(avg, 2), "Grade": grade
        })
        st.sidebar.success(f"Added {name}!")
        st.rerun()

if st.session_state.students:
    df = pd.DataFrame(st.session_state.students)
    df_sorted = df.sort_values(by="Total", ascending=False).reset_index(drop=True)
    df_sorted.index += 1
    df_sorted.insert(0, "Rank", df_sorted.index)
    st.subheader("📊 Ranking Table")
    st.dataframe(df_sorted, use_container_width=True)
else:
    st.info("No students yet. Add from sidebar!")

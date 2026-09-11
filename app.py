import streamlit as st
import pandas as pd
from io import BytesIO

st.title("MY SCHOOL RANKING SYSTEM")
st.write("### Enter Student Marks")

if 'db' not in st.session_state:
    st.session_state.db = []

name = st.text_input("Student Name")
c1 = st.columns(3)
with c1[0]:
    eng = st.number_input("English", 0, 100, 50)
    math = st.number_input("Maths", 0, 100, 50)
with c1[1]:
    sci = st.number_input("Science", 0, 100, 50)
    soc = st.number_input("Social", 0, 100, 50)
with c1[2]:
    rme = st.number_input("RME", 0, 100, 50)
    bdt = st.number_input("BDT", 0, 100, 50)

total = eng + math + sci + soc + rme + bdt
st.write(f"**TOTAL: {total} / 600**")

if total >= 500:
    grade = "A - EXCELLENT"
elif total >= 400:
    grade = "B - VERY GOOD"
elif total >= 300:
    grade = "C - GOOD"
else:
    grade = "D - NEEDS IMPROVEMENT"

st.write(f"**GRADE: {grade}**")

if st.button("Add Student"):
    st.session_state.db.append({
        "Name": name,
        "English": eng,
        "Maths": math,
        "Science": sci,
        "Social": soc,
        "RME": rme,
        "BDT": bdt,
        "Total": total,
        "Grade": grade
    })
    st.success("ADDED!")

if st.session_state.db:
    df = pd.DataFrame(st.session_state.db)
    df = df.sort_values(by="Total", ascending=False)
    df.insert(0, 'RANK', range(1, 1 + len(df)))
    st.write("### FINAL RANKING LIST")
    st.table(df)

    # --- EXCEL DOWNLOAD (2 lines logic) ---
    output = BytesIO()
    df.to_excel(output, index=False)
    st.download_button("📥 Download Excel File", output.getvalue(), "Final_Ranking.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    if st.button("Clear All"):
        st.session_state.db = []
        st.rerun()import streamlit as st
import pandas as pd
from io import BytesIO

st.title("MY SCHOOL RANKING SYSTEM")
st.write("### Enter Student Marks")

if 'db' not in st.session_state:
    st.session_state.db = []

name = st.text_input("Student Name")
c1 = st.columns(3)
with c1[0]:
    eng = st.number_input("English", 0, 100, 50)
    math = st.number_input("Maths", 0, 100, 50)
with c1[1]:
    sci = st.number_input("Science", 0, 100, 50)
    soc = st.number_input("Social", 0, 100, 50)
with c1[2]:
    rme = st.number_input("RME", 0, 100, 50)
    bdt = st.number_input("BDT", 0, 100, 50)

total = eng + math + sci + soc + rme + bdt
st.write(f"**TOTAL: {total} / 600**")

if total >= 500:
    grade = "A - EXCELLENT"
elif total >= 400:
    grade = "B - VERY GOOD"
elif total >= 300:
    grade = "C - GOOD"
else:
    grade = "D - NEEDS IMPROVEMENT"

st.write(f"**GRADE: {grade}**")

if st.button("Add Student"):
    st.session_state.db.append({
        "Name": name,
        "English": eng,
        "Maths": math,
        "Science": sci,
        "Social": soc,
        "RME": rme,
        "BDT": bdt,
        "Total": total,
        "Grade": grade
    })
    st.success("ADDED!")

if st.session_state.db:
    df = pd.DataFrame(st.session_state.db)
    df = df.sort_values(by="Total", ascending=False)
    df.insert(0, 'RANK', range(1, 1 + len(df)))
    st.write("### FINAL RANKING LIST")
    st.table(df)

    # --- EXCEL DOWNLOAD (2 lines logic) ---
    output = BytesIO()
    df.to_excel(output, index=False)
    st.download_button("📥 Download Excel File", output.getvalue(), "Final_Ranking.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    if st.button("Clear All"):
        st.session_state.db = []
        st.rerun()import streamlit as st
import pandas as pd
from io import BytesIO

st.title("MY SCHOOL RANKING SYSTEM")
st.write("### Enter Student Marks")

if 'db' not in st.session_state:
    st.session_state.db = []

name = st.text_input("Student Name")
c1 = st.columns(3)
with c1[0]:
    eng = st.number_input("English", 0, 100, 50)
    math = st.number_input("Maths", 0, 100, 50)
with c1[1]:
    sci = st.number_input("Science", 0, 100, 50)
    soc = st.number_input("Social", 0, 100, 50)
with c1[2]:
    rme = st.number_input("RME", 0, 100, 50)
    bdt = st.number_input("BDT", 0, 100, 50)

total = eng + math + sci + soc + rme + bdt
st.write(f"**TOTAL: {total} / 600**")

if total >= 500:
    grade = "A - EXCELLENT"
elif total >= 400:
    grade = "B - VERY GOOD"
elif total >= 300:
    grade = "C - GOOD"
else:
    grade = "D - NEEDS IMPROVEMENT"

st.write(f"**GRADE: {grade}**")

if st.button("Add Student"):
    st.session_state.db.append({
        "Name": name,
        "English": eng,
        "Maths": math,
        "Science": sci,
        "Social": soc,
        "RME": rme,
        "BDT": bdt,
        "Total": total,
        "Grade": grade
    })
    st.success("ADDED!")

if st.session_state.db:
    df = pd.DataFrame(st.session_state.db)
    df = df.sort_values(by="Total", ascending=False)
    df.insert(0, 'RANK', range(1, 1 + len(df)))
    st.write("### FINAL RANKING LIST")
    st.table(df)

    # --- EXCEL DOWNLOAD (2 lines logic) ---
    output = BytesIO()
    df.to_excel(output, index=False)
    st.download_button("📥 Download Excel File", output.getvalue(), "Final_Ranking.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    if st.button("Clear All"):
        st.session_state.db = []
        st.rerun()import streamlit as st
import pandas as pd
from io import BytesIO

st.title("MY SCHOOL RANKING SYSTEM")
st.write("### Enter Student Marks")

if 'db' not in st.session_state:
    st.session_state.db = []

name = st.text_input("Student Name")
c1 = st.columns(3)
with c1[0]:
    eng = st.number_input("English", 0, 100, 50)
    math = st.number_input("Maths", 0, 100, 50)
with c1[1]:
    sci = st.number_input("Science", 0, 100, 50)
    soc = st.number_input("Social", 0, 100, 50)
with c1[2]:
    rme = st.number_input("RME", 0, 100, 50)
    bdt = st.number_input("BDT", 0, 100, 50)

total = eng + math + sci + soc + rme + bdt
st.write(f"**TOTAL: {total} / 600**")

if total >= 500:
    grade = "A - EXCELLENT"
elif total >= 400:
    grade = "B - VERY GOOD"
elif total >= 300:
    grade = "C - GOOD"
else:
    grade = "D - NEEDS IMPROVEMENT"

st.write(f"**GRADE: {grade}**")

if st.button("Add Student"):
    st.session_state.db.append({
        "Name": name,
        "English": eng,
        "Maths": math,
        "Science": sci,
        "Social": soc,
        "RME": rme,
        "BDT": bdt,
        "Total": total,
        "Grade": grade
    })
    st.success("ADDED!")

if st.session_state.db:
    df = pd.DataFrame(st.session_state.db)
    df = df.sort_values(by="Total", ascending=False)
    df.insert(0, 'RANK', range(1, 1 + len(df)))
    st.write("### FINAL RANKING LIST")
    st.table(df)

    # --- EXCEL DOWNLOAD (2 lines logic) ---
    output = BytesIO()
    df.to_excel(output, index=False)
    st.download_button("📥 Download Excel File", output.getvalue(), "Final_Ranking.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    if st.button("Clear All"):
        st.session_state.db = []
        st.rerun()import streamlit as st
import pandas as pd
from io import BytesIO

st.title("MY SCHOOL RANKING SYSTEM")
st.write("### Enter Student Marks")

if 'db' not in st.session_state:
    st.session_state.db = []

name = st.text_input("Student Name")
c1 = st.columns(3)
with c1[0]:
    eng = st.number_input("English", 0, 100, 50)
    math = st.number_input("Maths", 0, 100, 50)
with c1[1]:
    sci = st.number_input("Science", 0, 100, 50)
    soc = st.number_input("Social", 0, 100, 50)
with c1[2]:
    rme = st.number_input("RME", 0, 100, 50)
    bdt = st.number_input("BDT", 0, 100, 50)

total = eng + math + sci + soc + rme + bdt
st.write(f"**TOTAL: {total} / 600**")

if total >= 500:
    grade = "A - EXCELLENT"
elif total >= 400:
    grade = "B - VERY GOOD"
elif total >= 300:
    grade = "C - GOOD"
else:
    grade = "D - NEEDS IMPROVEMENT"

st.write(f"**GRADE: {grade}**")

if st.button("Add Student"):
    st.session_state.db.append({
        "Name": name,
        "English": eng,
        "Maths": math,
        "Science": sci,
        "Social": soc,
        "RME": rme,
        "BDT": bdt,
        "Total": total,
        "Grade": grade
    })
    st.success("ADDED!")

if st.session_state.db:
    df = pd.DataFrame(st.session_state.db)
    df = df.sort_values(by="Total", ascending=False)
    df.insert(0, 'RANK', range(1, 1 + len(df)))
    st.write("### FINAL RANKING LIST")
    st.table(df)

    # --- EXCEL DOWNLOAD (2 lines logic) ---
    output = BytesIO()
    df.to_excel(output, index=False)
    st.download_button("📥 Download Excel File", output.getvalue(), "Final_Ranking.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    if st.button("Clear All"):
        st.session_state.db = []
        st.rerun()import streamlit as st
import pandas as pd
from io import BytesIO

st.title("MY SCHOOL RANKING SYSTEM")
st.write("### Enter Student Marks")

if 'db' not in st.session_state:
    st.session_state.db = []

name = st.text_input("Student Name")
c1 = st.columns(3)
with c1[0]:
    eng = st.number_input("English", 0, 100, 50)
    math = st.number_input("Maths", 0, 100, 50)
with c1[1]:
    sci = st.number_input("Science", 0, 100, 50)
    soc = st.number_input("Social", 0, 100, 50)
with c1[2]:
    rme = st.number_input("RME", 0, 100, 50)
    bdt = st.number_input("BDT", 0, 100, 50)

total = eng + math + sci + soc + rme + bdt
st.write(f"**TOTAL: {total} / 600**")

if total >= 500:
    grade = "A - EXCELLENT"
elif total >= 400:
    grade = "B - VERY GOOD"
elif total >= 300:
    grade = "C - GOOD"
else:
    grade = "D - NEEDS IMPROVEMENT"

st.write(f"**GRADE: {grade}**")

if st.button("Add Student"):
    st.session_state.db.append({
        "Name": name,
        "English": eng,
        "Maths": math,
        "Science": sci,
        "Social": soc,
        "RME": rme,
        "BDT": bdt,
        "Total": total,
        "Grade": grade
    })
    st.success("ADDED!")

if st.session_state.db:
    df = pd.DataFrame(st.session_state.db)
    df = df.sort_values(by="Total", ascending=False)
    df.insert(0, 'RANK', range(1, 1 + len(df)))
    st.write("### FINAL RANKING LIST")
    st.table(df)

    # --- EXCEL DOWNLOAD (2 lines logic) ---
    output = BytesIO()
    df.to_excel(output, index=False)
    st.download_button("📥 Download Excel File", output.getvalue(), "Final_Ranking.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    if st.button("Clear All"):
        st.session_state.db = []
        st.rerun()import streamlit as st
import pandas as pd
from io import BytesIO

st.title("MY SCHOOL RANKING SYSTEM")
st.write("### Enter Student Marks")

if 'db' not in st.session_state:
    st.session_state.db = []

name = st.text_input("Student Name")
c1 = st.columns(3)
with c1[0]:
    eng = st.number_input("English", 0, 100, 50)
    math = st.number_input("Maths", 0, 100, 50)
with c1[1]:
    sci = st.number_input("Science", 0, 100, 50)
    soc = st.number_input("Social", 0, 100, 50)
with c1[2]:
    rme = st.number_input("RME", 0, 100, 50)
    bdt = st.number_input("BDT", 0, 100, 50)

total = eng + math + sci + soc + rme + bdt
st.write(f"**TOTAL: {total} / 600**")

if total >= 500:
    grade = "A - EXCELLENT"
elif total >= 400:
    grade = "B - VERY GOOD"
elif total >= 300:
    grade = "C - GOOD"
else:
    grade = "D - NEEDS IMPROVEMENT"

st.write(f"**GRADE: {grade}**")

if st.button("Add Student"):
    st.session_state.db.append({
        "Name": name,
        "English": eng,
        "Maths": math,
        "Science": sci,
        "Social": soc,
        "RME": rme,
        "BDT": bdt,
        "Total": total,
        "Grade": grade
    })
    st.success("ADDED!")

if st.session_state.db:
    df = pd.DataFrame(st.session_state.db)
    df = df.sort_values(by="Total", ascending=False)
    df.insert(0, 'RANK', range(1, 1 + len(df)))
    st.write("### FINAL RANKING LIST")
    st.table(df)

    # --- EXCEL DOWNLOAD (2 lines logic) ---
    output = BytesIO()
    df.to_excel(output, index=False)
    st.download_button("📥 Download Excel File", output.getvalue(), "Final_Ranking.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    if st.button("Clear All"):
        st.session_state.db = []
        st.rerun()import streamlit as st
import pandas as pd
from io import BytesIO

st.title("MY SCHOOL RANKING SYSTEM")
st.write("### Enter Student Marks")

if 'db' not in st.session_state:
    st.session_state.db = []

name = st.text_input("Student Name")
c1 = st.columns(3)
with c1[0]:
    eng = st.number_input("English", 0, 100, 50)
    math = st.number_input("Maths", 0, 100, 50)
with c1[1]:
    sci = st.number_input("Science", 0, 100, 50)
    soc = st.number_input("Social", 0, 100, 50)
with c1[2]:
    rme = st.number_input("RME", 0, 100, 50)
    bdt = st.number_input("BDT", 0, 100, 50)

total = eng + math + sci + soc + rme + bdt
st.write(f"**TOTAL: {total} / 600**")

if total >= 500:
    grade = "A - EXCELLENT"
elif total >= 400:
    grade = "B - VERY GOOD"
elif total >= 300:
    grade = "C - GOOD"
else:
    grade = "D - NEEDS IMPROVEMENT"

st.write(f"**GRADE: {grade}**")

if st.button("Add Student"):
    st.session_state.db.append({
        "Name": name,
        "English": eng,
        "Maths": math,
        "Science": sci,
        "Social": soc,
        "RME": rme,
        "BDT": bdt,
        "Total": total,
        "Grade": grade
    })
    st.success("ADDED!")

if st.session_state.db:
    df = pd.DataFrame(st.session_state.db)
    df = df.sort_values(by="Total", ascending=False)
    df.insert(0, 'RANK', range(1, 1 + len(df)))
    st.write("### FINAL RANKING LIST")
    st.table(df)

    # --- EXCEL DOWNLOAD (2 lines logic) ---
    output = BytesIO()
    df.to_excel(output, index=False)
    st.download_button("📥 Download Excel File", output.getvalue(), "Final_Ranking.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    if st.button("Clear All"):
        st.session_state.db = []
        st.rerun()

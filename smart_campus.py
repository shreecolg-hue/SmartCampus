import streamlit as st
import pandas as pd
import numpy as np
import os
import tempfile

st.set_page_config(page_title="Smart Campus", page_icon="🎓", layout="wide")

TITLE = "Smart Campus Information System"
COLLEGE = "Dayanada Sagar College of Engineering"
MODULES = [
    "Dashboard",
    "Grade Evaluation",
    "Course Enrollment",
    "Student Records",
    "Sort & Search IDs",
    "Fee Calculator",
    "File Records",
    "Directory Scanner",
    "Performance Analytics",
]

if "students" not in st.session_state:
    st.session_state.students = []
if "courses" not in st.session_state:
    st.session_state.courses = []
if "student_ids" not in st.session_state:
    st.session_state.student_ids = []
if "records" not in st.session_state:
    st.session_state.records = []
if "event_a" not in st.session_state:
    st.session_state.event_a = []
if "event_b" not in st.session_state:
    st.session_state.event_b = []


def temp_file(name="student_records.csv"):
    return os.path.join(tempfile.gettempdir(), name)


def grade_for_score(score: float):
    if score >= 90:
        return "A", "Excellent"
    if score >= 75:
        return "B", "Very Good"
    if score >= 60:
        return "C", "Good"
    if score >= 40:
        return "D", "Average"
    return "F", "Needs Improvement"


def search_in_sorted(ids, value):
    sorted_ids = sorted(ids)
    try:
        pos = sorted_ids.index(value)
        return True, pos, sorted_ids
    except ValueError:
        return False, -1, sorted_ids


def build_tree(path):
    lines = []
    for root, _, files in os.walk(path):
        level = root.replace(path, "").count(os.sep)
        prefix = "  " * level
        lines.append(f"{prefix}{os.path.basename(root) or root}/")
        for file in files:
            lines.append(f"{prefix}  {file}")
    return lines


def show_table(data, title=None):
    if title:
        st.subheader(title)
    st.dataframe(pd.DataFrame(data))


st.sidebar.title("Smart Campus")
module = st.sidebar.radio("Choose Module", MODULES)
st.sidebar.markdown("---")
st.sidebar.write("Built with Streamlit")

st.title(TITLE)
st.caption(COLLEGE)
st.markdown("---")

if module == "Dashboard":
    st.header("Dashboard")
    cols = st.columns(4)
    values = [
        ("Students", len(st.session_state.students)),
        ("Courses", len(st.session_state.courses)),
        ("IDs", len(st.session_state.student_ids)),
        ("Records", len(st.session_state.records)),
    ]
    for col, (label, value) in zip(cols, values):
        col.metric(label, value)

    st.write("### Quick overview")
    st.write(
        "This simplified dashboard keeps the same eight functional modules while removing redundant markup and repetitive styling. "
        "Use the sidebar to switch between modules."
    )
    if st.session_state.students:
        show_table(st.session_state.students[-3:], "Recent Graded Students")

elif module == "Grade Evaluation":
    st.header("Grade Evaluation")
    name = st.text_input("Student Name")
    score = st.number_input("Exam Score", min_value=0.0, max_value=100.0, step=0.5)

    if st.button("Evaluate Grade"):
        if not name.strip():
            st.error("Student name is required.")
        else:
            grade, remark = grade_for_score(score)
            st.session_state.students.append({
                "Name": name.strip(),
                "Score": score,
                "Grade": grade,
                "Remark": remark,
            })
            st.success(f"{name.strip()} registered with grade {grade}.")

    if st.session_state.students:
        show_table(st.session_state.students, "All Registered Students")

elif module == "Course Enrollment":
    st.header("Course Enrollment")
    course = st.text_input("Course Name")
    credits = st.number_input("Credits", min_value=1, max_value=10, value=3)

    if st.button("Add Course"):
        if course.strip() and credits > 0:
            if len(st.session_state.courses) < 5:
                st.session_state.courses.append({"Course": course.strip(), "Credits": credits})
                st.success("Course added.")
            else:
                st.warning("Maximum 5 courses allowed.")
        else:
            st.error("Provide a course name and credits.")

    if st.session_state.courses:
        total = sum(item["Credits"] for item in st.session_state.courses)
        st.write(f"**Total courses:** {len(st.session_state.courses)}  •  **Credits:** {total}")
        show_table(st.session_state.courses, "Current Enrollment")

elif module == "Student Records":
    st.header("Student Records")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=10, max_value=100, value=18)
    grades_text = st.text_input("Grades (comma-separated)")

    if st.button("Add Student Record"):
        try:
            grades = [int(x.strip()) for x in grades_text.split(",") if x.strip()]
            if not name.strip() or not grades:
                raise ValueError
            st.session_state.records.append({"Name": name.strip(), "Age": age, "Grades": grades})
            st.success("Student record added.")
        except ValueError:
            st.error("Enter a name and valid comma-separated grades.")

    if st.session_state.records:
        simplified = [
            {"Name": r["Name"], "Age": r["Age"], "Average": round(sum(r["Grades"]) / len(r["Grades"]), 1)}
            for r in st.session_state.records
        ]
        show_table(simplified, "Student Records Summary")

    st.markdown("---")
    st.subheader("Event Participation")
    a_participants = st.text_input("Event A participants", key="event_a_input")
    b_participants = st.text_input("Event B participants", key="event_b_input")

    if st.button("Set Events"):
        st.session_state.event_a = [p.strip() for p in a_participants.split(",") if p.strip()]
        st.session_state.event_b = [p.strip() for p in b_participants.split(",") if p.strip()]
        st.success("Event participants updated.")

    if st.session_state.event_a or st.session_state.event_b:
        set_a = set(st.session_state.event_a)
        set_b = set(st.session_state.event_b)
        st.write("**Common participants:**", sorted(set_a & set_b))
        st.write("**All participants:**", sorted(set_a | set_b))
        st.write("**Only Event A:**", sorted(set_a - set_b))

elif module == "Sort & Search IDs":
    st.header("Sort & Search IDs")
    new_id = st.number_input("Student ID", min_value=1, max_value=99999, value=101, step=1)

    if st.button("Add ID"):
        st.session_state.student_ids.append(int(new_id))
        st.success("ID added.")

    if st.session_state.student_ids:
        found, pos, sorted_ids = search_in_sorted(st.session_state.student_ids, 0)
        st.write("Sorted IDs:", sorted_ids)
        target = st.number_input("Search ID", min_value=1, max_value=99999, value=101, step=1, key="search_target")
        if st.button("Search"):
            found, pos, sorted_ids = search_in_sorted(st.session_state.student_ids, int(target))
            if found:
                st.success(f"Found ID {target} at index {pos} in sorted list.")
            else:
                st.error("ID not found.")

elif module == "Fee Calculator":
    st.header("Fee Calculator")
    tuition = st.number_input("Tuition Fee", min_value=0, value=50000, step=1000)
    hostel = st.number_input("Hostel Fee", min_value=0, value=30000, step=1000)
    transport = st.number_input("Transport Fee", min_value=0, value=10000, step=500)

    if st.button("Calculate Total Fee"):
        total = tuition + hostel + transport
        st.success(f"Total Fee: ₹{total:,}")
        st.write("---")
        st.write(f"Tuition: ₹{tuition:,}")
        st.write(f"Hostel: ₹{hostel:,}")
        st.write(f"Transport: ₹{transport:,}")

elif module == "File Records":
    st.header("File Records")
    file_path = temp_file("student_records.csv")
    st.write(f"Using file: `{file_path}`")

    record_id = st.number_input("Student ID", min_value=1, value=101, step=1)
    record_name = st.text_input("Name")
    record_marks = st.number_input("Marks", min_value=0, max_value=100, value=85, step=1)

    if st.button("Add Record"):
        if record_name.strip():
            st.session_state.records.append({"ID": int(record_id), "Name": record_name.strip(), "Marks": int(record_marks)})
            st.success("Record added.")
        else:
            st.error("Name is required.")

    if st.button("Save Records"):
        if st.session_state.records:
            pd.DataFrame(st.session_state.records).to_csv(file_path, index=False)
            st.success("Saved to file.")
        else:
            st.warning("No records to save.")

    if st.button("Load Records"):
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            show_table(df, "Loaded Records")
        else:
            st.error("File not found.")

    if st.session_state.records:
        show_table(st.session_state.records, "Current Records")

elif module == "Directory Scanner":
    st.header("Directory Scanner")
    path = st.text_input("Directory Path", value=os.getcwd())

    if st.button("Scan Directory"):
        if os.path.exists(path):
            tree = build_tree(path)
            st.text("\n".join(tree[:100]))
            if len(tree) > 100:
                st.info(f"Showing first 100 lines of {len(tree)} entries.")
        else:
            st.error("Invalid directory path.")

elif module == "Performance Analytics":
    st.header("Performance Analytics")
    uploaded = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded is not None:
        df = pd.read_csv(uploaded)
        st.write("### Raw data")
        st.dataframe(df)

        if "Name" not in df.columns:
            st.error("CSV must include a 'Name' column.")
        else:
            numeric = df.select_dtypes(include=["number"])
            if numeric.shape[1] == 0:
                st.warning("Upload a CSV with numeric score columns.")
            else:
                summary = numeric.agg(["mean", "median", "std"]).round(1).T
                st.write("### Subject statistics")
                st.dataframe(summary)

                student_averages = numeric.mean(axis=1).round(1)
                df_scores = df[["Name"]].copy()
                df_scores["Average"] = student_averages
                df_scores = df_scores.sort_values("Average", ascending=False)

                st.write("### Top performers")
                top_n = df_scores.head(3)
                for rank, row in enumerate(top_n.itertuples(index=False), start=1):
                    st.write(f"{rank}. {row.Name} — avg score: {row.Average}")

                st.write("### Student comparison")
                st.bar_chart(df_scores.set_index("Name")["Average"])

                st.write("### Subject averages")
                st.bar_chart(numeric.mean())

                st.write("### Median and standard deviation")
                st.write(summary[["median", "std"]])

st.markdown("---")
st.write("© Dayanada Sagar College of Engineering — Smart Campus Demo")

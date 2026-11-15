
from pathlib import Path
from datetime import date, timedelta
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# ENGINEERING DEGREE OS
# PREMIUM ACADEMIC MANAGEMENT SYSTEM
# ==========================================

st.set_page_config(
    page_title="Engineering Degree OS",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "Data"
if not DATA.exists():
    DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)

# ==========================================
# PINK + GREEN PREMIUM DESIGN
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');

:root {
    --pink: #FF3B91;
    --pink-light: #FF75B5;
    --green: #00E6C5;
    --green-light: #8FFFF0;
    --dark: #111116;
    --panel: #19191f;
}

.stApp {
    background:
    radial-gradient(circle at 80% 0%, #123e39 0%, transparent 35%),
    linear-gradient(135deg,#100817,#171c22,#100a19);
    color: var(--pink-light);
    font-family:'DM Sans',sans-serif;
}

/* GENERAL TEXT */

.stApp p,
.stApp span,
.stApp label,
.stApp li,
.stApp small,
.stApp strong,
.stApp em,
.stApp td,
.stApp th,
.stApp caption {
    color: var(--pink-light);
}

/* GREEN HEADINGS */

.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4,
.stApp h5,
.stApp h6 {
    font-family:'Space Grotesk',sans-serif !important;
    color:var(--green) !important;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background:linear-gradient(180deg,#123b36,#160d20);
    border-right:1px solid var(--green);
}

[data-testid="stSidebar"] * {
    color:var(--pink-light) !important;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color:var(--green) !important;
}

/* MAIN CONTENT */

.block-container {
    padding-top:1.5rem;
    max-width:1600px;
}

/* HERO */

.hero {
    padding:24px;
    border-radius:20px;
    background:linear-gradient(110deg,#123d39,#192c35,#252039);
    border:1px solid var(--green);
    box-shadow:0 8px 35px #0008;
    margin-bottom:22px;
}

.hero h1 {
    font-size:34px;
    color:var(--green) !important;
    -webkit-text-fill-color:var(--green) !important;
}

.hero p {
    color:var(--pink-light) !important;
}

/* METRIC CARDS */

.metric-card {
    padding:19px;
    min-height:120px;
    border-radius:17px;
    background:linear-gradient(140deg,#173b37,#24172f);
    border:1px solid #168d80;
    box-shadow:0 8px 20px #0005;
}

.metric-label {
    color:var(--green) !important;
    font-size:13px;
    font-weight:700;
}

.metric-value {
    font-size:29px;
    font-weight:800;
    color:var(--pink) !important;
    margin-top:8px;
}

.metric-caption {
    font-size:11px;
    color:var(--pink-light) !important;
}

/* PANELS */

.panel {
    background:linear-gradient(145deg,#172f30,#21152d);
    border:1px solid #168d80;
    border-radius:18px;
    padding:20px;
    margin-bottom:16px;
    box-shadow:0 8px 25px #0005;
}

/* SEMESTER CARDS */

.semester-card {
    background:linear-gradient(145deg,#173c38,#26182f);
    border:1px solid #168d80;
    border-radius:16px;
    padding:17px;
    min-height:155px;
    margin-bottom:12px;
}

.semester-title {
    font-size:17px;
    font-weight:800;
    color:var(--green) !important;
}

.semester-status {
    color:var(--pink-light) !important;
    font-size:12px;
}

/* COURSE CARDS */

.course-card {
    background:linear-gradient(145deg,#173533,#24162e);
    border:1px solid #168d80;
    border-radius:14px;
    padding:15px;
    margin-bottom:12px;
}

/* SECTION TITLES */

.section-title {
    font-size:20px;
    font-weight:800;
    color:var(--green) !important;
    margin-bottom:15px;
}

.small-text {
    color:var(--pink-light) !important;
    font-size:12px;
}

/* BUTTONS */

.stButton>button,
.stFormSubmitButton>button {
    background:linear-gradient(100deg,#00bfa9,#c74391);
    color:#ffffff !important;
    border:1px solid var(--green);
    border-radius:10px;
    font-weight:700;
    min-height:40px;
}

.stButton>button:hover,
.stFormSubmitButton>button:hover {
    border-color:var(--pink-light);
    color:#ffffff !important;
    box-shadow:0 0 16px #00e6c580;
}

/* INPUT FIELDS */

.stTextInput input,
.stTextArea textarea,
.stNumberInput input,
.stDateInput input {
    background:#172c2c !important;
    color:var(--pink) !important;
    -webkit-text-fill-color:var(--pink) !important;
    border-color:#00bfa9 !important;
}

.stSelectbox div,
.stMultiSelect div {
    color:var(--pink-light) !important;
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color:#FF75B5 !important;
    opacity:1;
}

/* METRICS */

div[data-testid="stMetric"] {
    background:#173331;
    border:1px solid #00bfa9;
    padding:15px;
    border-radius:14px;
}

div[data-testid="stMetric"] label {
    color:var(--green) !important;
}

div[data-testid="stMetric"] [data-testid="stMetricValue"],
div[data-testid="stMetric"] [data-testid="stMetricDelta"] {
    color:var(--pink) !important;
}

/* DATAFRAMES */

[data-testid="stDataFrame"],
[data-testid="stDataEditor"] {
    color:var(--pink-light) !important;
}

[data-testid="stExpander"] * {
    color:var(--pink-light) !important;
}

.stCaption,
[data-testid="stCaptionContainer"],
[data-testid="stAlert"] * {
    color:var(--pink-light) !important;
}

.stRadio label,
.stCheckbox label,
.stTabs button {
    color:var(--pink-light) !important;
}

/* PROGRESS BARS */

.stProgress > div > div > div {
    background-color:var(--green) !important;
}

/* DIVIDERS */

hr {
    border-color:#168d80;
}

/* FOOTER */

footer {
    visibility:hidden;
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# CSV DATA MANAGEMENT
# ==========================================

FILES = {
    "semesters": ["semesters.csv", "semester.csv"],
    "courses": ["courses.csv", "course.csv"],
    "calendar": ["academic_calendar.csv", "academic_calendar_events.csv"],
    "assessments": ["assessments.csv", "assessment.csv"],
    "scores": ["scores.csv", "score.csv"],
    "tasks": ["plan_checklist.csv", "checklist.csv"],
    "profile": ["university_profile.csv"]
}


def get_file(key):
    for name in FILES[key]:
        path = DATA / name
        if path.exists():
            return path
    return DATA / FILES[key][0]


def load_data(key, columns):
    path = get_file(key)

    if not path.exists():
        df = pd.DataFrame(columns=columns)
        df.to_csv(path, index=False)
        return df

    try:
        df = pd.read_csv(path)
        for col in columns:
            if col not in df.columns:
                df[col] = ""
        return df[columns]
    except Exception:
        st.warning(f"Please check {path.name}")
        return pd.DataFrame(columns=columns)


def number(series):
    return pd.to_numeric(series, errors="coerce").fillna(0)


sem = load_data(
    "semesters",
    ["semester", "status", "total_credits", "completed_credits"]
)

courses = load_data(
    "courses",
    ["semester", "course_code", "course_name",
     "credits", "syllabus", "status"]
)

calendar = load_data(
    "calendar",
    ["academic_year", "semester", "date", "event_type", "title"]
)

assessments = load_data(
    "assessments",
    ["semester", "course_code", "assessment_type",
     "date", "max_marks", "status"]
)

scores = load_data(
    "scores",
    ["semester", "course_code", "assessment_type",
     "score", "max_marks", "grade"]
)

tasks = load_data(
    "tasks",
    ["task", "category", "target_date", "status", "notes"]
)


# ==========================================
# DEFAULT STUDENT PROFILE
# ==========================================

PROFILE_COLUMNS = [
    "college", "branch", "admission_year",
    "current_semester", "regulation", "syllabus_url"
]

profile = load_data("profile", PROFILE_COLUMNS)

DEFAULT_PROFILE = {
    "college": "Sri Venkateshwara College of Engineering, Mangaluru",
    "branch": "Computer Science and Engineering (CSE)",
    "admission_year": "2025",
    "current_semester": "3",
    "regulation": "2025 Admission Batch - Official scheme code to be confirmed",
    "syllabus_url": ""
}

if profile.empty:
    profile = pd.DataFrame([DEFAULT_PROFILE])
    profile.to_csv(get_file("profile"), index=False)

student = profile.iloc[0].to_dict()


# ==========================================
# INITIAL SEMESTER DATA
# ==========================================

if sem.empty:
    sem = pd.DataFrame([
        [1, "Completed", 22, 22],
        [2, "Completed", 22, 22],
        [3, "In Progress", 24, 12],
        [4, "Not Started", 24, 0],
        [5, "Not Started", 24, 0],
        [6, "Not Started", 24, 0],
        [7, "Not Started", 24, 0],
        [8, "Not Started", 24, 0]
    ], columns=[
        "semester", "status", "total_credits", "completed_credits"
    ])
    sem.to_csv(get_file("semesters"), index=False)


# ==========================================
# INITIAL COURSE DEMONSTRATION DATA
# Replace with your official college subjects
# ==========================================

if courses.empty:
    courses = pd.DataFrame([
        [3, "CS301", "Data Structures and Algorithms", 4,
         "Arrays; Linked Lists; Stacks; Queues; Trees; Graphs",
         "In Progress"],
        [3, "CS302", "Database Management Systems", 4,
         "ER Model; SQL; Normalization; Transactions",
         "In Progress"],
        [3, "CS303", "Operating Systems", 4,
         "Processes; Scheduling; Deadlocks; Memory",
         "Not Started"],
        [3, "CS304", "Computer Networks", 3,
         "OSI Model; TCP/IP; Routing; Security",
         "Not Started"],
        [3, "CS305", "Software Engineering", 3,
         "SDLC; Agile; UML; Testing",
         "Not Started"]
    ], columns=[
        "semester", "course_code", "course_name",
        "credits", "syllabus", "status"
    ])
    courses.to_csv(get_file("courses"), index=False)


# ==========================================
# DATA CLEANING
# ==========================================

for df in [sem, courses, calendar, assessments, scores]:
    if "semester" in df.columns:
        df["semester"] = pd.to_numeric(
            df["semester"], errors="coerce"
        )

sem["total_credits"] = number(sem["total_credits"])
sem["completed_credits"] = number(sem["completed_credits"])

total_credits = sem["total_credits"].sum()
completed_credits = sem["completed_credits"].sum()

progress = (
    completed_credits / total_credits * 100
    if total_credits else 0
)

current_semester = int(student.get("current_semester", 3) or 3)


# ==========================================
# KARNATAKA GOVERNMENT HOLIDAYS 2026
# ==========================================

HOLIDAYS_2026 = [
    ("2026-01-15", "Makara Sankranti"),
    ("2026-01-26", "Republic Day"),
    ("2026-03-19", "Ugadi Festival"),
    ("2026-03-21", "Khutub-E-Ramzan"),
    ("2026-03-31", "Mahaveera Jayanthi"),
    ("2026-04-03", "Good Friday"),
    ("2026-04-14", "Dr. B. R. Ambedkar Jayanthi"),
    ("2026-04-20", "Basava Jayanthi / Akshaya Tritiya"),
    ("2026-05-01", "May Day"),
    ("2026-05-28", "Bakrid"),
    ("2026-06-26", "Last Day of Moharam"),
    ("2026-08-15", "Independence Day"),
    ("2026-08-26", "Eid-Milad"),
    ("2026-09-14", "Varasiddhi Vinayaka Vrata"),
    ("2026-10-02", "Gandhi Jayanthi"),
    ("2026-10-20", "Mahanavami / Ayudhapooja"),
    ("2026-10-21", "Vijayadasami"),
    ("2026-11-10", "Balipadyami / Deepavali"),
    ("2026-11-27", "Kanakadasa Jayanthi"),
    ("2026-12-25", "Christmas")
]


def create_holiday_calendar():
    rows = []

    for holiday_date, title in HOLIDAYS_2026:
        rows.append({
            "academic_year": "2026",
            "semester": "",
            "date": holiday_date,
            "event_type": "Government Holiday",
            "title": title
        })

    # Karnataka notification also includes all Sundays,
    # second Saturdays and fourth Saturdays.
    d = date(2026, 1, 1)

    while d.year == 2026:
        if d.weekday() == 6:
            rows.append({
                "academic_year": "2026",
                "semester": "",
                "date": str(d),
                "event_type": "Weekly Holiday",
                "title": "Sunday"
            })

        elif d.weekday() == 5 and (d.day - 1) // 7 in [1, 3]:
            rows.append({
                "academic_year": "2026",
                "semester": "",
                "date": str(d),
                "event_type": "Weekly Holiday",
                "title": "Second/Fourth Saturday"
            })

        d += timedelta(days=1)

    return pd.DataFrame(rows)


# Seed the 2026 holidays once. Existing calendar entries are preserved.
if "2026 government holidays loaded" not in st.session_state:
    if calendar.empty or not (
        (calendar["event_type"] == "Government Holiday").any()
    ):
        holiday_df = create_holiday_calendar()
        calendar = pd.concat(
            [calendar, holiday_df],
            ignore_index=True
        ).drop_duplicates(subset=["date", "title"])

        calendar.to_csv(get_file("calendar"), index=False)

    st.session_state["2026 government holidays loaded"] = True


# ==========================================
# CALENDAR WITH IA ASSESSMENT EVENTS
# ==========================================

def get_combined_calendar():
    result = calendar.copy()

    if not assessments.empty:
        ia = assessments.copy()

        ia["date"] = ia["date"].astype(str).str[:10]
        ia = ia[
            ia["date"].str.match(
                r"^\d{4}-\d{2}-\d{2}$", na=False
            )
        ].copy()

        if not ia.empty:
            ia["academic_year"] = ia["date"].str[:4]
            ia["event_type"] = "Internal Assessment"
            ia["title"] = (
                ia["course_code"].astype(str)
                + " - "
                + ia["assessment_type"].astype(str)
            )

            ia = ia[
                ["academic_year", "semester", "date",
                 "event_type", "title"]
            ]

            result = pd.concat(
                [result, ia],
                ignore_index=True
            )

    result["_date"] = pd.to_datetime(
        result["date"], errors="coerce"
    )

    return result.sort_values("_date")


# ==========================================
# CHART THEME
# ==========================================

def chart_layout(fig, height=280):
    fig.update_layout(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#ffc6df",
        margin=dict(l=10, r=10, t=30, b=10),
        legend=dict(
            orientation="h",
            y=-0.2,
            font=dict(color="#ffc6df")
        )
    )
    return fig


# ==========================================
# LEFT NAVIGATION
# ==========================================

with st.sidebar:

    st.markdown("## 🎓 EDOS")
    st.caption("ENGINEERING DEGREE OS")
    st.markdown("---")

    menu = [
        "🏠 Dashboard",
        "🎓 Semesters 1–8",
        "📚 Courses & Syllabus",
        "🏛️ University Syllabus",
        "📅 Academic Calendar",
        "📝 Internal Assessments",
        "📊 Status Tracker",
        "🏆 Scorecard",
        "📋 Plan & Checklist",
        "🤖 Ask Degree AI",
        "⚙️ Data Admin"
    ]

    selected = st.radio(
        "MAIN NAVIGATION",
        menu,
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("### 👨‍🎓 Student Profile")
    st.markdown(f"**{student['branch']}**")
    st.caption(f"Admission Year: {student['admission_year']}")
    st.caption(f"Current Semester: {current_semester}")
    st.caption("Your complete academic journey")
    st.markdown("---")
    st.caption("ENGINEERING DEGREE OS")
    st.caption("ACADEMIC COMMAND CENTER")


# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div class="hero">
    <h1>🎓 ENGINEERING DEGREE OS</h1>
    <p>
    YOUR COMPLETE ACADEMIC COMMAND CENTER |
    FIRST TO EIGHTH SEMESTER
    </p>
</div>
""", unsafe_allow_html=True)


# ==========================================
# 1. HOME DASHBOARD
# ==========================================

if selected == "🏠 Dashboard":

    st.markdown("## Welcome back, Student! 👋")
    st.caption("Your academic journey at a glance.")

    a, b, c, d = st.columns(4)

    cards = [
        (a, "TOTAL SEMESTERS", "08", "Complete degree roadmap"),
        (b, "TOTAL CREDITS", int(total_credits), "Degree credit requirement"),
        (c, "COMPLETED CREDITS", int(completed_credits), "Credits earned"),
        (d, "DEGREE PROGRESS", f"{progress:.1f}%", "Overall completion")
    ]

    for col, label, value, caption in cards:
        col.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-caption">{caption}</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    left, right = st.columns(2)

    with left:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown("### ◉ Overall Degree Progress")

        fig = go.Figure(
            go.Pie(
                labels=["Completed", "Remaining"],
                values=[
                    completed_credits,
                    max(0, total_credits - completed_credits)
                ],
                hole=.72,
                marker=dict(colors=["#ff78b7", "#75406e"]),
                textinfo="none"
            )
        )

        fig.update_layout(
            height=260,
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="#ffc6df",
            showlegend=True,
            annotations=[dict(
                text=f"{progress:.1f}%",
                x=.5, y=.5,
                font_size=25,
                font_color="#ffb6d9",
                showarrow=False
            )],
            margin=dict(l=5, r=5, t=10, b=10)
        )

        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown("### ✨ Semester Performance")

        fig = px.line(
            sem.copy(),
            x="semester",
            y="completed_credits",
            markers=True,
            labels={
                "semester": "Semester",
                "completed_credits": "Completed Credits"
            }
        )

        fig.update_traces(
            line_color="#ff8fc5",
            marker_color="#ffd0e7",
            line_width=3
        )

        st.plotly_chart(
            chart_layout(fig, 260),
            use_container_width=True
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("## ⚡ Academic Overview")

    x, y, z = st.columns(3)

    with x:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown("### 📝 Upcoming Assessments")

        if assessments.empty:
            st.info("No assessments added yet.")
        else:
            upcoming = assessments.copy()
            upcoming["_date"] = pd.to_datetime(
                upcoming["date"], errors="coerce"
            )
            upcoming = upcoming.sort_values("_date")

            for _, r in upcoming.head(5).iterrows():
                st.write(
                    f"📌 {r['course_code']} · {r['assessment_type']}"
                )
                st.caption(str(r["date"]))

        st.markdown("</div>", unsafe_allow_html=True)

    with y:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown("### 📅 Upcoming Events")

        combined = get_combined_calendar()
        upcoming = combined[
            combined["_date"] >= pd.Timestamp(date.today())
        ]

        if upcoming.empty:
            st.info("No upcoming events.")
        else:
            for _, r in upcoming.head(5).iterrows():
                st.write(f"📍 {r['title']}")
                st.caption(f"{r['date']} · {r['event_type']}")

        st.markdown("</div>", unsafe_allow_html=True)

    with z:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown("### 📋 Study Plan")

        if tasks.empty:
            st.info("Your study plan is empty.")
        else:
            for _, r in tasks.head(5).iterrows():
                st.write(f"☑ {r['task']}")
                st.caption(str(r["status"]))

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("## 🎓 Eight Semester Roadmap")

    cols = st.columns(4)

    for i, (_, r) in enumerate(
        sem.sort_values("semester").iterrows()
    ):
        pct = (
            r["completed_credits"] / r["total_credits"] * 100
            if r["total_credits"] else 0
        )

        with cols[i % 4]:
            st.markdown(f"""
            <div class="semester-card">
                <div class="semester-title">
                    SEMESTER {int(r['semester'])}
                </div>
                <p class="semester-status">{r['status']}</p>
                <h3>{int(r['completed_credits'])}/
                {int(r['total_credits'])} Credits</h3>
                <div style="background:#59334f;border-radius:20px;height:8px">
                    <div style="background:linear-gradient(90deg,#ff83bd,#d65aa4);
                    width:{min(pct,100)}%;height:8px;border-radius:20px">
                    </div>
                </div>
                <p class="small-text">{pct:.0f}% Completed</p>
            </div>
            """, unsafe_allow_html=True)


# ==========================================
# 2. SEMESTER DASHBOARD
# ==========================================

elif selected == "🎓 Semesters 1–8":

    st.markdown("## 🎓 Semester Management")
    st.caption("Explore all eight semesters and monitor academic progress.")

    cols = st.columns(4)

    for i, (_, r) in enumerate(
        sem.sort_values("semester").iterrows()
    ):
        pct = (
            r["completed_credits"] / r["total_credits"] * 100
            if r["total_credits"] else 0
        )

        with cols[i % 4]:
            st.markdown(f"""
            <div class="semester-card">
                <div class="semester-title">
                    SEMESTER {int(r['semester'])}
                </div>
                <p class="semester-status">{r['status']}</p>
                <h3>{pct:.0f}%</h3>
                <p class="small-text">
                    {int(r['completed_credits'])} /
                    {int(r['total_credits'])} credits
                </p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    chosen = st.selectbox(
        "SELECT SEMESTER",
        list(range(1, 9)),
        index=max(0, min(current_semester - 1, 7))
    )

    row = sem[sem["semester"] == chosen]

    if not row.empty:
        r = row.iloc[0]

        st.markdown(f"### Semester {chosen} Details")

        a, b, c = st.columns(3)
        a.metric("Total Credits", int(r["total_credits"]))
        b.metric("Completed Credits", int(r["completed_credits"]))
        c.metric(
            "Remaining Credits",
            int(max(0, r["total_credits"] - r["completed_credits"]))
        )

        pct = (
            r["completed_credits"] / r["total_credits"] * 100
            if r["total_credits"] else 0
        )
        st.progress(min(int(pct), 100))

    st.markdown("### 📚 Semester Subjects")

    detail = courses[courses["semester"] == chosen]

    if detail.empty:
        st.info("No subjects entered for this semester.")
    else:
        st.dataframe(detail, use_container_width=True, hide_index=True)


# ==========================================
# 3. COURSES & SYLLABUS
# ==========================================

elif selected == "📚 Courses & Syllabus":

    st.markdown("## 📚 Courses & Syllabus Library")

    c1, c2, c3 = st.columns([1, 1, 2])

    sem_filter = c1.selectbox("Semester", ["All"] + list(range(1, 9)))
    status_filter = c2.selectbox(
        "Status",
        ["All", "Completed", "In Progress", "Not Started"]
    )
    search = c3.text_input("Search course")

    view = courses.copy()

    if sem_filter != "All":
        view = view[view["semester"] == sem_filter]

    if status_filter != "All":
        view = view[
            view["status"].astype(str).str.lower()
            == status_filter.lower()
        ]

    if search:
        view = view[
            view.astype(str).apply(
                lambda col: col.str.contains(
                    search, case=False, na=False
                )
            ).any(axis=1)
        ]

    for _, r in view.iterrows():
        with st.expander(
            f"📘 {r['course_code']} | {r['course_name']}"
        ):
            a, b, c = st.columns(3)
            a.metric("Semester", r["semester"])
            b.metric("Credits", r["credits"])
            c.metric("Status", r["status"])

            st.markdown("### 📖 Unit-wise Syllabus")

            for unit, topic in enumerate(
                str(r["syllabus"]).split(";"), 1
            ):
                if topic.strip():
                    st.write(f"**Topic {unit}:** {topic.strip()}")


# ==========================================
# 4. UNIVERSITY SYLLABUS
# ==========================================

elif selected == "🏛️ University Syllabus":

    st.markdown("## 🏛️ University / College Details")

    with st.form("university_details"):

        college = st.text_input(
            "College Name",
            value=str(student["college"])
        )

        branch = st.text_input(
            "Engineering Branch",
            value=str(student["branch"])
        )

        admission_year = st.text_input(
            "Admission Year",
            value=str(student["admission_year"])
        )

        regulation = st.text_input(
            "Regulation / Scheme",
            value=str(student["regulation"])
        )

        current_sem = st.number_input(
            "Current Semester",
            min_value=1,
            max_value=8,
            value=current_semester
        )

        syllabus_url = st.text_input(
            "Official Syllabus URL",
            value=str(student.get("syllabus_url", ""))
        )

        save_profile = st.form_submit_button(
            "Save University Details"
        )

    if save_profile:
        updated_profile = pd.DataFrame([{
            "college": college,
            "branch": branch,
            "admission_year": admission_year,
            "current_semester": current_sem,
            "regulation": regulation,
            "syllabus_url": syllabus_url
        }])

        updated_profile.to_csv(get_file("profile"), index=False)
        st.success("College details saved successfully!")
        st.rerun()

    st.markdown("### Semester-wise Curriculum")
    st.dataframe(courses, use_container_width=True, hide_index=True)

    st.caption(
        "The displayed course list is demonstration data until you enter "
        "your official college syllabus."
    )


# ==========================================
# 5. ACADEMIC CALENDAR
# ==========================================

elif selected == "📅 Academic Calendar":

    st.markdown("## 📅 Academic & Government Holiday Calendar")
    st.caption("Karnataka Government Holidays — January to December 2026")

    combined = get_combined_calendar()

    calendar_filter = st.selectbox(
        "Filter Events",
        [
            "All",
            "Government Holiday",
            "Weekly Holiday",
            "Internal Assessment",
            "Academic Event"
        ]
    )

    if calendar_filter != "All":
        combined = combined[
            combined["event_type"] == calendar_filter
        ]

    month_filter = st.selectbox(
        "Select Month",
        ["All"] + [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
        ]
    )

    if month_filter != "All":
        month_number = [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
        ].index(month_filter) + 1

        combined = combined[
            combined["_date"].dt.month == month_number
        ]

    st.dataframe(
        combined.drop(columns=["_date"]),
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### 📌 Calendar Events")

    for _, r in combined.iterrows():
        st.markdown(f"""
        <div class="course-card">
            <h4>📅 {r['title']}</h4>
            <p>{r['event_type']}</p>
            <span class="small-text">{r['date']}</span>
        </div>
        """, unsafe_allow_html=True)

    st.caption(
        "The Karnataka notification includes Sundays and second/fourth "
        "Saturdays as weekly holidays. College-specific closures may differ."
    )


# ==========================================
# 6. INTERNAL ASSESSMENTS
# ==========================================

elif selected == "📝 Internal Assessments":

    st.markdown("## 📝 Internal Assessment Center")

    if assessments.empty:
        st.info("No assessment records available.")
    else:
        st.dataframe(
            assessments,
            use_container_width=True,
            hide_index=True
        )

        st.metric("Total Assessments", len(assessments))

        st.markdown("### Assessment Status")

        counts = assessments["status"].value_counts()

        fig = px.pie(
            names=counts.index,
            values=counts.values,
            hole=.6
        )

        fig.update_traces(
            marker=dict(colors=["#ff83bd", "#c05a9b", "#79436f"])
        )

        st.plotly_chart(
            chart_layout(fig),
            use_container_width=True
        )

    st.markdown("### ＋ Add Internal Assessment")

    with st.form("add_assessment", clear_on_submit=True):

        assessment_semester = st.selectbox(
            "Semester",
            list(range(1, 9)),
            index=max(0, min(current_semester - 1, 7))
        )

        course_codes = courses[
            courses["semester"] == assessment_semester
        ]["course_code"].astype(str).tolist()

        course_code = st.selectbox(
            "Course",
            course_codes if course_codes else ["Not added"]
        )

        assessment_type = st.selectbox(
            "Assessment Type",
            ["IA 1", "IA 2", "IA 3", "Assignment", "Quiz", "Lab Assessment"]
        )

        assessment_date = st.date_input("Assessment Date")
        max_marks = st.number_input(
            "Maximum Marks",
            min_value=1,
            value=30
        )

        add_assessment = st.form_submit_button("Save Assessment")

    if add_assessment and course_code != "Not added":
        new_assessment = pd.DataFrame([{
            "semester": assessment_semester,
            "course_code": course_code,
            "assessment_type": assessment_type,
            "date": str(assessment_date),
            "max_marks": max_marks,
            "status": "Upcoming"
        }])

        assessments = pd.concat(
            [assessments, new_assessment],
            ignore_index=True
        )

        assessments.to_csv(get_file("assessments"), index=False)
        st.success("Assessment added!")
        st.rerun()


# ==========================================
# 7. STATUS TRACKER
# ==========================================

elif selected == "📊 Status Tracker":

    st.markdown("## 📊 Course Status Tracker")

    counts = courses["status"].value_counts()

    a, b, c = st.columns(3)

    a.metric("Completed", int(counts.get("Completed", 0)))
    b.metric("In Progress", int(counts.get("In Progress", 0)))
    c.metric("Not Started", int(counts.get("Not Started", 0)))

    st.markdown("### Subject Progress")

    st.dataframe(
        courses[
            ["semester", "course_code", "course_name", "status"]
        ],
        use_container_width=True,
        hide_index=True
    )


# ==========================================
# 8. SCORECARD
# ==========================================

elif selected == "🏆 Scorecard":

    st.markdown("## 🏆 Academic Scorecard")

    if scores.empty:
        st.info("Enter marks in the Scores data table.")
    else:
        scores["score"] = number(scores["score"])
        scores["max_marks"] = number(scores["max_marks"])

        valid = scores[scores["max_marks"] > 0]

        percentage = (
            valid["score"].sum() / valid["max_marks"].sum() * 100
            if not valid.empty else 0
        )

        a, b, c = st.columns(3)

        a.metric("Total Records", len(scores))
        b.metric("Percentage", f"{percentage:.2f}%")
        c.metric("Marks Obtained", f"{valid['score'].sum():g}")

        st.dataframe(scores, use_container_width=True, hide_index=True)

        st.caption(
            "CGPA requires your university's official grading and credit rules."
        )


# ==========================================
# 9. PLAN & CHECKLIST
# ==========================================

elif selected == "📋 Plan & Checklist":

    st.markdown("## 📋 Smart Study Planner")

    with st.form("add_task", clear_on_submit=True):

        task = st.text_input("Task Name")

        category = st.selectbox(
            "Category",
            ["Academic", "Exams", "Projects", "Placement", "Personal"]
        )

        due = st.date_input("Due Date")
        notes = st.text_input("Notes")

        submit = st.form_submit_button("＋ Add Task")

    if submit and task.strip():
        new_task = pd.DataFrame(
            [[task, category, str(due), "Pending", notes]],
            columns=tasks.columns
        )

        tasks = pd.concat([tasks, new_task], ignore_index=True)
        tasks.to_csv(get_file("tasks"), index=False)

        st.success("Task added!")
        st.rerun()

    if not tasks.empty:
        edited = st.data_editor(
            tasks,
            use_container_width=True,
            num_rows="dynamic",
            hide_index=True
        )

        if st.button("Save Checklist"):
            edited.to_csv(get_file("tasks"), index=False)
            st.success("Checklist saved!")
            st.rerun()


# ==========================================
# 10. ASK DEGREE AI
# ==========================================

elif selected == "🤖 Ask Degree AI":

    st.markdown("## 🤖 Ask Degree AI")
    st.caption("Academic assistant using your saved CSV records.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for role, message in st.session_state.messages:
        with st.chat_message(role):
            st.write(message)

    prompt = st.chat_input(
        "Ask about semesters, subjects, credits or assessments..."
    )

    if prompt:
        st.session_state.messages.append(("user", prompt))
        q = prompt.lower()

        if "credit" in q:
            answer = (
                f"You completed {int(completed_credits)} out of "
                f"{int(total_credits)} credits. "
                f"Your progress is {progress:.1f}%."
            )

        elif "subject" in q or "remaining" in q:
            import re

            found = re.findall(r"\b[1-8]\b", q)
            target = int(found[0]) if found else current_semester

            subset = courses[courses["semester"] == target]

            remaining = subset[
                subset["status"].astype(str).str.lower()
                != "completed"
            ]

            answer = (
                f"Semester {target} has {len(remaining)} subjects remaining: "
                + ", ".join(
                    remaining["course_name"].astype(str).tolist()
                )
            )

        elif "assessment" in q or "exam" in q or "ia" in q:
            answer = (
                assessments.to_string(index=False)
                if not assessments.empty
                else "No assessment records found."
            )

        elif "holiday" in q or "calendar" in q:
            answer = (
                get_combined_calendar().drop(
                    columns=["_date"]
                ).to_string(index=False)
            )

        else:
            answer = (
                "I can help you check your recorded semester progress, "
                "credits, remaining subjects, assessments and holidays. "
                "For official university rules, consult your college syllabus."
            )

        st.session_state.messages.append(("assistant", answer))
        st.rerun()


# ==========================================
# 11. DATA ADMIN
# ==========================================

elif selected == "⚙️ Data Admin":

    st.markdown("## ⚙️ Academic Data Administration")

    tables = {
        "Semesters": sem,
        "Courses": courses,
        "Calendar": calendar,
        "Assessments": assessments,
        "Scores": scores,
        "Checklist": tasks
    }

    selected_table = st.selectbox(
        "Select Data Table",
        list(tables.keys())
    )

    edited = st.data_editor(
        tables[selected_table],
        use_container_width=True,
        num_rows="dynamic",
        hide_index=True
    )

    if st.button("💾 Save Data", type="primary"):

        key = {
            "Semesters": "semesters",
            "Courses": "courses",
            "Calendar": "calendar",
            "Assessments": "assessments",
            "Scores": "scores",
            "Checklist": "tasks"
        }[selected_table]

        edited.to_csv(get_file(key), index=False)

        st.success("Data saved successfully!")
        st.rerun()


# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown("""
<center>
<p style="color:#ffb6d9">
🎓 ENGINEERING DEGREE OS |
YOUR COMPLETE ACADEMIC COMMAND CENTER
</p>
</center>
""", unsafe_allow_html=True)
# Import required libraries
import streamlit as st
import matplotlib.pyplot as plt
import random
from falphin import evolve_falphin

# ----------------------------
# STORE TASKS IN SESSION STATE
# ----------------------------
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# ----------------------------
# PAGE TITLE
# ----------------------------
st.title("🐬 Falphin Productivity Planner")

# ----------------------------
# SIDEBAR DASHBOARD
# ----------------------------
st.sidebar.title("🐬 Falphin Dashboard")

st.sidebar.write("Total Tasks:", len(st.session_state.tasks))

if len(st.session_state.tasks) > 0:
    high = sum(1 for t in st.session_state.tasks if t["priority"] == 3)
    medium = sum(1 for t in st.session_state.tasks if t["priority"] == 2)
    low = sum(1 for t in st.session_state.tasks if t["priority"] == 1)

    st.sidebar.write("High Priority:", high)
    st.sidebar.write("Medium Priority:", medium)
    st.sidebar.write("Low Priority:", low)

# ----------------------------
# RESET TASKS
# ----------------------------
if st.button("Reset All Tasks"):
    st.session_state.tasks = []
    st.success("All tasks cleared!")

# ----------------------------
# DESCRIPTION
# ----------------------------
st.write(
    "🐬 Falphin is a gamified AI productivity companion that helps "
    "students prioritize tasks, track progress, and stay motivated."
)

# ----------------------------
# ADD TASK SECTION
# ----------------------------
st.subheader("Add Task")

task_name = st.text_input("Task name")

deadline = st.number_input(
    "Deadline (days)",
    min_value=0
)

priority = st.slider(
    "Priority",
    1,
    3
)

# Add task button
if st.button("Add Task"):

    if task_name == "":
        st.warning("Enter a task name first")

    else:
        st.session_state.tasks.append({
            "name": task_name,
            "deadline": deadline,
            "priority": priority
        })

        st.success("Task added!")

# ----------------------------
# SHOW TASK LIST
# ----------------------------
st.subheader("Your Tasks")

if len(st.session_state.tasks) == 0:

    st.write("No tasks added yet.")

else:

    for i, task in enumerate(st.session_state.tasks):

        col1, col2 = st.columns([4, 1])

        with col1:
            st.markdown(
                f"""
                **{task['name']}**

                ⏳ Deadline: {task['deadline']} days  
                ⭐ Priority: {task['priority']}
                """
            )

        with col2:
            if st.button("Remove", key=i):
                st.session_state.tasks.pop(i)
                st.rerun()

# ----------------------------
# FALPHIN AI OPTIMIZER
# ----------------------------
st.subheader("🐬 Falphin AI Task Optimizer")

if st.button("Show Suggested Order"):

    if len(st.session_state.tasks) == 0:

        st.warning("Add tasks first!")

    else:

        sorted_tasks = sorted(
            st.session_state.tasks,
            key=lambda x: (x["priority"] * 10 - x["deadline"]),
            reverse=True
        )

        st.write("🐬 Falphin suggests this order:")

        for i, task in enumerate(sorted_tasks):
            st.write(
                f"{i+1}. {task['name']} "
                f"(Priority {task['priority']}, Deadline {task['deadline']})"
            )

        best_task = sorted_tasks[0]

        st.success(
            f"Start with **{best_task['name']}** — most urgent!"
        )

# ----------------------------
# PRODUCTIVITY PROGRESS
# ----------------------------
st.subheader("Daily Progress")
st.info("🎯 Mission: Complete 3 tasks today to evolve Falphin!")

if len(st.session_state.tasks) > 0:

    completed = st.slider(
        "Tasks completed today",
        0,
        len(st.session_state.tasks)
    )

    progress = completed / len(st.session_state.tasks)

    st.progress(progress)

    # Dashboard metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Tasks Completed", completed)

    with col2:
        score = completed * 10
        st.metric("Productivity Score", score)

    with col3:
        st.metric("Total Tasks", len(st.session_state.tasks))

    # Falphin evolution
    stage = evolve_falphin(completed)

    st.subheader("🐬 Falphin Status")

    if stage == "sad":
        st.error("Falphin looks sad today 😢")

    elif stage == "egg":
        st.info("🥚 Falphin is still an egg")

    elif stage == "baby":
        st.success("🐬 Baby Falphin appeared!")

    elif stage == "winged":
        st.success("🪽🐬 Winged Falphin evolved!")

    elif stage == "legendary":
        st.success("🐉 Legendary Falphin awakened!")

    # Motivation messages
    messages = [
        "🐬 Falphin believes in your productivity!",
        "🐬 Small progress still counts.",
        "🐬 Let's finish one task together.",
        "🐬 Consistency builds legends."
    ]

    st.info(random.choice(messages))

# ----------------------------
# DIVIDER
# ----------------------------
st.divider()

# ----------------------------
# PRIORITY PIE CHART
# ----------------------------
if len(st.session_state.tasks) > 0:

    st.subheader("Task Priority Distribution")

    high = 0
    medium = 0
    low = 0

    for task in st.session_state.tasks:

        if task["priority"] == 3:
            high += 1
        elif task["priority"] == 2:
            medium += 1
        else:
            low += 1

    labels = ["High", "Medium", "Low"]
    values = [high, medium, low]

    fig, ax = plt.subplots()

    ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.axis("equal")

    st.pyplot(fig)
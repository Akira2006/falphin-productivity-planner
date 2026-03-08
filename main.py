# Import required libraries
import random
import matplotlib.pyplot as plt
from falphin import evolve_falphin

# List to store tasks
tasks = []


# Function to display productivity chart
def show_progress_chart(completed, total):

    remaining = total - completed

    labels = ["Completed", "Remaining"]
    values = [completed, remaining]

    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.axis("equal")
    plt.title("Falphin Productivity Progress")
    plt.show()


# Function that acts like Falphin's "AI brain"
def suggest_task(tasks):

    # If no tasks exist
    if len(tasks) == 0:
        print("🐬 Falphin says: Add some tasks first!")
        return

    # Compute urgency score for each task
    scored_tasks = []

    for task in tasks:
        score = task["priority"] * 10 - task["deadline"]
        scored_tasks.append((score, task))

    # Sort tasks by highest score
    scored_tasks.sort(reverse=True)

    best_task = scored_tasks[0][1]

    print("\n🐬 Falphin says:")
    print(
        f"Start with '{best_task['name']}' — "
        "it is the most urgent and important!"
    )


# Main program loop
while True:

    print("\n-- Falphin Task Manager --")
    print("1. Add Task")
    print("2. Generate Schedule")
    print("3. Remove Task")
    print("4. Ask Falphin (AI Suggestion)")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # -------------------
    # ADD TASK
    # -------------------
    if choice == "1":

        name = input("Task name: ")

        # Deadline validation
        while True:
            try:
                deadline = int(input("Deadline (days): "))

                if deadline >= 0:
                    break
                else:
                    print("Deadline cannot be negative.")

            except ValueError:
                print("Enter a valid number.")

        # Priority validation
        while True:
            try:
                priority = int(input("Priority (1=Low, 3=High): "))

                if 1 <= priority <= 3:
                    break
                else:
                    print("Priority must be 1–3.")

            except ValueError:
                print("Enter a valid number.")

        tasks.append({
            "name": name,
            "deadline": deadline,
            "priority": priority
        })

        print("Task added!")

    # -------------------
    # GENERATE SCHEDULE
    # -------------------
    elif choice == "2":

        tasks.sort(key=lambda x: (-x["priority"], x["deadline"]))

        print("\n-- Generated Schedule --")

        for task in tasks:
            print(
                f"- {task['name']} | Deadline: {task['deadline']} | "
                f"Priority: {task['priority']}"
            )

        try:
            completed = int(
                input("\nHow many tasks did you complete today? ")
            )
        except ValueError:
            completed = 0

        stage = evolve_falphin(completed)

        print("\n--- Falphin Status ---")

        if stage == "sad":
            print("Falphin looks sad today 😢")

        elif stage == "egg":
            print("🥚 Falphin is still an egg")

        elif stage == "baby":
            print("🐬 Baby Falphin appeared!")

        elif stage == "winged":
            print("🪽🐬 Winged Falphin evolved!")

        elif stage == "legendary":
            print("🐉 Legendary Falphin awakened!")

        messages = [
            "Great work today!",
            "Falphin is proud of you!",
            "Consistency builds legends.",
            "Small progress still counts."
        ]

        print(random.choice(messages))

        show_progress_chart(completed, len(tasks))

    # -------------------
    # REMOVE TASK
    # -------------------
    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks to remove.")
            continue

        print("\nCurrent Tasks:")

        for i, task in enumerate(tasks):
            print(f"{i+1}. {task['name']}")

        try:
            index = int(input("Enter task number to remove: ")) - 1

            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"{removed['name']} removed.")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Enter a valid number.")

    # -------------------
    # AI SUGGESTION
    # -------------------
    elif choice == "4":

        suggest_task(tasks)

    # -------------------
    # EXIT
    # -------------------
    elif choice == "5":

        print("Goodbye from Falphin 🐬")
        break

    else:
        print("Invalid choice.")
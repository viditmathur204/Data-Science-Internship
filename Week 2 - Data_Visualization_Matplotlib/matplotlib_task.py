import matplotlib.pyplot as plt


# =========================
# 1. LINE CHART
# =========================

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
sales = [120, 150, 180, 140, 200, 250, 220]

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(days, sales, marker="o")

ax.set_title("Weekly Sales")
ax.set_xlabel("Day")
ax.set_ylabel("Sales")
ax.grid(True)

plt.tight_layout()
plt.savefig("line_chart.png", dpi=300)
plt.show()


# =========================
# 2. SCATTER PLOT
# =========================

hours = [1, 2, 3, 4, 5, 6, 7, 8]
marks = [45, 50, 55, 60, 65, 72, 78, 85]

fig, ax = plt.subplots(figsize=(8, 5))

ax.scatter(hours, marks)

ax.set_title("Study Hours vs Marks")
ax.set_xlabel("Study Hours")
ax.set_ylabel("Marks")
ax.grid(True)

plt.tight_layout()
plt.savefig("scatter_chart.png", dpi=300)
plt.show()


# =========================
# 3. BAR CHART
# =========================

subjects = ["Python", "Biology", "Maths", "Statistics", "Database"]
marks = [85, 78, 72, 80, 88]

fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(subjects, marks)

ax.set_title("Marks by Subject")
ax.set_xlabel("Subject")
ax.set_ylabel("Marks")

plt.xticks(rotation=20)

plt.tight_layout()
plt.savefig("bar_chart.png", dpi=300)
plt.show()


# =========================
# 4. HISTOGRAM
# =========================

student_marks = [
    45, 50, 55, 60, 62, 65, 65,
    68, 70, 72, 72, 75, 78, 80,
    82, 85, 85, 88, 90, 92, 95
]

fig, ax = plt.subplots(figsize=(8, 5))

ax.hist(student_marks, bins=5)

ax.set_title("Distribution of Student Marks")
ax.set_xlabel("Marks")
ax.set_ylabel("Number of Students")

plt.tight_layout()
plt.savefig("histogram.png", dpi=300)
plt.show()
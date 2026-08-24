import matplotlib.pyplot as plt


# =========================
# DATA
# =========================

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
sales = [120, 150, 180, 140, 200]

subjects = ["Python", "Biology", "Maths", "Statistics", "Database"]
marks = [85, 78, 72, 80, 88]


# =========================
# CREATE SUBPLOTS
# =========================

fig, axes = plt.subplots(1, 2, figsize=(12, 5))


# =========================
# SUBPLOT 1 - LINE CHART
# =========================

axes[0].plot(days, sales, marker="o")

axes[0].set_title("Weekly Sales")
axes[0].set_xlabel("Day")
axes[0].set_ylabel("Sales")

axes[0].grid(True)


# =========================
# SUBPLOT 2 - BAR CHART
# =========================

axes[1].bar(subjects, marks)

axes[1].set_title("Marks by Subject")
axes[1].set_xlabel("Subject")
axes[1].set_ylabel("Marks")

axes[1].tick_params(axis="x", rotation=20)


# =========================
# ADJUST LAYOUT
# =========================

plt.tight_layout()


# =========================
# SAVE FIGURE
# =========================

plt.savefig("subplots.png", dpi=300)


# =========================
# DISPLAY FIGURE
# =========================

plt.show()
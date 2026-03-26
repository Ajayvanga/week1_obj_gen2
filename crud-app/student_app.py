# ============================================
# Student Management System - CRUD Console App
# ============================================

students = {}  # Our "database" (a dictionary)

# ── CREATE ──
def add_student():
    sid = input("Enter Student ID: ")
    if sid in students:
        print("❌ Student ID already exists.")
        return
    name = input("Enter Name: ")
    grade = input("Enter Grade: ")
    students[sid] = {"name": name, "grade": grade}
    print(f"✅ Student '{name}' added successfully!")

# ── READ ──
def view_students():
    if not students:
        print("📭 No students found.")
        return
    print("\n📋 Student List:")
    print("-" * 35)
    for sid, info in students.items():
        print(f"ID: {sid} | Name: {info['name']} | Grade: {info['grade']}")
    print("-" * 35)

# ── UPDATE ──
def update_student():
    sid = input("Enter Student ID to update: ")
    if sid not in students:
        print("❌ Student not found.")
        return
    name = input("Enter new Name: ")
    grade = input("Enter new Grade: ")
    students[sid] = {"name": name, "grade": grade}
    print("✅ Student updated successfully!")

# ── DELETE ──
def delete_student():
    sid = input("Enter Student ID to delete: ")
    if sid not in students:
        print("❌ Student not found.")
        return
    confirm = input(f"Are you sure you want to delete '{students[sid]['name']}'? (yes/no): ")
    if confirm.lower() == "yes":
        del students[sid]
        print("🗑️ Student deleted.")

# ── MAIN MENU ──
def main():
    print("=" * 40)
    print("  Welcome to Student Management System")
    print("=" * 40)
    while True:
        print("\n📌 MENU:")
        print("  1. Add Student")
        print("  2. View All Students")
        print("  3. Update Student")
        print("  4. Delete Student")
        print("  5. Exit")
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter 1 to 5.")

main()
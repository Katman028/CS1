from pathlib import Path

file_path = Path("student_info.txt")
content = "Name: Tom\nCourse: intro to comp sci\nFavorite Programming language: Python\ncurrent semester: Fall 2026"
file_path.write_text(content)

data = file_path.read_text().splitlines()
for line in data:
    print(line)
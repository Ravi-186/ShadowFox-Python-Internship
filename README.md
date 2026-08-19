# ShadowFox Python Internship — Task 1 (Beginner Level)

All 9 subheadings completed (the brief only requires 5 of 9, but all are included).

| File | Subheading | Notes |
|---|---|---|
| `1_variables.py` | Variables | `pi`, `for` keyword behaviour, Simple Interest |
| `2_numbers.py` | Numbers | Octal formatting, pond area + bonus water calc, speed |
| `3_list.py` | List | Justice League list operations |
| `4_if_condition.py` | If Condition | BMI category, city→country, same-country check (interactive) |
| `5_for_loop.py` | For Loop | Dice roll simulation, jumping jacks workout (interactive) |
| `6_dictionary.py` | Dictionary | Friend name-length tuples, trip expense comparison |
| `7_file_handling.py` | File Handling | Reads `student_marks.csv`, writes `student_marks_updated.csv` |
| `8_classes_and_objects.py` | Classes and Objects | `Avenger` class, 6 heroes, `is_leader()` |
| `9_inheritance.py` | Inheritance | `MobilePhone` base → `Apple`/`Samsung` subclasses, with `display_info()` overridden and `super()` used in both constructor and method |

## How to run
```
python3 1_variables.py
python3 2_numbers.py
python3 3_list.py
python3 4_if_condition.py     # prompts for input
python3 5_for_loop.py         # prompts for input
python3 6_dictionary.py
python3 7_file_handling.py
python3 8_classes_and_objects.py
python3 9_inheritance.py
```

## Notes
- **`student_marks.csv`**: this is the actual dataset (Name, Gender, DOB,
  and 8 subject columns — Maths, Physics, Chemistry, English, Biology,
  Economics, History, Civics). `7_file_handling.py` computes each
  student's `total_marks` and `Average` and writes the result to
  `student_marks_updated.csv`. Suresh's blank Chemistry mark is treated
  as 0 (`row["Chemistry"] or 0`), so his total/average still compute
  correctly.
- Scripts 4 and 5 use `input()` for interactivity, per the brief
  ("Ask the user to...", "it should ask..."). Run them directly in a
  terminal to interact, or pipe input for testing.
- Verified: all scripts run cleanly with no errors, and
  `7_file_handling.py`'s output matches the submitted
  `student_marks_updated.csv` exactly.

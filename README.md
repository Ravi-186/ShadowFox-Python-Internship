# ShadowFox Python Internship

**GitHub Repository:** https://github.com/Ravi-186/ShadowFox-Python-Internship

This repository contains all the tasks completed as part of the **ShadowFox Python Development Internship**.

---

## Task 1 — Beginner Level

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

### How to run Task 1
```bash
cd "Task 1 - Beginner"
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

## Task 2 — Intermediate Level
Both parts completed as required.
1. Hangman (hangman.py)
A complete word-guessing game with visual progress and hints.
Features implemented:

Random word selection from a predefined list
Visual ASCII hangman figure that updates with each wrong guess
Hint system (type hint to get a clue)
Input validation (only single letters allowed)
Tracks guessed letters
Win and Loss conditions
Play Again option

How to run:
Bashcd "Task 2 - Intermediate"
python3 hangman.py
2. Web Scraper (web_scraper.py)
Scrapes data from the official ShadowFox website (https://www.shadowfox.org.in/) using BeautifulSoup.
Features implemented:

Extracts Headings, Links, and Paragraphs
Proper error handling
Saves data in CSV and JSON format

Output files:

shadowfox_headings_20260820_104555.csv
shadowfox_links_20260820_104555.csv
shadowfox_report_20260820_104555.json

How to run:
Bashpip install requests beautifulsoup4
cd "Task 2 - Intermediate"
python3 web_scraper.py

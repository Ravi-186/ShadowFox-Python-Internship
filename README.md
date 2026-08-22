# ShadowFox Python Internship

**GitHub Repository:** https://github.com/Ravi-186/ShadowFox-Python-Internship

This repository contains all tasks completed as part of the **ShadowFox Python Development Internship**.

---

# Task 1 — Beginner Level

All **9 subheadings** have been completed, although the internship brief requires only 5 out of 9.

| File                       | Subheading          | Description                                                                       |
| -------------------------- | ------------------- | --------------------------------------------------------------------------------- |
| `1_variables.py`           | Variables           | `pi`, `for` keyword behaviour, Simple Interest                                    |
| `2_numbers.py`             | Numbers             | Octal formatting, pond area + bonus water calculation, speed                      |
| `3_list.py`                | List                | Justice League list operations                                                    |
| `4_if_condition.py`        | If Condition        | BMI category, city-to-country, same-country check                                 |
| `5_for_loop.py`            | For Loop            | Dice roll simulation, jumping jacks workout                                       |
| `6_dictionary.py`          | Dictionary          | Friend name-length tuples, trip expense comparison                                |
| `7_file_handling.py`       | File Handling       | Reads `student_marks.csv`, calculates total and average marks, writes updated CSV |
| `8_classes_and_objects.py` | Classes and Objects | `Avenger` class, six superhero objects, `is_leader()`                             |
| `9_inheritance.py`         | Inheritance         | `MobilePhone` base class with `Apple` and `Samsung` subclasses using `super()`    |

## How to Run Task 1

```bash
cd "Task 1 - Beginner"

python3 1_variables.py
python3 2_numbers.py
python3 3_list.py
python3 4_if_condition.py
python3 5_for_loop.py
python3 6_dictionary.py
python3 7_file_handling.py
python3 8_classes_and_objects.py
python3 9_inheritance.py
```

---

# Task 2 — Intermediate Level

Both required intermediate projects have been completed.

## 1. Hangman

### File

`hangman.py`

A complete word-guessing game with visual progress and hints.

### Features

* Random word selection from a predefined list
* ASCII Hangman visualization
* Hint system
* Input validation
* Tracking of guessed letters
* Win and loss conditions
* Play-again functionality

### How to Run

```bash
cd "Task 2 - Intermediate"

python3 hangman.py
```

---

## 2. Web Scraper

### File

`web_scraper.py`

A Python web scraper implemented using **Requests and BeautifulSoup**.

The scraper extracts information from the official ShadowFox website.

### Features

* Extracts headings from `h1` to `h4`
* Extracts unique links
* Extracts meaningful paragraphs
* Handles timeout, connection, and HTTP errors
* Saves extracted information in CSV and JSON formats

### Output Files

```text
shadowfox_headings_20260820_104555.csv
shadowfox_links_20260820_104555.csv
shadowfox_report_20260820_104555.json
```

### How to Run

```bash
pip install requests beautifulsoup4

cd "Task 2 - Intermediate"

python3 web_scraper.py
```

---

# Task 3 — Advanced Level

## Option 1 — Cricket Fielding Analysis Data Collection

This project analyzes the fielding performance of **three players from a T20 innings** and calculates a Fielding Performance Score.

### Match Used

**DC vs MI — IPL 2025, 29th Match**

* Date: April 13, 2025
* Venue: Arun Jaitley Stadium, Delhi
* Team in field: Mumbai Indians
* Source: ESPNcricinfo ball-by-ball commentary and match information

### Players Tracked

| Player           | Role         |
| ---------------- | ------------ |
| Ryan Rickelton   | Wicketkeeper |
| Will Jacks       | Fielder      |
| Mitchell Santner | Fielder      |

### Fielding Events

The dataset contains real fielding events identified from match commentary.

| Over | Player           | Fielding Event                  |
| ---- | ---------------- | ------------------------------- |
| 17.5 | Ryan Rickelton   | Stumping                        |
| 18.4 | Will Jacks       | Good throw resulting in run out |
| 18.5 | Ryan Rickelton   | Run-out completion              |
| 18.6 | Mitchell Santner | Direct-hit run out              |

### Performance Score Formula

```text
PS = (CP × WCP)
   + (GT × WGT)
   + (C × WC)
   + (DC × WDC)
   + (ST × WST)
   + (RO × WRO)
   + (MRO × WMRO)
   + (DH × WDH)
   + RS
```

### Weights

| Metric | Meaning             |       Weight |
| ------ | ------------------- | -----------: |
| CP     | Clean Pick          |           +1 |
| GT     | Good Throw          |           +1 |
| C      | Catch               |           +3 |
| DC     | Dropped Catch       |           -3 |
| ST     | Stumping            |           +3 |
| RO     | Run Out             |           +3 |
| MRO    | Missed Run Out      |           -2 |
| DH     | Direct Hit          |           +2 |
| RS     | Runs Saved/Conceded | Actual value |

### Results

| Player               | Fielding Actions Score | Runs Saved | Final PS |
| -------------------- | ---------------------: | ---------: | -------: |
| **Ryan Rickelton**   |                      6 |          0 |    **6** |
| **Mitchell Santner** |                      3 |          0 |    **3** |
| **Will Jacks**       |                      2 |          0 |    **2** |

**Best Fielder: Ryan Rickelton — Performance Score = 6**

### Important Note About the Data

The four logged events are real and traceable to the match commentary. However, written commentary mainly records notable fielding events and does not document every routine fielding action.

Therefore, this dataset is **real but not a complete ball-by-ball record of every fielding action in the innings**.

### Task 3 Files

```text
raw_fielding_data.csv
fielding_performance_matrix.csv
IPL_Fielding_Analysis.xlsx
analyze_fielding.py
performance_score_chart.png
category_breakdown_chart.png
requirements.txt
README.md
```

### What the Python Script Does

1. Loads the raw fielding-event data.
2. Identifies the three players.
3. Counts fielding actions.
4. Calculates fielding-action scores.
5. Adds Runs Saved/Conceded.
6. Calculates the final Performance Score.
7. Generates the performance matrix.
8. Generates performance visualizations.
9. Creates the final Excel deliverable.

### How to Run

```bash
pip install -r requirements.txt
python3 analyze_fielding.py
```

---

# Repository Structure

```text
ShadowFox-Python-Internship/
│
├── README.md
│
├── Task 1 - Beginner/
│   ├── 1_variables.py
│   ├── 2_numbers.py
│   ├── 3_list.py
│   ├── 4_if_condition.py
│   ├── 5_for_loop.py
│   ├── 6_dictionary.py
│   ├── 7_file_handling.py
│   ├── 8_classes_and_objects.py
│   ├── 9_inheritance.py
│   ├── student_marks.csv
│   └── student_marks_updated.csv
│
├── Task 2 - Intermediate/
│   ├── hangman.py
│   ├── web_scraper.py
│   ├── shadowfox_headings_*.csv
│   ├── shadowfox_links_*.csv
│   └── shadowfox_report_*.json
│
└── Task 3 - Advanced/
    └── Cricket-Fielding-Analysis/
        ├── raw_fielding_data.csv
        ├── fielding_performance_matrix.csv
        ├── IPL_Fielding_Analysis.xlsx
        ├── analyze_fielding.py
        ├── performance_score_chart.png
        ├── category_breakdown_chart.png
        └── requirements.txt
```

---

# Internship Progress

| Task   | Level                                | Status      |
| ------ | ------------------------------------ | ----------- |
| Task 1 | Beginner                             | ✅ Completed |
| Task 2 | Intermediate                         | ✅ Completed |
| Task 3 | Advanced — Cricket Fielding Analysis | ✅ Completed |

---

# Technologies Used

* Python
* Pandas
* Matplotlib
* NumPy
* OpenPyXL
* Requests
* BeautifulSoup
* CSV
* JSON

---

# Internship Repository

https://github.com/Ravi-186/ShadowFox-Python-Internship

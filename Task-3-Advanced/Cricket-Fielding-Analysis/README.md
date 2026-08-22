# ShadowFox Python Internship — Task 3 (Advanced Level)
## Option 1: Cricket Fielding Analysis Data Collection

## ⚠️ Read this first — how this data was collected

**This data is REAL, not made up** — but it was built from written match
commentary, not by watching video. Here's exactly what that means and
why it matters.

### The source
**DC vs MI, IPL 2025, 29th Match, April 13, 2025, Arun Jaitley Stadium,
Delhi.** Delhi Capitals batted second, chasing 206, and were bowled out
for 193 — Mumbai Indians won by 12 runs. The match ended in dramatic
fashion with three run-outs in the second-last over.
Source: ESPNcricinfo's ball-by-ball commentary and match report for
this match.

### The 3 players tracked
Ryan Rickelton (wicketkeeper), Will Jacks, and Mitchell Santner — all
Mumbai Indians fielders with clearly described fielding involvement in
this match's commentary.

### The 4 events logged — all real, all verifiable
| Over | Player | What actually happened |
|---|---|---|
| 17.5 | Ryan Rickelton | Stumped Vipraj Nigam off Mitchell Santner's bowling — Nigam was down the track and missed |
| 18.4 | Will Jacks | Fielded cleanly and made a good throw to the striker's end, running out Ashutosh Sharma |
| 18.5 | Ryan Rickelton | Completed the run out of Kuldeep Yadav at the keeper's end (the throw itself came from a substitute fielder, RA Bawa, who isn't one of the 3 tracked players) |
| 18.6 | Mitchell Santner | Direct hit at mid-on, running out Mohit Sharma to win Mumbai Indians the match |

### ⚠️ Why there are only 4 rows, and what that means for your submission

Written commentary only describes a fielding action when something
**notable** happens — a wicket, a big misfield, a boundary save. It does
NOT describe the dozens of routine fielding moments (a clean pick and
return with no incident) that happen throughout an innings — those
only show up if you're actually watching. So a dataset built from text
commentary will always be much sparser than one built by watching a
full innings yourself.

**This means these 4 rows are 100% real, sourced, and verifiable — but
they are not a complete fielding record of the innings.** The task
brief expects "for each ball bowled" — a genuinely thorough submission
would ideally have considerably more rows than this.

**My honest recommendation:** if you have time before submitting,
watch the last few overs of this actual match on YouTube (search
"DC vs MI IPL 2025 highlights April 13" or similar) and add the
routine fielding moments you can now literally see — clean picks that
didn't lead to wickets, any misfields, etc. — to this same CSV, in the
same format. That turns this from "4 real but sparse events" into a
genuinely thorough submission, without inventing anything, since
you'd be watching the exact match this data is already sourced from.

## Weights used

Taken directly from the formulas embedded in the provided
`IPL_sample_data.xlsx` sample performance matrix (not stated as plain
numbers anywhere in the PDF brief):

| Metric | Weight |
|---|---|
| CP (Clean Pick) | +1 |
| GT (Good Throw) | +1 |
| C (Catch) | +3 |
| DC (Dropped Catch) | -3 |
| ST (Stumping) | +3 |
| RO (Run Out) | +3 |
| MRO (Missed Run Out) | -2 |
| DH (Direct Hit) | +2 |
| RS (Runs Saved) | added as-is |

## Results from this dataset

```
Player                Fielding Actions    Runs Saved      Final PS
Ryan Rickelton                       6             0             6
Mitchell Santner                     3             0             3
Will Jacks                           2             0             2
```

Ryan Rickelton comes out on top — a stumping (+3) and a run out
completion (+3).

## How the script works

1. Loads `raw_fielding_data.csv`.
2. Aggregates per player: counts Clean Picks, Catches, Dropped
   Catches, Stumpings (from the `Pick` column) and Good Throws,
   Direct Hits, Run Outs, Missed Run Outs (from the `Throw` column),
   and sums `Runs` as Runs Saved.
3. Applies the Performance Score formula with the weights above.
4. Prints a clear breakdown table (Fielding Actions / Runs Saved /
   Final PS side by side).
5. Saves the matrix to `fielding_performance_matrix.csv`.
6. Generates two charts:
   - `performance_score_chart.png` — total PS per player
   - `category_breakdown_chart.png` — full category breakdown
     including Runs Saved, labeled with each player's Final PS
7. Produces `IPL_Fielding_Analysis.xlsx` — a combined spreadsheet
   with the raw data and the computed matrix as two sheets.

## How to run

```
pip install -r requirements.txt
python3 analyze_fielding.py
```

## Files in this folder

| File | Description |
|---|---|
| `raw_fielding_data.csv` | Real fielding events sourced from actual match commentary (see notes above on sparsity) |
| `analyze_fielding.py` | Aggregation + scoring + chart generation script |
| `fielding_performance_matrix.csv` | Computed output (regenerated each run) |
| `performance_score_chart.png` | Chart: total PS per player |
| `category_breakdown_chart.png` | Chart: full category breakdown incl. Runs Saved, labeled with Final PS |
| `IPL_Fielding_Analysis.xlsx` | Combined spreadsheet deliverable (raw + matrix) |
| `requirements.txt` | Python dependencies |

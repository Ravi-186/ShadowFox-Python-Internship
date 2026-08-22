# ==========================================
# TASK 3 (ADVANCED): CRICKET FIELDING ANALYSIS
# ==========================================
#
# Reads ball-by-ball fielding event data for a T20 innings, aggregates
# it into per-player totals (clean picks, catches, run outs, etc.),
# and computes each player's Performance Score using the formula
# and weights specified in the ShadowFox task brief:
#
#   PS = (CP x WCP) + (GT x WGT) + (C x WC) + (DC x WDC) + (ST x WST)
#        + (RO x WRO) + (MRO x WMRO) + (DH x WDH) + RS
#
# Weights (taken directly from the task's sample performance matrix):
#   CP  = +1   GT  = +1   C   = +3   DC  = -3   ST  = +3
#   RO  = +3   MRO = -2   DH  = +2   RS  = added as-is
#
# Column code legend (from the task's dataset):
#   Pick  : Y = Clean Pick | N = Fumble | C = Catch
#           DC = Dropped Catch | S = Stumping
#   Throw : Y = Good Throw | N = Bad Throw | DH = Direct Hit
#           RO = Run Out | MR = Missed Run Out

import pandas as pd
import matplotlib.pyplot as plt

RAW_DATA_FILE = "raw_fielding_data.csv"
OUTPUT_MATRIX_FILE = "fielding_performance_matrix.csv"
OUTPUT_EXCEL_FILE = "IPL_Fielding_Analysis.xlsx"

# Weights straight from the task brief
WEIGHTS = {
    "CP": 1,    # Clean Pick
    "GT": 1,    # Good Throw
    "C": 3,     # Catch
    "DC": -3,   # Dropped Catch
    "ST": 3,    # Stumping
    "RO": 3,    # Run Out
    "MRO": -2,  # Missed Run Out
    "DH": 2,    # Direct Hit
}
CATEGORY_ORDER = ["CP", "GT", "C", "DC", "ST", "RO", "MRO", "DH"]


def load_raw_data(filepath):
    """Load the ball-by-ball fielding log."""
    df = pd.read_csv(filepath)
    # Normalize the Pick/Throw codes to uppercase so 'y'/'Y' both work
    df["Pick"] = df["Pick"].astype(str).str.strip().str.upper().replace("NAN", "")
    df["Throw"] = df["Throw"].astype(str).str.strip().str.upper().replace("NAN", "")
    return df


def build_performance_matrix(df):
    """
    Aggregate raw ball-by-ball events into one row per player, counting
    each category the Performance Score formula needs.
    """
    players = df["Player Name"].dropna().unique()
    records = []

    for player in players:
        player_rows = df[df["Player Name"] == player]

        record = {
            "Player Name": player,
            "CP": (player_rows["Pick"] == "Y").sum(),
            "GT": (player_rows["Throw"] == "Y").sum(),
            "C": (player_rows["Pick"] == "C").sum(),
            "DC": (player_rows["Pick"] == "DC").sum(),
            "ST": (player_rows["Pick"] == "S").sum(),
            "RO": (player_rows["Throw"] == "RO").sum(),
            "MRO": (player_rows["Throw"] == "MR").sum(),
            "DH": (player_rows["Throw"] == "DH").sum(),
            "RS": player_rows["Runs"].sum(),
        }

        # Weighted contribution from fielding actions only (everything
        # except Runs Saved) - used for the summary table and chart.
        fielding_actions_score = sum(record[cat] * WEIGHTS[cat] for cat in CATEGORY_ORDER)
        record["Fielding Actions Score"] = fielding_actions_score

        # Full Performance Score = weighted actions + Runs Saved
        record["Performance Score"] = fielding_actions_score + record["RS"]

        records.append(record)

    matrix = pd.DataFrame(records)
    matrix = matrix.sort_values("Performance Score", ascending=False).reset_index(drop=True)
    return matrix


def print_summary_table(matrix):
    """
    Clean, human-readable breakdown showing exactly how each player's
    Final PS is built: Fielding Actions Score + Runs Saved = Final PS.
    This makes the math immediately understandable without needing to
    reconcile it against the stacked chart.
    """
    print("\nFielding Performance Breakdown")
    print("-" * 68)
    print(f"{'Player':<20}{'Fielding Actions':>18}{'Runs Saved':>14}{'Final PS':>14}")
    print("-" * 68)
    for _, row in matrix.iterrows():
        print(f"{row['Player Name']:<20}{row['Fielding Actions Score']:>18}"
              f"{row['RS']:>14}{row['Performance Score']:>14}")
    print("-" * 68)


def plot_performance_scores(matrix):
    """Bar chart comparing each player's overall Performance Score."""
    plt.figure(figsize=(8, 5))
    colors = ["#2ca02c" if score >= 0 else "#d62728" for score in matrix["Performance Score"]]
    plt.bar(matrix["Player Name"], matrix["Performance Score"], color=colors)
    plt.title("Fielding Performance Score by Player")
    plt.xlabel("Player")
    plt.ylabel("Performance Score (PS)")
    plt.axhline(0, color="black", linewidth=0.8)
    plt.tight_layout()
    plt.savefig("performance_score_chart.png")
    plt.close()
    print("Saved chart: performance_score_chart.png")


def plot_category_breakdown(matrix):
    """
    Stacked bar chart showing the weighted contribution of each
    category PLUS Runs Saved, so the total bar height for each player
    equals their actual Final PS - no more discrepancy between this
    chart and the Performance Score chart.
    """
    columns_to_plot = CATEGORY_ORDER + ["RS"]
    weighted = matrix.set_index("Player Name")[CATEGORY_ORDER].mul(pd.Series(WEIGHTS))
    weighted["RS"] = matrix.set_index("Player Name")["RS"]
    weighted = weighted[columns_to_plot]

    ax = weighted.plot(kind="bar", stacked=True, figsize=(9, 6), colormap="tab10")
    plt.title("Performance Score Breakdown by Category (including Runs Saved)")
    plt.xlabel("Player")
    plt.ylabel("Points Contributed to Final PS")
    plt.axhline(0, color="black", linewidth=0.8)
    plt.legend(title="Category", bbox_to_anchor=(1.02, 1), loc="upper left")

    # Label each bar with the Final PS total so it's unambiguous
    for i, player in enumerate(matrix["Player Name"]):
        total = matrix.loc[matrix["Player Name"] == player, "Performance Score"].values[0]
        y_pos = total + (1 if total >= 0 else -1)
        ax.text(i, y_pos, f"PS={total}", ha="center",
                va="bottom" if total >= 0 else "top", fontweight="bold")

    plt.tight_layout()
    plt.savefig("category_breakdown_chart.png")
    plt.close()
    print("Saved chart: category_breakdown_chart.png (bar heights now sum to Final PS)")


def save_excel_deliverable(raw_df, matrix_df, filepath):
    """
    Combine the raw event log and the computed performance matrix into
    a single spreadsheet with two sheets - matching the task brief's
    'well-organized spreadsheet' deliverable requirement.
    """
    with pd.ExcelWriter(filepath, engine="openpyxl") as writer:
        raw_df.to_excel(writer, sheet_name="Raw Ball-by-Ball Data", index=False)
        matrix_df.to_excel(writer, sheet_name="Performance Matrix", index=False)
    print(f"Saved combined spreadsheet: {filepath}")


if __name__ == "__main__":
    df = load_raw_data(RAW_DATA_FILE)
    print(f"Loaded {len(df)} fielding events across {df['Player Name'].nunique()} players.\n")

    matrix = build_performance_matrix(df)
    print("Performance Matrix:")
    print(matrix.to_string(index=False))

    print_summary_table(matrix)

    matrix.to_csv(OUTPUT_MATRIX_FILE, index=False)
    print(f"\nSaved performance matrix to {OUTPUT_MATRIX_FILE}")

    plot_performance_scores(matrix)
    plot_category_breakdown(matrix)
    save_excel_deliverable(df, matrix, OUTPUT_EXCEL_FILE)

    top_player = matrix.iloc[0]
    print(f"\nTop fielder of the innings: {top_player['Player Name']} "
          f"with a Performance Score of {top_player['Performance Score']}")

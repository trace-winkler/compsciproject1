"""
NFL Offensive Statistics — 2025-26 Regular Season
--------------------------------------------------
Reads player data out of Phase_0_NFL_Offensive_Statistics.xlsx and lets the
user look up total/average receiving & rushing stats for a team's
WR1, RB1, or TE1.

No pandas / polars / similar libraries are used. openpyxl is used ONLY to
pull the raw cell values out of the binary .xlsx file -- everything after
that (storing, searching, grouping, averaging) is done with plain Python
lists, dicts, and loops.
"""
import os
import openpyxl

DATA_FILE = r"C:\Users\ncwin_05165p4\OneDrive\Desktop\Intro to Computer Science 2\Project\Phase_0_NFL_Offensive_Statistics.xlsx.xlsx"

# ---------------------------------------------------------------------------
# STEP 1 & 2: Open the file, read the rows, store them in a data structure
# ---------------------------------------------------------------------------
def load_data(filename):
    """
    Opens the workbook, reads every row after the header, and returns a
    list of dictionaries -- one dictionary per player -- e.g.:
    {
        "player_position": "WR",
        "player_name": "Keon Coleman",
        "team": "BUF",
        "games_played": 13,
        "total_receptions": 38,
        "total_targets": 59,
        "receiving_yards": 404,
        "receiving_touchdowns": 4,
        "total_carries": 0,
        "rushing_yards": 0,
        "rushing_touchdowns": 0,
    }
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(
            f"Could not find '{filename}'. Make sure it's in the same "
            f"folder as this script."
        )
    workbook = openpyxl.load_workbook(filename, data_only=True)
    sheet = workbook.active  # only one sheet in this workbook
    rows = list(sheet.iter_rows(values_only=True))
    headers = rows[0]
    data_rows = rows[1:]
    players = []
    for row in data_rows:
        record = {}
        for header, value in zip(headers, row):
            record[header] = value
        players.append(record)
    return players

# ---------------------------------------------------------------------------
# STEP 3: Transform / organize -- find the player(s) that match what the
# user typed, and compute the averages
# ---------------------------------------------------------------------------
def find_matches(players, position, identifier):
    """
    Returns every player record at the given position whose name OR team
    abbreviation contains 'identifier' (case-insensitive, partial match).
    """
    position = position.strip().upper()
    identifier = identifier.strip().lower()
    matches = []
    for player in players:
        if player["player_position"] != position:
            continue
        name_match = identifier in player["player_name"].lower()
        team_match = identifier in player["team"].lower()
        if name_match or team_match:
            matches.append(player)
    return matches

def per_game(total, games):
    """Safely computes a per-game average, rounded to 2 decimal places."""
    if not games:
        return 0.0
    return round(total / games, 2)

# ---------------------------------------------------------------------------
# STEP 4: Present the results
# ---------------------------------------------------------------------------
def print_receiving_block(player):
    games = player["games_played"]
    print(f"  Games Played:              {games}")
    print(f"  Receptions:  {player['total_receptions']:>4} total   "
          f"({per_game(player['total_receptions'], games)} avg/game)")
    print(f"  Targets:     {player['total_targets']:>4} total   "
          f"({per_game(player['total_targets'], games)} avg/game)")
    print(f"  Rec. Yards:  {player['receiving_yards']:>4} total   "
          f"({per_game(player['receiving_yards'], games)} avg/game)")
    print(f"  Rec. TDs:    {player['receiving_touchdowns']:>4} total   "
          f"({per_game(player['receiving_touchdowns'], games)} avg/game)")

def print_rushing_block(player):
    games = player["games_played"]
    print(f"  Carries:     {player['total_carries']:>4} total   "
          f"({per_game(player['total_carries'], games)} avg/game)")
    print(f"  Rush Yards:  {player['rushing_yards']:>4} total   "
          f"({per_game(player['rushing_yards'], games)} avg/game)")
    print(f"  Rush TDs:    {player['rushing_touchdowns']:>4} total   "
          f"({per_game(player['rushing_touchdowns'], games)} avg/game)")

def print_player_header(player, role_label):
    print("-" * 50)
    print(f"{player['player_name']}  ({player['team']}) -- {role_label}")
    print("-" * 50)

# ---------------------------------------------------------------------------
# FUNCTION 1 -- Wide Receiver 1
# ---------------------------------------------------------------------------
def rec_rus_stats_wr1(players, identifier):
    matches = find_matches(players, "WR", identifier)
    if not matches:
        print(f"No WR1 found matching '{identifier}'.")
        return
    for player in matches:
        print_player_header(player, "Wide Receiver 1")
        print("Receiving Statistics:")
        print_receiving_block(player)
        if player["total_carries"] and player["total_carries"] > 0:
            print("\nRushing Statistics (if applicable):")
            print_rushing_block(player)
        print()

# ---------------------------------------------------------------------------
# FUNCTION 2 -- Running Back 1
# ---------------------------------------------------------------------------
def rec_rus_stats_rb1(players, identifier):
    matches = find_matches(players, "RB", identifier)
    if not matches:
        print(f"No RB1 found matching '{identifier}'.")
        return
    for player in matches:
        print_player_header(player, "Running Back 1")
        print("Rushing Statistics:")
        print_rushing_block(player)
        if player["total_targets"] and player["total_targets"] > 0:
            print("\nReceiving Statistics (if applicable):")
            print_receiving_block(player)
        print()

# ---------------------------------------------------------------------------
# FUNCTION 3 -- Tight End 1
# ---------------------------------------------------------------------------
def rec_rus_stats_te1(players, identifier):
    matches = find_matches(players, "TE", identifier)
    if not matches:
        print(f"No TE1 found matching '{identifier}'.")
        return
    for player in matches:
        print_player_header(player, "Tight End 1")
        print("Receiving Statistics:")
        print_receiving_block(player)
        if player["total_carries"] and player["total_carries"] > 0:
            print("\nRushing Statistics (if applicable):")
            print_rushing_block(player)
        print()

# ---------------------------------------------------------------------------
# Program entry point / menu
# ---------------------------------------------------------------------------
def main():
    try:
        players = load_data(DATA_FILE)
    except FileNotFoundError as e:
        print(e)
        return
    print("=" * 50)
    print("  2025-26 NFL Offensive Statistics Lookup")
    print("=" * 50)
    while True:
        print("\nChoose a position:")
        print("  1) WR (Wide Receiver 1)")
        print("  2) RB (Running Back 1)")
        print("  3) TE (Tight End 1)")
        print("  4) Quit")
        choice = input("Enter 1, 2, 3, or 4: ").strip()
        if choice == "4" or choice.lower() in ("q", "quit", "exit"):
            print("Goodbye!")
            break
        if choice not in ("1", "2", "3"):
            print("Please enter 1, 2, 3, or 4.")
            continue
        identifier = input(
            "\nEnter a player name OR team abbreviation "
            "(e.g. 'Tyreek Hill' or 'MIA'): "
        ).strip()
        if not identifier:
            print("You didn't enter anything -- try again.")
            continue
        print()
        if choice == "1":
            rec_rus_stats_wr1(players, identifier)
        elif choice == "2":
            rec_rus_stats_rb1(players, identifier)
        elif choice == "3":
            rec_rus_stats_te1(players, identifier)

if __name__ == "__main__":
    main()
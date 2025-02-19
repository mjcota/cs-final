
"""
Analysis Functions Module

This module provides utility functions for analyzing team compositions, cheater behaviors,
and interactions between cheaters and non-cheaters in a multiplayer game dataset.

"""

def count_cheaters_per_team(teams_data, cheaters_data):
    """
    Count the number of teams with 0, 1, 2, 3, or 4+ cheaters.
    """
    # Initialize dictionaries
    team_cheater_counts = {}
    unique_teams = set((match_id, team_id) for match_id, _, team_id in teams_data)

    # Count cheaters for each team
    for match_id, player_id, team_id in teams_data:
        if player_id in cheaters_data:  # Only process cheaters
            team_key = (match_id, team_id)
            if team_key not in team_cheater_counts:
                team_cheater_counts[team_key] = 0
            team_cheater_counts[team_key] += 1

    # Summarize the results
    summary = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    for team in unique_teams:
        count = team_cheater_counts.get(team, 0)  # Default to 0 if team has no cheaters
        if count >= 4:
            summary[4] += 1
        else:
            summary[count] += 1

    return summary


def get_non_cheater_victims(kills_data, cheaters_data):
    """
    Filters kills to identify victims who are not cheaters at the time of the kill.
    """
    # Extract start dates for all cheaters
    cheater_start_dates = {acc_id: start_date for acc_id, (start_date, _) in cheaters_data.items()}
    cheaters_set = set(cheater_start_dates.keys())  
    seen_victims = set()  
    result = []

    # Iterate through each kill event in the game to identify non-cheater victims. 
    for match_id, killer_id, victim_id, kill_date in kills_data:
        if killer_id not in cheaters_set or cheater_start_dates[killer_id] > kill_date:
            continue
        if victim_id in seen_victims or (victim_id in cheaters_set and cheater_start_dates[victim_id] <= kill_date):
            continue
        result.append((victim_id, kill_date))
        seen_victims.add(victim_id)

    return result


def get_converted_to_cheater(victims_list, cheaters_data):
    """
    Counts victims who became cheaters after being killed.
    """
    cheater_start_dates = {acc_id: start_date for acc_id, (start_date, _) in cheaters_data.items()}
    return sum(
        1
        for victim_id, kill_date in victims_list
        if victim_id in cheater_start_dates and cheater_start_dates[victim_id] > kill_date
    )


def get_observable_cheaters(kills_data, cheaters_data):
    """
    Identifies active cheaters in each match who killed at least 3 players
    and records the kill date of their 3rd kill.
    """
    # Dictionary to keep track of each cheater's kills in a match
    cheater_kill_counts = {}

    # Iterate through each kill event to identify cheaters who achieved at least 3 kills in a match.
    for match_id, killer_id, _, kill_date in kills_data:
        if killer_id in cheaters_data:
            start_date, ban_date = cheaters_data[killer_id]
            if start_date <= kill_date <= ban_date:
                key = (match_id, killer_id)  # Unique identifier for the cheater in a specific match

                if key not in cheater_kill_counts:
                    cheater_kill_counts[key] = {"count": 0, "third_kill_date": None}
                
                cheater_kill_counts[key]["count"] += 1
                if cheater_kill_counts[key]["count"] == 3:
                    cheater_kill_counts[key]["third_kill_date"] = kill_date

    # Filter the results to return only cheaters who achieved at least 3 kills in a match
    return {
        key: value["third_kill_date"]
        for key, value in cheater_kill_counts.items()
        if value["count"] >= 3
    }

def get_observers(kills_data, observable_cheaters):
    """
    Identifies non-cheaters in each match whose kill_date is after the kill_date_of_the_third
    or who were not killed in the match, and keeps the most recent interaction.
    """
    # Dictionary to track victims per match and their kill dates
    victims_per_match = {}
    all_players_per_match = {}

    for match_id, killer_id, victim_id, kill_date in kills_data:
        if match_id not in victims_per_match:
            victims_per_match[match_id] = {}
        victims_per_match[match_id][victim_id] = kill_date

        # Track all players in the match (killers and victims)
        if match_id not in all_players_per_match:
            all_players_per_match[match_id] = set()
        all_players_per_match[match_id].add(killer_id)
        all_players_per_match[match_id].add(victim_id)

    # Dictionary to store the latest interaction for each victim_id
    latest_dates = {}

    # Process each cheater's 3rd kill in observable_cheaters
    for (match_id, cheater_id), kill_date_of_the_third in observable_cheaters.items():
        # Get victims for this match
        match_victims = victims_per_match.get(match_id, {})
        all_players = all_players_per_match.get(match_id, set())

        # Find victims killed after the 3rd kill date
        for victim_id, victim_kill_date in match_victims.items():
            if victim_kill_date > kill_date_of_the_third:
                if victim_id not in latest_dates or kill_date_of_the_third > latest_dates[victim_id]:
                    latest_dates[victim_id] = kill_date_of_the_third

        # Identify players who were not killed in the match
        players_not_killed = all_players - set(match_victims.keys())
        for victim_id in players_not_killed:
            if victim_id not in latest_dates or kill_date_of_the_third > latest_dates[victim_id]:
                latest_dates[victim_id] = kill_date_of_the_third

    # Convert the dictionary to a list of tuples
    return [(victim_id, latest_date) for victim_id, latest_date in latest_dates.items()]
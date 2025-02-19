
"""
Simulations and Statistical Analysis Module

This module provides functions for performing randomizations on game data and
calculating statistical measures such as mean, standard deviation, and confidence intervals.
It includes tools for shuffling data and simulating random scenarios.

"""

import random
from math import sqrt
from typing import List, Dict

def randomize_team_ids(teams_data, num_randomizations=1):
    """
    Randomly shuffle team IDs among players within each match for multiple iterations.
    """
    randomizations = []
    
    for _ in range(num_randomizations):
        # Group players by match_id
        matches = {}
        for match_id, player_id, team_id in teams_data:
            matches.setdefault(match_id, []).append((player_id, team_id))
        
        # Shuffle team IDs within each match
        randomized_data = []
        for match_id, players in matches.items():
            team_ids = [team_id for _, team_id in players]
            random.shuffle(team_ids)
            randomized_data.extend(
                (match_id, player_id, shuffled_team_id)
                for (player_id, _), shuffled_team_id in zip(players, team_ids)
            )
        
        # Append the randomized data to the results
        randomizations.append(randomized_data)
    
    return randomizations

def randomize_player_ids(kills_data, num_randomizations=1):
    """
    Randomizes player IDs (killer and victim) within each match for multiple iterations.
    """
    randomizations = []
    
    for _ in range(num_randomizations):
        # Group kills by match_id
        matches = {}
        for match_id, killer_id, victim_id, kill_date in kills_data:
            matches.setdefault(match_id, []).append((killer_id, victim_id, kill_date))
        
        # Randomize player IDs within each match
        randomized_data = []
        for match_id, events in matches.items():
            unique_players = {player for killer_id, victim_id, _ in events for player in (killer_id, victim_id)}
            shuffled_ids = list(unique_players)
            random.shuffle(shuffled_ids)
            player_mapping = {original: shuffled for original, shuffled in zip(unique_players, shuffled_ids)}
            
            randomized_data.extend(
                (match_id, player_mapping[killer_id], player_mapping[victim_id], kill_date)
                for killer_id, victim_id, kill_date in events
            )
        
        # Append the randomized data to the results
        randomizations.append(randomized_data)
    
    return randomizations

def calculate_statistics(data):
    """
    Calculate mean, standard deviation, and 95% confidence interval for a list of numbers,
    rounded to 1 decimal place.
    """
    # Step 1: Calculate mean
    mean = round(sum(data) / len(data), 1)

    # Step 2: Calculate standard deviation
    variance = round(sum((x - mean) ** 2 for x in data) / (len(data) - 1), 1)
    std_dev = round(sqrt(variance), 1)

    # Step 3: Calculate 95% confidence interval
    ci_half_width = round(1.96 * (std_dev / sqrt(len(data))), 1)
    ci_lower = round(mean - ci_half_width, 1)
    ci_upper = round(mean + ci_half_width, 1)

    # Step 4: Return the results
    return {
        "mean": mean,
        "std_dev": std_dev,
        "ci_lower": ci_lower,
        "ci_upper": ci_upper,
    }


def calculate_confidence_interval_dict(data_dict):
    """
    Calculate mean, standard deviation, and 95% confidence interval for each category
    across all randomizations.
    """
    # Infer categories from the first dictionary
    categories = data_dict[0].keys()
    summary_statistics = {}

    for category in categories:
        # Extract the values for the current category across all randomizations
        category_counts = [count[category] for count in data_dict]

        # Use the base function to calculate statistics
        summary_statistics[category] = calculate_statistics(category_counts)

    return summary_statistics

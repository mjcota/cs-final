
"""
Output Module

This module provides functions to prepare data and perform analyses for 
Answers 1, 2, and 3. Each function is designed to work with data loaded 
from external files, and it calculates real results as well as simulations 
with confidence intervals for comparison.

Dependencies:
- `data_loader`: To load data from external files.
- `analysis_functions`: To perform specific analytical operations.
- `simulations`: For randomization and statistical calculations.
"""

import data_loader
import analysis_functions
import simulations


def prepare_data(teams_path: str, cheaters_path: str, kills_path: str):
    """
    Load the data from the provided file paths.
    """
    teams_data = data_loader.get_team_ids_data(teams_path)
    cheaters_data = data_loader.get_cheaters_data(cheaters_path)
    kills_data = data_loader.get_kills_data(kills_path)
    return teams_data, cheaters_data, kills_data


def answer_1(teams_data, cheaters_data, num_randomizations=20):
    """
    Perform real data analysis and simulations for Answer 1.
    """
    # PART 1: Real data - Cheater Counts
    real_cheater_counts = analysis_functions.count_cheaters_per_team(teams_data, cheaters_data)

    # PART 2: Simulation - Confidence Intervals for Cheater Counts
    randomized_teams = simulations.randomize_team_ids(teams_data, num_randomizations)
    sim_cheater_counts = [analysis_functions.count_cheaters_per_team(teams, cheaters_data) for teams in randomized_teams]
    ci_sim_cheater_counts = simulations.calculate_confidence_interval_dict(sim_cheater_counts)

    return real_cheater_counts, ci_sim_cheater_counts


def answer_2(kills_data, cheaters_data, randomized_kills):
    """
    Perform real data analysis and simulations for Answer 2.
    """
    # Real data calculation
    non_cheater_victims = analysis_functions.get_non_cheater_victims(kills_data, cheaters_data)
    converted_from_killed = analysis_functions.get_converted_to_cheater(non_cheater_victims, cheaters_data)

    # Simulation: Using precomputed randomized kills to find converted from killed
    sim_non_cheater = [analysis_functions.get_non_cheater_victims(kills, cheaters_data) for kills in randomized_kills]
    sim_converted_from_killed = [analysis_functions.get_converted_to_cheater(non_cheater_victims, cheaters_data) for non_cheater_victims in sim_non_cheater]
    ci_confidence_intervals = simulations.calculate_statistics(sim_converted_from_killed)

    return converted_from_killed, ci_confidence_intervals


def answer_3(kills_data, cheaters_data, randomized_kills):
    """
    Perform real data analysis and simulations for Answer 3.
    """
    # Real data calculation
    observable_cheaters = analysis_functions.get_observable_cheaters(kills_data, cheaters_data)
    observers = analysis_functions.get_observers(kills_data, observable_cheaters)
    converted_from_observed = analysis_functions.get_converted_to_cheater(observers, cheaters_data)

    # Simulation: Using precomputed randomized kills to find converted from observed
    sim_observable_cheaters = [analysis_functions.get_observable_cheaters(kills, cheaters_data) for kills in randomized_kills]
    sim_observers = [analysis_functions.get_observers(kills, observable_cheaters) for kills, observable_cheaters in zip(randomized_kills, sim_observable_cheaters)]
    sim_converted_from_observed = [analysis_functions.get_converted_to_cheater(observers, cheaters_data) for observers in sim_observers]
    ci_sim_converted_from_observed = simulations.calculate_statistics(sim_converted_from_observed)

    return converted_from_observed, ci_sim_converted_from_observed


"""
Data Loader Module

This module provides utility functions for loading and cleaning game-related data
from text files. It processes data for teams, cheaters, and kills, ensuring
consistent formatting for downstream analysis.

"""

from datetime import datetime
import csv

def clean_account_id(account_id):
    """Removes 'account.' prefix from the account ID."""
    return account_id.replace("account.", "")

def get_team_ids_data(fpath):
    """
    Reads the 'team_ids.txt' file and extracts match ID, player account ID, and team ID.
    Returns a list of tuples: [(match_id, player_id, team_id), ...]
    """
    with open(fpath, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        return [
            (row[0], clean_account_id(row[1]), int(row[2]))
            for row in reader
        ]

def get_cheaters_data(fpath):
    """
    Reads the 'cheaters.txt' file and extracts player account IDs and 
    cheating start and ban dates.
    Returns a dictionary: {account_id: (start_date, ban_date), ...}
    """
    with open(fpath, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        return {
            clean_account_id(row[0]): (
                datetime.strptime(row[1], '%Y-%m-%d'),
                datetime.strptime(row[2], '%Y-%m-%d')
            )
            for row in reader
        }

def get_kills_data(fpath):
    """
    Reads the 'kills.txt' file and extracts match ID, killer account ID, victim account ID, 
    and kill timestamp.
    Returns a list of tuples: [(match_id, killer_id, victim_id, kill_date), ...]
    """
    with open(fpath, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        return [
            (
                row[0],
                clean_account_id(row[1]),
                clean_account_id(row[2]),
                datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f')
            )
            for row in reader
        ]
        

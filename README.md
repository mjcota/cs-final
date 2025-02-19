UBG Cheating Analysis

Overview

This project is the final assignment for the course, requiring the application of computational thinking and programming skills to investigate an empirical social science question. The focus of the study is to analyze homophily and social contagion in cheating behavior in the massive multiplayer online game PlayerUnknown's Battlegrounds (PUBG). Cheating in this context refers to the use of unapproved software that grants players unfair advantages (e.g., seeing through walls).

The hypotheses under investigation are:

Cheaters tend to associate with other cheaters more than expected by chance.

Players who interact with cheaters are more likely to become cheaters themselves.

Players who are killed by cheaters are more likely to become cheaters themselves.

To test these hypotheses, we simulate alternative game universes in which players participate under different conditions and compare real-world observations to these randomized scenarios.

Project Structure

This project follows best practices in programming, ensuring that the code is modular, legible, and optimized. It is structured into multiple modules to maintain separation of concerns:

1. Data Loader Module

Provides utility functions for loading and cleaning game-related data from text files.

Ensures consistent formatting of data for downstream analysis.

Processes data on teams, cheaters, and kills.

2. Analysis Functions Module

Contains functions to analyze team compositions and behaviors of cheaters.

Investigates interactions between cheaters and non-cheaters in the dataset.

3. Simulations and Statistical Analysis Module

Performs data randomization to simulate alternative game universes.

Computes statistical measures such as mean, standard deviation, and confidence intervals.

Includes tools for shuffling data and simulating random scenarios to test hypotheses.

4. Output Module

Prepares data and performs analyses to answer the research questions.

Works with data from external files and calculates real results alongside simulated comparisons.

Utilizes:

data_loader for loading data.

analysis_functions for specific analytical operations.

simulations for randomization and statistical analysis.

Constraints and Guidelines

Allowed Tools: Only fundamental Python data types (lists, tuples, dictionaries, etc.) and basic modules (datetime, pickle, deepcopy, itertools, os, etc.) are permitted.

Prohibited Tools: Libraries such as pandas, sqlite, networkx, and numpy are NOT allowed to ensure fundamental programming concepts are tested.

Modular Design: The code is structured to allow flexibility for future modifications, such as adapting to new datasets or changing the focus of analysis.

Code Legibility: Functions and modules are named informatively, avoiding direct references to problem set instructions.

AI Usage: Generative AI tools (e.g., Copilot) are permitted, but collaboration with other individuals or external sources is prohibited.


# PUBG Cheating Analysis

## 📌 Overview

This project applies computational thinking and programming principles to analyze social dynamics in gaming, specifically focusing on cheating behavior in PUBG. The modular approach ensures maintainability and adaptability for future studies.

## 🔍 Research Hypotheses

1️⃣ Cheaters tend to associate with other cheaters more than expected by chance.
2️⃣ Players who interact with cheaters are more likely to become cheaters themselves.
3️⃣ Players who are killed by cheaters are more likely to become cheaters themselves.

To test these hypotheses, we simulate alternative game universes in which players participate under different conditions and compare real-world observations to these randomized scenarios.

## 📂 Project Structure

This project follows best practices in programming, ensuring that the code is modular, legible, and optimized. It is structured into multiple modules to maintain separation of concerns:

### 📁 1. Data Loader Module

📌 Provides utility functions for loading and cleaning game-related data from text files.
📌 Ensures consistent formatting of data for downstream analysis.
📌 Processes data on teams, cheaters, and kills.

#### 📁 2. Analysis Functions Module

📌 Contains functions to analyze team compositions and behaviors of cheaters.
📌 Investigates interactions between cheaters and non-cheaters in the dataset.

#### 📁 3. Simulations and Statistical Analysis Module

📌 Performs data randomization to simulate alternative game universes.
📌 Computes statistical measures such as mean, standard deviation, and confidence intervals.
📌 Includes tools for shuffling data and simulating random scenarios to test hypotheses.

#### 📁 4. Output Module

📌 Prepares data and performs analyses to answer the research questions.
📌 Works with data from external files and calculates real results alongside simulated comparisons.






#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[8]:


# Define the initial data
data = {
  "Player": ["McGwire", "Sosa", "Griffey", "Castilla", "Gonzalez", "Galaragga", "Palmeiro", "Vaughn", "Bonds", "Bagwell",
        "Piazza", "Thome", "Thomas", "T. Martinez", "Walker", "Burks", "Buhner"],
  "Yi": [7, 9, 4, 7, 3, 6, 2, 10, 2, 2, 4, 3, 2, 5, 3, 2, 6],
  "ni": [58, 59, 74, 84, 69, 63, 60, 54, 53, 60, 66, 66, 72, 64, 42, 38, 58],
  "AB": [509, 643, 633, 645, 606, 555, 619, 609, 552, 540, 561, 440, 585, 531, 454, 504, 244],
  "pi": [0.138, 0.103, 0.089, 0.071, 0.074, 0.079, 0.070, 0.066, 0.067, 0.063, 0.057, 0.068, 0.050, 0.053, 0.051, 0.042, 0.062],
  "HR": [70, 66, 56, 46, 45, 44, 43, 40, 37, 34, 32, 30, 29, 28, 23, 21, 15], 
}

df = pd.DataFrame(data)

# Calculate pre-season probabilities
df['p'] = df['Yi'] / df['ni'] 

# Calculate Xi using arcsin transformation (using 'p')
df['Xi'] = np.sqrt(df['ni']) * np.arcsin(2 * df['p'] - 1)

# Calculate the mean (X_bar) and variance (V) of Xi
X_bar = df['Xi'].mean()
V = sum((xi - X_bar) ** 2 for xi in df['Xi'])

# Number of players (p)
p = len(df)

# Calculate JSi estimator
df['JSi'] = X_bar + (1 - ((p - 3) / V)) * (df['Xi'] - X_bar)

# Calculate mu_i using the given transformation formula 
df['mu_i'] = np.sqrt(df['ni']) * np.arcsin(2 * df['pi'] - 1)  

# Calculate the estimated number of home runs using both approaches
df['HR_hat'] = df['pi'] * df['AB']
df['HR̂_s'] = df['Yi'] / df['ni'] * df['AB']

# Display the results
print(df) 


# In[13]:


# Function to create the DataFrame with estimates
def create_estimate_df(df):
    return pd.DataFrame({
        'Player': df['Player'],
        'MLE_est': df['Xi'],  # Use your specific column name for MLE estimates
        'GJS_est': df['JSi']    # Use your specific column name for GJS estimates
    })

# Plot shrinkage
def plot_shrinkage(df, players_to_plot):
    estimate_df = create_estimate_df(df)
    estimate_df_subset = estimate_df[estimate_df['Player'].isin(players_to_plot)] 

    for _, row in estimate_df_subset.iterrows():
        player = row['Player']
        mle_est = row['MLE_est']
        gjs_est = row['GJS_est']
        plt.plot([mle_est, gjs_est], [2, 1], marker='o', label=player)

    plt.text(np.mean([estimate_df['MLE_est'].min(), estimate_df['MLE_est'].max()]), 2.25, 'MLE Estimates', horizontalalignment='center')
    plt.text(np.mean([estimate_df['MLE_est'].min(), estimate_df['MLE_est'].max()]), 0.75, 'James-Stein Estimates', horizontalalignment='center')

    plt.xlim(estimate_df['MLE_est'].min() - 0.1, estimate_df['MLE_est'].max() + 0.1)
    plt.title("Shrinkage Effect in James-Stein Estimator")
    plt.legend()
    plt.tight_layout()
    plt.show()

players_to_plot = ["Sosa", "Griffey"]
plot_shrinkage(df, players_to_plot)


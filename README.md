# Baseball Performance Predictions with James-Stein Estimator

This project explores the application of the James-Stein estimator to predict home run strike rates of baseball players based on 1998 pre-season data. It challenges traditional prediction methods by providing more accurate estimates under specific conditions.

## Background

In statistical analysis, accurately estimating parameters is crucial for making informed decisions. While the Maximum Likelihood Estimate (MLE) is commonly used, it has limitations, particularly when estimating multiple parameters. The James-Stein estimator offers a counter-intuitive approach that yields more accurate estimates by leveraging shared information across parameters.

## Dataset

The dataset comprises pre-season statistics from 17 top baseball players in 1998, focusing on predicting their full-season home run strike rates. The `data` dictionary includes player names, home runs (`Yi`), times at bat (`ni`), at-bats (`AB`), pre-season probabilities (`pi`), and actual home runs (`HR`).

## Analysis

The project employs the James-Stein estimator to refine the accuracy of home run strike rate predictions. Traditional methods based on direct extrapolation from pre-season performance are compared to James-Stein estimates, demonstrating the latter's superior accuracy.

### Calculations

- Pre-season probabilities are calculated as `Yi / ni`.
- `Xi` uses an arcsin transformation.
- The mean (`X_bar`) and variance (`V`) of `Xi` are computed.
- The James-Stein estimator (`JSi`) and estimated number of home runs using both approaches are calculated.

## Visualization

A function `plot_shrinkage` visualizes the shrinkage effect of the James-Stein estimator by comparing MLE and James-Stein estimates for selected players.

## Results

The application of the James-Stein estimator resulted in more accurate predictions of players' home run strike rates compared to naive MLE-based estimates.

## Conclusion

The James-Stein estimator's application to baseball performance predictions showcases its potential to improve prediction accuracy by adjusting individual estimates based on collective data analysis. This project demonstrates the value of innovative statistical methodologies in sports analytics and beyond.

## How to Run

1. Ensure you have Python and necessary libraries (e.g., pandas, numpy, matplotlib) installed.
2. Clone this repository.
3. Run the provided Python script to generate the dataset, perform calculations, and visualize the results.

## Contributors

A.Robson

## Example

### An example of how Shrinkage works. Note the JS estimate for Sosa and Griffey are closer to $\mu_i$ than $X_i$ (i.e. demonstrating shrinkage towards the mean) 

<div align="center">
  
  ![JS_plot](https://github.com/andrewrobson3000/Bayesian-Shrinkage-Statistical-Estimates-with-James-Stein/assets/87878168/276f7c96-f1ec-495b-997b-ac55aa239b4b)

</div>

# [Spotify Usage Data Analysis](https://github.com/nazhifkojaz/my-spotify-usage-analysis/)

This is a fun project where I do various data science-y kinda things on my own spotify usage data.
## [Data Collection](https://github.com/nazhifkojaz/my-spotify-usage-analysis/blob/main/spanalysis_datacollect.ipynb)
This jupyter notebook includes:
- Explain the data I'm using and how to obtain/request it from spotify
- Preparing the data and separated the music and podcast streaming history
- Collecting additional data using [Spotify Web API](https://developer.spotify.com/)
- Simple exploratory data analysis (EDA) in order create a to-do list for the data cleaning/processing stage

## [Data Analysis](https://github.com/nazhifkojaz/my-spotify-usage-analysis/blob/main/spanalysis_dataanalysis.ipynb)
This jupyter notebook includes:
- Analysing the trend in my streaming activity on spotify through out the year (like activity per month/year, top artists, etc)
- Checking if there is any correlation in the quantity of tracks I listened from an artist to the overall streaming duration (and also its average streaming duration)
- Visualizing my top artists and how much I have listened to their music throughout my subscription in spotify using [Bar Chart Race](https://www.dexplo.org/bar_chart_race/) library

## Notes
the list goes on as I add new things. This project will serve as a practice project where as I explore more the world of data science and machine learning.
if you have any suggestion on things I should try on, feel free to shoot a message on my [Twitter / X](https://twitter.com/nazhifkojaz).

## Installation
1. Create the environment from the `environment.yml` file
```bash
conda env create -f environment.yml
```
2. Activate the environment
```bash
conda activate my-spotify-usage-analysis
```

## License and Data Usage
This project is licensed under the MIT License, which allows you to freely use, modify, and distribute the code as long as appropriate attribution is given. The data collected from the Spotify API is used for educational purposes. Please refer to the [Spotify Developer Terms of Service](https://developer.spotify.com/terms/) for more information on the usage of Spotify data.




## Inspiration
While researching for COVID-19 data, I noticed that all of the popular visualization resources either only showed the [current situation](https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html), or showed a [quick timeline](https://kitware.github.io/covid-19-vis/). This is not very helpful for researching the number of cases for a specific county on any day since it provides too general of a visualization. Thus, I created a day-by-day visualization tool that allows researchers to query the data for a specific day in a user friendly and visually appealing way.

## What it does
This is a web API to allow the user to visualize a snapshot of the COVID-19 situation in the USA on a specific day. The user can see exactly how many cases there were in a specific county in this snapshot of time.

## How I built it
This application is built using Dash with Python. This is used with the Bootstrap framework to make the site attractive.

## Challenges I ran into
It was difficult to actually find the data in a usable form online, because it was either fragmented or contained irrelevant data to my purpose. This introduced me to the pandas libraries to clean and filter the dataset. I've never worked with visualizations before, so it was also difficult to find a framework to create those visualize for a web API.

## Accomplishments that I'm proud of
I created my first real web API and made a visually appealing application to solve a real world problem, while introducing me to data science in the process.

## What I learned
I learned the fundamentals of data science through cleaning and filtering data and how to make useful visualizations by using python's many data science libraries.

## What's next for COVID-19 Date Selector
In the future I will implement different types of visualization of the data to provide a more complete picture of the situation.

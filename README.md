## Inspiration
While researching for COVID-19 data, I noticed that all of the popular visualization resources either only showed the [current situation](https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html), or showed a [quick timeline](https://kitware.github.io/covid-19-vis/). This is not very helpful for researching the number of cases in a specific county on any day as it provides too general of a visualization. Thus, I created a day-by-day visualization tool that allows researchers to query the data for a specific day in a user friendly and visually appealing way.

## What it does
This is a web API to allow the user to visualize a snapshot of the COVID-19 situation in the USA on a specific day. The user can see exactly how many cases there were in a specific county in this snapshot of time. 

## How we built it
This application is built using Dash with Python, the Plotly library to generate the choropleth map, the Bootstrap framework to quickly develop the CSS.

## Challenges we ran into
It was difficult to actually find the data in a usable form online, because it was either fragmented or contained irrelevant data to my purpose. This introduced me to the pandas libraries to clean and filter the dataset. I've never worked with visualizations of datasets before, so the hardest part was actually starting.

## Accomplishments that we're proud of
I created my first deployable web API and made a visually appealing application to solve a real world problem, while introducing me to data science concepts along the way.

## What we learned
I learned the fundamentals of data science through cleaning and filtering data and how to make useful visualizations by taking advantage of python's many data science libraries.

## What's next for COVID-19 Date Selector
In the future I will implement different types of visualization of the data like different graphs to provide a more complete picture of the situation.

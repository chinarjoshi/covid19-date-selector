[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/cjoshi7/covid19-date-selector">
    <img src="images/logo.png" alt="Logo" width="100" height="100">
  </a>

  <h1 align="center">COVID-19 Date Selector</h1>

  <p align="center">
    Visualize the spread of the coronavirus on a day-by-day basis.
    <br />
    <a href="https://github.com/cjoshi7/covid19-date-selector"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://youtu.be/v6lsjcFfK9Q">View Demo</a>
    ·
    <a href="https://github.com/cjoshi7/covid19-date-selector">Report Bug</a>
    ·
    <a href="https://github.com/cjoshi7/covid19-date-selector">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<p align="center">
  <a href="https://github.com/cjoshi7/covid19-date-selector">
    <img src="images/deaths.png" alt="example-image" width=700 height=500>
  </a>
</p>


### Inspiration
While researching for COVID-19 data, I noticed that all of the popular visualization resources either only showed the [current situation](https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html), or showed a [quick timeline](https://kitware.github.io/covid-19-vis/). This is not very helpful for researching the number of cases in a specific county on any day as it provides too general of a visualization. Thus, I created a day-by-day visualization tool that allows researchers to query the data for a specific day in a user friendly and visually appealing way.

### What it does
This is a web API to allow the user to visualize a snapshot of the COVID-19 situation in the USA on a specific day. The user can see exactly how many cases there were in a specific county in this snapshot of time. 

### How I built it
This application is built using Dash with Python, the Plotly library to generate the choropleth map, and the Bootstrap framework to quickly develop the CSS. The New York Time's COVID-19 dataset was used along with a JSON map of the United States from Plotly.

### Challenges I ran into
It was difficult to actually find the data in a usable form online, because it was either fragmented or contained irrelevant data to my purpose. This introduced me to the pandas libraries to clean and filter the dataset. I've also never worked with visualizations of datasets before, so the hardest part was actually starting.

### Accomplishments that I'm proud of
I created my first deployable web API and made a visually appealing application to solve a real world problem, while introducing me to data science concepts along the way.

### What I learned
I learned the fundamentals of data science through cleaning and filtering data and how to make useful visualizations by taking advantage of python's many data science libraries. I also learned how to use a new web application framework with Dash.


### Built With

* [Dash](https://plotly.com/dash)
* [Bootstrap](https://getbootstrap.com)


## Getting Started

No API key is needed to access the tool, so the application may be locally run through the python file.

### Prerequisites

The prerequisite frameworks and libraries are dash, plotly, and pandas.
* pip
  ```sh
  pip install requirements.txt
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/cjoshi7/covid19-date-selector
   ```
2. Install prerequisite packages
   ```sh
   pip install requirements.txt
   ```
4. Directly run the python file
   ```sh
   python covid19-date-selector/app.py
   ```


<!-- USAGE EXAMPLES -->
## Usage

This tool can be used for research purposes to find the exact number of cases in a specific county on any day. It is useful to see the patterns of infection and death rate increases/decreases. For example, it can be seen that the number of infections skyrocketed in early January after the holiday season. The tool is useful for establishing patterns such as this.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

__See the [open issues](https://github.com/cjoshi7/covid19-date-selector) for a list of proposed features (and known issues).__
<br>
<p>
  The following features will be implemented in the indefinite future:
  <ol>
    <li>
      Expanded dataset to include:
      <ul>
        <li>Mask usage</li>
        <li>Population density</li>
        <li>Demographic breakdown</li>
      </ul>
    </li>
    <li>Dark theme through altered CSS</li>
    <li>An option to use the program in the command line</li>
  </ol>
</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->


<!-- CONTACT -->
## Contact

Chinar Joshi - chinarjoshi7@gmail.com

Project Link: [https://github.com/cjoshi7/covid19-date-selector](https://github.com/cjoshi7/covid19-date-selector)


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Virus Icon](https://dndi.org/diseases/covid-19/target-product-profile/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png

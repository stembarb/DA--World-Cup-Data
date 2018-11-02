# 2018 FIFA World Cup Russia™ Prediction Project

## Table of Contents

* [Description](#description)
* [Tools & Dependencies](#tools)
* [Installation](#installation)
* [Contributing](#contributing)
* [License](#license)


### Description

The goal of this notebook is to show how I collected data from the FIFA World Cup website for the 2018 World Cup Russia - Group Stage Prediction Project. Data was collected using a web crawler due to lack of API. 

I collected groups statistics for all FIFA World Cups between 1994 and 2014. 

That gives us 6 FIFA World Cups:

 - 2014 FIFA World Cup Brazil™
 - 2010 FIFA World Cup South Africa™
 - 2006 FIFA World Cup Germany™
 - 2002 FIFA World Cup Korea/Japan™
 - 1998 FIFA World Cup France™
 - 1994 FIFA World Cup USA™

The tournaments between 1998 and 2014 included 32 teams, divided into eight groups (A to H) - four teams (countries) per group. 1994 FIFA World Cup USA™ included 24 teams, divided into six groups (A to F) - four teams (countries) per group.

For each World Cup edition, I collected the following groups' statistics:

 - Group - name of the group
 - Teams - name of the team (country)
 - Match played - how many matches did the team play
 - Match won - how many matches it won    
 - Draw - number of draws
 - Lost - number of loses
 - Goals for - total number of goals
 - Goals against - total number of lost goals
 - Goals difference - difference between goals for and against
 - Points - total points

I went through the process of building this web scraper in the [Let the robot do your work! Web scraping with Python!](https://medium.com/ub-women-data-scholars/let-the-robot-do-your-work-web-scraping-with-python-9c147fb7690f) article posted on Medium. 

## Tools & Dependencies

This data is publicaly accessible on the FIFA website in the <a href="https://www.fifa.com/fifa-tournaments/statistics-and-records/worldcup/index.html">statistics and records section</a>. According to the `robots.txt`, data scraping from the statistics and records page is allowed [June 10, 2018].

Analysis has been performed in the [Jupyter Notebook](http://jupyter.org/), using Python 3.x. 

The following libraries were used:
* [Requests](http://docs.python-requests.org/en/master/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
* [Pandas](https://pandas.pydata.org/)

## Installation

To run this project:
  
1. With python 3.x installed, create a virtual environment and activate it as shown:
  
```shell
  virtualenv -p python3 my_virtualenv
  source my_virtualenv/bin/activate
```
2. Clone this repository into your virtual environment:  

```shell
git clone https://github.com/BarbaraStempien/DA--World-Cup-Data.git
```
3. Install project dependencies:  

```shell
pip install -r DA--World-Cup-Data/requirements.txt
```
  
4. Open Jupter Notebook, and run the project or open `web_scraping.py` in your code editor.


## Contributing

I accept contributions. For details, check out [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT License](LICENSE)

Copyright (c) 2018 Barbara Stempien

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

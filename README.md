# Data Collection
### 2018 FIFA World Cup Russia™ Prediction Project

The goal of this notebook is to show how I collected data from the FIFA World Cup website. Data was collected using a web crawler, due to lack of API.

The content of this notebook is as follows:

1. Web crawler code in .py format - heavily commented version, used to teach others how to build a similar program
2. Web crawler code in Jupyter notebook format 
3. requirements.txt

### Dependencies

With python 3.x installed, create a virtual environment and activate it as shown:
```
  virtualenv -p python3 my_virtualenv
  source my_virtualenv/bin/activate
```
The following libraries were used::
* [Requests](http://docs.python-requests.org/en/master/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
* [Pandas](https://pandas.pydata.org/)

### Running the project

Clone this repository into your virtual environment, install project dependencies and then run the project as shown below:
```
git clone https://github.com/bara-bash/worldcupproject.git
pip install -r worldcupproject/requirements.txt
python worldcupproject/Web_Scraping.py
```

## License

This project is licensed under the MIT License.


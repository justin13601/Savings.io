![Savings.io](/imgs/savings_logo.png)

---------  

# Savings.io

The COVID-19 pandemic has forever changed the lives of billions of people across the world. As a direct result of the economic shutdown that followed the pandemic, the unemployment rate in Canada more than doubled from 5.6% in February 2020 to a record high 13.7% in May 2020 [1]. With so many jobs lost, many people found themselves without their pre-pandemic financial support. An emergency savings fund that one would accumulate throughout their career can drastically reduce the financial impacts of such a disaster. Additionally, along with the ever-increasing popularity of freelance work amongst students, it is all-the-more important to cultivate a sense of financial literacy with savings and investments.

Savings.io is a webapp designed to strategically help students and others set aside a small amount of money each month towards an emergency savings fund through the use of an extensive cost-of-living dataset. It also advocates for financial investment education by providing resources and links to guides and articles. Finally, it is able to return US securities determined through a ML sentiment analysis model (VADER) to be performing "well", which acts as a good starting point for beginner traders.

[![Python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://colab.research.google.com/)

![License](https://img.shields.io/github/license/justin13601/AICancer) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/justin13601/Savings.io/HEAD?filepath=%2Fnotebooks%2Finvestment_portfolio.ipynb)

**Credits:**
- https://github.com/kimmc6008
- https://github.com/dreamspeedrun
- https://github.com/justin13601
- https://github.com/donmin062501

***Disclaimer:** This is purely an educational project. The information in this repository is not intended or implied to be a substitute for professional financial advice. All content, including text, graphics, images and code, contained in or available through this repository is for educational purposes only.*


## Dependencies
- NumPy
- Pandas
- Matplotlib
- Yahoo-fin
- BeautifulSoup
- NLTK
- Pandas-Datareader
- Twython

## Features: 
- Uses NUMBEO Cost of Living Dataset
- Provides suggestions on monthly amount in CAD to save towards an emergency fund
- News scrubbing for US stocks via FinViz
- Sentiment analysis for investment portfolio using VADER
- Displays resources for students to increase their financial literacy
- Python 3.6.10

## Quick Start

Install necessary packages:

    pip install -r requirements.txt
    
Change working directory to project directory
    ...
    $ cd path/to/project/directory
    ...
    
Run webapp server:

    python manage.py runserver

Access webapp at indicated localhost address.


## References
[1] Government of Canada, Statistics Canada, “The Daily — Labour Force Survey, September 2020,” Statcan.gc.ca, 2020. https://www150.statcan.gc.ca/n1/daily-quotidien/201009/dq201009a-eng.htm (accessed Feb. 21, 2021).

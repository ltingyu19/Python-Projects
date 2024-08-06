"""
File: webcrawler.py
Name: 劉庭宇
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        # ---algo---
        # 1. loop over the data imported by soup
        # 2. re-organize it into lines
        # 3. re-organize it into lists
        # 4. re-format it into str without "," in the numbers
        # 5. process the values and add them up

        # define all parameters to be used later
        tags = soup.find_all('tbody')
        number_boys = []
        number_girls = []
        pro_number_boys = []
        pro_number_girls = []

        value_b=0
        value_g=0

        # initial loop over data, split by lines
        for tag in tags:
            data = tag.text
            data_lists = data.split('\n')

            # second loop to splits by blank space
            for info in data_lists:
                lines = info.split()

                # to acquire specific info
                if len(lines) >1 and lines[0].isalpha and 3<len(lines)<5 :

                    # append specific info into list
                    number_boys.append(lines[1])
                    number_girls.append(lines[3])

                    # loop over newly created list of "boys" to transform them into str and getting rid of "," in the numbers
                    for value in number_boys:
                        new_value_str_boys = ''
                        for i in range (len(value)):
                            if value[i].isdigit():
                                new_value_str_boys += value[i]
                    # append newly processed data
                    pro_number_boys.append(new_value_str_boys)

                    # loop over newly created list of "girls" to transform them into str and getting rid of "," in the numbers
                    for value in number_girls:
                        new_value_str_girls = ''
                        for i in range (len(value)):
                            if value[i].isdigit():
                                new_value_str_girls += value[i]
                    # append newly processed data
                    pro_number_girls.append(new_value_str_girls)

        # calculate the final value
        for actual_value_boys in pro_number_boys:
            value_b += int(actual_value_boys)

        for actual_value_girls in pro_number_girls:
            value_g += int(actual_value_girls)

        # print out the ans
        print('Male Number: ',value_b)
        print('Female Number: ', value_g)




if __name__ == '__main__':
    main()

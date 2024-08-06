"""
File: babynames.py
Name: 劉庭宇
--------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any value.
    """
    # This part is copied from milestone 1

    new_values = {}
    new_values[year] = rank

    # If name in not in data
    if name not in name_data:
        name_data[name] = new_values

    # If name is in data
    else:

        # If name is in data and year is in conflict
        if year in name_data[name]:
            # if int is not used below, value callouts are "str" instead of "int"
            # Therefore causing an error in comparing value
            if int(rank) < int(name_data[name][year]):
                name_data[name][year] = rank

        # If name is in data BUT year is NOT in conflict
        if year not in name_data[name]:
            name_data[name][year] = rank


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.
    """

    # ---algo---
    # 1. start reading the file to get baby name data
    # 2. processing the data that are read
    # 3. add the data to the dictionary

    # reading lines from file and processing them into tokens
    with open(filename, 'r') as f:
        line_count = 0
        for line in f:
            if line_count == 0:
                year = line
                line_count += 1
            else:
                tokens = line.split(',')
                rank = tokens[0]
                boy_name = tokens[1]
                girl_name = tokens[2]

                # with tokens defined, process the parameters with strip()
                rank = rank.strip()
                boy_name = boy_name.strip()
                girl_name = girl_name.strip()
                year = year.strip()

                # add this data into database with function defined in milestone 1
                add_data_for_name(name_data, year, rank, boy_name)
                add_data_for_name(name_data, year, rank, girl_name)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """

    # ---algo---
    # 1. create a new dictionary to store the data that are added from addfile function and return the data
    name_data = {}
    for file in filenames:
        add_file(name_data, file)
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string
    """

    # ---algo---
    # 1. create a new list to store names that matches our search
    # 2. processing the input "target" to make it case insensitive
    # 3. loop over the dictionary to process it into case insensitive as well since there could be cases like "Aa" &"aa"
    # 4. using str method xxx.find() to find matching names, append it into list and return the list

    # defining new list and process input into case-insensitive
    matching_names = []
    pro_target = ''
    for ch in target:
        if ch.islower():
            pro_target += ch.upper()
        else:
            pro_target += ch

    # process data in database into case-insensitive
    for name in name_data:
        pro_name = ''
        for chara in name:
            if chara.islower():
                pro_name += chara.upper()
            else:
                pro_name += chara

        # using str methods (.find()) to look for matching names and use return index value to determine if ans exists
        index = pro_name.find(pro_target)
        if index > -1:
            matching_names.append(name)
    return matching_names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()

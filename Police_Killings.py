import csv
import urllib2
import matplotlib.pyplot as plt
import calendar

"""Access The Counted 2015 ('the-counted-2015.csv') data from 
https://www.dropbox.com/s/ohknei1ivvogq7z/the-counted-2015.csv?dl=1
"""
url_counted2015 = urllib2.urlopen(
        'https://www.dropbox.com/s/ohknei1ivvogq7z/the-counted-2015.csv?dl=1')
file_counted2015 = [row for row in csv.DictReader(url_counted2015)]
lst_killings2015 = file_counted2015 #list of dictionaries, each dictionary 
                                    # represents a particular record
                                    
"""Access The Counted 2016 ('the-counted-2016.csv') data from
https://www.dropbox.com/s/h9kff40kamgut69/the-counted-2016.csv?dl=1
"""
url_counted2016 = urllib2.urlopen(
        'https://www.dropbox.com/s/h9kff40kamgut69/the-counted-2016.csv?dl=1')
file_counted2016 = [row for row in csv.DictReader(url_counted2016)]
lst_killings2016 = file_counted2016 #list of dictionaries, each dictionary 
                                    # represents a particular record
                                    
"""Access the 'National, State, and Puerto Rico Commonwealth Totals' 
('NST-EST2015-alldata.csv') dataset from 
http://www.census.gov/popest/data/national/totals/2015/files/
NST-EST2015-alldata.csv
"""
url_population_state = urllib2.urlopen('http://goo.gl/YVgbWI')
file_population_state = [row for row in csv.DictReader(url_population_state)]
lst_allpopulation_state = file_population_state # list of dictionaries with
                                    # each dictionary containing population
                                    # estimates for each state

"""Takes in the abbreviated form of a state's name and returns the full name
Parameters:
    state: a string representing the abbreviated form of a state's name
Returns:
    a string representing the full form of the state's name
"""
def get_fullname(state):
    state_abbrev = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
    return state_abbrev[state]
    
"""Takes in a state name and a list of populations by
state as inputs. Looks for the given state in the list and returns the estimated
population in 2015 for that state.
Parameters:
    state_name: Name of a state in US
    lst_population_state: a list of dictionaries where each dictionary
    represents a record of various population estimates for each state
Returns:
    a float representing the 2015 population estimate for the given state or
    None if the state is not found in the list
"""
def get_state_population(state_name, lst_population_state):
    for record in lst_population_state:
        if record['NAME'] == state_name:
            return float(record['POPESTIMATE2015']) # POPESTIMATE2015: column
    return None             # containing population estimates for each state

"""Given a list of killings for a particular year, computes the number of 
killings for each state and maps it to the respective state.Given a list of 
population estimates, extracts each population estimate and maps it to the 
respective state. Then computes Per Capita Kills for each state.
Parameters:
    lst_allkillings: a list of dictionaries with each dictionary containing
    details of each killing.
    lst_population_state: list of dictionaries with each dictionary containing
    population estimates for each state.
Returns:
    A dictionary of dictionaries in the form: 
    {'State1': {'Population': 1, 'Killings': 1, 'Per Capita Kills': 1}, ...}
"""
def state_killings_stats(lst_allkillings, lst_population_state):
    killed_by_state = dict()
    for record in  lst_allkillings:
        state = record['state']
        if state not in killed_by_state:
            killed_by_state[state] = {'Population':0, 'Killings':0, 
                                    'Per Capita Kills' : 0}
        killed_by_state[state]['Population'] = get_state_population(
                                    get_fullname(state), lst_population_state)
        killed_by_state[state]['Killings'] += 1
     
    # Computes per capita kills using the formula: 
    # (Number of Kills / Population) * 1000000   
    for state in killed_by_state:
        killed_by_state[state]['Per Capita Kills'] = ( 
        float(killed_by_state[state]['Killings']) / 
        killed_by_state[state]['Population']) * 1000000
    return killed_by_state
        
"""Given the axis labels, graph title, y axis values
and output file name, plots a bar graph.
Parameters:
    Xs: list of X axis values 
    x_label: X axis name (string)
    axis_y: list of y axis values
    title: Name of graph (string)
    y_label: name of y axis (string)
    file_output: name of output file to be saved (string)
"""
def plot_bar(Xs, x_label, axis_y, title, y_label, file_output):
    plt.clf()
    x_axis = Xs
    y_axis = axis_y
    pos = range(len(y_axis))
    plt.xlabel(x_label)
    plt.ylabel(y_label)  
    plt.xticks(pos, x_axis)
    plt.suptitle(title)
    plt.bar(pos, y_axis, align = 'center', alpha = 0.5, width = 0.6)
    mng = plt.get_current_fig_manager()
    mng.window.showMaximized() # Plot window always maximized
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.savefig(file_output, bbox_inches='tight')
    plt.show()
    print
    print "Data plotting complete."
    print

"""Given a dictionary of dictionaries containing kills data by state and a 
string specifying whether maximum number of total or per capita kills need to be
considered, prints the name of the state with the maximum number of 
'total_or_percapita' kills and the number of kills.
Parameters:
    killed_by_state: A dictionary of dictionaries in the form: 
    {'State1': {'Population': 1, 'Killings': 1, 'Per Capita Kills': 1}, ...}
    total_or_percapita: a string representing the 'Killings' key or 
    'Per Capita Kills' key for a dictionary in killed_by_state
"""
def max_kills(killed_by_state, total_or_percapita): 
    max_kills = None
    max_state = None
    for state in killed_by_state:
        kills = killed_by_state[state][total_or_percapita]
        print "State:", get_fullname(state) 
        print "Population:", killed_by_state[state]['Population']
        print "Kills:", str(kills)
        print
        if max_kills == None or kills > max_kills:
            max_kills = kills
            max_state = get_fullname(state)
            
    if total_or_percapita == 'Killings' :
        print "State with the highest number of police killings in 2015:", (
                max_state)
        print "Total number of kills in", max_state + ": " + str(max_kills)
    else:
        print "State with the highest Police Killings Per Capita in 2015:", (
                max_state)
        print "Per Capita Kills in", max_state + ": " + str(max_kills)

"""Given a list of dictionaries where each dictionary contains details of a 
particular killing, returns a dictionary mapping each weapon victims were 
armed with to the number of kills by the weapon victims weapon type.
Parameters:
    lst_kills: list of dictionaries where each dictionary contains details of a 
particular killing
Returns:
    A dictionary in the form:
    {'Unarmed': 1, 'Weapon1': 2, ...}
"""
def kills_by_armed_unarmed(lst_kills):
    result = dict()
    for record in lst_kills:
        armed = record['armed']
        if armed == 'No':
            armed = 'Unarmed'
        if armed not in result.keys():
            result[armed] = 0
        result[armed] += 1    
    return result

"""Given a dictionary containing armament/weapon type as the key and number of 
people carrying the armament killed as the value, converts raw numbers (values) 
to percentages and returns a new dictionary mapping the weapon to computed 
percent for that weapon.
Prints weapon type, total number of victims carrying that weapon and the
percentage of victims carrying that weapon.
Parameters:
    raw_armed_unarmed: A dictionary containing raw data / total number of kills
    mapped to victim's weapon type
Returns:
    A dictionary mapping weapon type to percent of victims carrying that 
    weapon
"""
def armed_unarmed_percent(raw_armed_unarmed):
    percent_armed_stats = dict()
    total_kills = sum(raw_armed_unarmed.values())
    print
    print "Number of Armed/Unarmed people killed by the police:"
    print
    for weapon in raw_armed_unarmed:
        percent_armed_stats[weapon] = ((float(raw_armed_unarmed[weapon]) / 
                                                total_kills) * 100)
        print "Weapon:", weapon 
        print "Total:", str(raw_armed_unarmed[weapon]) 
        print"Percentage:", str(round(percent_armed_stats[weapon], 2)) + "%" 
        print
    return percent_armed_stats

"""Given a dictionary containing weapon type as the key and total number of 
victims carrying that weapon, computes and prints 2 probabilities:
    The probability that a victim of Police Homicide was armed and
    the probability that the victim was unarmed
"""
def print_probabilty_armed_stats(raw_armed_unarmed):
    total_kills = sum(raw_armed_unarmed.values())
    sum_armed = total_kills - raw_armed_unarmed['Unarmed']
    print "Total Armed:", sum_armed
    print "Probability that a police homicide victim was armed:", str(
                                                float(sum_armed) / total_kills)
    print "Probability that a police homicide victim was unarmed:",str(
                            float(raw_armed_unarmed['Unarmed']) / total_kills)
    print
    
"""Given a list of dictionaries containg Police Killings data for a particular
year, plots a pie chart with each slice representing the percentage of Police 
Homicide victims distinguished by the weapon they were carrying.
Parameters:
    lst_kills: list of dictionaries with each dicionary conating data for each
    police killing
"""
def plot_armed_stats(lst_kills):
    plt.clf()
    raw_data = kills_by_armed_unarmed(lst_kills)
    kills_by_armed = armed_unarmed_percent(raw_data)
    labels = kills_by_armed.keys()
    sizes = kills_by_armed.values()
    explode = (0, 0, 0.1, 0, 0, 0, 0, 0)
    colors = ['lightcoral', 'lightcoral', 'white', 'lightcoral', 'lightcoral', 
                'lightcoral', 'lightcoral', 'lightcoral']
    plt.pie(sizes, shadow = True, startangle = 90, explode = explode, 
    colors = [color for color in colors], labels = labels, autopct='%1.1f%%')
    plt.suptitle('Police Killings by Armed vs. Unarmed')
    plt.tight_layout()
    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()
    plt.savefig('armed_unarmed_stats.png')
    plt.show()
    print_probabilty_armed_stats(raw_data)
    print "Data plotting complete."

""" Given list of dictionaries containg Police Homicide data for each police
killing for a particular year, returns a dictionary of dictionaries mapping each 
Race/Ethnicity to the number of victims, number of unarmed victims and the
probability (that a particular victim belonging to that race was unarmed)
for that race.
Parameters:
    lst_allkills: list of dictionaries containg Police Homicide data for each 
    police killing for a particular year
Returns:
    A dictionary of dictionaries in the form:
        {'Race1':{'Unarmed': 2, 'Total Killed': 2, 'Kill_Prob': 0.5}, ...}
""" 
def kills_by_race_unarmed(lst_allkills):
    result = dict()
    for record in lst_allkills:
        if record['armed'] == 'No':
            race = record['raceethnicity']
            if race not in result.keys():
                result[race] = dict()
                result[race]['Unarmed'] = 0
            result[race]['Unarmed'] += 1
            result[race]['Total Killed'] = get_total_race_killed(race, 
                                                                lst_allkills)
    # For each race, calculate the probability that a particular victim 
    # belonging to that race was unarmed. Map this data to a new 'Kill_Prob' key
    # in the 'result' dictionary.
    for race in result:
        result[race]['Kill_Prob'] = (float(result[race]['Unarmed']) / 
                                    result[race]['Total Killed'])      
    return result

""" Given a particular race and a list of dictionaries containing Police 
Homicide data for a particular year, returns the total number of people 
belonging to the given race killed.
Parameters: 
    race: A string representing a particular race
    lst_allkills: a list of dictionaries with each dictionary representing a 
    particular Police Homicide record.
"""
def get_total_race_killed(race, lst_allkills):
    result = 0
    for record in lst_allkills:
        if race == record['raceethnicity']:
            result += 1
    return result

""" Given a dictionary of dictionaries containing data for total and unarmed
people killed by race, prints the given data.
Parameters:
    dict_race: A dictionary of dictionaries in the form:
    {'Race1':{'Unarmed': 2, 'Total Killed': 2, 'Kill_Prob': 0.5}, ...}
"""
def print_race_stats(dict_race):
    print "Kill details of Police Homicide victims by Race:"
    print
    for race in dict_race:
        print "Total Number of unarmed", race + " people killed:", str(
                                                    dict_race[race]['Unarmed'])
        print "Total", race + " victims of Police Homicide:", str(
                                                dict_race[race]['Total Killed'])
        print "Probability that a", race + " victim of police homicide was unarmed:", str(
                                        round(dict_race[race]['Kill_Prob'], 2))
        print

""" Given a dictionary of dictionaries containing data total and unarmed
people killed by race, sorts the data by total number killed in descending order
and returns a new dictionary containing the only the first three races from the 
sorted dictionary. 
Parameters: 
    dict_race: A dictionary of dictionaries in the form:
    {'Race1':{'Unarmed': 2, 'Total Killed': 2, 'Kill_Prob': 0.5}, ...}
Returns:
    a new dictionary containing data only for the top three races that 
    experienced a high number of killings.
"""
def race_top3_kills(dict_race):
    sorted_race = sorted(dict_race.items(), key=lambda x: x[1]['Total Killed'], 
                                                                reverse=True)
    lst_result = []
    result = dict()
    for race in sorted_race:
        lst_result.append(race[0])
    for i in range(3):
        print lst_result[i]
        result[lst_result[i]] = dict_race[lst_result[i]]
    return result

""" Given a list of dictionaries containing Police Homicide data for a 
particular year, returns a list containing total kills for each month with each
list index representing a month from 1 to 12.
Parameters:
    lst_allkills: a list of dictionaries with each dictionary representing a 
    particular Police Homicide record.
Returns:
    list containing total kills for each month with each list index representing 
    a month from 1 to 12.
"""
def kills_by_month(lst_allkills):
    result = dict()
    lst_result = []
    for record in lst_allkills:
        month = record['month']
        if month not in result.keys():
            result[month] = 0
        result[month] += 1
    for i in range(13):
        if (calendar.month_name[i]) in result.keys():
            lst_result.append(result[calendar.month_name[i]])
    return lst_result

""" Takes in two lists with each list containing the total number of victims
for each month(kills sorted by month) for each year.
Uses the given data to plot two trendlines (each trendline representing a 
particular year), showing killing trends over a 12 month period.
"""
def compare_month_trend(lst_year1, lst_year2):
    xs = range(1, 13)
    plt.plot([i for i in range(1, len(lst_year1) + 1)], lst_year1, 
                                                        label = '2015')
    plt.plot([i for i in range(1, len(lst_year2) + 1)],lst_year2, 
                                                        label = '2016')
    plt.xlim(1, 11, 1)
    labels = [calendar.month_name[i] for i in range(1, 13)]
    plt.xticks(xs, labels)
    plt.legend()
    plt.xlabel('Month')
    plt.ylabel('Total Number of Kills')
    plt.suptitle('Police Homicide Trend: Current (2016) VS. 2015')
    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()
    plt.savefig('trend_compare.png')
    plt.show()
    
def main():

    """Research Question 1
    """
    kills_by_state = state_killings_stats(file_counted2015,    # list of 
                                file_population_state) # dictionaries(records)
    
    ##Plot bar graph for State vs. Total Population
    #y_pop = [kills_by_state[key]['Population'] for key in kills_by_state]
    #plot_bar(kills_by_state.keys(), 'States', y_pop, 
    #'State Populations 2015', 'Population', 'state_population.png')
    #
    ## Plot bar graph for State vs. Total Police Kills
    #y_values = [kills_by_state[key]['Killings'] for key in kills_by_state]
    #plot_bar(kills_by_state.keys(), 'States', y_values, 
    #'Total Number of Police Killings by State', 'Total Number of Kills', 
    #'state_total_kills.png')
    #max_kills(kills_by_state, 'Killings')
    
    # Plot bar graph for State vs. Per Capita Police Kills
    y_per_capita = [kills_by_state[key]['Per Capita Kills'] for key in 
                    kills_by_state]
    plot_bar(kills_by_state.keys(), 'States', y_per_capita, 
    'Police Killings Per Capita by State', 'Kills Per Capita', 
    'state_kills_percapita.png')
    max_kills(kills_by_state, 'Per Capita Kills')
    
    """Research Question 2
    Plot a pie chart for the year 2015 with each slice representing the 
    percentage of Police Homicide victims distinguished by the weapon they were 
    carrying.
    """
    plot_armed_stats(lst_killings2015)
    
#    """Research Question 3
#    """
    race_kills_stats = kills_by_race_unarmed(lst_killings2015)
    
    # Plot bar graph for Race vs. Total Number of people killed
    y_axis_total = [race_kills_stats[key]['Total Killed'] for key in race_kills_stats]
    plot_bar(race_kills_stats.keys(), 'Race', y_axis_total, 
            'Total Number of Police Homicide Victims by Race', 
            'Total Number of Kills', 'race_killings.png')   
            
    # Plot bar graph for Race vs. Number of unarmed people killed
    y_axis_race = [race_kills_stats[key]['Unarmed'] for key in race_kills_stats]
    plot_bar(race_kills_stats.keys(), 'Race', y_axis_race, 
            'Number of Police Homicide Victims (Unarmed) by Race', 
            'Number of Kills', 'race_unarmed_killings.png')
    
    # Plot bar graph to show the probability that a victim belonging to a 
    # particular race was unarmed for the top three races that experienced the 
    # highest number of total killings
    race_top3 = race_top3_kills(race_kills_stats)
    y_prob = [race_top3[race]['Kill_Prob'] for race in race_top3]
    plot_bar(race_top3.keys(), 'Race', y_prob, 
'Race vs. Probability that the killed victim belonging to that race was unarmed'
        , 'Probability', 'race_unarmed_probability.png')
    print_race_stats(race_kills_stats)
#    
    """Research Question 4
    Plot a graph to compare Police Killings trend in 2015 and 2016.
    """
    compare_month_trend(kills_by_month(lst_killings2015), 
                        kills_by_month(lst_killings2016))
    
         
if __name__ == "__main__":
    main()
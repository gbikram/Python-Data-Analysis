import csv
import urllib2

# counted_15: State and total killings for that state, state
# state_populations: POPESTIMATE2015, Name
# [{state: , pop:, kill:, }]

url = 'https://www.dropbox.com/s/ohknei1ivvogq7z/the-counted-2015.csv?dl=1'
response_url = urllib2.urlopen(url)
counted_2015 = csv.DictReader(response_url)

lst_killings_2015  = []
for row in counted_2015:
    lst_killings_2015.append(row)
#print lst_killings_2015
#print
#    
url_pop = 'http://goo.gl/YVgbWI'
resp = urllib2.urlopen(url_pop)
state_pop = csv.DictReader(resp)

indivpop = []
for row in state_pop:
    indivpop.append(row)
print indivpop
print

def state_exist(state, state_pop_killed):
    for record in state_pop_killed:
        if record['state'] == 'state':
            return True
    return False

def get_pop(state):
    for record in indivpop:
        if record['NAME'] == state:
            return record['POPESTIMATE2015']
    return None

def get_full(state):
    state_abbrev = states = {
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
    

state_pop_killed = dict()
for record in lst_killings_2015:
    state = record['state']
    if state not in state_pop_killed.keys():
        state_pop_killed[state] = {'pop':0, 'killed':0}
    state_pop_killed[state]['killed'] += 1
    state_pop_killed[state]['pop'] = get_pop(get_full(state))
print state_pop_killed
    
    
    
    {armed: {weapon1: , weapon2: ...} unarmed:}

    
    print "Total Armed:", sum_armed
    print "Probability that a police homicide victim was armed:", str(
                                                float(sum_armed) / total_kills)
    print "Probability that a police homicide victim was unarmed:",str(
                                        float(result['Unarmed']) / total_kills)
                                        
                                           Unavailable 
                            Asian/Pacific Islander        NHPI + Asian 5+4
                            Black                          Black  2
                            Hispanic/Latino                8
                            Native American                Nativity 1
                            Other
                            White                          White 1
    {White: {}, Black: {}, Hisp/Lat: {}, Nat Am: {}, Other/Unknown: }


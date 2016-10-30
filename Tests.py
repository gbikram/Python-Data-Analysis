import Police_Killings
reload(Police_Killings)
from Police_Killings import *

def test_get_state_population():
    assert get_state_population(get_fullname('GA'), lst_allpopulation_state) == 10214860
    assert get_state_population(get_fullname('AL'), lst_allpopulation_state) == (
                                4858979)







if __name__ == "__main__":
    
    test_get_state_population()
    
    print "Tests Passed."
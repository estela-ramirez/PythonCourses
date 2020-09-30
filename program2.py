import prompt
import goody

# Use these global variables to index the list associated with each name in the dictionary.
# e.g., if men is a dictionary, men['m1'][match] is the woman who matches man 'm1', and 
# men['m1'][prefs] is the list of preference for man 'm1'.
# It would seems that this list might be better represented as a named tuple, but the
# preference list it contains is mutated, which is not allowed in a named tuple. 

match = 0   # Index 0 of list associate with name is match (str)
prefs = 1   # Index 1 of list associate with name is preferences (list of str)


def read_match_preferences(open_file : open) -> {str:[str,[str]]}:
    matches_dict = dict()
    for line in open_file:
        total, match, preferences = [], None, []
        line = line.rstrip('\n').split(';')
        preferences = [line[1], line[2], line[3]]
        total.append(match)
        total.append(preferences)
        matches_dict[line[0]] = total 
    return matches_dict
    


def dict_as_str(d : {str:[str,[str]]}, key : callable=None, reverse : bool=False) -> str:
    line, two_spaces= '', '  '
    for key in sorted(d.keys(), key = key, reverse = reverse):
        line += two_spaces + key + ' -> ' + str(d[key]) + '\n'
        
    if key.startswith('m'):
        return '\nMen Preferences\n' + line
    else:
        return 'Women Preferences\n' + line
    
    
def who_prefer(order : [str], p1 : str, p2 : str) -> str:
    return order[0][0]


def extract_matches(men : {str:[str,[str]]}) -> {(str,str)}:
    pass
#     match_tuple = ()
#     matched_set = set()
#     for man in men.keys():
#         match_tuple.add(man, who_prefer([men[man][1]], men[man][1][2], men[man][1][0])
        #matched_set.update(match_tuple)
    #return matched_set
        
        
    


def make_match(men : {str:[str,[str]]}, women : {str:[str,[str]]}, trace : bool = False) -> {(str,str)}:
    men_dict_copy = dict(men)
    print(men_dict_copy)
    unmatched_men_set = set()
    for num in range(len(men_dict_copy.keys())):
        for man in men_dict_copy.keys():
            unmatched_men_set.add(man)
        #print('these are unmatched men', unmatched_men_set)
        #print(man, men_dict_copy[man], [men_dict_copy[man][1]], men_dict_copy[man][1][2], men_dict_copy[man][1][0])
        #preferred_women = who_prefer([men_dict_copy[man][1]], men_dict_copy[man][1][2], men_dict_copy[man][1][0])
        #print('preferred women =', preferred_women) 
        
        while unmatched_men_set != set():
            print('unmatched men ', unmatched_men_set)
            print('change of dict = ', men_dict_copy )
            soon_to_be_matched_man = unmatched_men_set.pop()
            preferred_woman = who_prefer([men_dict_copy[soon_to_be_matched_man][1]], men_dict_copy[soon_to_be_matched_man][1][-1:], men_dict_copy[soon_to_be_matched_man][1][0])
          
            print('man ', soon_to_be_matched_man, 'woman ', preferred_woman)
           # if women[preferred_woman][0] == None:
            
            taken_women = set()
            for value in men_dict_copy.keys():
                taken_women.add(men_dict_copy[value][0])
            
            print('these are the taken women so far  ', taken_women)
            if preferred_woman not in taken_women:        
            

                men_dict_copy[soon_to_be_matched_man][0] = preferred_woman
                men_dict_copy[soon_to_be_matched_man][1].remove(preferred_woman)
            else:
                print('this woman is taken *******')
                women_prefernce_list = women[preferred_woman][1]
                print('woman_prefernce_list', women_prefernce_list)
                man_that_wants_to_propose_index  = women_prefernce_list.index(soon_to_be_matched_man)
                
                #man_that_already_proposed = women[preferred_woman][1][0]
                
                for key, value in men_dict_copy.items():
                    if preferred_woman in value:
                       man_that_already_proposed = key  
            
                man_that_already_proposed_index = women_prefernce_list.index(man_that_already_proposed)
                print('new man ', man_that_wants_to_propose_index, 'old_man =',man_that_already_proposed,  man_that_already_proposed_index)
                if man_that_wants_to_propose_index > man_that_already_proposed_index:
                    print('soon to be matched  === ', soon_to_be_matched_man)
                    unmatched_men_set.add(soon_to_be_matched_man)
                    men_dict_copy[soon_to_be_matched_man][1].remove(preferred_woman)
                else:
                    men_dict_copy[soon_to_be_matched_man][0] = preferred_woman
                    unmatched_men_set.add(man_that_already_proposed)
                    men_dict_copy[soon_to_be_matched_man][1].remove(preferred_woman)
                    
        break
     
  


  
    
if __name__ == '__main__':
    open_men_file = goody.safe_open('Enter a file storing preferences of men', 'r', 'Illegal file name')
    open_women_file = goody.safe_open('Enter a file storing preferences of women', 'r', 'Illegal file name')

    men_dict = read_match_preferences(open_men_file)
    women_dict = read_match_preferences(open_women_file)
    
    print(dict_as_str(men_dict))
    print(dict_as_str(women_dict))
    make_match(men_dict, women_dict)
    #extract_matches(men_dict) 
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()

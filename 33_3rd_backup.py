import prompt
from goody       import safe_open
from math        import ceil 
from collections import defaultdict


def read_graph(open_file : open) -> {str:{str}}:
    infl_dict = defaultdict(list)
    
    for line in open_file:
        line = line.rstrip('\n').split(';')
        if len(line) != 1:
            infl_dict[line[0]].append(line[1])
            infl_dict[line[1]].append(line[0])
        else:
            infl_dict[line[0]] = []
            
    return infl_dict
    


def graph_as_str(graph : {str:{str}}) -> str:
    line =''
    for key in sorted(graph.keys()):
        line += key + "->" + str(graph[key]) + '\n'
    return line





def find_influencers(graph : {str:{str}}, trace : bool = False):

    trace = prompt.for_bool('Trace the Algorithm[True]', default = False)
    infl_dict = defaultdict(list)
    
    for key in graph.keys():
        friend_count = int(len(graph[key]))
        if friend_count != 0:
            friend_ceil = friend_count - ceil(friend_count/2) 
            infl_dict[key] += friend_ceil, friend_count, key
        else:
            friend_ceil = -1
            infl_dict[key] += friend_ceil, friend_count, key
    
    while True:
        infl_dict_list = []
        for value in infl_dict.values():
            value = tuple(value)
            negative = '-'
            if negative not in str(value[0]):
                infl_dict_list.append(value)
     

     

        if infl_dict_list != []:
            remove_tup = sorted(infl_dict_list)[0] 
            if trace:
                print('influencer dictionary =')
                print(infl_dict)
                print('removal candidates    = ' + str(infl_dict_list))
                print(str(remove_tup) + ' is the smallest candidate')
                print("Removing " + remove_tup[2] + " as key from influencer dictionary; decrementing friend's values there\n")
          
            else:
                pass 

            for x in graph[remove_tup[2]]:
                if x in infl_dict.keys():
                    infl_dict[x][0] -= 1
                    infl_dict[x][1] -= 1
                else:
                    pass
             
            del infl_dict[remove_tup[2]]     

        else:
            keys_set = set()
            for key in infl_dict.keys():
                keys_set.add(key)
            if trace:
                print('influencer dictionary =')
                print(infl_dict)
                print('removal candidates    = ' + str(infl_dict_list))
            else:
                print('Influencers = ' + str(keys_set))

            return keys_set


      
def all_influenced(graph : {str:{str}}, influencers : {str}) -> {str}:
 
    while True:
        
        user_nodes = prompt.for_string('\nEnter influencers set (or else quit)', default= influencers, is_legal=(lambda x : True), error_message='Please enter a legal String')
        total = len(graph.keys())
        if user_nodes == 'quit':
            break
        else:
            user_nodes = eval(user_nodes)
            influenced_nodes_list = []
            for x in user_nodes:
                if x.isalpha():
                    influenced_nodes_list.append(x)
            
            count = 0        
            for node in influenced_nodes_list:
                if node in graph.keys():
                    count += 1
            if count == len(influenced_nodes_list):
                print('yay', influenced_nodes_list)
                
                for node in influenced_nodes_list:
                    for friend in graph[node]:
                        print(friend)
                    
                
            
            
            
            
            
            
            
            else:
                print("Entry Error: "+ "'"+ str(user_nodes) +"'" +';' + "\nPlease enter a legal String")
                user_nodes = prompt.for_string('\nEnter influencers set (or else quit)', default= influencers, is_legal=(lambda x : True), error_message='Please enter a legal String')

                    
                
                

#             print('length', length_of_values, values_list)
#             for x in values_list:
#                 if x in graph.keys():
#                     count += 1
#             if count == length_of_values:
#                 print('yay')
#             else:
#                 pass
                    
                    
#                 if x not in graph.keys():
#                     print('value is not a key', value)  ### need to reprompt
#                 else:
#                     print('value is a key', value)
                    

                    
    
        
       
            
    
if __name__ == '__main__':
    file = safe_open('Enter a file', 'r', 'illegal file name')
    graph = read_graph(file)
    # for key in infl_dict:
    #    print(key, infl_dict[key])
        
    print(graph_as_str(graph))
    influencers = find_influencers(graph)

    all_influenced(graph, influencers)
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()




#finds network name (SSID) occurences, look for a sepcific networks occurence or all of them 
def find_net_occ(masterFrame):
    user = input("Enter A for a specific network, B for all networks: ")
    if user.lower() == 'a':
        net_name = input("Enter network name: ")
        find_occurences = masterFrame[(masterFrame['C'] == net_name)]
        print(net_name, " was found: ", len(find_occurences)," times. ")
        print(find_occurences)
    
    elif user.lower() == 'b':

        all_networks = masterFrame['C']
        network_names_dict = {}
    
        for name in all_networks:
            try:
                if name in network_names_dict:
                    network_names_dict[name] += 1
                elif name not in network_names_dict and name[1].isalpha():
                    network_names_dict[name] =1        
            except(TypeError):
                continue
        print("The found networks and the amount of times found: ")
        print(network_names_dict)

                    
#finds security type occurences, look for a sepcific type or all types
def find_sec_occ(masterFrame):
    user = input("Enter A for a specific security type, B all security types: ")
    if user.lower() == 'a':
        sec_name = input("Enter security Type name: ")
        find_occurences = masterFrame[(masterFrame['F'] == sec_name)]
        print(sec_name, " was found: ", len(find_occurences)," times. ")
        print(find_occurences)
    
    elif user.lower() == 'b':

        all_security = masterFrame['F'].dropna(how="any")
        
        sec_names_dict = {}
    
        for name in all_security:
            try:
                if name in sec_names_dict:
                    sec_names_dict[name] += 1

                else:
                    sec_names_dict[name] = 1

            except(TypeError):
                continue
    
        print("The found Security Types and the amount of times found(nan values removed): ")
        print(sec_names_dict)


#finds frequency occurences , lets you search a specific freq or all of them and displays the busiest at the end. 
def find_freq_occ(masterFrame):
    user = input("Enter A for a specific frequency, B all frequencies and busiest freq: ")
    if user.lower() == 'a':
        freq_name = float(input("Enter Frequency: "))
        find_occurences = masterFrame[(masterFrame['D'] == freq_name)]
        print(freq_name, " was found: ", len(find_occurences)," times. ")
        print(find_occurences)
    
    elif user.lower() == 'b':

        all_freq = masterFrame['D'].dropna(how="any")
        
        freq_names_dict = {}
    
        for name in all_freq:
            try:
                if name in freq_names_dict:
                    freq_names_dict[name] += 1

                else:
                    freq_names_dict[name] = 1

            except(TypeError):
                continue
        
        busiest_freq = 'none'
        highest = 0
        for key in freq_names_dict:
            
            if highest == 0:
                busiest_freq = key
                highest = freq_names_dict[key]
            elif highest < freq_names_dict[key]:
                highest = freq_names_dict[key]
                busiest_freq = key
            else:
                continue

        print("The found Frequencies and the amount of times found(nan values removed): ")
        print(freq_names_dict)
        print("The busiest frequency is: " , busiest_freq, " with: ", freq_names_dict[busiest_freq], "occurences.")


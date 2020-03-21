#A dictionary of lists

def mostPres():
    state_dict = {}
    with open("USPresidents.txt", "r") as fhandle:
        for line in fhandle:
            (state,pres) = line.split("\t")
            if state in state_dict:
                state_dict.get(state).append(pres.rstrip())
            else:
                state_dict[state] = [pres.rstrip()]
    fhandle.close()
    max_dict = {}
    
    for keys in state_dict.keys():
        max_dict[keys]=len(state_dict.get(keys))
        
    max_val= max(max_dict.values())
    for i,j in max_dict.items():
        if j == max_val:
            maxState = i
    print("\nThe state with the most presidents is", maxState, "with", max_val, "presidents:")
    for i in state_dict.get(maxState):
        print("   ", i)
        
    return max_dict

#Dictionary keys and sets

def popPres(num_pres):
    popStates = set(["CA", "TX", "FL", "NY", "IL", "PA", "OH", "GA", "NC", "MI"])
    statePres = popStates.intersection(set(num_pres.keys()))
    print("\n", len(statePres), "of the 10 high population states have had presidents born in them:")
    statePres = sorted(statePres)
    for i in statePres:
        print("   ", i, ":", num_pres.get(i))

def main():
    highPop_Midwest()
    var1 = mostPres()
    popPres(var1)

if __name__ == "__main__":
    main()

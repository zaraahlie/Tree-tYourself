import screen as s
USER = ""

#Determines if the player is at the end location → returns if at end and which tree
def determiningFinalLocation(loc):
    tree1 = ["LLLLL","LLLML","LLLRL", "LLML"]
    tree2 = ["LLLLR", "LLLMR","LLLRR","LLMR"]
    tree3 = ["LLR","LRL", "LRRL","LRLR","RLLL","RLLLR","RLRLL","RLRLR"]
    tree4 = ["LRLM","RLLLM","RLRLM","LRRM", "RLLR"]
    tree5 = ["RLRRL","RRLR", "RRRR", "RLLM"]
    tree6 = ["RLRRR","RRLL","RRRL", "LRRR"]
    allTrees = [tree1,tree2,tree3,tree4,tree5,tree6]
    for i in range(len(allTrees)):
        if loc in allTrees[i]:
            return True , i
    return False , 0

#Adds the Direction to the USER
def addDirectionL():
    s.USER += "L"
    determineScreen()

def addDirectionR():
    s.USER += "R"
    determineScreen()

def addDirectionM():
    s.USER += "M"
    determineScreen()

#Determines what screen that should be displaying
def determineScreen():
    stop , name = determiningFinalLocation(s.USER)
    if stop:
        treeNames = ["Cherry Tree","Money Tree", "Rainbow Tree", "Pando Aspen", "Dragon's Blood Tree", "Kauri Tree"]
        s.endScreen(treeNames[name])

    else:
        questions, numPath = determineQuesions(s.USER)
        if numPath == 2:
            s.path_screen2(questions[0],questions[1])
        elif numPath == 3:
            s.path_screen3(questions[0],questions[1],questions[2])


#displays the correct question at each intersection/crossroads
#return a string where it contains the quesion(String) and possible routes(int)
def determineQuesions(loc):
    if loc == "":
        return ["Leaves", "Branch"] , 2

    elif loc == "L":
        return ["Paper" , "Metal"] , 2

    elif loc == "LL":
        return ["Watch", "Listen" , "Feel"] , 3

    elif loc == "LLL":
        return ["Glitter", "Shine" , "Glow"] , 3

    elif loc == "LLLL":
        return ["Luck", "Beauty"] , 2

    elif loc == "LLLM":
        return ["Colourful" , "Green"] , 2

    elif loc == "LLLR":
        return ["Simple", "Complex "] , 2

    elif loc == "LLM":
        return ["Fleeting" ,"Eternal"] , 2

    elif loc == "LR":
        return ["Leaf" ,"Branches"] , 2

    elif loc == "R":
        return ["Disguise" ,"Reveal"] ,2

    elif loc == "RR":
        return ["Long", "Short"] ,2

    elif loc == "RL":
        return ["Danger", "Safety"] , 2

    elif loc == "RLL":
        return ["Earth", "Water", "Wood"],3

    elif loc == "RLR":
        return ["Rare", "Common"], 2

    elif loc == "RRL":
        return ["Damp" , "dry"],2

    elif loc == "RRR":
        return ["Believe", "Doubt"], 2

    elif loc == "RLRL":
        return ["Glitter", "Shine","Glow"],3

    elif loc == "LRR":
        return ["Hot", "Warm","Cool"], 3

    elif loc =="RLRR":
        return ["Tall", "Short"] , 2

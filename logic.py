def determiningFinalLocation():
    tree1 = ["LLLLL","LLLML","LLLRL", "LLML"]
    tree2 = ["LLLLR", "LLLMR","LLLRR","LLMR"]
    tree3 = ["LLR","LRL", "LRRL","LRLR","RLLL","RLLLR","RLRLL","RLRLR"]
    tree4 = ["LRLM","RLLLM","RLRLM"]
    tree5 = ["RLRRL","RRLR", "RRRR"]
    tree6 = ["RLRRR","RRLL","RRRL"]
    allTrees = [tree1,tree2,tree3,tree4,tree5,tree6]
    userTree = 0
    user = ""
    while True:
        questions, numDir = displayQuesions(user)
        user += userInput
        for tree in range(len(allTrees)):
            if user in allTrees[tree]:
                return tree



#displays the correct question at each intersection/crossroads
#return a string where it contains the quesion(String) and possible routes(int)
def displayQuesions(loc):
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
        return "Colourful" , "Green"] , 2

     elif loc == "LLLR":
        return ["Simple", "Complex "] , 2

     elif loc == "LLM":
        return ["Fleeting" ,"Eternal"] , 2

     elif loc == "LR":
        return ["Leaf" ,"Branches"] , 2 

     elif loc == "R":
        return ["Disguise" ,"Reveal"] ,2

     elif loc == "RL":
        return ["Danger", "Safety"] , 2

     elif loc == "RLL":
        return ["Earth", "Water", "Wood"],3

     elif loc == "RLR":
        return ["Disguise", "Reveal"], 2

     elif loc == "RRL":
        return ["Damp" , "dry"]

     elif loc == "RRR":
        return ["Believe", "Doubt"], 2

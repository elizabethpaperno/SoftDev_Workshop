jobs = {
    
    }
def createDict(){
    
    with open("occupations.csv","r") as txt:
    try:
        
        while(True):
            line = txt.readline()
            last = line.rindex(",")
            jobs[0:last] = int(jobs[last + 1:])
    except:
        None
}


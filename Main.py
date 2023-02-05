import pandas  as pd
# Wrok Place
opcode = {}
SourceCode={}

def Add_Loc(dataProject ,  FilePath):
    Location_
    for index in dataProject:
            if index['Operation'] == 'Start' or index ['Label'] == 'FIRST':
                index['Loc'] = hex(index['Source'])
                Location_ = hex(index['Loc'])
            else :
                if index['Operation']!= 'REW' or index['Operation'] != 'REB':
                    index['Loc'] = Location_ + hex(3) 
                 
    
    

def Add_OpCode():
    pass

def fileReader (FilePath):
    file = pd.read_csv(FilePath)
    SourceCode=file.to_dict('index')
    testing(SourceCode)
    
    
# Tools 

def testing (_DataFrame):
    try :
        for item , key in _DataFrame.items():
            print (item , '\t', key)    
    except :
        pass
# build architecture
    
def main ():
    fileReader('2PASSFILE.csv')
    Add_Loc()
    Add_OpCode()
    pass
        

# Run Commands
#main()
s = '45564;54665;4654;'  
y =s.split(';')
print(len(y))



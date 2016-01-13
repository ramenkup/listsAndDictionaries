'''
fishcatch.py
Spencer Klinge
Ista 130- Prof. Thompson
Due: 11/20/2015
'''

'''
def fish_dict_from_file(file):
-file: file with list of fish to be read
literally maps numeric values to english fish names ( True: fishmap[1] =="Bream")
create empty dictonary, read fish species and weight from fish-catch.dat
Map english key to list of weight of each fish(floats)
skip fish with 'N/A' weight

'''
def fish_dict_from_file(word):
    filer= open(word, "r")
    fishmap={'1':'Bream', '2':'Whitefish', '3':'Roach','4':'?','5':'Smelt','6':'Pike','7':'Perch'}
    temp_dict={}
    for line in filer:
        one_fish=line.split()
        fish_Count=one_fish[0]
        fish_Species= one_fish[1]
        fish_Weight= one_fish[2]
        if fishmap[fish_Species] not in temp_dict :# cant do if fish_Species not in temp_dict
            temp_dict[fishmap[fish_Species]]=[]
        if fish_Weight != 'NA':
            temp_dict[fishmap[fish_Species]].append(float(fish_Weight))
    return temp_dict

'''
def main():

calls fish_dict_from_file()

'''


def main():
    fish_dictonary= fish_dict_from_file('fishcatch.dat')
    print(str('#').rjust(4)+' '+str('NAME').ljust(10)+' '+ str('MEAN WT').rjust(10))
    for key in sorted(fish_dictonary.keys()):
        print ((str(len(fish_dictonary[key])).rjust(4))+' '+key.ljust(10)+(str(round(sum(fish_dictonary[key]) /len(fish_dictonary[key]),1))+'g').rjust(11))
        #print(sum(int(fish_dictonary[key]))



if __name__ == '__main__':
    main()
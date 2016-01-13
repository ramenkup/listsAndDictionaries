'''
emoticons.py
Spencer Klinge
Ista 130- Prof. Thompson
Due: 11/20/2015
'''


'''
def load_twitter_dicts_from_file(file, dictionary, dictionary):
    filename: reference to file being opened and read
    emoticons_to_ids: dictonary, emoticon keys, user ID values
    ids_to_emoticons: dictonary, of user ID emoticons, and a copy of an emoji from every tweet.
    fills the two dictonarys in main from the contents of the file
    Returns nothing
'''
def load_twitter_dicts_from_file(filename, emoticons_to_ids, ids_to_emoticons):
    #creating two empty dictonary's here overides the ones calling the method in main
    filer= open(filename, 'r')
    for line in filer:
        one_tweet= line.split()
        emoji= one_tweet[0][1:len(one_tweet[0])-1] # parses double parenthesis.
        tweet=one_tweet[1]
        user= one_tweet[2][1: len(one_tweet[2])-1]
        if emoji not in emoticons_to_ids:
            emoticons_to_ids[emoji]=[]
        emoticons_to_ids[emoji].append(user)#string-type being appeneded
        if user not in ids_to_emoticons:
            ids_to_emoticons[user]=[]
        ids_to_emoticons[user].append(emoji)
    return None
'''
def find_most_common(dictonary):
    emoji_id: dictonary parameter containing emojies as keys and user ID's as values

    takes a single parameter and outputs the key with the longest list of values. prints the length of the lists[]
    in an easy to read format

'''

def find_most_common(emoji_id):
    max_key=''
    times=0
    for key in emoji_id.keys():
        if int(len(emoji_id[key])) > times:
            max_key=key
            times= len(emoji_id[max_key])
    #print(type(key))
    print (max_key.ljust(21)+'occurs'+ str(times).rjust(9)+' times') #NO IDEA ABOUT THIS FORMAT
    return max_key
'''
def main():

    creates two empty dictonaries, runs the methods, then finds the 5 most common emoticons in the list

'''

def main():
    emoticons_to_ids={}
    ids_to_emoticons={}
    load_twitter_dicts_from_file('twitter_emoticons.dat', emoticons_to_ids,ids_to_emoticons)
    #print(emoticons_to_ids)
    print('Emoticons: ' + str(len(emoticons_to_ids.keys())))
    
    print('UserIDs:   ' + str(len(ids_to_emoticons.keys())))
    print()

    i=0
    while i <5:
        most_common=find_most_common(emoticons_to_ids)
        #print(most_common,'occurs',str(len(emoticons_to_ids[most_common])),'times')
        #emoticons_to_ids.pop("most_commom", None)
        del emoticons_to_ids[most_common]
        i+=1
if __name__ == '__main__':
    main()
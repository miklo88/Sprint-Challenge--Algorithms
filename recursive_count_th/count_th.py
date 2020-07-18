'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
'''
UPER
this was just like the problem don did in the code challenge.

so i'm going to be finding the len of 'th' which is 2. by doing this i can sort words out if they 
have 'th' or not.
if they do then i can increment how many times they have th in them.
anything else just return a 0
if anything is less than that value/len then it isn't a 'th'
if else is equal to that value/len then return the number of times its in the word. ex, thump = 1

'''
def count_th(word):
    #if word len is not less than 'th'. it isn't the one
    if len(word) < len('th'):
        return 0
    #if the word begins with th then we have a winner.  we add one for every th detected.
    elif word[:2] == 'th':
        return count_th(word[2:]) + 1
    # keep searching through the word if th doesn't begin it. ex weather
    else:
        return count_th(word[1:])
    # TBC
# word = 'pie'
# word = 'THtHThth'
#word = 'weather'
# word = 'Thursday'
# word = 'thumper'
# word = 'thumpy thumps things'
# print(count_th(word))
    # pass
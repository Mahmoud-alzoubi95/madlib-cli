import re
arrayForInput=[]


# function for inputs
def fin(x):
    a=input()
    arrayForInput.append(a)
    
    return arrayForInput[x] 




# tp open the text.txt file
with open('assets/video_game_output_from_user.txt') as f:
    content=f.read()


content
# to change the changable words with %s to do the string format
x=re.sub("{\w*}","%s",content)

# to store the changable words into list
words=re.findall("{\w*}",content)
# print(x,words)



# for test purposes
def parse(txt):
    words=re.findall("{\w*}",txt)
    str1 = ''.join(words)
    return str1,words

# print(parse(content))


# for test purposes

def  read_template(txt):
    return txt.read().strip()




# an empty array to store input from user
emp_arr=[]   

# function to do the input from user and show the final result
def fun_input(statement):

    for i in words:
        remove_char=re.sub("{|}",'',i)
        
        emp_arr.append(input("\n\nPlease Enter a/an %s  : "%(remove_char)))
    with open('assets/video_game_output_from_user.txt','w') as f2:
        f2.write(x % tuple(emp_arr))
    return (x % tuple(emp_arr))

print(fun_input(words))

def fun_input_test(statement,entries):
    # input_arr=["mohammed","study","alone","computer","home","sleepy","table","mouse","laptop"]
    # test_word=re.findall("{\w*}",statement)
    x=re.sub("{\w*}","%s",statement)
    # print(x)
    return (x % entries)
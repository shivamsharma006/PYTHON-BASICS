'''Write a program to fill in a letter template given below with name and date.
letter = 
       Dear <|Name|>,
       You are selected!
       <|Date|>

'''

letter = '''
Dear <|Name|>,
You are selected! on
<|Date|>
'''

print(letter.replace("<|Name|>","Shivam").replace("<|Date|>","24 September"))
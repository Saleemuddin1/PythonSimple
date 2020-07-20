convert_dict = { 
    'one': '1', 
    'two': '2', 
    'three': '3', 
    'four': '4', 
    'five': '5', 
    'six': '6', 
    'seven': '7', 
    'eight': '8', 
    'nine': '9', 
    'zero' : '0',
    'ten' : '10',
    'eleven': '11',
    'twelve':'12',
    'thirteen':13,
    'fourteen':'14',
    'fifteen':15,
    'sixteen' :'16', 
    'seventeen':'17',
    'eighteen':'18', 
    'nineteen':'19',	
    'twenty':'20'
} 

try:
	wordHold= raw_input("Enter Number in Word Form Between 1 and 20 (lowercase and hyphenate numbers with two words): ")
	finResult = ''.join(convert_dict[ele] for ele in wordHold.split()) 

# input string  
# print the result 
	print("The Number in Integer Form: " +finResult)
except:
	print ("Number is not in range!")

num_dict = {
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
    'sixteen' :'16', 'seventeen':'17','eighteen':'18', 'nineteen':'19','twenty':'20'}
num_dict2 = {
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
    'sixteen' :'16', 'seventeen':'17','eighteen':'18', 'nineteen':'19', 'twenty':'20'}

try:
	words= raw_input("Enter First Number in Word Form Between 1 and 20 (Lowercase and hyphenate two words)  : ")
	word2= raw_input("Enter First Number in Word Form Between 1 and 20 (Lowercase and hyphenate two words) : ")
	result = ''.join(num_dict[ele] for ele in words.split())
	result2 = ''.join(num_dict2[ele] for ele in word2.split())
# input string
# print the result
#x = result *result2;
	x = int(result);
	y = int(result2);
	z = x*y;

	print("The Product in Integer Form: " +str(int(z)))
except: print("Out of Range!")



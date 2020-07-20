numToWords = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
numToWords2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
def numbercalc(NumHolder):
    if 0 <= NumHolder <= 19:
        return numToWords[NumHolder]
    elif 20 <= NumHolder <= 99:
        tenHolder, remainder = divmod(NumHolder, 10)
        return numToWords2[tenHolder - 2] + '-' + numToWords[remainder] if remainder else numToWords2[tenHolder - 2]
    else:
        print('Number out of range of numbers.')
def main():
    num = eval(raw_input("Please enter a number between 0 and 99: "))
    if __name__== "__main__":
    	print(numbercalc(num))
main()


'''
f = open('C://Users//lenovo//mycode//py//python_programming_codebasics//funny.txt', 'r')
f_out = open('C://Users//lenovo//mycode//py//python_programming_codebasics//funny_wc.txt', 'w')

for line in f:
    tokens = line.split(' ')
    f_out.write('Wordcount: ' + str(len(tokens)) + ' ' + line)

f_out.close()
f.close()
'''

'''
1. poem.txt contains famous poem "Road not taken" by poet Robert Frost. 
You have to read this file in your python program and find out words with maximum occurance.
'''
word_dict = {}
with open('C:\\Users\\lenovo\\mycode\\py\\python_programming_codebasics\\poem.txt', 'r') as f:
    for line in f:
        words = line.split(' ')
        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
word_occurance = list(word_dict.values())
max_occurance = max(word_occurance)
print('Maximum occurance of word is: ', max_occurance)


for word, count in word_dict.items():
    if count == max_occurance:
        print('Word with max occurances are: ', word)
        break
'''
2. stocks.csv contains stock price, earnings per share and book value.
You are writing a stock market application that will process this file and create a new file with 
financial metrics such as pe ratio and price to book ratio. These are calculated as,
pe ratio = price / earnings per share
price to book ratio = price / book value
Your input format (stocks.csv) is,

Company Name	Price	Earnings Per Share	Book Value
Reliance	    1467	    66	                653
Tata Steel	    391	        89	                572
Output.csv should look like this,

Company Name	PE Ratio	PB Ratio
Reliance	    22.23	    2.25
Tata Steel	    4.39	    0.68
'''
with open('C:\\Users\lenovo\mycode\py\python_programming_codebasics\stocks.csv', 'r') as f, \
        open('C:\\Users\lenovo\mycode\py\python_programming_codebasics\out.csv', 'w') as out:
    out.write('Company Name  PE Ratio  PB Ratio\n')
    next(f)
    for line in f:
        tokens = line.split(',')
        company_name = tokens[0]
        price = float(tokens[1])
        earnings_per_share = float(tokens[2])
        book_value = float(tokens[3])
        pe_ratio = round(price/earnings_per_share, 2)
        price_to_book_ratio = round(price/book_value, 2)
        out.write(f'{company_name}, {pe_ratio}, {price_to_book_ratio}\n')




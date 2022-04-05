'''Numpy is not a default library and need to be installed apart. It helps to manipulate the data in arrays'''
import numpy as np
''''Capital to identify a constant variable'''
FILE = 'pitch_example_data.txt'

'''Function to check the number of lines and compare the sum of results onto the tests'''
def countLines ( file ) :
    with open (FILE) as f :
        line_count = 0
        for line in f :
            line_count += 1

    return int (line_count)

'''Function is responsible to check the status of trades and extract the symbol and save them  in an array. '''
def checkTrades ( file ) :
    symbols = [ ]

    for i in file:
        if i [ 9 ] == 'X' :
            symbols.append ('CANCELLED')

        elif i [ 9 ] == 'E' :
            symbols.append (i[33:35])

        elif i[9] != 'X' and len (i.split ()) < 2 :

            symbols.append (i [ 33 :35 ])
        else:
            i = i.split ()
            symbols.append (i[ 0] [29:])

    return symbols

'''Function is responsible for the output either via console (only top10) or html(results.html) with a summary'''
def reportTrades ( file ) :

    header = '<!doctyle html><html><head><title>Cboe Assesment</title></head><body>'
    body = '<table border="1"><caption><b>Cboe Top 10 Trades</b></caption></h1><thead><tr><th>SYMBOL</th><th>AMOUNT</th></tr>'
    test = '</table><p>'
    footer = '<p><caption>Created by João Vitor Skonienczwy</body><p></html>'
    with open('results.html' , 'w') as output :
        output.write (header)
        output.write (body)
        a = np.array (checkTrades(file))
        unique , counts = np.unique (a , return_counts = True)
        a = dict (zip (unique , counts))

        sort_trades = sorted (a.items () , key = lambda x : x [1] , reverse = True)
        count = 0
        for i in sort_trades :

            if count < 10 :
                if i [0] == 'CANCELLED' :
                    pass


                else :
                    print(i[0], i[1])
                    count += 1
                    col1 = i[0]
                    col2 = i[1]
                    output.write(f'<tr><td>{col1}</td><td>{col2}</td</tr>')

        with open (FILE) as f :
            cancelled=0
            tradeMessage=0
            addOrder=0
            orderExecuted=0
            for i in f :
                if i[9]=='X' :
                    cancelled+=1
                elif i[9]=='P' :
                    tradeMessage+=1
                elif i[9]=='A' :
                    addOrder+=1
                else :
                    orderExecuted+=1
        output.write (test)
        output.write ('<b> Summary: <p></b>')
        output.write (f'<b>Cancelled Trades: {cancelled}<p> </b>')
        output.write (f'<b>Trade Messages: {tradeMessage}<p> </b>')
        output.write (f'<b>Add Order: {addOrder}<p></b>')
        output.write (f'<b>Executed Order: {orderExecuted}<p></b>')
        output.write (f'<b>Total of Trades: {countLines (file)}<p> </b>')
        output.write (footer)


with open(FILE, 'r') as file:
    reportTrades(file)































from multiprocessing.dummy import Value
import pandas as pd
import time
import plotly.express as px
import datetime
import numpy

debug = False
year =[]


table = pd.read_csv('env\microfound.csv')
table['Score'] = table['Close'] - table['Open']

print('\n'*5)
print(f'\033[7m{"Microsoft | Stock Market Analysis | Founding Years": ^87}\n\033[0;m')



for c in range(0,4):
    time.sleep(0.2)
    print(f'\033[3{c+1}m{"."*87}\033[m')

time.sleep(0.3)
table = table.set_index(['Date'])

    
while debug == False:
    y = input('Founding Year (1986-2022): ')
    try:
        if 1986<= int(y) <= 2022:
            debug = True
        else:
            print('\033[31m!!! \033[mOnly dates between 1986 and 2022\033[31m !!! \033[m')
    except:
            print('\033[31m!!! \033[mOnly dates between 1986 and 2022 \033[31m!!! \033[m ')
          


y = int(y)
i = datetime.date(y,1,1)
f = datetime.date(y,12,31)

yt = table.loc[f"{i}":f"{f}"]
yt.reset_index(inplace=True)
print('\n'*3)
print('Date         Open    Close    Score\n')

for n in yt.index:
    time.sleep(0.02)
    if yt["Score"][n] > 0:
        print(f'\033[32m{yt["Date"][n]: <12} {round(yt["Open"][n], 3): <7} {round(yt["Close"][n], 3): <7}  {round(yt["Score"][n], 3): <7}\033[m')
    elif yt["Score"][n] < 0:
        print(f'\033[31m{yt["Date"][n]: <12} {round(yt["Open"][n], 3): <7} {round(yt["Close"][n], 3): <7}  {round(yt["Score"][n], 3): <7}\033[m')
    else:
        print(f'\033[m{yt["Date"][n]: <12} {round(yt["Open"][n], 3): <7} {round(yt["Close"][n], 3): <7}  {round(yt["Score"][n], 3): <7}')


open = yt['Open'].iloc[0]
close = yt['Close'].iloc[len(yt)-1]

time.sleep(1)
print(f'''{'-'*40}
Year  : {y}
Open  : {round(open,3)}
Close : {round(close,3)}
{'-'*40}

''')

g = px.line(yt, x='Date', y='Close')
g.show()




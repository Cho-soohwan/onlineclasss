import webbrowser
import datetime
hour = int(input('hour : '))
minute = int(input('minute : '))
url = str(input('url : '))
while True:
    now = str(datetime.datetime.now())
    h = int(now[11:13])
    m = int(now[14:16])
    if h == hour and m == minute :
        webbrowser.open(url)
        break


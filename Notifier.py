import requests
import json
from pytz import timezone
from time import sleep
from datetime import datetime
def checkprice():
    d=requests.get("https://api.wazirx.com/api/v2/tickers/shibinr").text
    res = json.loads(d)
    res = res['ticker']
    sell_price=float(res['sell'])
    if(True):
        message="SHIB\tprice.....!!!\nCurent\u0020Sell\u0020Price\u0020:\u0020"+res['sell']+"\nCurrent\u0020Buy\u0020Price\u0020:\u0020"+res['buy']
        sendmsg(message,res['sell'],res['buy'])


def sendmsg(str1,sp,bp):
    token="1957046533:AAHfkgxNsxgeyEJcfy9LQXFd-Ftrd4B0vfQ"
    requests.post(
    url='https://api.telegram.org/bot{0}/{1}'.format(token, "sendMessage"),
    data={'chat_id': -1001509678582, 'text': str1}
    ).json()
    loggr(sp,bp)

def loggr(sp,bp):
    log=open('log.txt','a')
    IST = timezone('Asia/Kolkata')
    log.write(str(datetime.now(IST))+" Sell : "+sp+", Buy : "+bp+"\n")
    log.close()

if __name__=="__main__":
    counter=0
    while(1):
        token="1957046533:AAHfkgxNsxgeyEJcfy9LQXFd-Ftrd4B0vfQ"
        checkprice()
        counter+=1
        if(counter==24):
            requests.post(
                url='https://api.telegram.org/bot{0}/{1}'.format(token, "sendDocument"),
                data={'chat_id': -1001509678582},
                files={'document': open('log.txt','rb')},
            )
            log=open('log.txt','w')
            log.write("")
            log.close()
            counter=0
        sleep(5)

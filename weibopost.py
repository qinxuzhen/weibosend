#-*-coding:utf-8 -*-
"""
Create on Sep 17, 2014

@author:xuzhen.qxz

"""
from initclient import initclient
import ConfigParser

def getClient():
     
    sina_weibo_config = ConfigParser.ConfigParser()
    try:
        sina_weibo_config.readfp(open('/home/property/sina_weibo_config.ini'))
    except ConfigParser.Error:
        print ('read sina_weibo_config.ini failed.')
    APP_KEY = sina_weibo_config.get('appinfo','APP_KEY')
    APP_SECRET = sina_weibo_config.get('appinfo','APP_SECRET')
    CALLBACK_URL = sina_weibo_config.get('appinfo','CALLBACK_URL')

    user = sina_weibo_config.get('userinfo','user')
    pwd = sina_weibo_config.get('userinfo','password')
    
    client = initclient.get_client(APP_KEY,APP_SECRET,CALLBACK_URL)
    if not client:
        print 'Get client Error!'
        return
    return client
    

def postWeibo(client,content):
    client.statuses.update.post(status=content)
    


if __name__ == '__main__':
    client = getClient()
    content = """广发银行招聘副行长，职责 1.贯彻总、分行发展战略，协助分行行长工作并参与决策所在分行经营管理事项；
    2.在总、分行授权范围内，负责所在分行个人金融业务，组织制定和实施本业务条线的发展策略及年度计划，推动业务增长和风险控制；
    http://www.jinrongbole.com/info/detail/377/info/"""
    postWeibo(client,content)

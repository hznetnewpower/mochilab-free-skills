import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 agenda=r['agenda'];need(agenda and all(x.get('topic') for x in agenda),'Agenda needs topics');minutes=int(r['minutes']);need(minutes>0,'Meeting duration must be positive');total=sum(int(x.get('minutes',0)) for x in agenda);need(all(int(x.get('minutes',0))>=0 for x in agenda),'Topic minutes must not be negative')
 questions=[{'topic':x['topic'],'question':'What decision is needed?'} for x in agenda if not x.get('decision')];text='# '+r['title']+'\n\n'+'\n'.join('- '+x['topic']+' ('+str(x.get('minutes',0))+' min): '+x.get('decision','Decision to confirm') for x in agenda);c.emit('meeting-prep.md',text)
 return {'allocatedMinutes':total,'availableMinutes':minutes,'overBudget':total>minutes,'openQuestions':questions,'invitationsSent':False,'attendeeDataFetched':False}

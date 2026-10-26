import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 segments=r['segments'];need(segments,'Transcript segments required');need(all(float(x['start'])>=0 and float(x['end'])>float(x['start']) for x in segments),'Invalid segment times');ids={x['id'] for x in segments};need(len(ids)==len(segments),'Duplicate transcript segment ID');chapters=sorted(r['chapters'],key=lambda x:float(x['start']));need(chapters,'Chapters required');need(len({float(x['start']) for x in chapters})==len(chapters),'Duplicate chapter start');end=max(float(x['end']) for x in segments);lines=[]
 for x in chapters:
  need(0<=float(x['start'])<end and x.get('sourceIds') and set(x['sourceIds'])<=ids,'Chapter must refer to supplied transcript segments');v=int(float(x['start']));lines.append(f'{v//3600:02d}:{v//60%60:02d}:{v%60:02d} '+x['title'])
 c.emit('chapters.txt','\n'.join(lines)+'\n');return {'chapterCount':len(chapters),'durationSeconds':end,'summariesFactChecked':False,'videoFetched':False}

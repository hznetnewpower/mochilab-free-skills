import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 need(float(r.get('maxCharsPerSecond',20))>0,'Reading rate must be positive')
 text=c.read(r['file']).replace('\r\n','\n');pattern=re.compile(r'(?m)^((?:\d+:)?\d{2}:\d{2}[,.]\d{3})\s*-->\s*((?:\d+:)?\d{2}:\d{2}[,.]\d{3})[^\n]*\n(.*?)(?=\n\s*\n|\Z)',re.S);cues=[];issues=[]
 def seconds(s):
  parts=s.replace(',','.').split(':');need(len(parts) in [2,3],'Invalid subtitle time');values=[float(x) for x in parts];need(all(0<=x<60 for x in values[-2:]),'Invalid subtitle minute or second');return sum(x*m for x,m in zip(reversed(values),[1,60,3600]))
 previous=-1
 for i,m in enumerate(pattern.finditer(text),1):
  a,b=seconds(m[1]),seconds(m[2]);length=len(re.sub(r'<[^>]*>|\s','',m[3]));duration=b-a;cps=length/duration if duration>0 else None
  if duration<=0:issues.append({'cue':i,'issue':'nonpositive-duration'})
  if a<previous:issues.append({'cue':i,'issue':'overlap'})
  if cps is not None and cps>float(r.get('maxCharsPerSecond',20)):issues.append({'cue':i,'issue':'high-reading-rate'})
  previous=max(previous,b);cues.append({'cue':i,'start':a,'end':b,'characters':length,'charsPerSecond':round(cps,2) if cps is not None else None})
 need(cues,'No supported SRT or WebVTT cues found');return {'cueCount':len(cues),'issues':issues,'cues':cues,'mediaAlignmentVerified':False,'subtitleModified':False}

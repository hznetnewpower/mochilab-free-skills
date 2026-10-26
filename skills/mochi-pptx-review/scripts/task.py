import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 z=safezip(c.bytes(r['file']));ns={'a':'http://schemas.openxmlformats.org/drawingml/2006/main'};slides=[]
 for name in sorted(x for x in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml',x)):
  root=ET.fromstring(z.read(name));texts=[x.text or '' for x in root.findall('.//a:t',ns)];total=sum(len(x) for x in texts);slides.append({'part':name,'textCharacters':total,'emptyText':total==0,'overTextBudget':total>int(r.get('maxCharsPerSlide',900))})
 need(slides,'No PPTX slide parts found');return {'slides':slides,'slideCount':len(slides),'visualRenderingChecked':False,'layoutOverflowConfirmed':False,'presentationModified':False}

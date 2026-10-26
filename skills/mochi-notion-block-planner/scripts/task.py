import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 blocks=[]
 for line in c.read(r['file']).splitlines():
  if not line.strip():continue
  level=len(line)-len(line.lstrip('#'));kind='heading_'+str(min(level,3)) if level and line[level:level+1]==' ' else 'bulleted_list_item' if line.startswith('- ') else 'paragraph';text=line[level+1:] if kind.startswith('heading_') else line[2:] if kind=='bulleted_list_item' else line
  chunks=[text[i:i+1900] for i in range(0,len(text),1900)] or ['']
  for value in chunks:blocks.append({'object':'block','type':kind,kind:{'rich_text':[{'type':'text','text':{'content':value}}]}})
 c.emit('notion-blocks.json',json.dumps({'children':blocks},ensure_ascii=False,indent=2));return {'blocks':len(blocks),'uploadBatches':(len(blocks)+99)//100,'notionApiCalled':False,'supportedInput':'headings, paragraphs and bullet lines; not a general Markdown renderer'}

import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 probe=c.data(r['probeFile']);audio=[x for x in probe.get('streams',[]) if x.get('codec_type')=='audio'];need(audio,'No audio stream in probe');target=float(r.get('targetLufs',-16));peak=float(r.get('targetTruePeak',-1));need(-30<=target<=-5 and -9<=peak<=0,'Loudness target outside supported range');filter='loudnorm=I='+str(target)+':TP='+str(peak)+':LRA=11:print_format=json'
 return {'audioStreams':len(audio),'analysisFilter':filter,'secondPassReady':False,'requiredNextStep':'Run the analysis pass on the selected input and capture real loudnorm measurements before building the second pass.','audioModified':False,'noiseRemovalGuaranteed':False}

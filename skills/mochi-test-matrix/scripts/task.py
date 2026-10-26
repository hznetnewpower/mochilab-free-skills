import collections,csv,datetime as dt,email.parser,email.policy,html,io,itertools,json,re,statistics,textwrap,urllib.parse,xml.etree.ElementTree as ET
from runtime import need,instant,decimal,table,safezip

def handle(r,c):
 factors=r['factors'];need(factors and all(isinstance(v,list) and v for v in factors.values()),'Nonempty factor lists required');keys=sorted(factors);need(len(keys)<=8,'At most8 factors');size=1
 for k in keys:size*=len(factors[k])
 need(size<=10000,'Cartesian product exceeds10000');candidates=[tuple(x) for x in itertools.product(*(range(len(factors[k])) for k in keys))]
 def pairs(row):return {(i,row[i],j,row[j]) for i in range(len(keys)) for j in range(i+1,len(keys))}
 remaining=set().union(*(pairs(x) for x in candidates));chosen=[]
 if len(keys)==1:chosen=candidates
 while remaining:
  best=max(candidates,key=lambda x:len(pairs(x)&remaining));chosen.append(best);remaining-=pairs(best);candidates.remove(best)
 return {'cases':[dict(zip(keys,[factors[k][x] for k,x in zip(keys,row)])) for row in chosen],'caseCount':len(chosen),'cartesianCount':size,'pairCoverageComplete':True,'testsExecuted':False}

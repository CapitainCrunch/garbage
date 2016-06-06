import re, codecs

tweets = []
f = codecs.open(u'adastraz.htm', 'r', 'utf-8-sig')
for line in f:
    line.lower()
    m = re.findall('class="twitter-atreply pretty-link" dir="ltr" ><s>@</s><b>([\\w]+)</b></a>([\\w]+)*/p>$', line)
    tweets.append(m)



            
                   


                   

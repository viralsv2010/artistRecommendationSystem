import re

wordlist = ["soundigest","vile","paris"	,"carlyaquilino","chrispolanco13","bimbo's","mcr","jack","lauren_hoggs","siriusxm","force","7th","muz4now","christ","orchestra","100","rampb","gla","ferrygodmother","paperliliesny","sonysquarenyc","diana","rydell","julia","gorillaz","sarah","dannylopriore","palestinian","playboy","boingo","renatogouveiaaa","factor00a0singer","billyjoel","strings","amp","rosamunde","chance","jamming","boom","guitarist","renowned","schomburgcenter","excitement","metallica s","official","alysonstoner","blabbermouthnet","nostalgia","music","band","orchestra","song","pianist","drummer","singer"]

data = []
counter=0
with open("Music_Words.txt","w") as fout:
    with open("Data_File.txt") as fin:
        for line in fin:
            for term in line.split():
                term = term.lower()
                term= re.sub('[\n]+', ' ', term)
                # Remove not alphanumeric symbols white spaces
                term = re.sub(r'[^\w]', ' ', term)
                # Replace #word with word
                term = re.sub(r'#([^\s]+)', r'\1', term)
                # Remove :( or :)
                term = term.replace(':)', '')
                term = term.replace(':(', '')
                # trim
                term = term.strip('\'"')
                #print term
                if term in wordlist:
		        	if counter==0:
		        		data.append(term)

		        	else:
		        		data.append(term)
		        		#print data
            if len(data)>0:
				text=','.join(data)
				fout.write('"' + text + '",' )
				#print "data to write :", data
				fout.write("\n")
            data =[]

				
		    










	    # music soundigest vile paris band carlyaquilino          chrispolanco13  bimbo's  
	    # mcr  Jack lauren_hoggs siriusxm force 7th muz4now  christ orchestra 100 rampb GLA  christ
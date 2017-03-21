import csv

def list_words(text):
    words = []
    words_tmp = text.lower().split()
    for p in words_tmp:
        if p not in words and len(p) > 2:
            words.append(p)
    return words

def training(texts):
    c_words ={}
    c_categories ={}
    c_texts = 0
    c_tot_words =0
    c_spam=0
    c_ham=0
	#claculate text count and category wise count of emails
    for t in texts:
        c_texts = c_texts + 1
	#print t[1]
        if t[1] not in c_categories:
            c_categories[t[1]] = 1
        else:
            c_categories[t[1]]= c_categories[t[1]] + 1

    for t in texts:
	if t[1]=="spam":
	       c_spam=c_spam+1
	if t[1]=="nospam":
	       c_ham=c_ham+1
    	words = []
    	words_tmp = t[0].lower().split()
    	for p in words_tmp:
            if p not in words and len(p) > 2:
            	words.append(p)
        for p in words:
            if p not in c_words:
               c_tot_words = c_tot_words +1
               c_words[p] = {}
               for c in c_categories:
                   c_words[p][c] = 0
            c_words[p][t[1]] = c_words[p][t[1]] + 1
    ###with open("mtd.csv","a") as out:
    	###for p in c_words :
	   ### print (p , c_words[p]["spam"] , c_words[p]["nospam"])
    print ("total spam mails=" ,c_spam)
    print ("total ham mails=" ,c_ham)
    print (c_categories["spam"] , c_categories["nospam"])
    print (c_texts, c_tot_words)
    return (c_words, c_categories, c_texts, c_tot_words)


def classifier(subject_line, c_words, c_categories, c_texts, c_tot_words):
    category ="spam"
    category_prob = 0

    for c in c_categories:
      
        prob_c = float(c_categories[c])/float(c_texts)
        words = list_words(subject_line)
        prob_total_c = prob_c
        for p in words:
         
            if p in c_words:
                prob_p= float(c_words[p][c])/float(c_tot_words)
                prob_cond = prob_p/prob_c
                prob =(prob_cond * prob_p)/ prob_c
                prob_total_c = prob_total_c * prob

            if category_prob < prob_total_c:
                category = c
                category_prob = prob_total_c
    return (category, category_prob)


if __name__ == "__main__":
    #### call to main Training procedure ####
    with open('dataham.csv') as f:
        subjects = dict(csv.reader(f, delimiter=','))
        p,c,t,tp = training(subjects.items())


    #### main Test procedure  #####
    with open("test.csv") as f:
        correct = 0
	total=0
        tests = csv.reader(f)
        for subject in tests:
            clase = classifier(subject[0],p,c,t,tp)
	    print (clase[0],clase[1],subject[1])            
	    if clase[0] == subject[1]:
                correct += 1
	    total+=1
	eff=float((float(correct)/float(total)))*100	
        print("Efficiency is {0}".format(eff))

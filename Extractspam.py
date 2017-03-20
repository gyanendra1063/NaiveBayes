import os
files = os.listdir(r"spam")
with open("dataham.csv","a") as out:
    n = 0
    for fname in files:
	path = os.path.join(os.path.expanduser('~'), 'spam',fname)
        with open(path) as f:
            data = f.readlines()
            for line in  data:
                if line.startswith("Subject:"):
		    line=line.replace(",", "")
		    print(line)
                    n +=1
                    out.write("{0},spam\n".format(line[8:-1]))
		if n >= 250:
	            break
            print(fname)

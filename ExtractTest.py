import os
files = os.listdir(r"testing_hm")
#files = os.listdir(r"testing_sp")
with open("test.csv","a") as out:
    n = 0
    for fname in files:
	path = os.path.join(os.path.expanduser('~'), 'testing_hm',fname)
        with open(path) as f:
            data = f.readlines()
            for line in  data:
                if line.startswith("Subject:"):
		    if len(line)<=10:
		       line="11111111NULL1"
		    line=line.replace(",", "")
		    print(line)
                    n +=1
                    out.write("{0},nospam\n".format(line[8:-1]))
            print(fname)

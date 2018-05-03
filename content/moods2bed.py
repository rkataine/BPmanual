import sys


resultline = ""
for line in sys.stdin:

	split = line.split(",")
	chr = split[0].split(" ")[0]

	if split[2].isdigit():

		resultline = chr +"\t" +split[2] +"\t" +str((int(split[2]) + len(split[5]))) +"\t" +split[1].replace(".pfm","") +"\t" +split[4] +"\t" +split[3]
	else:
	
		resultline = chr +"\t" +split[3] +"\t" +str((int(split[3]) + len(split[6]))) +"\t" +split[2].replace(".pfm","") +"\t" +split[5] +"\t" +split[4]
  
	print resultline

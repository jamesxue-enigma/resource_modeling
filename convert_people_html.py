l =  ['AFROOZE, JALEH', 'AHEARN, EVE', 'ATTAHRI, MOHAMED', 'BARKER, JOHN', 'BECKER, NICK', 
'BENOIT, MICHAEL', 'BOMAN, BLAINE', 'CHAN, KELVIN', 'CHOLAS-WOOD, ALEX', 'CHRISTENSEN, EMIL',
'CREIGHTON, JENNIFER', 'DACOSTA, MARC', 'DANTON, CRAIG', 'DELGADILLO, SUSANA', 'DONATZ, MICHAEL',
'EASTBURN, BENJAMIN', 'EDGAR, JAMES', 'ESTES, STEPHEN', 'FLOWERS, MICHAEL', 'GAO, DAVID',
'GELB, BENJAMIN', 'GONZALEZ, JUAN', 'GUTMAN, LEE', 'HALLOCK, SAMANTHA', 'HAMMER, MELODY',
'HENDERSON, PETER', 'HILEWICZ, RONEN', 'HORAN, MATTHEW', 'IANIUK, OLGA', 'JOHNSON, COURTNEY',
'KEITER, KENNETH', 'KELMANSKIY, YEFIM', 'KERLE, INDIA', 'KHALIFA, DONIA', 'KIRCHER, ASHLEY',
'KNUPP, JEFFREY', 'KREMLER, GREGORY', 'KRINSLEY, JEREMY', 'LEONE, MICHAEL', 'LEV, IGOR',
'LEVIN, JONATHAN', 'LI, ANN', 'MADDALA, BHASKAR', 'MELEMED, DANIEL', 'MIKAELIAN, ALEXIS',
'MONK, CLINTON', 'MORAN, THOMAS', 'MUKHERJEE, ISHANI', 'NORTHINGTON, ALEXANDRA', 'OMI, ALISA',
'OUDGHIRI, HICHAM', 'PARIKH, URVISH', 'PARKER, JARROD', 'PRAINITO, JOE', 'PRATER, RICHARD',
'PRICE, REBECCA', 'ROTH, ALEXANDER', 'RUBENSTEIN, ABRAHAM', 'RUBINSTEIN, DAVID', 'SESSER, BENJAMIN',
'SHAO, BRYAN', 'SPIEGEL, STEPHANIE', 'STANLEY, MICHAEL', 'SULLAM, JULIANA', 'TEYSSIER, MAUREEN',
'ULMAN, JEREMY', 'VARSHAVSKY, PETER', 'WARDY, JASON', 'WATT, CECILIA', 'WEBB, WILLIAM', 'WEINBERG, JEFF',
'WELLS, THOMAS', 'WHALEN, CAITLIN', 'WHITING, OWEN', 'WILSON, JOSHUA', 'WRISINGER, ANDREW', 'YANG, YANG']


with open('output.txt', 'w') as f:
	for i in range(0, len(l)):
	 	f.write('<li><a href="#" class="small" data-value="' + l[i] + '" tabIndex="-1"> \
	 		<input type="checkbox" class="people" checked/>&nbsp;' + l[i] + '</a></li>' + '\n')


f.close()
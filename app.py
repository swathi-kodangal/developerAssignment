from datetime import datetime
#datalist
mylist1 = []
#read data from file
with open('sales-data.txt','r') as text_file:
    for line in text_file:
        mylist = []
        #append data line by line to list
        mylist.append(line.rstrip('\n'))
        listToStr = ' '.join([str(elem) for elem in mylist]) 
        stringsplitted = listToStr.split(',')
        mylist1.append(stringsplitted)
#another copy of data
anothercopyoflist = list(mylist1)
del anothercopyoflist[0]
totalsales = 0
janmonthsale = 0
febmonthsale = 0
marmonthsale = 0
#january month data list
jantotallist1 = []
#febrauary month data list
febtotallist1 = []
#march month data list
martotallist1 = []
for itemlist in  anothercopyoflist:
    #convert string to date
    dateofsale = datetime.strptime(itemlist[0] , '%Y-%m-%d')
    #check if month is january
    if dateofsale.month == 1:
        jantotallist = itemlist
        jantotallist1.append(jantotallist)
        totalsalesofjanmonth = itemlist[4]
        janamont = int(totalsalesofjanmonth)
        janmonthsale = janamont +  janmonthsale
    #check if month is febrauary 
    elif dateofsale.month == 2:
        febtotallist = itemlist
        febtotallist1.append(febtotallist)
        totalsalesoffebmonth = itemlist[4]
        febamont = int(totalsalesoffebmonth)
        febmonthsale = febamont +  febmonthsale
    #check if month is march
    else:
        martotallist = itemlist
        martotallist1.append(martotallist)
        totalsalesofmarmonth = itemlist[4]
        maramont = int(totalsalesofmarmonth)
        marmonthsale = maramont +  marmonthsale
#sum of january sales, febrauray sales and march sales
totalamount = janmonthsale +  febmonthsale + marmonthsale
jannqty_dict = {}
febqty_dict = {}
marqty_dict = {}
janrevenue_dict = {}
febrevenue_dict = {}
marrevenue_dict = {}
#add items from january data to dictionary
for itemlist in jantotallist1:
    keys = ''.join(itemlist[1])
    key =  keys.strip('"')
    #if key is same add it to the same key
    if itemlist[1] in jannqty_dict:
        jannqty_dict[itemlist[1]]+= int(itemlist[3])
    
    else:
        #add it as new key
        jannqty_dict[itemlist[1]] = int(itemlist[3])
#the most popular item in january
janmaxqtysold = max(jannqty_dict, key=jannqty_dict.get) 

#add items from february data to dictionary

for itemlist in febtotallist1:
    keys = ''.join(itemlist[1])
    key =  keys.strip('"')
    #if key is same add it to the same key
    if key in febqty_dict:
        febqty_dict[key]+= int(itemlist[3])
    
    else:
        #add it as new key
        febqty_dict[itemlist[1]] = int(itemlist[3])
#the most popular item in february

febmaxqtysold = max(febqty_dict, key=febqty_dict.get) 

#add items from march data to dictionary
for itemlist in martotallist1:
    keys = ''.join(itemlist[1])
    key =  keys.strip('"')
    #if key is same add it to the same key
    if key in marqty_dict:
        marqty_dict[key]+= int(itemlist[3])
    
    else:
        #add it as new key
        marqty_dict[itemlist[1]] = int(itemlist[3])
#the most popular item in march
marmaxqtysold = max(marqty_dict, key=marqty_dict.get) 

#Item generating most revenue in january month.
for itemlist in jantotallist1:
    keys = ''.join(itemlist[1])
    key =  keys.strip('"')
    #if key is same add it to the same key
    if itemlist[1] in janrevenue_dict:
        janrevenue_dict[itemlist[1]]+= int(itemlist[4])
    
    else:
        #add it as new key
        janrevenue_dict[itemlist[1]] = int(itemlist[4])
#most  revenu generated in january month
janmaxrevenuesold = max(janrevenue_dict, key=janrevenue_dict.get) 

#Item generating most revenue in febrauary month.
for itemlist in febtotallist1:
    keys = ''.join(itemlist[1])
    key =  keys.strip('"')
    #if key is same add it to the same key
    if key in febrevenue_dict:
        febrevenue_dict[key]+= int(itemlist[4])
    else:
        #add it as new key
        febrevenue_dict[itemlist[1]] = int(itemlist[4])
#most  revenu generated in febrauary month
febmaxrevenuesold = max(febrevenue_dict, key=febrevenue_dict.get) 

#Item generating most revenue in march month.
for itemlist in martotallist1:
    keys = ''.join(itemlist[1])
    key =  keys.strip('"')
    #if key is same add it to the same key
    if key in marrevenue_dict:
        marrevenue_dict[key]+= int(itemlist[4])
    else:
        #add it as new key
        marrevenue_dict[itemlist[1]] = int(itemlist[4])
#most  revenu generated in march month
marmaxrevenuesold = max(marrevenue_dict, key=marrevenue_dict.get) 

jannqtyy_dict = {}
itemlisst = []
#loop the january data
for itemlist in jantotallist1:
    keys = ''.join(itemlist[1])
    key =  keys.strip('"')
    #check if item exists
    if itemlist[1] in jannqty_dict:
        #search for max solded item 
        if itemlist[1] == janmaxqtysold:
            #append qty to list
            itemlisst.append(int(itemlist[3]))
            jannqtyy_dict[itemlist[1]] = itemlisst
#max  auantity sold in january
janmaxqtysoldd = max(max(jannqtyy_dict.values())) 
#min  quantity sold in january
janminqtysoldd = min(min(jannqtyy_dict.values())) 


jancount = 0
popularitemjantotal = 0
for k in jannqtyy_dict.keys():
    for i in jannqtyy_dict[k]:
        jancount+= 1
        #sum of  quantity of the most solded item
        popularitemjantotal += i
#avg quantity sold in january
avgnumberofpopularitemsoldinjan = popularitemjantotal/jancount


febnqtyy_dict = {}
itemlisstinfeb = []
#loop the febrauary data

for itemlist in febtotallist1:
    keys = ''.join(itemlist[1])
    key =  keys.strip('"')
    #check if item exists
    if itemlist[1] in febnqtyy_dict:
        #search for max solded item
        
        if itemlist[1] == febmaxqtysold:
            #append qty to list
            
            itemlisstinfeb.append(int(itemlist[3]))
            febnqtyy_dict[itemlist[1]] = itemlisstinfeb
    else:
            if itemlist[1] == febmaxqtysold:
                itemlisstinfeb.append(int(itemlist[3]))
                febnqtyy_dict[itemlist[1]] = itemlisstinfeb

#maximum  quantity sold by popular item in febrauary
febmaxqtysoldd = max(max(febnqtyy_dict.values())) 
#minimum  quantity sold by popular item in febrauary
febminqtysoldd = min(min(febnqtyy_dict.values())) 


febcount = 0
popularitemfebtotal = 0
for k in febnqtyy_dict.keys():
    for i in febnqtyy_dict[k]:
        febcount+= 1
        #sum of  quantity of the most solded item
        popularitemfebtotal += i
#average  quantity sold by popular item in febrauary  
avgnumberofpopularitemsoldinfeb = popularitemfebtotal/febcount

marnqtyy_dict = {}
itemlisstinmar = []
#loop the march data
for itemlist in martotallist1:
    keys = ''.join(itemlist[1])
    key =  keys.strip('"')
    #check if item exists
    if itemlist[1] in marnqtyy_dict:
        #search for max solded item
        if itemlist[1] == marmaxqtysold:
            #append qty to list
            itemlisstinmar.append(int(itemlist[3]))
            marnqtyy_dict[itemlist[1]] = itemlisst
    else:
        if itemlist[1] == marmaxqtysold:
            itemlisstinmar.append(int(itemlist[3]))
            marnqtyy_dict[itemlist[1]] = itemlisst
#maximum  quantity sold by popular item in march
marmaxqtysoldd = max(max(marnqtyy_dict.values()))
#minimum  quantity sold by popular item in march 
marminqtysoldd = min(min(marnqtyy_dict.values())) 

marcount = 0
popularitemmartotal = 0
for k in marnqtyy_dict.keys():
    for i in marnqtyy_dict[k]:
        marcount+= 1
        #sum of  quantity of the most solded item
        popularitemmartotal += i
#average  quantity sold by popular item in march  
avgnumberofpopularitemsoldinmar = popularitemmartotal/marcount


print("total sales of january month of the store is Rs.{}".format(janmonthsale))
print("total sales of febrauary month of the store is Rs.{}".format(febmonthsale))
print("total sales of march month of the store is Rs.{}".format(marmonthsale))
print("total amount is Rs.{}".format(totalamount))
print("Most popular item (most quantity sold)  in january is {} ".format(janmaxqtysold))
print("Most popular item (most quantity sold)  in febrauary is {} ".format(febmaxqtysold))
print("Most popular item (most quantity sold)  in march is {} ".format(marmaxqtysold))

print("Items generating most revenue in january is {} ".format(janmaxrevenuesold))
print("Items generating most revenue in   in febrauary is {} ".format(febmaxrevenuesold))
print("Items generating most revenue in  in march is {} ".format(marmaxrevenuesold))

print("Most popular item in january is {}  and max order is {}".format(janmaxqtysold,janmaxqtysoldd))
print("Most popular item in january is {}  and min order is {}".format(janmaxqtysold,janminqtysoldd ))
print("Most popular item in january is {}  and avg order is {}".format(janmaxqtysold,avgnumberofpopularitemsoldinjan ))

print("Most popular item in febrauary is {}  and max order is {}".format(febmaxqtysold,febmaxqtysoldd))
print("Most popular item in febrauary is {}  and min order is {}".format(febmaxqtysold,febminqtysoldd ))
print("Most popular item in febrauary is {}  and avg order is {}".format(febmaxqtysold,avgnumberofpopularitemsoldinfeb ))

print("Most popular item in march is {}  and max order is {}".format(marmaxqtysold,marmaxqtysoldd))
print("Most popular item in march is {}  and min order is {}".format(marmaxqtysold,marminqtysoldd ))
print("Most popular item in march is {}  and avg order is {}".format(marmaxqtysold,avgnumberofpopularitemsoldinmar ))

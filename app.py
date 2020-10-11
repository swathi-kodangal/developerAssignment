from datetime import datetime

#mostpopular item in each month
def mostpopularitem(monthsdata):
    #add items from monthsdata data to dictionary
    qty_dict = {}
    for itemlist in monthsdata:
        #if key is same add it to the same key
        if itemlist[1] in qty_dict:
            qty_dict[itemlist[1]]+= int(itemlist[3])
        else:
            #add it as new key
            qty_dict[itemlist[1]] = int(itemlist[3])
    #the most popular item in every month
    maxqtysold = max(qty_dict, key=qty_dict.get) 
    return maxqtysold

#items generating most revenue
def mostrevenuegenerated(monthsdata):
    #Item generating most revenue in each month.
     revenue_dict = {}
     for itemlist in monthsdata:
         keys = ''.join(itemlist[1])
         key =  keys.strip('"')
         #if key is same add it to the same key
         if key in revenue_dict:
             revenue_dict[key]+= int(itemlist[4])
         else:
             #add it as new key
             revenue_dict[itemlist[1]] = int(itemlist[4])
             #most  revenu generated in each month
     maxrevenuesold = max(revenue_dict, key=revenue_dict.get) 
     return maxrevenuesold

#get minimum, maximum , average quantity of popular item in each month
def maxminavgineachmonth(monthsdata,maxqtysold):
    qtyy_dict = {}
    itemlisst = []
    #loop the month data
    for itemlist in jantotallist1:
        #check if item exists
        if itemlist[1] in qtyy_dict:
        #search for max solded item 
          if itemlist[1] == maxqtysold:
            #append qty to list
            itemlisst.append(int(itemlist[3]))
            qtyy_dict[itemlist[1]] = itemlisst
        else:
            if itemlist[1] == maxqtysold:
                itemlisst.append(int(itemlist[3]))
                qtyy_dict[itemlist[1]] = itemlisst
    #max  auantity sold in each month
    maxqtysoldd = max(max(qtyy_dict.values())) 
    #min  quantity sold in each month
    minqtysoldd = min(min(qtyy_dict.values())) 
    count = 0
    popularitemtotal = 0
    for k in qtyy_dict.keys():
        for i in qtyy_dict[k]:
            count+= 1
            #sum of  quantity of the most solded item
            popularitemtotal += i
    #avg quantity sold in each month
    avgnumberofpopularitemsold = popularitemtotal/count
    return(maxqtysoldd,minqtysoldd,avgnumberofpopularitemsold)

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
janmaxqtysold = mostpopularitem(jantotallist1)
febmaxqtysold = mostpopularitem(febtotallist1) 
marmaxqtysold = mostpopularitem(martotallist1) 
janmaxrevenuesold = mostrevenuegenerated(jantotallist1)
febmaxrevenuesold = mostrevenuegenerated(febtotallist1) 
marmaxrevenuesold = mostrevenuegenerated(martotallist1) 
janmaxqtysoldd, janminqtysoldd, avgnumberofpopularitemsoldinjan = maxminavgineachmonth(jantotallist1, janmaxqtysold) 
febmaxqtysoldd, febminqtysoldd, avgnumberofpopularitemsoldinfeb = maxminavgineachmonth(febtotallist1, febmaxqtysold)
marmaxqtysoldd, marminqtysoldd, avgnumberofpopularitemsoldinmar = maxminavgineachmonth(martotallist1, marmaxqtysold)

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

import pycassa
from collections import defaultdict

retailers = [(1,"Tops & T-Shirts",1,1,1,1,3),
(2,"Knitwear",1,1,1,1,2),
(3,"Trousers & Jeans",1,1,1,1,1),
(4,"Skirts",0,1,0,1,4),
(5,"Dresses",0,1,0,1,5),
(6,"Formal Wear",1,1,1,1,6),
(7,"Outer Wear",1,1,1,1,7),
(8,"Under Wear",1,1,1,1,8),
(9,"Swim Wear",1,1,1,1,9),
(10,"Night Wear",1,1,1,1,10),
(11,"Foot Wear",1,1,1,1,11),
(12,"Bags",1,1,1,1,12),
(13,"Hats",1,1,1,1,13),
(14,"Jewellery",1,1,1,1,14),
(15,"Accessories",1,1,1,1,15),
(1032,"~UNPROCESSED~",1,1,0,0),
(0,"~UNPROCESSED~",1,1,0,0)]

retailer_lookup = {}

for r in retailers:
    retailer_lookup[r[0]] = r[1]

print retailer_lookup

connection_pool = pycassa.ConnectionPool("FS_PROD",server_list=['10.229.15.240'],timeout=None)
products_cf = pycassa.ColumnFamily(connection_pool,"Product")

res = products_cf.get_range(start='a')


cat_prices = defaultdict( lambda: defaultdict( lambda: [] ))
counter = defaultdict( lambda: defaultdict( lambda: 0 ))
total_price = defaultdict( lambda: defaultdict( lambda: 0 ))

limit = 100
processed = 0
limit_results = False

for pid, pdata in res:
    #print pdata
    
    retailer_id = pdata.get('ret_id', None)
    out_of_stock = pdata['out_of_stock']
    if out_of_stock !="0":
        continue
    if not retailer_id:
        print "Product has no retailer id %s" % pdata
    price = float(pdata['price'])
    cat = pdata['fs_cid']
    region = retailer_id[-2:]

    #print retailer_id, region, cat, price

    counter[region][cat]+=1

    if region == "uk":
        price = price * 1.5843

    total_price[region][cat]+=price
    cat_prices[region][cat].append(price)

    processed+=1
    if limit_results and processed > limit:
        break

print "Processed %s products" % processed

print counter
print total_price

avg_price = defaultdict( lambda: defaultdict( lambda: 0.0 ))
median_price = defaultdict( lambda: defaultdict( lambda: 0.0 ))

for region, rcounter in counter.items():
    for cat, total in rcounter.items():
        avg_price[region][cat] = (total_price[region][cat] *1.0) / total    

for region, rcat_prices in cat_prices.items():
    for cat, cat_list in rcat_prices.items():
        l = len(cat_list)
        median = sorted(cat_list)[int(l/2)]
        median_price[region][cat] = median

for region, ravg_prices in avg_price.items():
    for cat, avg_price in ravg_prices.items():
        print "%s,%s,%s,%s,%s,%s" % (region, retailer_lookup[int(cat)], cat, counter[region][cat], avg_price, median_price[region][cat])
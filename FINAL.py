import scrap_utils
import AI_thingies
from multiprocessing import Manager, Process
max_price = 0
min_price = 0
def Process_scrape(FUNC, QUERY, WEBSITE, LIST):
    try:
        Info = FUNC(QUERY)
        LIST.extend(Info) 
    except Exception as e:
        print(f"Error in {WEBSITE} scraping: {e}")

def SCRAPE(query):
    with Manager() as manager:
        result_list = manager.list()  # Correct way to create a manager list
        website = AI_thingies.Dore_no_website(query)
        website = website.strip()
        for web in website:
            print("A:", web)
        print(website, "hi there")
        # Create processes based on website
        if website.lower() == "amaflip":
            print("amafliping")
            processes = [
                Process(target=Process_scrape, args=(scrap_utils.get_amazon, query, website, result_list)),
                Process(target=Process_scrape, args=(scrap_utils.get_flipkart, query, website, result_list))
            ]
        elif website.lower() == "zekit":
            print("zekitting")
            processes = [
                Process(target=Process_scrape, args=(scrap_utils.get_blinkit, query, website, result_list)),
                Process(target=Process_scrape, args=(scrap_utils.get_zepto, query, website, result_list))
            ]
        else:
            print("NO NOT HERE")
            processes = [
                Process(target=Process_scrape, args=(scrap_utils.get_amazon, query, website, result_list)),
                Process(target=Process_scrape, args=(scrap_utils.get_flipkart, query, website, result_list)),
                Process(target=Process_scrape, args=(scrap_utils.get_blinkit, query, website, result_list)),
                Process(target=Process_scrape, args=(scrap_utils.get_zepto, query, website, result_list))
            ]

        for p in processes:
            p.start()

        for p in processes:
            p.join()

        return list(result_list)


def kushu_big(inf):
    global max_price
    global min_price
    norm_price = (inf['price'] - min_price)/(max_price - min_price)
    norm_rating  = float(inf['rating'] or 0)/5
    fin_rating = norm_price/(norm_rating + 0.001)
    inf['fin_rating'] = fin_rating
    return inf

def sort_list(info):
    global max_price
    global min_price
    print("enter sorting", len(info))
    if info[0]["website"] == "amaflip":
        min_price = min(info, key=lambda x: x['price'])['price']
        max_price = max(info, key=lambda x: x['price'])['price']
        print(min_price, max_price)
        for inf in info:
            norm_price = (inf['price'])/(max_price)
            norm_rating  = float(inf['rating'] or 0)/5
            fin_rating = norm_price/(norm_rating + 0.001)
            inf['fin_rating'] = fin_rating

        # info = list(map(kushu_big, info))

    info.sort(key=lambda x: (x['fin_rating']))

    return info


# if __name__ == "__main__":
#     resu = SCRAPE("phones")
#     res = sort_list(resu)
#     for re in res:
#         print(res)
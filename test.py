import scrap_utils


res = scrap_utils.get_blinkit("curry leaf")

for t, p , r, s, g in res:
    print(t ,   p ,      r,    s     ,     g)
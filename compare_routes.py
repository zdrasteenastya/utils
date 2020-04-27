import xlrd

rb_sc = xlrd.open_workbook('scraped.xlsx')
list_sc = rb_sc.sheet_by_index(0)
vals_sc = [list_sc.row_values(rownum) for rownum in range(list_sc.nrows)]

scraped_routes = [(route[0], route[1]) for route in vals_sc]

rb_mn = xlrd.open_workbook('manual.xlsx')
list_mn = rb_mn.sheet_by_index(0)
vals_mn = [list_mn.row_values(rownum) for rownum in range(list_mn.nrows)]

manual_routes = [(route[0], route[1]) for route in vals_mn]

unique_routes = []
for route in manual_routes:
    if route not in scraped_routes:
        unique_routes.append(route)

print len(unique_routes)

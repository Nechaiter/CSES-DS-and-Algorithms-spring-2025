def min_count(product_count, box_size):
    min_box_count=0
    if product_count%box_size>0:
        min_box_count=1
    min_box_count=min_box_count+(product_count//box_size)
    
    return min_box_count
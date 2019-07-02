#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Product purchase analytics
# Sumit Dutta
# 7/1/2019
# Runs in Python 3


# In[2]:


import csv
# import numpy as np


# In[3]:


orders = []
product_ct = {}
first_p_ct = {}
with open('../input/order_products.csv') as csvfile:
    try:
        reader = csv.DictReader(csvfile, fieldnames=('order_id','product_id','add_to_cart_order','reordered'))
        line_number = 0
        for row in reader:
            line_number += 1
            if (line_number == 1):
                continue
            # print(row)
            product_id = int(row['product_id'])
            if product_id in product_ct.keys():
                product_ct[product_id] = product_ct[product_id] + 1
            else:
                product_ct[product_id] = 1
            first_time_ordered = not(bool(int(row['reordered'])))
            if (first_time_ordered):
                if product_id in first_p_ct.keys():
                    first_p_ct[product_id] = first_p_ct[product_id] + 1
                else:
                    first_p_ct[product_id] = 1
    except Exception as e:
        print(e)
# csvfile.close()


# In[4]:


print(product_ct)


# In[5]:


print(first_p_ct)


# In[6]:


departments = []
dept_products = {}
with open('../input/products.csv') as csvfile:
    try:
        reader = csv.DictReader(csvfile, fieldnames=('product_id','product_name','aisle_id','department_id'))
        line_number = 0
        for row in reader:
            line_number += 1
            if (line_number == 1):
                continue
            # print(row)
            product_id = int(row['product_id'])
            dept_id = int(row['department_id'])
            if dept_id in dept_products.keys():
                if not(product_id in dept_products[dept_id]):
                    dept_products[dept_id].append(product_id)
            else:
                dept_products[dept_id] = [product_id]
    except Exception as e:
        print(e)
# csvfile.close()


# In[7]:


print(dept_products)


# In[8]:


# Put ordered list of products ordered, and ordered for the first time into a new dictionary data structure
dept_orders = {}
dept_orders_csv = [['department_id','number_of_orders','number_of_first_orders','percentage']]
for dept_id in sorted(dept_products.keys()):
    product_ids = dept_products[dept_id]
    department_order_sum = 0
    department_first_order_sum = 0
    for product_id in product_ids:
        if (product_id in product_ct.keys()):
            department_order_sum += product_ct[product_id]
        if (product_id in first_p_ct.keys()):
            department_first_order_sum += first_p_ct[product_id]
    number_of_orders = department_order_sum
    number_of_first_orders = department_first_order_sum
    percentage = number_of_first_orders / number_of_orders
    dept_orders[dept_id] = [number_of_orders,number_of_first_orders,percentage]
    dept_orders_csv.append([dept_id,number_of_orders,number_of_first_orders,percentage])
    

    
# List this department only if number_of_orders > 0
#%.2f


# In[9]:


print(dept_orders)


# In[10]:


with open('../output/report.csv', 'w') as outcsvfile:
    writer = csv.writer(outcsvfile)
    writer.writerows(dept_orders_csv)

outcsvfile.close()


# In[ ]:





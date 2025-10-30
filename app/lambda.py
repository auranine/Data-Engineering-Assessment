import sys
import json
import os
import pandas as pd

from src.orders.services.order_service import OrderService

"""
Modify this lambda function to perform the following questions

1. Find the most profitable Region, and its profit
2. What shipping method is most common for each Category
3. Output a glue table containing the number of orders for each Category and Sub Category 


NOTE: Skipping instructions above and following the instruction.md (write 3 files to s3 as output - the comments above do not match the requirements)
"""


def handler(event, context):
    print(event)
    print(context)
    return

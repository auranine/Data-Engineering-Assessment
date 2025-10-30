import pandas as pd
from pathlib import Path
import pytest

from orders.services.order_service import OrderService

def load_df():
    file = Path(__file__).parent / "resources" / "sample_orders.csv"
    df = pd.read_csv(file)
    return df

###
# OrderService.calculate_profit_by_order
###
def test_calculate_profit_by_order_basic():
    df = pd.DataFrame({
        "Order Id": [1],
        "cost price": [50.0],
        "List Price": [100.0],
        "Quantity": [2],
        "Discount Percent": [10.0],
    })
    result = OrderService.calculate_profit_by_order(df)
    assert result.loc[0, "Profit"] == 80.0

def test_calculate_profit_by_order_from_file():
    result = OrderService.calculate_profit_by_order(load_df())
    aggregated_row = result.loc[result["Order Id"] == "CA-2023-1019"]
    print(aggregated_row)
    assert aggregated_row["Profit"].iloc[0] == pytest.approx(303.7)

###
# OrderService.calculate_most_profitable_region
###
def test_calculate_most_profitable_region_from_file():
    result = OrderService.calculate_most_profitable_region(load_df())
    print(result)
    assert result.iloc[0]["Region"] == "East"
    assert result.iloc[0]["Profit"] == pytest.approx(2465.5)


###
# OrderService.find_most_common_ship_method():
###
def test_find_most_common_ship_method():
    result = OrderService.find_most_common_ship_method(load_df())
    print(result)
    assert result.iloc[0]["Ship Mode"] == "Same Day"
    assert result.iloc[0]["Count"] == 8

###
# OrderService.find_number_of_orders_per_category
###
def test_find_number_of_orders_per_category():
    result = OrderService.find_number_of_orders_per_category(load_df())
    print(result)
    assert result.iloc[0]["Category"] == "Office Supplies"
    assert result.iloc[0]["Sub Category"] == "Binders"
    assert result.iloc[0]["Count"] == 3



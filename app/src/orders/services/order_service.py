import pandas as pd
from typing import Iterable, Optional

class OrderService:

    # TODO: Map df to domain entities
    @staticmethod
    def map(orders_df:pd.DataFrame):
        return []

    @staticmethod
    def validate_and_load(orders_df: pd.DataFrame) -> pd.DataFrame:
        # TODO: Validate and clean data
        return orders_df.copy()

    @staticmethod
    def calculate_profit(orders_df: pd.DataFrame) -> pd.DataFrame:
        # TODO: setup validation of input (Order Id, cost price, List Price, Quantity, Discount Percent)
        #       this would also typecheck and coerce numbers from strings
        # NOTE: i am leaving the inconsistent 'cost price' here assuming that the input cannot be changed as external data
        df = OrderService.validate_and_load(orders_df)
        df["Profit"] = (
                (
                        (df['List Price'] * (1 - df["Discount Percent"] / 100))
                        - df["cost price"]
                )  * df["Quantity"]
        )
        return df

    @staticmethod
    def calculate_profit_by_order(orders_df: pd.DataFrame, group_by: Optional[Iterable[str]] = ("Order Id",)) -> pd.DataFrame:
        """
        Calculate Order DataFrame - The data may be flat one to many (e.g. duplicate order ids with different products - Maybe???)

        Args:
            orders_df (pd.DataFrame): Orders DataFrame (Order Id, cost price, List Price, Quantity, Discount Percent)
            group_by (Iterable[str]): Order By Columns for Aggregate Calculation - Default group by OrderId

        Returns:
            result_df (pd.DataFrame): Result DataFrame OrderId, Profit


        """

        df = OrderService.calculate_profit(orders_df)
        # Assuming that Order Id is a primary key for this data - just in case, we'll group/aggregate in the event it's flattened one to many data
        if group_by:
            grouped_cols = list(group_by)
            # as_index=False so pandas doens't use the group as new index - which is default
            aggregate = (
                df.groupby(grouped_cols, as_index=False).agg(Profit=("Profit", "sum"))
            )
            return aggregate

        return df

    @staticmethod
    def calculate_most_profitable_region(orders_df: pd.DataFrame) -> pd.DataFrame:
        """
        Get the most profitable region as a single row DataFrame

        Args:
            orders_df (pd.DataFrame): Orders DataFrame (Order Id, cost price, List Price, Quantity, Discount Percent, Region)

        Returns:
            result_df (pd.DataFrame): Result DataFrame OrderId, Profit

        """
        df = OrderService.calculate_profit(orders_df)
        # as_index=False so pandas doens't use the group as new index - which is default
        aggregate = (
            df.groupby(["Region"], as_index=False).agg(Profit=("Profit", "sum"))
        )
        return aggregate.loc[[aggregate["Profit"].idxmax()]]

    @staticmethod
    def find_most_common_ship_method(orders_df: pd.DataFrame) -> pd.DataFrame:
        """
        Get the most frequent shipping method as a single row DataFrame

        Args:
            orders_df (pd.DataFrame): Orders DataFrame (Ship Mode)

        Returns:
            result_df (pd.DataFrame): Result DataFrame Ship Mode, Count

        """
        df = OrderService.validate_and_load(orders_df)
        counts = (
            df.value_counts("Ship Mode")
              .rename_axis("Ship Mode")
              .reset_index(name="Count")
        )
        return counts.head(1).reset_index(drop=True) # drop original index and recreate new, clean one

    @staticmethod
    def find_number_of_orders_per_category( orders_df: pd.DataFrame) -> pd.DataFrame:
        """
        Find the number of orders for each Category and Sub Category

        Args:
            orders_df (pd.DataFrame): Orders DataFrame (Order Id, Category, Sub Category)

        Returns:
            result_df (pd.DataFrame): Result DataFrame Category, SubCategory, Order Count

        """
        df = OrderService.validate_and_load(orders_df)
        # first create a df with unique composite of order, cat and subcat
        order_cat_subcat = (
            orders_df[["Order Id", "Category", "Sub Category"]]
            .drop_duplicates()
        )
        # as_index=False so pandas doens't use the group as new index - which is default
        counts = (
            df.groupby(["Category", "Sub Category"], as_index=False)
            .agg(Count=("Order Id", "nunique")) # ensure we only counting unique orders with this grouping
            .sort_values(["Count", "Category", "Sub Category"], ascending=[False, True, True]) # sort descending with determistic sorting for cat and subcat
            .reset_index(drop=True)
        )
        return counts

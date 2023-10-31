import logging
from transaction.transaction import Transaction

logger = logging.getLogger("Market_logger")
logger.setLevel(logging.WARN)


class Market:
    def __init__(self, good_available: dict, transactions: Transaction, prices: dict):
        """
        Initialize a Market object.

        Parameters:
            good_available (dict): A dictionary specifying the available quantity of goods in the market.
                The keys are the names of goods, and the values are the initial quantities available.
            transactions (Transaction): An object or class that handles transaction-related operations in the market.
            prices (dict): A dictionary specifying the initial prices of goods in the market.
                The keys are the names of goods, and the values are the initial prices.

        Returns:
            None
        """

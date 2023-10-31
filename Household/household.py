import logging
from collections import defaultdict

logger = logging.getLogger("Household_logger")
logger.setLevel(logging.WARN)


class Household:
    def __init__(
        self, name: str, cash: int, utility_functions: dict, items: defaultdict
    ):
        self.name = name
        self.cash = cash
        self.utility_functions = utility_functions
        self.items = items

    def buy_supply(self, seller, item, transaction_amount):
        try:
            seller.sell(item, transaction_amount)
            self.cash -= transaction_amount
            if item not in self.items.keys():
                self.items[item] = 0
            self.items[item] += transaction_amount
        except:
            logger.warn(f"{self.name} tried to buy from {seller.name} but failed")

    def choose_items_to_buy(self, market):
        shoplist = defaultdict(default_factory=lambda x: 0)
        available_cash = cash
        while available_cash > 0:
            best_utility_item = None
            max_utility_increase = 0
            for item in self.utility_functions.keys():
                utility_func = self.utility_functions[item]
                current_utility_value = utility_func[self.items[item]]
                if current_utility_value > max_utility_increase:
                    max_utility_increase = (
                        utility_func[self.items[item + 1]] - current_utility_value
                    )
                    best_utility_item = item

            shoplist[best_utility_item] += 1
            available_cash -= min(market.prices[best_utility_item])

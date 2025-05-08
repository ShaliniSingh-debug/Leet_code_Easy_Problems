class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        amount= floor((purchaseAmount + 5) / 10) * 10
        if amount<10:
            return 100-purchaseAmount*amount
        else:
            return 100-amount

        
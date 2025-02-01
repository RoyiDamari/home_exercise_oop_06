from BankAccount import BankAccount
from CustomError import (NonActiveAccountError, MaxAccountsError, NegativeBalanceError, InsufficientFundsError,
                         EmptyNameError, EmptyEmailError, InvalidDepositError, InvalidWithdrawalError)


def main():
     try:
          try:
               BankAccount("", "test@example.com", 1000)
          except EmptyNameError as e:
               print("Expected error:", e)

          try:
               BankAccount("InvalidEmail", "", 1000)
          except EmptyEmailError as e:
               print("Expected error:", e)

          try:
               BankAccount("NegativeBalance", "negative@example.com", -1000)
          except NegativeBalanceError as e:
               print("Expected error:", e)

          accounts = []
          for i in range(10):
               accounts.append(BankAccount(f"User{i}", f"user{i}@example.com", 1000 * (i + 1)))

          # Attempt to create an 11th account (should raise MaxAccountsError)
          try:
               BankAccount("ExtraUser", "extra@example.com", 500)
          except MaxAccountsError as e:
               print("Expected error:", e)

          try:
               accounts[0].deposit(-50)
          except InvalidDepositError as e:
               print("Expected error:", e)

          try:
               accounts[0].withdraw(-10)
          except InvalidWithdrawalError as e:
               print("Expected error:", e)

          try:
               accounts[0].withdraw(2000)
          except InsufficientFundsError as e:
               print("Expected error:", e)

          # Close an account and attempt operations on it
          accounts[2].close_account()
          try:
               accounts[2].deposit(300)
          except NonActiveAccountError as e:
               print("Expected error:", e)

          try:
               accounts[2].withdraw(100)
          except NonActiveAccountError as e:
               print("Expected error:", e)

          try:
               accounts[2].close_account()
          except NonActiveAccountError as e:
               print("Expected error:", e)

          # Updating the balance of active account
          accounts[0].balance = 5000

          # Perform operations on active accounts
          accounts[0].deposit(200)
          accounts[1].withdraw(200)

          # Print final balances and stats
          for acc in accounts:
               print(acc)

          print("Max Balance:", BankAccount.max_balance)
          print("Min Balance:", BankAccount.min_balance)
          print("Total Balance in Bank:", BankAccount.balance_all_accounts)


     except Exception as e:
          print("Unexpected error:", e)


if __name__ == "__main__":
     main()
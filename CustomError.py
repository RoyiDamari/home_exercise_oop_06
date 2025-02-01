class NonActiveAccountError(ValueError):
    """Raised when trying to perform an operation on an inactive account."""
    def __init__(self, message="Cannot perform this operation on an inactive account."):
        super().__init__(message)

class MaxAccountsError(ValueError):
    """Raised when trying to create more than 10 accounts."""
    def __init__(self, message="Cannot create more than 10 accounts."):
        super().__init__(message)

class NegativeBalanceError(ValueError):
    """Raised when attempting to create an account with a negative balance."""
    def __init__(self, message="Balance cannot be negative."):
        super().__init__(message)

class InsufficientFundsError(ValueError):
    """Raised when attempting to withdraw more than the available balance."""
    def __init__(self, message="Insufficient funds."):
        super().__init__(message)

class EmptyNameError(ValueError):
    """Raised when attempting to create an account with an empty name."""
    def __init__(self, message="Name cannot be empty."):
        super().__init__(message)

class EmptyEmailError(ValueError):
    """Raised when attempting to create an account with an empty email."""
    def __init__(self, message="Email cannot be empty."):
        super().__init__(message)

class InvalidDepositError(ValueError):
    """Raised when attempting to deposit a non-positive amount."""
    def __init__(self, message="Deposit amount must be positive."):
        super().__init__(message)

class InvalidWithdrawalError(ValueError):
    """Raised when attempting to withdraw a non-positive amount."""
    def __init__(self, message="Withdrawal amount must be positive."):
        super().__init__(message)
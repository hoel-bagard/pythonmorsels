# [Bank Account](https://www.pythonmorsels.com/exercises/7b02e2aae0634dc4a6f8cec15d1e1a8a)

### My notes
Boring exercise with fairly uninspired instructions (I would say instructions made to induce errors). Nothing to learn for anyone even somewhat familiar with python.\
Maybe for absolute beginners (as an exercise to introduce classes).

### Usage
Run the python morsels tests with `python src/bank_account/test_bank_account.py`.\
Run the main file with `python src/bank_account/bank_account.py`.

### Description:
#### Base problem
I'd like you to make a class that represents a bank account.\
Your bank account should accept an optional balance argument (defaulting to 0), have a balance attribute, and have deposit, withdraw, and transfer methods:

#### Bonus 1
For the first bonus, I'd like you to add some checks to your class to make sure negative numbers cannot be withdrawn, deposited, or transferred and that the balance of an account can never become negative (due to a withdrawal or transfer).

The exception type should be ValueError for invalid amount scenarios above, but you can write whatever error messages you'd like.

Note that you don't need to worry about someone manually changing the balance attribute to a negative number (we'll address that concern in bonus 3).

#### Bonus 2
For the second bonus, I'd like you to assign a unique account number to each account.\
The number does not necessarily need to be incrementing by 1 or starting at 1000, it just needs to be unique.

I'd also like you to keep track of all opened accounts in an class-level accounts attribute, as a list.\
Note that the account number doesn't show up in the string representation of our BankAccount objects above, but you're welcome to add the account number to the string representation if you'd like.

#### Bonus 3
For the third bonus, I'd like you to ensure the balance attribute on your BankAccount class is a read-only attribute.

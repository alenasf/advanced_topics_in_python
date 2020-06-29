import logging
import os

os.remove("test.log")


"""Example_1"""
# logger = logging.getLogger("our logger")
# logger.setLevel(logging.DEBUG)
# logger_file = logging.FileHandler("test.log")
# logger_file.setFormatter(logging.Formatter("%(levelname)s:%(asctime)s:%(message)s"))
# logger.addHandler(logger_file)
#
#
# def division(a,b):
#     if (b == 0):
#         logger.error("tried to divide by o")
#     return a/b
#
# division(10, 0)


"""Example_2"""
import random

logger = logging.getLogger("our logger")
logger.setLevel(logging.DEBUG)
logger_file = logging.FileHandler("test.log")
logger_file.setFormatter(logging.Formatter("%(levelname)s:%(asctime)s:%(message)s"))
logger.addHandler(logger_file)


class Client:
    def __init__(self, username):
        self.username = username
        self.balance = 0
        logger.info("client with username {} was created".format(username))


    def get_username(self):
        return self.username

    def get_balance(self):
        return self.balance

    def add_funds(self,amount):
        self.balance += amount
        logger.info("adding amount {} for client {}".format(amount, self.username ))

    def withdraw_funds(self,amount):
        if (amount > self.balance):
            logger.warning("can't withdraw: balance is {}, withdraw amount is {} for user {}".format(self.balance,amount,self.username))
        else:
            self.balance -= amount
            logger.info("withdraw successful for user {} amount is {}".format(self.username, amount))

    def transfer_to_another_account(self,amount, clientTo):
        exists = random.getrandbits(1)
        print(exists)
        if not exists:
            logger.error("Transfer failed: The user with username {} does not exists".format(clientTo.get_username()))
        else:
            if self.balance < amount:
                logger.error("Transaction failed: The balance {} is less than transaction amount {}".format(self.balance,amount))
            else:
                self.withdraw_funds(amount)
                clientTo.add_funds(amount)
                logger.info("Transaction successful: Transferred {} from user {} to {}".format(amount, self.get_username(),clientTo.get_username()))



client = Client("Mark")
client.add_funds(1000)
# client.withdraw_funds(1400)

other_client = Client("Tom")
client.transfer_to_another_account(2000, other_client)
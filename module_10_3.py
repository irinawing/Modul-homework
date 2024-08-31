import threading
import time
from random import randint

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for renew in range(100):
            renewal = randint(50,500)
            self.balance = self.balance + renewal
            print(f"Пополнение: {renewal}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for withdrawal in range(100):
            withdraw = randint(50,500)
            print(f"Запрос на {withdraw}")
            if self.balance >= withdraw:
                self.balance = self.balance - withdraw
                print(f"Снятие: {withdraw}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
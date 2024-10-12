from threading import Lock
import threading
import time
from random import randint


class Bank:

    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            in_ = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += in_
            print(f"Пополнение: {in_}. Баланс: {self.balance}\n")
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            out = randint(50, 500)
            print(f'Запрос на {out}\n')
            if out > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            else:
                self.balance -= out
                print(f'Снятие {out}: Баланс: {self.balance}\n')
                time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

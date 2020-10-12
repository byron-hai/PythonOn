import threading
import time

class Account:
    def __init__(self, acnt_id, balance=0):
        self.id = acnt_id
        self.balance=balance

def withdraw(account, draw_amount):
    if account.balance >= draw_amount:
        print(threading.current_thread().name\
            + "Success. " + str(draw_amount))
        time.sleep(0.01)
        account.balance -= draw_amount
        print("Balance: " + str(account.balance))
    else:
        print(threading.current_thread().name\
            + " Failed. Insufficient Balance")

def withdraw_with_lock(account, draw_amount, lock):
    with lock:
        if account.balance >= draw_amount:
            print(threading.current_thread().name\
                + " Success. " + str(draw_amount))
            time.sleep(0.01)
            account.balance -= draw_amount
            print("Balance: " + str(account.balance))
        else:
            print(threading.current_thread().name\
                + " Failed. Insufficient Balance")

acct = Account('1003', 1000)
threads = []
lock = threading.Lock()

for _ in range(3):
    threads.append(threading.Thread(target=withdraw , args=(acct , 600)))
    #threads.append(threading.Thread(target=withdraw_with_lock , args=(acct , 600, lock)))

for td in threads:
    td.start()
for td in threads:
    td.join()

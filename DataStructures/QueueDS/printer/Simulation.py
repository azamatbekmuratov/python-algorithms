from DataStructures.QueueDS.Queue import Queue

import random

from DataStructures.QueueDS.printer.Printer import Printer
from DataStructures.QueueDS.printer.Task import Task


def simulation(num_seconds, pages_per_minute):

    labprinter = Printer(pages_per_minute)
    printQueue = Queue
    waitingtimes = []

    for currentSecond in range(num_seconds):
        if new_print_task():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waittime(currentSecond))
            labprinter.start_next(nexttask)

        labprinter.tick()

    average_wait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(average_wait, printQueue.size()))


def new_print_task():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False


for i in range(10):
    simulation(3600, 5)
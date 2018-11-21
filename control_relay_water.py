import relay_water
from multiprocessing import Process, Queue
import time

# To check watering cycle


def Main(p_cycle):
    processes = []
    print("control relay process is started")
    cycle = 86400
    send_cycle = Queue()
    send_cycle.put(cycle)  # default cycle is 1 day
    process_watering = Process(target=relay_water.water_relay, args=(send_cycle, ))
    processes.append(process_watering)
    process_watering.start()
    print("process_watering is alive")

    while True:
        target_cycle = p_cycle.get()
        # print('target_cycle is ', target_cycle)
        if target_cycle is None:
            continue

        if cycle != target_cycle:
            process_watering.terminate()
            print("process_watering is dead")
            send_cycle.put(target_cycle)
            processes.append(process_watering)
            process_watering.start()
            print("process_watering is alive again!")
            cycle = target_cycle

        # time.sleep(10)


if __name__ == '__main__':
    Main()

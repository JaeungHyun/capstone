import relay_water
from multiprocessing import Process, Queue
import time
import json

# To check watering cycle


def Main(p_cycle, recv_cycle):
    print("control relay process is started")

    with open('config.json', 'r') as f:
        config_data = json.loads(f)

    cycle = config_data["target_cycle"]
    print("Loaded target cycle is ", cycle)
    send_cycle = Queue()
    send_cycle.put(cycle)  # default cycle is 1 day
    process_watering = Process(target=relay_water.water_relay, args=(send_cycle, ))
    process_watering.start()
    print("process_watering is alive")

    while True:
        target_cycle = p_cycle.get()

        if target_cycle is None:
            continue

        if cycle != target_cycle:
            process_watering.terminate()
            print("process_watering is dead")
            time.sleep(1)
            send_cycle.put(target_cycle)
            process_watering = Process(target=relay_water.water_relay, args=(send_cycle,))
            # 프로세스 종료 후 동일한 프로세스를 다시 시작하지 못한다. 따라서 프로세스를 다시 선언해야함
            process_watering.start()
            print("process_watering is alive again!")
            cycle = target_cycle

        recv_cycle.value = target_cycle


if __name__ == '__main__':
    Main()

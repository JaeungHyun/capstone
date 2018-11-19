import server
import relay_water
from multiprocessing import Process


def Main(p_cycle):
    print("control relay process is started")
    cycle = 86400  # initial cycle is 1 day
    process_watering = Process(target=relay_water.water_relay(cycle))
    process_watering.start()
    while True:
        if p_cycle.recv() is None:
            continue
        else:
            if cycle != server.p_cycle.recv():
                process_watering.terminate()
                cycle = server.p_cycle.recv()
                process_watering.start()


if __name__ == '__main__':
    Main()

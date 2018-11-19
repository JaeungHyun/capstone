import server
import relay_water
from multiprocessing import Process

# To check watering cycle


def Main(p_cycle):
    print("control relay process is started")
    cycle = 86400  # default cycle is 1 day
    process_watering = Process(target=relay_water.water_relay(cycle))
    process_watering.start()
    while True:
        if p_cycle.recv() is None:
            continue
        else:
            if cycle != server.p_cycle.recv():
                process_watering.terminate()
                relay_water.water_relay()
                cycle = server.p_cycle.recv()
                process_watering.start()


if __name__ == '__main__':
    Main()

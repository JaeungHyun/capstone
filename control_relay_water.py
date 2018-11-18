import server
import relay_water
from multiprocessing import Process


def main():
    cycle = 86400  # initial cycle is 1 hour
    process_watering = Process(target=relay_water.water_relay(cycle))
    process_watering.start()
    while True:
        if server.p_cycle.recv() is None:
            continue
        else:
            if cycle != server.p_cycle.recv():
                process_watering.terminate()
                cycle = server.p_cycle.recv()
                process_watering.start()


if __name__ == '__main__':
    main()

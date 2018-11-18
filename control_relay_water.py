import threading
import server
import relay_water


def main():
    while True:
        cycle = server.p_cycle.recv()
        if cycle is not None:
            save_cycle = cycle
        else:
            cycle = save_cycle

        relay_water.water_relay_first()
        threading.Timer(cycle, relay_water.water_relay()).start()


if __name__ == '__main__':
    main()

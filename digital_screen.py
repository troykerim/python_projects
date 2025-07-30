import random, sys, time, shutil

MIN_STREAM_LENGTH = 1 # 1 or 50
MAX_STREAM_LENGTH = 100 # 0 to 100

PAUSE = 0.2 #Delay, 0.0 or 2.0
STREAM_CHARS = ['0', '1']

DENSITY = 0.1 # 0.10 or 0.30

WIDTH = shutil.get_terminal_size()[0]

WIDTH -= 1 

print('Press Ctrl-C to quit!')
time.sleep(2)

try:
    columns = [0] * WIDTH
    while True:
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    columns[i] = random.randint(MIN_STREAM_LENGTH,MAX_STREAM_LENGTH)
            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print()
        sys.stdout.flush()
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()
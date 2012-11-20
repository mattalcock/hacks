import time
from multiprocessing import Pool

def run(arg):
    text, secs = arg
    while(True):
        print text
        time.sleep(secs)

if __name__ == "__main__":
    process_count = 3
    secs = 2

    p = Pool(process_count)

    args = []
    for i in xrange(process_count):
        text = "Thread%s:Hello" % i
        args.append((text,secs))
    
    p.map(run, args)

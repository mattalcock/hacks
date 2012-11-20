import threading, time

def run(text, secs):
    while(True):
        print text
        time.sleep(secs)

if __name__ == "__main__":
    thread_count = 3

    threads = []
    for i in range(thread_count):
        text = "Thread%s:Hello" % i
        secs = 2
        t = threading.Thread(target=run, args=(text, secs))
        threads.append(t)
    
    for t in threads:
        t.start()



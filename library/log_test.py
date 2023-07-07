import logging
import time

logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(message)s',filename="log.txt")

cnt=0
while cnt<5:
    logging.info("Surveiling...")
    time.sleep(3)
    cnt+=1

logging.error("Error found")
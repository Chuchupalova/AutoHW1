import csv
from datetime import datetime

KEY = "Key TSTFEED0300|7E3E|0400"
INPUT_FILE = "hblog.txt"
OUTPUT_FILE = "hb_test.log"

def analyze_heartbeat():
    timestamp = []
    with open(INPUT_FILE, "r") as file:
        for line in file:
            if KEY in line:

                ts_start = line.find("Timestamp ") + len("Timestamp ")
                ts_str = line[ts_start:ts_start+ 8] # HH:MM:SS
                ts = datetime.strptime(ts_str, "%H:%M:%S")
                timestamp.append(ts)

    with open(OUTPUT_FILE, "w") as log:
        for i in range(1, len(timestamp)):
            diff = int((timestamp[i] - timestamp[i - 1]).total_seconds())

            if 31 < diff < 33:
                log.write(
                    f"WARNING | {timestamps[i - 1].time()} -> {timestamps[i].time()} | diff={diff}s\n"
                    )
            elif diff >= 33:
                log.write(
                    f"ERROR   | {timestamps[i - 1].time()} -> {timestamps[i].time()} | diff={diff}s\n"
        )
if __name__ == "__main__":
    analyze_heartbeat()


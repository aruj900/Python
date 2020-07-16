def reorderLogFiles(logs):
    letterLogs = []
    digitLogs = []
    for log in logs:
        log_entry = log.split()
        if log_entry[1].isnumeric():
            digitLogs.append(log)
        else:
            letterLogs.append(log)
    letterLogs.sort(key=lambda x: x.split()[1:] + [x[0]] )
    return letterLogs+digitLogs


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(reorderLogFiles(logs))
from settings import LOGGING

def log(output):
    if LOGGING:
        print(output)
        return

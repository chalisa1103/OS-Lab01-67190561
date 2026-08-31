import os
import time

def create_zombie():
    pid = os.fork()
    
    if pid > 0:
        # Parent process: sleeps without calling wait()
        print(f"Parent process PID: {os.getpid()}, created child PID: {pid}")
        print("Parent is sleeping... Child should be a Zombie now!")
        time.sleep(30)  # Keeps parent alive so zombie persists
    else:
        # Child process: exits immediately
        print(f"Child process PID: {os.getpid()} exiting...")
        os._exit(0)

if __name__ == "__main__":
    create_zombie()
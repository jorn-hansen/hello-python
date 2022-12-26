import os
import sys
import time
import getpass
import hashlib

# See https://death.andgravity.com/pwned

path = sys.argv[1]
file = open(path, 'rb')

try:
    password = sys.argv[2]
except IndexError:
    password = getpass.getpass()
hexdigest = hashlib.sha1(password.encode()).hexdigest()
del password

print("looking for", hexdigest)

def find_line(lines, prefix):
    for line in lines:
        if line.startswith(prefix):
            return line
        if line > prefix:
            break
    return None

start = time.monotonic()
line = find_line(file, hexdigest.upper().encode())
end = time.monotonic()

if line:
    times = int(line.decode().rstrip().partition(':')[2])
    print(f"pwned! seen {times:,} times before")
else:
    print("not found")

print(f"in {end-start:.6f} seconds")

if __name__ == "__main__":
    pass
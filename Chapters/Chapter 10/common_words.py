alice = "resources/alice.txt"

with open(alice) as f:
    count = f.read().lower().count('alice')
    print(f"The word 'alice' appears {count} times.")
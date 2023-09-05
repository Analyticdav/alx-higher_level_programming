#!/usr/bin/python3
for p in range(9):
    for q in range(p + 1, 10):
        if p < 8:
            print(f"{p}{q}", end=", ")
        else:
            print(f"{p}{q}")

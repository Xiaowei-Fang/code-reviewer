#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def main():
    # Read the entire code from stdin
    code = sys.stdin.read()
    
    # Print the code to see what we received
    print("Received code:")
    print(repr(code))
    
    # Also print the length
    print(f"Code length: {len(code)}")

if __name__ == "__main__":
    main()
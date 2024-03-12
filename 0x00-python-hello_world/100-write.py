#!/usr/bin/python3
import sys
from datetime import datetime
dt = datetime(2015, 10, 19)
error_msg = f"and that piece of art is useful - Dora Korpar, {dt.strftime('%Y-%m-%d')}\n"
sys.stderr.write(error_msg)

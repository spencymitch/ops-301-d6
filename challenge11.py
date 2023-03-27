#!/usr/bin/env python3

# Script: Ops 301 Class 11 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 3/27/23
# Purpose:

import psutil

# Generate CPU times as a named tuple
print(psutil.cpu_times())

# Show current CPU consumption
print(psutil.cpu_percent())
# Time spent by normal processes executing in user mode
print(psutil.cpu_times().user)
# Time spent by processes executing in kernel mode
print(psutil.cpu_times().system)
# Time when system was idle
print(psutil.cpu_times().idle)
# Time spent by priority processes executing in user mode
print(psutil.cpu_times().nice)
# Time spent waiting for I/O to complete.
print(psutil.cpu_times().iowait)
# Time spent for servicing hardware interrupts.
print(psutil.cpu_times().irq)
# Time spent for servicing software interrupts.
print(psutil.cpu_times().softirq)
# Time spent by other operating systems running in a virtualized environment
print(psutil.cpu_times().steal)
# Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
print(psutil.cpu_times().guest)
# end

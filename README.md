# LatencyMaker
Program for applying latency to the current setup

Used in master project examining the effect of latency and other factors on VR user experience. The program was run on a Linux machine. It uses the 'tc' command to add a latency rule to the package queue. Since the Linux machine was an intermediary between the VR headset and the gaming PC, this effectively implementet latency both ways. The initial script (without Python) was written by Elias Hoel Birketvedt, and the Python GUI was written by Håkon Medhus Fornes to streamline the user studies.

The file 'latency_commands.txt' contiains the code for enabling latency in the system. The code should be copied to the computer's bashrc file and the file compiled/updated to enable the use of the command setlat(). This is used by the Python GUI program. The two relevant ports of the original PC were named 'enp1s0f0' and 'enp1s0f1'. These were bridged using bridge-tools in Linux. This allows us to hide the latency PC so the VR headset sees onlt the Windows PC at the other end of the latency setup.

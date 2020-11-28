# CAN_xls2C
2020/8/30 V2.0<br>
Fill in information of CAN signals in a standard xls file, which the python script can read.<br> 
![img](https://github.com/Flanker-E/repository_photo-gif/blob/main/can2xls_1.png)<br>
We have 3 sheets and up to 350 signals to convert. Theoretically, the number of sheets and signals can reach higher. <br>
![img](https://github.com/Flanker-E/repository_photo-gif/blob/main/Can_xls_number.jpg)<br>
Run the script, and the script will generate several files.<br>
![img](https://github.com/Flanker-E/repository_photo-gif/blob/main/can2xls_1.gif)<br>
THe generated files would appear in the original path. It will generate .c and .h files which run the dbc unpack and communication functions.<br>
This script will generate a wireless version and a SD card version, which satisfied the needs of users.<br>
![img](https://github.com/Flanker-E/repository_photo-gif/blob/main/can2xls_2.png)<br>
The generation code can reach 3000 lines, which is hard to maintain mannually. With this tool, changes of database can be easily handled.<br>
![img](https://github.com/Flanker-E/repository_photo-gif/blob/main/Can_xls_lines.jpg)<br>
brief screenshot of .c file. It also generates comments which make the code readable.<br>
![img](https://github.com/Flanker-E/repository_photo-gif/blob/main/can2xls_4.png)<br>

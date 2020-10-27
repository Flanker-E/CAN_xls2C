# encoding:utf-8
import os, sys, shutil
import win32ui
import pandas as pd
import numpy as np
import openpyxl
import win32api, win32con

######打开文件#####################################
dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
# dlg.SetOFNInitialDir(r"D:\\")  # 设置打开文件对话框中的初始显示目录
filename_and_extension = ("", "")
while filename_and_extension[1] != ".xlsx" and filename_and_extension[1] != ".xls":  # 判断获取文件格式
    open_file = 0
    while open_file != 1:  # 判断是否获取文件
        open_file = dlg.DoModal()  # 显示对话框，返回一个整数，这个整数指定对话框的操作
        path_file_name = dlg.GetPathName()  # 获取选择的文件路径文件名称文件后缀 其中分隔符为"\\"
        if open_file != 1:
            win32api.MessageBox(0, "Select a File", "提示", win32con.MB_OK)  # 如果未获取文件则弹窗
    filepath_and_filename = os.path.split(path_file_name)  # 将文件名（含扩展名）和文件路径分开,形成元组
    filename_and_extension = os.path.splitext(filepath_and_filename[1])  # 将文件名和扩展名分开，形成元组
    if filename_and_extension[1] != ".xlsx" and filename_and_extension[1] != ".xls":
        win32api.MessageBox(0, "Select a EXCEL File", "提示", win32con.MB_OK)  # 如果获取文件格式不正确则弹窗
filename = filename_and_extension[0]
filename_withpath = os.path.splitext(path_file_name)[0]  # 路径加文件名，不包含扩展名
print(filename_withpath)
######################写入txt开头固定的几行######################
CANhName = filename_withpath + "_CAN.h"
CANhtxtName = filename_withpath + "_CANh.txt"
f = open(CANhName, "w", encoding='utf-8', errors="replace")  # 只写
f.writelines("/*\tDRe20 dbc定义\t*/" + "\n")  # writelines不会每次输入自动换行，故补换行符号。注意区分print每次输出会自动换行
f.close()  # 本脚本，存储在临时list中的语句末尾无换行符，若list中一个元素包含多行，则换行符在语句字符串末尾
######################写入main.c(for SD_card)开头固定的几行######################
main_CANName_SD = filename_withpath + "_main_CAN_SD_card.c"
main_CANtxtName_SD = filename_withpath + "_main_CAN_SD_card.txt"
f = open(main_CANName_SD, "w", encoding='utf-8', errors="replace")  # 只写
f.writelines("/*\tContain 函数声明 静态变量声明 分拣函数及解包函数\t*/" + "\n")  # 方便打开文件后查找的备注
f.close()
######################写入main.c(without SD_card)开头固定的几行######################
main_CANName = filename_withpath + "_main_CAN.c"
main_CANtxtName = filename_withpath + "_main_CAN.txt"
f = open(main_CANName, "w", encoding='utf-8', errors="replace")  # 只写
f.writelines("/*\tContain 函数声明 静态变量声明 分拣函数及解包函数\t*/" + "\n")  # 方便打开文件后查找的备注
f.close()


##############定义函数：将excel的n行转换成n个list格式；并将所有列名保存到一个list里面#############
def print_data(key_of_dict, SD_card_version):  # 函数在使用前先定义
    dbc_data_part = dbc_excel_total[key_of_dict]  # 取出key_of_dict所对应的页表
    dbc_temp = np.array(dbc_data_part)  # 转换为numpy的数组
    dbc_list = dbc_temp.tolist()  # 数组转列表
    ###############获取表头，各个sheet都通用###############
    header = dbc_list[0]
    ###############获取各个列名对应的列号##################
    ECUS_index = dbc_list[0].index('ECUS')
    ECUR_index = dbc_list[0].index('ECUR')
    Message_index = dbc_list[0].index('Message')
    ID_index = dbc_list[0].index('MessageID')
    IDformat_index = dbc_list[0].index('ID-Format')
    DLC_index = dbc_list[0].index('MessageLength[Byte]')
    SendType_index = dbc_list[0].index('SendType')
    CycleTime_index = dbc_list[0].index('CycleTime[ms]')
    SignalName_index = dbc_list[0].index('SignalName')
    StartBit_index = dbc_list[0].index('StartBit')
    SignalLength_index = dbc_list[0].index('SignalLength[Bit]')
    ByteOrder_index = dbc_list[0].index('ByteOrder')
    ValueType_index = dbc_list[0].index('ValueType')
    InitialValue_index = dbc_list[0].index('InitialValue')
    Factor_index = dbc_list[0].index('Factor')
    Offset_index = dbc_list[0].index('Offset')
    Minimum_index = dbc_list[0].index('Minimum')
    Maximum_index = dbc_list[0].index('Maximum')
    Unit_index = dbc_list[0].index('Unit')
    ValueList_index = dbc_list[0].index('ValueList')
    ValueDescription_index = dbc_list[0].index('ValueDescription')
    Comment_index = dbc_list[0].index('Comment')
    ##########定义xlsx写入临时list#######
    excel_index.append("")
    excel_index.append("")
    excel_index.append("")
    excel_content.append(["", "", "", "", ""])  # CAN1，CAN2，CAN3之间buffer空三行
    excel_content.append([key_of_dict , "", "", "", ""])  # CAN1，CAN2，CAN3之间index空两行，并写入名称（即CANx
    excel_content.append(["", "", "", "", ""])  # Message_Name, Buffer_Index, Signal_Name, Data_Type, Byte_index
    ######################记录Message######################
    Msg_list = []
    Msg_index = []
    Msg_id = ''
    Msg_name = ''
    for i in range(1, len(dbc_list)):
        if str(dbc_list[i - 1][Message_index]) != str(dbc_list[i][Message_index]):
            Msg_id = str(dbc_list[i + 1][ID_index])  # 注意格式，i行是单独message，下一行才是含有signal，ID等其他21个内容的
            Msg_name = str(dbc_list[i][Message_index])
            Msg_list.append([Msg_name, Msg_id])
            Msg_index.append(i)
        else:
            continue
    ######################写入can.h,装载main.c的内容######################
    can_sorting.append("\t\t" + "//" + key_of_dict)
    if SD_card_version==0:
        f = open(CANhName, "a+", encoding='utf-8')  # 打开用于读写，文件已存在则追加
        f.writelines("\n/*\t" + key_of_dict + "\t*/" + "\n")
    # Message_index ID_index
    for i in range(0, len(Msg_list)):  # 对每个message进行操作
        if SD_card_version == 0:
            f.writelines("#define  " + Msg_list[i][0] + "\t" + Msg_list[i][1] + "\n")
        ######################装载函数声明######################
        define_unpack.append("uint8_t  " + Msg_list[i][0] + "_Unpack(uint8_t *buf);")
        ######################装载静态变量######################
        define_static.append("static uint16_t  " + Msg_list[i][0] + "_Counter = 0;")
        ######################装载分拣函数######################
        can_sorting.append(
            "\t\t" + "case  " + Msg_list[i][0] + ":\n\t\t\t" + "return  " + Msg_list[i][0] + "_Unpack(buf);")
        ######################装载All_Unpack的内容######################
        All_Unpack.append("/*******************************************************************/")
        All_Unpack.append("//" + Msg_list[i][0] + "\t" + Msg_list[i][1])
        #######初始化signal临时存储list和信号位置计数########存储结构：
        signal_u8 = []  # ;signalname_u8=[]
        signal_u16 = []  # ;signalname_u16=[]
        signal_u32 = []  # ;signalname_u32=[]
        signal_float = []  # Buff_byte_count,SignalName_index,StartBit,SignalLength,Factor,Offset
        Buff_byte_count = 0
        Index_in_u8 = 0
        Index_in_u16 = 0
        Index_in_u32 = 0
        Index_in = 0
        signal_Type = 0  # 0-float 8-u8 16-u16
        if i == (len(Msg_list) - 1):
            index_high = len(dbc_list)  # 防止最后一个message定位因为无末尾行而溢出
        else:
            index_high = Msg_index[i + 1]  # 到下一个message的开头
        for j in range(Msg_index[i] + 1, index_high):
            if 'eserve' in dbc_list[j][SignalName_index]:  # 过滤Reserved信号
                pass
            else:
                if float(dbc_list[j][Factor_index]) != 1:  # 有float则无u16和u8的定义
                    signal_Type = 'float'
                    signal_float.append(
                        [str(Buff_byte_count), dbc_list[j][SignalName_index], dbc_list[j][StartBit_index],
                         dbc_list[j][SignalLength_index], dbc_list[j][Factor_index],
                         dbc_list[j][Offset_index], dbc_list[j][ID_index], signal_Type])
                    # Buff_byte_count,SignalName_index,StartBit,SignalLength,Factor,Offset,ID_index, signal_Type
                    Buff_byte_count = Buff_byte_count + 4
                    # if (float(dbc_list[j][Maximum_index]) > 128):
                    #     Buff_byte_count = Buff_byte_count + 1
                    # else:
                    #     Buff_byte_count = Buff_byte_count + 2
                else:
                    if int(dbc_list[j][SignalLength_index]) <= 8:
                        signal_Type = 'u8'
                        signal_u8.append(
                            [str(Buff_byte_count), dbc_list[j][SignalName_index], dbc_list[j][StartBit_index],
                             dbc_list[j][SignalLength_index], dbc_list[j][ID_index], signal_Type])
                        # Buff_byte_count,SignalName_index,StartBit,SignalLength,ID_index
                        Index_in_u8 = Index_in_u8 + 1
                        Index_in = Index_in_u8
                        Buff_byte_count = Buff_byte_count + 1
                    elif (int(dbc_list[j][SignalLength_index]) > 8) and (int(dbc_list[j][SignalLength_index]) <= 16):
                        signal_Type = 'u16'
                        signal_u16.append(
                            [str(Buff_byte_count), dbc_list[j][SignalName_index], dbc_list[j][StartBit_index],
                             dbc_list[j][SignalLength_index], dbc_list[j][ID_index], signal_Type])
                        # Buff_byte_count,SignalName_index,StartBit,SignalLength,ID_index
                        Index_in_u16 = Index_in_u16 + 1
                        Index_in = Index_in_u16
                        Buff_byte_count = Buff_byte_count + 2
                    else:
                        signal_Type = 'u32'
                        signal_u32.append(
                            [str(Buff_byte_count), dbc_list[j][SignalName_index], dbc_list[j][StartBit_index],
                             dbc_list[j][SignalLength_index], dbc_list[j][ID_index], signal_Type])
                        # Buff_byte_count,SignalName_index,StartBit,SignalLength,ID_index
                        Index_in_u32 = Index_in_u32 + 1
                        Index_in = Index_in_u32
                        Buff_byte_count = Buff_byte_count + 4

            # if signal_Type==8:
            #     signalname_u8.append([dbc_list[j][SignalName_index],str(Index_in_u8)])
            # elif signal_Type==16:
            #     signalname_u16.append([dbc_list[j][SignalName_index],str(Index_in_u16)])
            # else:
            #     pass
        All_Unpack.append("uint8_t  " + Msg_list[i][0] + "_Unpack(uint8_t *buf)\n" + "{")  # unpack函数前几行的定义
        All_Unpack.append("\t#define  " + Msg_list[i][0] + "_DLC  " + str(
            len(signal_u8) + 2 * len(signal_u16) + 4 * len(signal_u32) + 4 * len(signal_float)) + "\n" + \
                          "\t#define  " + Msg_list[i][0] + "_Length  (" + Msg_list[i][0] + \
                          "_DLC+Package_Length)\n" + "\tuint8_t DTU_Buffer[" + Msg_list[i][0] + "_Length];\n" + \
                          "\tuint8_t i = 0;\n")
        #######声明名称数组########
        if signal_u8:  # 临时数组存在则执行
            All_Unpack.append("\tchar *SignalName8[] = {")
            for j in range(0, len(signal_u8) - 1):
                All_Unpack.append("\t\t\"" + signal_u8[j][1] + "\",")
            All_Unpack.append("\t\t\"" + signal_u8[len(signal_u8) - 1][1] + "\"};")
        if signal_u16:
            All_Unpack.append("\tchar *SignalName16[] = {")
            for j in range(0, len(signal_u16) - 1):
                All_Unpack.append("\t\t\"" + signal_u16[j][1] + "\",")
            All_Unpack.append("\t\t\"" + signal_u16[len(signal_u16) - 1][1] + "\"};\n")
        if signal_u32:
            All_Unpack.append("\tchar *SignalName32[] = {")
            for j in range(0, len(signal_u32) - 1):
                All_Unpack.append("\t\t\"" + signal_u32[j][1] + "\",")
            All_Unpack.append("\t\t\"" + signal_u32[len(signal_u32) - 1][1] + "\"};\n")
        if signal_float:
            All_Unpack.append("\tchar *SignalNamef[] = {")
            for j in range(0, len(signal_float) - 1):
                All_Unpack.append("\t\t\"" + signal_float[j][1] + "\",")
            All_Unpack.append("\t\t\"" + signal_float[len(signal_float) - 1][1] + "\"};\n")
        #######声明数据数组########
        if signal_u8:
            All_Unpack.append("\tuint8_t SignalValue8[" + str(len(signal_u8)) + "] = {0};\n" + "\t\t/*")
            for j in range(0, len(signal_u8) - 1):
                All_Unpack.append("\t\t\"" + signal_u8[j][1] + "\",")
            All_Unpack.append("\t\t\"" + signal_u8[len(signal_u8) - 1][1] + "\"\n" + "\t\t*/")
        if signal_u16:
            All_Unpack.append("\tuint16_t SignalValue16[" + str(len(signal_u16)) + "] = {0};\n" + "\t\t/*")
            for j in range(0, len(signal_u16) - 1):
                All_Unpack.append("\t\t\"" + signal_u16[j][1] + "\",")
            All_Unpack.append("\t\t\"" + signal_u16[len(signal_u16) - 1][1] + "\"\n" + "\t\t*/")
        if signal_u32:
            All_Unpack.append("\tuint32_t SignalValue32[" + str(len(signal_u32)) + "] = {0};\n" + "\t\t/*")
            for j in range(0, len(signal_u32) - 1):
                All_Unpack.append("\t\t\"" + signal_u32[j][1] + "\",")
            All_Unpack.append("\t\t\"" + signal_u32[len(signal_u32) - 1][1] + "\"\n" + "\t\t*/")
        if signal_float:
            All_Unpack.append(
                "\tfloat SignalValuef[" + str(len(signal_float)) + "];//Signals with float value\n" + "\t\t/*")
            for j in range(0, len(signal_float) - 1):
                All_Unpack.append("\t\t\"" + signal_float[j][1] + "\",")
            All_Unpack.append("\t\t\"" + signal_float[len(signal_float) - 1][1] + "\"\n" + "\t\t*/")
        #######帧计数########
        if SD_card_version:
            All_Unpack.append("\tTCHAR filebuffer[100];\n" + "\tRTC_TimeTypeDef RTC_Time;\n" + "\t" + \
                              Msg_list[i][0] + "_Counter++;//帧计数\n")
        #######信号分拣,并装入DTU_Buffer的临时list########
        All_Unpack.append("\t//Unpack CAN signals from buf")
        DTU_list = []
        DTU_count = 0  # 对对应的DTU_Buffer对应位进行计数。因为每个DTU_Buffer[i]只能存储8bits，所以u8占用一位（1byte），u16占用两位，float占用4位
        if signal_u8:
            for j in range(0, len(signal_u8)):
                Bias = (int(signal_u8[j][2]) % 8) > 0  # 判断是否需要移位
                if (int(signal_u8[j][2]) % 8 + int(signal_u8[j][3])) > 8:  # 判断signal是否横跨两个buf[i]，如是则进行合并
                    extend_bool = 1
                else:
                    extend_bool = 0
                All_Unpack.append("\tSignalValue8[" + str(j) + "] = " + Bias * "(" + \
                                  hex(int("0b" + int(signal_u8[j][3]) * "1" + (int(signal_u8[j][2]) % 8) * "0", 2)) + \
                                  "&" + extend_bool * "(" + "buf[" + str(
                    int(signal_u8[j][2]) // 8) + "]" + extend_bool * (
                                          "|(buf[" + str(1 + int(signal_u8[j][2]) // 8) + "]<<8))") + \
                                  Bias * (")>>" + str(int(signal_u8[j][2]) % 8)) + ";" + "//" + signal_u8[j][1])
                DTU_list.append(
                    ["\tDTU_Buffer[" + str(4 + int(signal_u8[j][0])) + "]", " = SignalValue8[" + str(j) + "];" + \
                     "//" + signal_u8[j][1], int(signal_u8[j][0]), signal_u8[j][1], signal_u8[j][4],
                     str(4 + int(signal_u8[j][0])), signal_u8[j][5], ""])
        if signal_u16:
            for j in range(0, len(signal_u16)):
                Bias = (int(signal_u16[j][2]) % 8) > 0
                if (int(signal_u16[j][2]) % 8 + int(signal_u16[j][3])) > 8:
                    extend_bool = 1
                else:
                    extend_bool = 0
                All_Unpack.append("\tSignalValue16[" + str(j) + "] = " + Bias * "(" + \
                                  hex(int("0b" + int(signal_u16[j][3]) * "1" + (int(signal_u16[j][2]) % 8) * "0", 2)) + \
                                  "&" + extend_bool * "(" + "buf[" + str(
                    int(signal_u16[j][2]) // 8) + "]" + extend_bool * (
                                          "|(buf[" + str(1 + int(signal_u16[j][2]) // 8) + "]<<8))") + \
                                  Bias * (")>>" + str(int(signal_u16[j][2]) % 8)) + ";" + "//" + signal_u16[j][1])
                # DTU_list.append(
                #     ["\tDTU_Buffer[" + str(4 + int(signal_u16[j][0])) + "]", " = SignalValue16[" + str(j) + "];" + \
                #      "//" + signal_u16[j][1], int(signal_u16[j][0]), signal_u16[j][1]])
                for k in range(0, 2):
                    DTU_list.append(["\tDTU_Buffer[" + str(4 + int(signal_u16[j][0]) + k) + "]",
                                     " = (SignalValue16[" + str(j) + "]&0x" + "ff" + k * "00" + ")" + (k != 0) * (
                                             ">>" + str(k * 8)) + ";" + \
                                     (k == 0) * ("//" + signal_u16[j][1]), int(signal_u16[j][0]),
                                     signal_u16[j][1], signal_u16[j][4], str(4 + int(signal_u16[j][0]) + k),
                                     signal_u16[j][5], str(k+1)])
        if signal_u32:
            for j in range(0, len(signal_u32)):
                Bias = (int(signal_u32[j][2]) % 8) > 0
                if (int(signal_u32[j][2]) % 8 + int(signal_u32[j][3])) > 8:
                    extend_bool = 1
                else:
                    extend_bool = 0
                All_Unpack.append("\tSignalValue32[" + str(j) + "] = " + Bias * "(" + \
                                  hex(int("0b" + int(signal_u32[j][3]) * "1" + (int(signal_u32[j][2]) % 8) * "0", 2)) + \
                                  "&" + extend_bool * "(" + "buf[" + str(
                    int(signal_u32[j][2]) // 8) + "]" + extend_bool * (
                                          "|(buf[" + str(1 + int(signal_u32[j][2]) // 8) + "]<<8))" + \
                                          "|(buf[" + str(2 + int(signal_u32[j][2]) // 8) + "]<<16))" + \
                                          "|(buf[" + str(3 + int(signal_u32[j][2]) // 8) + "]<<24))") + \
                                  Bias * (")>>" + str(int(signal_u32[j][2]) % 8)) + ";" + "//" + signal_u32[j][1])
                # DTU_list.append(
                #     ["\tDTU_Buffer[" + str(4 + int(signal_u32[j][0])) + "]", " = SignalValue32[" + str(j) + "];" + \
                #      "//" + signal_u32[j][1], int(signal_u32[j][0]), signal_u32[j][1]])
                for k in range(0, 4):
                    DTU_list.append(["\tDTU_Buffer[" + str(4 + int(signal_u32[j][0]) + k) + "]",
                                     " = (SignalValue32[" + str(j) + "]&0x" + "ff" + k * "00" + ")" + (k != 0) * (
                                             ">>" + str(k * 8)) + ";" + \
                                     (k == 0) * ("//" + signal_u32[j][1]), int(signal_u32[j][0]),
                                     signal_u32[j][1], signal_u32[j][4], str(4 + int(signal_u32[j][0]) + k),
                                     signal_u32[j][5], str(k+1)])
        #######计算float_value########
        if signal_float:
            for j in range(0, len(signal_float)):
                Bias = (int(signal_float[j][2]) % 8) > 0
                if (int(signal_float[j][2]) % 8 + int(signal_float[j][3])) > 8:
                    extend_bool = 1
                else:
                    extend_bool = 0
                All_Unpack.append("\tSignalValuef[" + str(j) + "] = (" + Bias * "(" + \
                                  hex(int("0b" + int(signal_float[j][3]) * "1" + (int(signal_float[j][2]) % 8) * "0",
                                          2)) + \
                                  "&" + extend_bool * "(" + "buf[" + str(
                    int(signal_float[j][2]) // 8) + "]" + extend_bool * (
                                          "|(buf[" + str(1 + int(signal_float[j][2]) // 8) + "]<<8))") + \
                                  Bias * (")>>" + str(int(signal_float[j][2]) % 8)) + ") * " + \
                                  signal_float[j][4] + (float(signal_float[j][5]) != 0) * (
                                          " + (" + signal_float[j][5] + ")") + ";")
                for k in range(0, 4):
                    DTU_list.append(["\tDTU_Buffer[" + str(4 + int(signal_float[j][0]) + k) + "+i]",
                                     " = ((uchar *)SignalValuef[" + str(j) + "])[" + str(k) + "];" + \
                                     (k == 0) * ("//" + signal_float[j][1]), int(signal_float[j][0]),
                                     signal_float[j][1], signal_float[j][6], str(4 + int(signal_float[j][0]) + k),
                                     signal_float[j][7], str(k+1)])
        #######装填DTU_Buffer########
        All_Unpack.append("\t//装填DTU_Buffer\n" + \
                          "\t//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）\n" + \
                          "\tDTU_Buffer[0] = 0x3A;\n" + "\tDTU_Buffer[1] = " + hex(int(Msg_list[i][1], 16) & 0xff) + \
                          ";\n" + "\tDTU_Buffer[2] = " + hex(int(Msg_list[i][1], 16) >> 8) + ";\n" + \
                          "\tDTU_Buffer[3] = " + Msg_list[i][0] + "_DLC;\n")
        DTU_list_sorted = sorted(DTU_list, key=lambda DTU_list: DTU_list[2])  # 将DTU_list临时数组进行排序，使之与原excel中顺序一致
        for j in range(0, len(DTU_list_sorted)):  # 将DTU_list临时数组压入unpack临时数组中
            All_Unpack.append(DTU_list_sorted[j][0] + DTU_list_sorted[j][1])
        All_Unpack.append("\tDTU_Buffer[" + Msg_list[i][0] + "_Length - 2] = 0x0D;\n" + \
                          "\tDTU_Buffer[" + Msg_list[i][0] + "_Length - 1] = 0x0A;\n")
        #######装填串口数据发送########
        All_Unpack.append("\t//发送串口数据\n" + "\tfor(i = 0; i < " + Msg_list[i][0] + "_Length; i++)\n" + \
                          "\t{\n" + "\t\twhile(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);\n" + \
                          "\t\tUSART_SendData(USART1, DTU_Buffer[i]);\n" + "\t}\n\n")
        if SD_card_version:
            All_Unpack.append("\t//获取当前时间\n" + \
                              "\tRTC_GetTime(RTC_Format_BIN, &RTC_Time);\n" + \
                              "\t//打开文件\n" + "\tf_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);\n" + \
                              "\tf_lseek(file, f_size(file));\n" + "\t//写入数据")
            if signal_u8:  # 将signal存储到sd卡中的函数，这里不需要考虑占用bit的个数
                All_Unpack.append("\tfor(i = 0; i < " + str(len(signal_u8)) + "; i++)\n" + "\t{\n" + \
                                  "\t\tsprintf(filebuffer, \"" + Msg_list[i][
                                      1] + ",%s,%02d,%02d:%02d:%02d,%02d\\r\\n\", SignalName8[i], SignalValue8[i]" + \
                                  ", RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, " + Msg_list[i][
                                      0] + "_Counter);\n" + \
                                  "\t\tf_puts(filebuffer, file);\n" + "\t}")
            if signal_u16:
                All_Unpack.append("\tfor(i = 0; i < " + str(len(signal_u16)) + "; i++)\n" + "\t{\n" + \
                                  "\t\tsprintf(filebuffer, \"" + Msg_list[i][
                                      1] + ",%s,%02d,%02d:%02d:%02d,%02d\\r\\n\", SignalName16[i], SignalValue16[i]" + \
                                  ", RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, " + Msg_list[i][
                                      0] + "_Counter);\n" + \
                                  "\t\tf_puts(filebuffer, file);\n" + "\t}")
            if signal_u32:
                All_Unpack.append("\tfor(i = 0; i < " + str(len(signal_u32)) + "; i++)\n" + "\t{\n" + \
                                  "\t\tsprintf(filebuffer, \"" + Msg_list[i][
                                      1] + ",%s,%02d,%02d:%02d:%02d,%02d\\r\\n\", SignalName32[i], SignalValue32[i]" + \
                                  ", RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, " + Msg_list[i][
                                      0] + "_Counter);\n" + \
                                  "\t\tf_puts(filebuffer, file);\n" + "\t}")
            if signal_float:
                All_Unpack.append("\tfor(i = 0; i < " + str(len(signal_float)) + "; i++)\n" + "\t{\n" + \
                                  "\t\tsprintf(filebuffer, \"" + Msg_list[i][
                                      1] + ",%s,%.2f,%02d:%02d:%02d,%02d\\r\\n\", SignalNamef[i], SignalValuef[i]" + \
                                  ", RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, " + Msg_list[i][
                                      0] + "_Counter);\n" + \
                                  "\t\tf_puts(filebuffer, file);\n" + "\t}")
        All_Unpack.append("\t//关闭文件\n" + "\treturn 0;\n" + "}\n")
        ######################补充excel的临时保存list######################
        excel_index.append(Msg_list[i][1])  # 在第一列加入message的ID
        for j in range(0, len(DTU_list_sorted)):
            excel_index.append("")
        excel_content.append([Msg_list[i][0], "", "", "", ""])  # 加入空行，分隔message
        # content: Message_Name, Buffer_Index, Signal_Name, Data_Type, Byte_index
        for j in range(0, len(DTU_list_sorted)):  # 将这个message的DTU_Buffer的顺序加入excel的临时list
            excel_content.append([Msg_list[i][0], DTU_list_sorted[j][5], DTU_list_sorted[j][3],
                                  DTU_list_sorted[j][6], DTU_list_sorted[j][7]])
    if SD_card_version == 0:
        f.close()  # 关闭之前的文件，少用一次循环


############根据有无sd卡运算两次############
for k in range(0, 2):  # k=0 without SD; k=1 with SD
    ############初始化临时存储list############
    define_unpack = []  # 函数声明
    define_static = []  # 静态变量声明
    can_sorting = []  # 分拣函数
    All_Unpack = []  # 所有的解包函数
    define_unpack.append("#define Package_Length 6\n\n//自定义函数声明\nuint8_t CAN_ID_Sorting(uint8_t *buf, uint32_t id);")
    # 方便打开文件后查找的备注
    define_static.append("TCHAR filename[50] = {0};")
    can_sorting.append("uint8_t CAN_ID_Sorting(uint8_t *buf, uint32_t id)\n{\n\tswitch(id)\n\t{")
    All_Unpack.append("//CAN 报文解析函数")

    ##############定义存取DTU_Buffer顺序的excel的空临时列表##############
    excel_index = []
    excel_content = []
    ##############读取键值并存取，方便提取##############
    dbc_excel_total = pd.read_excel(path_file_name, sheet_name=None,
                                    header=None)  # sheetname=None，返回所有页表 header=none,数据不含列名
    dbc_key = []
    for key in dbc_excel_total:  # 记录页表名
        dbc_key.append(key)
    sheet_len = len(dbc_key)
    for i in range(1, sheet_len + 1):  # 对每个页表名进行读取
        print_data(dbc_key[i - 1], k)
    ######################写入分拣函数######################
    if k:  # k=1 with SD
        f = open(main_CANName_SD, "a+", encoding='utf-8')  # 打开用于读写，文件已存在则追加
    else:
        f = open(main_CANName, "a+", encoding='utf-8')  # 打开用于读写，文件已存在则追加
    ######################写入分拣函数######################
    f.writelines("\n" + "//////Begin of Define_unpack//////" + "\n")
    for i in range(0, len(define_unpack)):
        f.writelines(define_unpack[i] + "\n")
    f.writelines("\n" + "//////End of Define_unpack//////" + "\n")
    ######################写入静态变量######################
    f.writelines("\n" + "//////Begin of Define_static//////" + "\n")
    for i in range(0, len(define_static)):
        f.writelines(define_static[i] + "\n")
    f.writelines("\n" + "//////End of Define_static//////" + "\n")
    ######################写入分拣函数######################
    f.writelines("\n" + "//////Begin of Can_Sorting//////" + "\n")
    for i in range(0, len(can_sorting)):
        f.writelines(can_sorting[i] + "\n")
    f.writelines("\t}" + "\n}" + "\n")
    f.writelines("\n" + "//////End of Can_Sorting//////" + "\n")
    ######################写入解析函数内容######################
    f.writelines("\n" + "//////Begin of Unpack_Function//////" + "\n")
    for i in range(0, len(All_Unpack)):
        f.writelines(All_Unpack[i] + "\n")
    f.writelines("\n" + "//////End of Unpack_Function//////" + "\n")
    f.close()  # 关闭之前的文件
######################定义xlsx写入函数逻辑，操作list######################
book_name_xlsx = filename_withpath + '_DTU_Buffer.xlsx'  # 定义表格名
sheet_name_xlsx = "DTU_Buffer"  # 定义页表名
# column_content: Message_Name, Buffer_Index, Signal_Name, Data_Type, Byte_index
Bufferdf = pd.DataFrame(excel_content, index=excel_index,
                        columns=["Message_Name", "Buffer_index", "Signal", "Data_Type", "Byte_index"])  # 定义column名
writer = pd.ExcelWriter(book_name_xlsx)  # 定义to_excel的工作引擎
Bufferdf.to_excel(excel_writer=writer, sheet_name=sheet_name_xlsx)  # 生成excel
writer.save()
writer.close()
#####################同时添加txt格式文件######################
shutil.copyfile(CANhName, CANhtxtName)  # 把前文件内容拷贝到后文件中
shutil.copyfile(main_CANName_SD, main_CANtxtName_SD)  # 把前文件内容拷贝到后文件中
shutil.copyfile(main_CANName, main_CANtxtName)  # 把前文件内容拷贝到后文件中
print("Done!")
win32api.MessageBox(0, "完成了奥利给", "提示", win32con.MB_OK)  # 完成弹窗奥利给

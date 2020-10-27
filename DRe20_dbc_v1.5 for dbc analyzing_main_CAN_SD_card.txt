/*	Contain 函数声明 静态变量声明 分拣函数及解包函数	*/

//////Begin of Define_unpack//////
#define Package_Length 6

//自定义函数声明
uint8_t CAN_ID_Sorting(uint8_t *buf, uint32_t id);
uint8_t  VCU_CAN1_CMD_Unpack(uint8_t *buf);
uint8_t  VCU_MC_Info_Unpack(uint8_t *buf);
uint8_t  VCU_CAN1_Info1_Unpack(uint8_t *buf);
uint8_t  VCU_CAN1_Info2_Unpack(uint8_t *buf);
uint8_t  HVBMS_Status_Unpack(uint8_t *buf);
uint8_t  HVBMS_Data_Unpack(uint8_t *buf);
uint8_t  HVBMS_Debug_Unpack(uint8_t *buf);
uint8_t  LVBMS_Data1_Unpack(uint8_t *buf);
uint8_t  LVBMS_Data2_Unpack(uint8_t *buf);
uint8_t  STN_Status_Unpack(uint8_t *buf);
uint8_t  GYRO_A_Unpack(uint8_t *buf);
uint8_t  OS_Unpack(uint8_t *buf);
uint8_t  SNF_KeySensor_Unpack(uint8_t *buf);
uint8_t  SNF_DataSensor_Unpack(uint8_t *buf);
uint8_t  WSN_IMUFL1_Unpack(uint8_t *buf);
uint8_t  WSN_IMUFL2_Unpack(uint8_t *buf);
uint8_t  WSN_IMUFR1_Unpack(uint8_t *buf);
uint8_t  WSN_IMUFR2_Unpack(uint8_t *buf);
uint8_t  WSN_IMURL1_Unpack(uint8_t *buf);
uint8_t  WSN_IMURL2_Unpack(uint8_t *buf);
uint8_t  WSN_IMURR1_Unpack(uint8_t *buf);
uint8_t  WSN_IMURR2_Unpack(uint8_t *buf);
uint8_t  WSN_TempFL_Unpack(uint8_t *buf);
uint8_t  WSN_TempFR_Unpack(uint8_t *buf);
uint8_t  WSN_TempRL_Unpack(uint8_t *buf);
uint8_t  WSN_TempRR_Unpack(uint8_t *buf);
uint8_t  MCFL_SetPoints_Unpack(uint8_t *buf);
uint8_t  MCFR_SetPoints_Unpack(uint8_t *buf);
uint8_t  MCFL_ActualValue1_Unpack(uint8_t *buf);
uint8_t  MCFL_ActualValue2_Unpack(uint8_t *buf);
uint8_t  MCFL_ActualValue3_Unpack(uint8_t *buf);
uint8_t  MCFR_ActualValue1_Unpack(uint8_t *buf);
uint8_t  MCFR_ActualValue2_Unpack(uint8_t *buf);
uint8_t  MCFR_ActualValue3_Unpack(uint8_t *buf);
uint8_t  MCRL_SetPoints_Unpack(uint8_t *buf);
uint8_t  MCRR_SetPoints_Unpack(uint8_t *buf);
uint8_t  MCRL_ActualValue1_Unpack(uint8_t *buf);
uint8_t  MCRL_ActualValue2_Unpack(uint8_t *buf);
uint8_t  MCRL_ActualValue3_Unpack(uint8_t *buf);
uint8_t  MCRR_ActualValue1_Unpack(uint8_t *buf);
uint8_t  MCRR_ActualValue2_Unpack(uint8_t *buf);
uint8_t  MCRR_ActualValue3_Unpack(uint8_t *buf);

//////End of Define_unpack//////

//////Begin of Define_static//////
TCHAR filename[50] = {0};
static uint16_t  VCU_CAN1_CMD_Counter = 0;
static uint16_t  VCU_MC_Info_Counter = 0;
static uint16_t  VCU_CAN1_Info1_Counter = 0;
static uint16_t  VCU_CAN1_Info2_Counter = 0;
static uint16_t  HVBMS_Status_Counter = 0;
static uint16_t  HVBMS_Data_Counter = 0;
static uint16_t  HVBMS_Debug_Counter = 0;
static uint16_t  LVBMS_Data1_Counter = 0;
static uint16_t  LVBMS_Data2_Counter = 0;
static uint16_t  STN_Status_Counter = 0;
static uint16_t  GYRO_A_Counter = 0;
static uint16_t  OS_Counter = 0;
static uint16_t  SNF_KeySensor_Counter = 0;
static uint16_t  SNF_DataSensor_Counter = 0;
static uint16_t  WSN_IMUFL1_Counter = 0;
static uint16_t  WSN_IMUFL2_Counter = 0;
static uint16_t  WSN_IMUFR1_Counter = 0;
static uint16_t  WSN_IMUFR2_Counter = 0;
static uint16_t  WSN_IMURL1_Counter = 0;
static uint16_t  WSN_IMURL2_Counter = 0;
static uint16_t  WSN_IMURR1_Counter = 0;
static uint16_t  WSN_IMURR2_Counter = 0;
static uint16_t  WSN_TempFL_Counter = 0;
static uint16_t  WSN_TempFR_Counter = 0;
static uint16_t  WSN_TempRL_Counter = 0;
static uint16_t  WSN_TempRR_Counter = 0;
static uint16_t  MCFL_SetPoints_Counter = 0;
static uint16_t  MCFR_SetPoints_Counter = 0;
static uint16_t  MCFL_ActualValue1_Counter = 0;
static uint16_t  MCFL_ActualValue2_Counter = 0;
static uint16_t  MCFL_ActualValue3_Counter = 0;
static uint16_t  MCFR_ActualValue1_Counter = 0;
static uint16_t  MCFR_ActualValue2_Counter = 0;
static uint16_t  MCFR_ActualValue3_Counter = 0;
static uint16_t  MCRL_SetPoints_Counter = 0;
static uint16_t  MCRR_SetPoints_Counter = 0;
static uint16_t  MCRL_ActualValue1_Counter = 0;
static uint16_t  MCRL_ActualValue2_Counter = 0;
static uint16_t  MCRL_ActualValue3_Counter = 0;
static uint16_t  MCRR_ActualValue1_Counter = 0;
static uint16_t  MCRR_ActualValue2_Counter = 0;
static uint16_t  MCRR_ActualValue3_Counter = 0;

//////End of Define_static//////

//////Begin of Can_Sorting//////
uint8_t CAN_ID_Sorting(uint8_t *buf, uint32_t id)
{
	switch(id)
	{
		//CAN1
		case  VCU_CAN1_CMD:
			return  VCU_CAN1_CMD_Unpack(buf);
		case  VCU_MC_Info:
			return  VCU_MC_Info_Unpack(buf);
		case  VCU_CAN1_Info1:
			return  VCU_CAN1_Info1_Unpack(buf);
		case  VCU_CAN1_Info2:
			return  VCU_CAN1_Info2_Unpack(buf);
		case  HVBMS_Status:
			return  HVBMS_Status_Unpack(buf);
		case  HVBMS_Data:
			return  HVBMS_Data_Unpack(buf);
		case  HVBMS_Debug:
			return  HVBMS_Debug_Unpack(buf);
		case  LVBMS_Data1:
			return  LVBMS_Data1_Unpack(buf);
		case  LVBMS_Data2:
			return  LVBMS_Data2_Unpack(buf);
		case  STN_Status:
			return  STN_Status_Unpack(buf);
		case  GYRO_A:
			return  GYRO_A_Unpack(buf);
		case  OS:
			return  OS_Unpack(buf);
		case  SNF_KeySensor:
			return  SNF_KeySensor_Unpack(buf);
		case  SNF_DataSensor:
			return  SNF_DataSensor_Unpack(buf);
		case  WSN_IMUFL1:
			return  WSN_IMUFL1_Unpack(buf);
		case  WSN_IMUFL2:
			return  WSN_IMUFL2_Unpack(buf);
		case  WSN_IMUFR1:
			return  WSN_IMUFR1_Unpack(buf);
		case  WSN_IMUFR2:
			return  WSN_IMUFR2_Unpack(buf);
		case  WSN_IMURL1:
			return  WSN_IMURL1_Unpack(buf);
		case  WSN_IMURL2:
			return  WSN_IMURL2_Unpack(buf);
		case  WSN_IMURR1:
			return  WSN_IMURR1_Unpack(buf);
		case  WSN_IMURR2:
			return  WSN_IMURR2_Unpack(buf);
		case  WSN_TempFL:
			return  WSN_TempFL_Unpack(buf);
		case  WSN_TempFR:
			return  WSN_TempFR_Unpack(buf);
		case  WSN_TempRL:
			return  WSN_TempRL_Unpack(buf);
		case  WSN_TempRR:
			return  WSN_TempRR_Unpack(buf);
		//CAN2
		case  MCFL_SetPoints:
			return  MCFL_SetPoints_Unpack(buf);
		case  MCFR_SetPoints:
			return  MCFR_SetPoints_Unpack(buf);
		case  MCFL_ActualValue1:
			return  MCFL_ActualValue1_Unpack(buf);
		case  MCFL_ActualValue2:
			return  MCFL_ActualValue2_Unpack(buf);
		case  MCFL_ActualValue3:
			return  MCFL_ActualValue3_Unpack(buf);
		case  MCFR_ActualValue1:
			return  MCFR_ActualValue1_Unpack(buf);
		case  MCFR_ActualValue2:
			return  MCFR_ActualValue2_Unpack(buf);
		case  MCFR_ActualValue3:
			return  MCFR_ActualValue3_Unpack(buf);
		//CAN3
		case  MCRL_SetPoints:
			return  MCRL_SetPoints_Unpack(buf);
		case  MCRR_SetPoints:
			return  MCRR_SetPoints_Unpack(buf);
		case  MCRL_ActualValue1:
			return  MCRL_ActualValue1_Unpack(buf);
		case  MCRL_ActualValue2:
			return  MCRL_ActualValue2_Unpack(buf);
		case  MCRL_ActualValue3:
			return  MCRL_ActualValue3_Unpack(buf);
		case  MCRR_ActualValue1:
			return  MCRR_ActualValue1_Unpack(buf);
		case  MCRR_ActualValue2:
			return  MCRR_ActualValue2_Unpack(buf);
		case  MCRR_ActualValue3:
			return  MCRR_ActualValue3_Unpack(buf);
	}
}

//////End of Can_Sorting//////

//////Begin of Unpack_Function//////
//CAN 报文解析函数
/*******************************************************************/
//VCU_CAN1_CMD	0x300
uint8_t  VCU_CAN1_CMD_Unpack(uint8_t *buf)
{
	#define  VCU_CAN1_CMD_DLC  15
	#define  VCU_CAN1_CMD_Length  (VCU_CAN1_CMD_DLC+Package_Length)
	uint8_t DTU_Buffer[VCU_CAN1_CMD_Length];
	uint8_t i = 0;

	char *SignalName8[] = {
		"SNF_cSHTD",
		"VCU_cBatFAN",
		"VCU_cMCFAN1",
		"VCU_cMCFAN2",
		"VCU_cMCFAN3",
		"VCU_cPUMP1",
		"VCU_cPUMP2",
		"VCU_cPUMP3",
		"Bat_cAIRP",
		"Bat_cAIRN",
		"Bat_cAIRPRE",
		"STN_cLED_Ready",
		"STN_cLED_IMD",
		"STN_cLED_AMS",
		"VCU_EFStep"};
	uint8_t SignalValue8[15] = {0};
		/*
		"SNF_cSHTD",
		"VCU_cBatFAN",
		"VCU_cMCFAN1",
		"VCU_cMCFAN2",
		"VCU_cMCFAN3",
		"VCU_cPUMP1",
		"VCU_cPUMP2",
		"VCU_cPUMP3",
		"Bat_cAIRP",
		"Bat_cAIRN",
		"Bat_cAIRPRE",
		"STN_cLED_Ready",
		"STN_cLED_IMD",
		"STN_cLED_AMS",
		"VCU_EFStep"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	VCU_CAN1_CMD_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue8[0] = 0x3&buf[0];//SNF_cSHTD
	SignalValue8[1] = 0x1&buf[1];//VCU_cBatFAN
	SignalValue8[2] = (0x2&buf[1])>>1;//VCU_cMCFAN1
	SignalValue8[3] = (0x4&buf[1])>>2;//VCU_cMCFAN2
	SignalValue8[4] = (0x8&buf[1])>>3;//VCU_cMCFAN3
	SignalValue8[5] = (0x10&buf[1])>>4;//VCU_cPUMP1
	SignalValue8[6] = (0x20&buf[1])>>5;//VCU_cPUMP2
	SignalValue8[7] = (0x40&buf[1])>>6;//VCU_cPUMP3
	SignalValue8[8] = 0x3&buf[2];//Bat_cAIRP
	SignalValue8[9] = (0xc&buf[2])>>2;//Bat_cAIRN
	SignalValue8[10] = (0x30&buf[2])>>4;//Bat_cAIRPRE
	SignalValue8[11] = (0xc0&buf[2])>>6;//STN_cLED_Ready
	SignalValue8[12] = 0x3&buf[3];//STN_cLED_IMD
	SignalValue8[13] = (0xc&buf[3])>>2;//STN_cLED_AMS
	SignalValue8[14] = (0xf0&buf[3])>>4;//VCU_EFStep
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x0;
	DTU_Buffer[2] = 0x3;
	DTU_Buffer[3] = VCU_CAN1_CMD_DLC;

	DTU_Buffer[4] = SignalValue8[0];//SNF_cSHTD
	DTU_Buffer[5] = SignalValue8[1];//VCU_cBatFAN
	DTU_Buffer[6] = SignalValue8[2];//VCU_cMCFAN1
	DTU_Buffer[7] = SignalValue8[3];//VCU_cMCFAN2
	DTU_Buffer[8] = SignalValue8[4];//VCU_cMCFAN3
	DTU_Buffer[9] = SignalValue8[5];//VCU_cPUMP1
	DTU_Buffer[10] = SignalValue8[6];//VCU_cPUMP2
	DTU_Buffer[11] = SignalValue8[7];//VCU_cPUMP3
	DTU_Buffer[12] = SignalValue8[8];//Bat_cAIRP
	DTU_Buffer[13] = SignalValue8[9];//Bat_cAIRN
	DTU_Buffer[14] = SignalValue8[10];//Bat_cAIRPRE
	DTU_Buffer[15] = SignalValue8[11];//STN_cLED_Ready
	DTU_Buffer[16] = SignalValue8[12];//STN_cLED_IMD
	DTU_Buffer[17] = SignalValue8[13];//STN_cLED_AMS
	DTU_Buffer[18] = SignalValue8[14];//VCU_EFStep
	DTU_Buffer[VCU_CAN1_CMD_Length - 2] = 0x0D;
	DTU_Buffer[VCU_CAN1_CMD_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < VCU_CAN1_CMD_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 15; i++)
	{
		sprintf(filebuffer, "0x300,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName8[i], SignalValue8[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, VCU_CAN1_CMD_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//VCU_MC_Info	0x501
uint8_t  VCU_MC_Info_Unpack(uint8_t *buf)
{
	#define  VCU_MC_Info_DLC  12
	#define  VCU_MC_Info_Length  (VCU_MC_Info_DLC+Package_Length)
	uint8_t DTU_Buffer[VCU_MC_Info_Length];
	uint8_t i = 0;

	char *SignalName8[] = {
		"VCU_MCFL_ErrorInfo",
		"VCU_MCFR_ErrorInfo",
		"VCU_MCRL_ErrorInfo",
		"VCU_MCRR_ErrorInfo"};
	char *SignalName16[] = {
		"VCU_MCFL_DiagnosticNum",
		"VCU_MCFR_DiagnosticNum",
		"VCU_MCRL_DiagnosticNum",
		"VCU_MCRR_DiagnosticNum"};

	uint8_t SignalValue8[4] = {0};
		/*
		"VCU_MCFL_ErrorInfo",
		"VCU_MCFR_ErrorInfo",
		"VCU_MCRL_ErrorInfo",
		"VCU_MCRR_ErrorInfo"
		*/
	uint16_t SignalValue16[4] = {0};
		/*
		"VCU_MCFL_DiagnosticNum",
		"VCU_MCFR_DiagnosticNum",
		"VCU_MCRL_DiagnosticNum",
		"VCU_MCRR_DiagnosticNum"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	VCU_MC_Info_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue8[0] = (0xf0&buf[1])>>4;//VCU_MCFL_ErrorInfo
	SignalValue8[1] = (0xf0&buf[3])>>4;//VCU_MCFR_ErrorInfo
	SignalValue8[2] = (0xf0&buf[5])>>4;//VCU_MCRL_ErrorInfo
	SignalValue8[3] = (0xf0&buf[7])>>4;//VCU_MCRR_ErrorInfo
	SignalValue16[0] = 0xfff&(buf[0]|(buf[1]<<8));//VCU_MCFL_DiagnosticNum
	SignalValue16[1] = 0xfff&(buf[2]|(buf[3]<<8));//VCU_MCFR_DiagnosticNum
	SignalValue16[2] = 0xfff&(buf[4]|(buf[5]<<8));//VCU_MCRL_DiagnosticNum
	SignalValue16[3] = 0xfff&(buf[6]|(buf[7]<<8));//VCU_MCRR_DiagnosticNum
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x1;
	DTU_Buffer[2] = 0x5;
	DTU_Buffer[3] = VCU_MC_Info_DLC;

	DTU_Buffer[4] = (SignalValue16[0]&0xff);//VCU_MCFL_DiagnosticNum
	DTU_Buffer[5] = (SignalValue16[0]&0xff00)>>8;
	DTU_Buffer[6] = SignalValue8[0];//VCU_MCFL_ErrorInfo
	DTU_Buffer[7] = (SignalValue16[1]&0xff);//VCU_MCFR_DiagnosticNum
	DTU_Buffer[8] = (SignalValue16[1]&0xff00)>>8;
	DTU_Buffer[9] = SignalValue8[1];//VCU_MCFR_ErrorInfo
	DTU_Buffer[10] = (SignalValue16[2]&0xff);//VCU_MCRL_DiagnosticNum
	DTU_Buffer[11] = (SignalValue16[2]&0xff00)>>8;
	DTU_Buffer[12] = SignalValue8[2];//VCU_MCRL_ErrorInfo
	DTU_Buffer[13] = (SignalValue16[3]&0xff);//VCU_MCRR_DiagnosticNum
	DTU_Buffer[14] = (SignalValue16[3]&0xff00)>>8;
	DTU_Buffer[15] = SignalValue8[3];//VCU_MCRR_ErrorInfo
	DTU_Buffer[VCU_MC_Info_Length - 2] = 0x0D;
	DTU_Buffer[VCU_MC_Info_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < VCU_MC_Info_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 4; i++)
	{
		sprintf(filebuffer, "0x501,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName8[i], SignalValue8[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, VCU_MC_Info_Counter);
		f_puts(filebuffer, file);
	}
	for(i = 0; i < 4; i++)
	{
		sprintf(filebuffer, "0x501,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName16[i], SignalValue16[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, VCU_MC_Info_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//VCU_CAN1_Info1	0x322
uint8_t  VCU_CAN1_Info1_Unpack(uint8_t *buf)
{
	#define  VCU_CAN1_Info1_DLC  24
	#define  VCU_CAN1_Info1_Length  (VCU_CAN1_Info1_DLC+Package_Length)
	uint8_t DTU_Buffer[VCU_CAN1_Info1_Length];
	uint8_t i = 0;

	char *SignalNamef[] = {
		"VCU_APPS",
		"VCU_BSE",
		"VCU_SoC",
		"VCU_OverallPower",
		"VCU_Current",
		"VCU_HBPSR"};

	float SignalValuef[6];//Signals with float value
		/*
		"VCU_APPS",
		"VCU_BSE",
		"VCU_SoC",
		"VCU_OverallPower",
		"VCU_Current",
		"VCU_HBPSR"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	VCU_CAN1_Info1_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValuef[0] = (0xff&buf[0]) * 0.01;
	SignalValuef[1] = (0xff&buf[1]) * 0.01;
	SignalValuef[2] = (0x3ff&(buf[2]|(buf[3]<<8))) * 0.1;
	SignalValuef[3] = ((0xfffc&(buf[3]|(buf[4]<<8)))>>2) * 0.01 + (-40);
	SignalValuef[4] = (0xfff&(buf[5]|(buf[6]<<8))) * 0.1221 + (-250);
	SignalValuef[5] = ((0xfff0&(buf[6]|(buf[7]<<8)))>>4) * 0.002014 + (-0.74994);
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x22;
	DTU_Buffer[2] = 0x3;
	DTU_Buffer[3] = VCU_CAN1_Info1_DLC;

	DTU_Buffer[4+i] = ((uchar *)SignalValuef[0])[0];//VCU_APPS
	DTU_Buffer[5+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[6+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[7+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[1])[0];//VCU_BSE
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[2])[0];//VCU_SoC
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[3])[0];//VCU_OverallPower
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[3])[1];
	DTU_Buffer[18+i] = ((uchar *)SignalValuef[3])[2];
	DTU_Buffer[19+i] = ((uchar *)SignalValuef[3])[3];
	DTU_Buffer[20+i] = ((uchar *)SignalValuef[4])[0];//VCU_Current
	DTU_Buffer[21+i] = ((uchar *)SignalValuef[4])[1];
	DTU_Buffer[22+i] = ((uchar *)SignalValuef[4])[2];
	DTU_Buffer[23+i] = ((uchar *)SignalValuef[4])[3];
	DTU_Buffer[24+i] = ((uchar *)SignalValuef[5])[0];//VCU_HBPSR
	DTU_Buffer[25+i] = ((uchar *)SignalValuef[5])[1];
	DTU_Buffer[26+i] = ((uchar *)SignalValuef[5])[2];
	DTU_Buffer[27+i] = ((uchar *)SignalValuef[5])[3];
	DTU_Buffer[VCU_CAN1_Info1_Length - 2] = 0x0D;
	DTU_Buffer[VCU_CAN1_Info1_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < VCU_CAN1_Info1_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 6; i++)
	{
		sprintf(filebuffer, "0x322,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, VCU_CAN1_Info1_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//VCU_CAN1_Info2	0x500
uint8_t  VCU_CAN1_Info2_Unpack(uint8_t *buf)
{
	#define  VCU_CAN1_Info2_DLC  23
	#define  VCU_CAN1_Info2_Length  (VCU_CAN1_Info2_DLC+Package_Length)
	uint8_t DTU_Buffer[VCU_CAN1_Info2_Length];
	uint8_t i = 0;

	char *SignalName8[] = {
		"HVBMS_CANError",
		"LVBMS_CANError",
		"SNF_CANError",
		"MC_CANError",
		"STN_CANError",
		"VCU_cDischarge",
		"VCU_cMC"};
	char *SignalNamef[] = {
		"VCU_SlipRatio_FL",
		"VCU_SlipRatio_FR",
		"VCU_SlipRatio_RL",
		"VCU_SlipRatio_RR"};

	uint8_t SignalValue8[7] = {0};
		/*
		"HVBMS_CANError",
		"LVBMS_CANError",
		"SNF_CANError",
		"MC_CANError",
		"STN_CANError",
		"VCU_cDischarge",
		"VCU_cMC"
		*/
	float SignalValuef[4];//Signals with float value
		/*
		"VCU_SlipRatio_FL",
		"VCU_SlipRatio_FR",
		"VCU_SlipRatio_RL",
		"VCU_SlipRatio_RR"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	VCU_CAN1_Info2_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue8[0] = 0x3&buf[6];//HVBMS_CANError
	SignalValue8[1] = (0xc&buf[6])>>2;//LVBMS_CANError
	SignalValue8[2] = (0x30&buf[6])>>4;//SNF_CANError
	SignalValue8[3] = (0xc0&buf[6])>>6;//MC_CANError
	SignalValue8[4] = 0x3&buf[7];//STN_CANError
	SignalValue8[5] = (0xc&buf[7])>>2;//VCU_cDischarge
	SignalValue8[6] = (0x30&buf[7])>>4;//VCU_cMC
	SignalValuef[0] = (0xfff&(buf[0]|(buf[1]<<8))) * 0.0005;
	SignalValuef[1] = ((0xfff0&(buf[1]|(buf[2]<<8)))>>4) * 0.0005;
	SignalValuef[2] = (0xfff&(buf[3]|(buf[4]<<8))) * 0.0005;
	SignalValuef[3] = ((0xfff0&(buf[4]|(buf[5]<<8)))>>4) * 0.0005;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x0;
	DTU_Buffer[2] = 0x5;
	DTU_Buffer[3] = VCU_CAN1_Info2_DLC;

	DTU_Buffer[4+i] = ((uchar *)SignalValuef[0])[0];//VCU_SlipRatio_FL
	DTU_Buffer[5+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[6+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[7+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[1])[0];//VCU_SlipRatio_FR
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[2])[0];//VCU_SlipRatio_RL
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[3])[0];//VCU_SlipRatio_RR
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[3])[1];
	DTU_Buffer[18+i] = ((uchar *)SignalValuef[3])[2];
	DTU_Buffer[19+i] = ((uchar *)SignalValuef[3])[3];
	DTU_Buffer[20] = SignalValue8[0];//HVBMS_CANError
	DTU_Buffer[21] = SignalValue8[1];//LVBMS_CANError
	DTU_Buffer[22] = SignalValue8[2];//SNF_CANError
	DTU_Buffer[23] = SignalValue8[3];//MC_CANError
	DTU_Buffer[24] = SignalValue8[4];//STN_CANError
	DTU_Buffer[25] = SignalValue8[5];//VCU_cDischarge
	DTU_Buffer[26] = SignalValue8[6];//VCU_cMC
	DTU_Buffer[VCU_CAN1_Info2_Length - 2] = 0x0D;
	DTU_Buffer[VCU_CAN1_Info2_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < VCU_CAN1_Info2_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 7; i++)
	{
		sprintf(filebuffer, "0x500,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName8[i], SignalValue8[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, VCU_CAN1_Info2_Counter);
		f_puts(filebuffer, file);
	}
	for(i = 0; i < 4; i++)
	{
		sprintf(filebuffer, "0x500,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, VCU_CAN1_Info2_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//HVBMS_Status	0x310
uint8_t  HVBMS_Status_Unpack(uint8_t *buf)
{
	#define  HVBMS_Status_DLC  19
	#define  HVBMS_Status_Length  (HVBMS_Status_DLC+Package_Length)
	uint8_t DTU_Buffer[HVBMS_Status_Length];
	uint8_t i = 0;

	char *SignalName8[] = {
		"HVBMS_DiagnosticNum",
		"HVBMS_bAIRP",
		"HVBMS_bAIRN",
		"HVBMS_bAIRPRE",
		"HVBMS_bDischarge",
		"HVBMS_bSHTD_Sta",
		"HVBMS_bSHTD_AMS",
		"HVBMS_bSHTD_IMD",
		"HVBMS_bSHTD_fIMDRelay",
		"HVBMS_bAMS_Sta",
		"HVBMS_bIMD_Sta"};
	char *SignalNamef[] = {
		"HVBMS_BatVolt",
		"HVBMS_BatCurrent"};

	uint8_t SignalValue8[11] = {0};
		/*
		"HVBMS_DiagnosticNum",
		"HVBMS_bAIRP",
		"HVBMS_bAIRN",
		"HVBMS_bAIRPRE",
		"HVBMS_bDischarge",
		"HVBMS_bSHTD_Sta",
		"HVBMS_bSHTD_AMS",
		"HVBMS_bSHTD_IMD",
		"HVBMS_bSHTD_fIMDRelay",
		"HVBMS_bAMS_Sta",
		"HVBMS_bIMD_Sta"
		*/
	float SignalValuef[2];//Signals with float value
		/*
		"HVBMS_BatVolt",
		"HVBMS_BatCurrent"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	HVBMS_Status_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue8[0] = 0xff&buf[0];//HVBMS_DiagnosticNum
	SignalValue8[1] = 0x1&buf[1];//HVBMS_bAIRP
	SignalValue8[2] = (0x2&buf[1])>>1;//HVBMS_bAIRN
	SignalValue8[3] = (0x4&buf[1])>>2;//HVBMS_bAIRPRE
	SignalValue8[4] = (0x8&buf[1])>>3;//HVBMS_bDischarge
	SignalValue8[5] = (0x10&buf[1])>>4;//HVBMS_bSHTD_Sta
	SignalValue8[6] = (0x20&buf[1])>>5;//HVBMS_bSHTD_AMS
	SignalValue8[7] = (0x40&buf[1])>>6;//HVBMS_bSHTD_IMD
	SignalValue8[8] = (0x80&buf[1])>>7;//HVBMS_bSHTD_fIMDRelay
	SignalValue8[9] = 0x1&buf[2];//HVBMS_bAMS_Sta
	SignalValue8[10] = (0x2&buf[2])>>1;//HVBMS_bIMD_Sta
	SignalValuef[0] = ((0xfff0&(buf[2]|(buf[3]<<8)))>>4) * 0.13594 + (25);
	SignalValuef[1] = (0xffff&(buf[4]|(buf[5]<<8))) * 0.1343 + (-250);
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x10;
	DTU_Buffer[2] = 0x3;
	DTU_Buffer[3] = HVBMS_Status_DLC;

	DTU_Buffer[4] = SignalValue8[0];//HVBMS_DiagnosticNum
	DTU_Buffer[5] = SignalValue8[1];//HVBMS_bAIRP
	DTU_Buffer[6] = SignalValue8[2];//HVBMS_bAIRN
	DTU_Buffer[7] = SignalValue8[3];//HVBMS_bAIRPRE
	DTU_Buffer[8] = SignalValue8[4];//HVBMS_bDischarge
	DTU_Buffer[9] = SignalValue8[5];//HVBMS_bSHTD_Sta
	DTU_Buffer[10] = SignalValue8[6];//HVBMS_bSHTD_AMS
	DTU_Buffer[11] = SignalValue8[7];//HVBMS_bSHTD_IMD
	DTU_Buffer[12] = SignalValue8[8];//HVBMS_bSHTD_fIMDRelay
	DTU_Buffer[13] = SignalValue8[9];//HVBMS_bAMS_Sta
	DTU_Buffer[14] = SignalValue8[10];//HVBMS_bIMD_Sta
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[0])[0];//HVBMS_BatVolt
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[18+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[19+i] = ((uchar *)SignalValuef[1])[0];//HVBMS_BatCurrent
	DTU_Buffer[20+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[21+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[22+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[HVBMS_Status_Length - 2] = 0x0D;
	DTU_Buffer[HVBMS_Status_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < HVBMS_Status_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 11; i++)
	{
		sprintf(filebuffer, "0x310,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName8[i], SignalValue8[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, HVBMS_Status_Counter);
		f_puts(filebuffer, file);
	}
	for(i = 0; i < 2; i++)
	{
		sprintf(filebuffer, "0x310,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, HVBMS_Status_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//HVBMS_Data	0x311
uint8_t  HVBMS_Data_Unpack(uint8_t *buf)
{
	#define  HVBMS_Data_DLC  12
	#define  HVBMS_Data_Length  (HVBMS_Data_DLC+Package_Length)
	uint8_t DTU_Buffer[HVBMS_Data_Length];
	uint8_t i = 0;

	char *SignalName16[] = {
		"HVBMS_Cell_TempMax",
		"HVBMS_Cell_TempMin"};

	char *SignalNamef[] = {
		"HVBMS_Cell_VoltMax",
		"HVBMS_Cell_VoltMin"};

	uint16_t SignalValue16[2] = {0};
		/*
		"HVBMS_Cell_TempMax",
		"HVBMS_Cell_TempMin"
		*/
	float SignalValuef[2];//Signals with float value
		/*
		"HVBMS_Cell_VoltMax",
		"HVBMS_Cell_VoltMin"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	HVBMS_Data_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue16[0] = 0xfff&(buf[0]|(buf[1]<<8));//HVBMS_Cell_TempMax
	SignalValue16[1] = (0xfff0&(buf[1]|(buf[2]<<8)))>>4;//HVBMS_Cell_TempMin
	SignalValuef[0] = (0xfff&(buf[3]|(buf[4]<<8))) * 0.00113288;
	SignalValuef[1] = ((0xfff0&(buf[4]|(buf[5]<<8)))>>4) * 0.00113288;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x11;
	DTU_Buffer[2] = 0x3;
	DTU_Buffer[3] = HVBMS_Data_DLC;

	DTU_Buffer[4] = (SignalValue16[0]&0xff);//HVBMS_Cell_TempMax
	DTU_Buffer[5] = (SignalValue16[0]&0xff00)>>8;
	DTU_Buffer[6] = (SignalValue16[1]&0xff);//HVBMS_Cell_TempMin
	DTU_Buffer[7] = (SignalValue16[1]&0xff00)>>8;
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[0])[0];//HVBMS_Cell_VoltMax
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[1])[0];//HVBMS_Cell_VoltMin
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[HVBMS_Data_Length - 2] = 0x0D;
	DTU_Buffer[HVBMS_Data_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < HVBMS_Data_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 2; i++)
	{
		sprintf(filebuffer, "0x311,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName16[i], SignalValue16[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, HVBMS_Data_Counter);
		f_puts(filebuffer, file);
	}
	for(i = 0; i < 2; i++)
	{
		sprintf(filebuffer, "0x311,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, HVBMS_Data_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//HVBMS_Debug	0x512
uint8_t  HVBMS_Debug_Unpack(uint8_t *buf)
{
	#define  HVBMS_Debug_DLC  4
	#define  HVBMS_Debug_Length  (HVBMS_Debug_DLC+Package_Length)
	uint8_t DTU_Buffer[HVBMS_Debug_Length];
	uint8_t i = 0;

	char *SignalName8[] = {
		"HVBMS_TempMaxID",
		"HVBMS_TempMinID",
		"HVBMS_VoltMaxID",
		"HVBMS_VoltMinID"};
	uint8_t SignalValue8[4] = {0};
		/*
		"HVBMS_TempMaxID",
		"HVBMS_TempMinID",
		"HVBMS_VoltMaxID",
		"HVBMS_VoltMinID"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	HVBMS_Debug_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue8[0] = 0xff&buf[0];//HVBMS_TempMaxID
	SignalValue8[1] = 0xff&buf[1];//HVBMS_TempMinID
	SignalValue8[2] = 0xff&buf[2];//HVBMS_VoltMaxID
	SignalValue8[3] = 0xff&buf[3];//HVBMS_VoltMinID
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x12;
	DTU_Buffer[2] = 0x5;
	DTU_Buffer[3] = HVBMS_Debug_DLC;

	DTU_Buffer[4] = SignalValue8[0];//HVBMS_TempMaxID
	DTU_Buffer[5] = SignalValue8[1];//HVBMS_TempMinID
	DTU_Buffer[6] = SignalValue8[2];//HVBMS_VoltMaxID
	DTU_Buffer[7] = SignalValue8[3];//HVBMS_VoltMinID
	DTU_Buffer[HVBMS_Debug_Length - 2] = 0x0D;
	DTU_Buffer[HVBMS_Debug_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < HVBMS_Debug_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 4; i++)
	{
		sprintf(filebuffer, "0x512,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName8[i], SignalValue8[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, HVBMS_Debug_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//LVBMS_Data1	0x315
uint8_t  LVBMS_Data1_Unpack(uint8_t *buf)
{
	#define  LVBMS_Data1_DLC  20
	#define  LVBMS_Data1_Length  (LVBMS_Data1_DLC+Package_Length)
	uint8_t DTU_Buffer[LVBMS_Data1_Length];
	uint8_t i = 0;

	char *SignalNamef[] = {
		"LVBMS_Volt1",
		"LVBMS_Volt2",
		"LVBMS_Volt3",
		"LVBMS_Volt4",
		"LVBMS_BatVolt"};

	float SignalValuef[5];//Signals with float value
		/*
		"LVBMS_Volt1",
		"LVBMS_Volt2",
		"LVBMS_Volt3",
		"LVBMS_Volt4",
		"LVBMS_BatVolt"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	LVBMS_Data1_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValuef[0] = (0xfff&(buf[0]|(buf[1]<<8))) * 0.0064;
	SignalValuef[1] = ((0xfff0&(buf[1]|(buf[2]<<8)))>>4) * 0.0064;
	SignalValuef[2] = (0xfff&(buf[3]|(buf[4]<<8))) * 0.0064;
	SignalValuef[3] = ((0xfff0&(buf[4]|(buf[5]<<8)))>>4) * 0.0064;
	SignalValuef[4] = (0xfff&(buf[6]|(buf[7]<<8))) * 0.0064;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x15;
	DTU_Buffer[2] = 0x3;
	DTU_Buffer[3] = LVBMS_Data1_DLC;

	DTU_Buffer[4+i] = ((uchar *)SignalValuef[0])[0];//LVBMS_Volt1
	DTU_Buffer[5+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[6+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[7+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[1])[0];//LVBMS_Volt2
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[2])[0];//LVBMS_Volt3
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[3])[0];//LVBMS_Volt4
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[3])[1];
	DTU_Buffer[18+i] = ((uchar *)SignalValuef[3])[2];
	DTU_Buffer[19+i] = ((uchar *)SignalValuef[3])[3];
	DTU_Buffer[20+i] = ((uchar *)SignalValuef[4])[0];//LVBMS_BatVolt
	DTU_Buffer[21+i] = ((uchar *)SignalValuef[4])[1];
	DTU_Buffer[22+i] = ((uchar *)SignalValuef[4])[2];
	DTU_Buffer[23+i] = ((uchar *)SignalValuef[4])[3];
	DTU_Buffer[LVBMS_Data1_Length - 2] = 0x0D;
	DTU_Buffer[LVBMS_Data1_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < LVBMS_Data1_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 5; i++)
	{
		sprintf(filebuffer, "0x315,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, LVBMS_Data1_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//LVBMS_Data2	0x316
uint8_t  LVBMS_Data2_Unpack(uint8_t *buf)
{
	#define  LVBMS_Data2_DLC  14
	#define  LVBMS_Data2_Length  (LVBMS_Data2_DLC+Package_Length)
	uint8_t DTU_Buffer[LVBMS_Data2_Length];
	uint8_t i = 0;

	char *SignalName8[] = {
		"LVBMS_Temp1",
		"LVBMS_Temp2"};
	char *SignalNamef[] = {
		"LVBMS_Current",
		"LVBMS_Volt5",
		"LVBMS_Volt6"};

	uint8_t SignalValue8[2] = {0};
		/*
		"LVBMS_Temp1",
		"LVBMS_Temp2"
		*/
	float SignalValuef[3];//Signals with float value
		/*
		"LVBMS_Current",
		"LVBMS_Volt5",
		"LVBMS_Volt6"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	LVBMS_Data2_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue8[0] = 0xff&buf[1];//LVBMS_Temp1
	SignalValue8[1] = 0xff&buf[2];//LVBMS_Temp2
	SignalValuef[0] = (0xff&buf[0]) * 50;
	SignalValuef[1] = (0xfff&(buf[3]|(buf[4]<<8))) * 0.0064;
	SignalValuef[2] = (0xfff&(buf[4]|(buf[5]<<8))) * 0.0064;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x16;
	DTU_Buffer[2] = 0x3;
	DTU_Buffer[3] = LVBMS_Data2_DLC;

	DTU_Buffer[4+i] = ((uchar *)SignalValuef[0])[0];//LVBMS_Current
	DTU_Buffer[5+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[6+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[7+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[8] = SignalValue8[0];//LVBMS_Temp1
	DTU_Buffer[9] = SignalValue8[1];//LVBMS_Temp2
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[1])[0];//LVBMS_Volt5
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[2])[0];//LVBMS_Volt6
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[LVBMS_Data2_Length - 2] = 0x0D;
	DTU_Buffer[LVBMS_Data2_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < LVBMS_Data2_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 2; i++)
	{
		sprintf(filebuffer, "0x316,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName8[i], SignalValue8[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, LVBMS_Data2_Counter);
		f_puts(filebuffer, file);
	}
	for(i = 0; i < 3; i++)
	{
		sprintf(filebuffer, "0x316,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, LVBMS_Data2_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//STN_Status	0x350
uint8_t  STN_Status_Unpack(uint8_t *buf)
{
	#define  STN_Status_DLC  12
	#define  STN_Status_Length  (STN_Status_DLC+Package_Length)
	uint8_t DTU_Buffer[STN_Status_Length];
	uint8_t i = 0;

	char *SignalName8[] = {
		"STN_Start",
		"STN_Stop",
		"STN_Mask",
		"STN_REG",
		"STN_TC",
		"STN_TV",
		"STN_MCErrorReset",
		"STN_MCReOn",
		"STN_SWR_1",
		"STN_SWR_2",
		"STN_TTorqueRatio",
		"STN_BTorqueRatio"};
	uint8_t SignalValue8[12] = {0};
		/*
		"STN_Start",
		"STN_Stop",
		"STN_Mask",
		"STN_REG",
		"STN_TC",
		"STN_TV",
		"STN_MCErrorReset",
		"STN_MCReOn",
		"STN_SWR_1",
		"STN_SWR_2",
		"STN_TTorqueRatio",
		"STN_BTorqueRatio"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	STN_Status_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue8[0] = 0x1&buf[0];//STN_Start
	SignalValue8[1] = (0x2&buf[0])>>1;//STN_Stop
	SignalValue8[2] = (0x4&buf[0])>>2;//STN_Mask
	SignalValue8[3] = (0x8&buf[0])>>3;//STN_REG
	SignalValue8[4] = (0x10&buf[0])>>4;//STN_TC
	SignalValue8[5] = (0x20&buf[0])>>5;//STN_TV
	SignalValue8[6] = (0x40&buf[0])>>6;//STN_MCErrorReset
	SignalValue8[7] = (0x80&buf[0])>>7;//STN_MCReOn
	SignalValue8[8] = 0xf&buf[1];//STN_SWR_1
	SignalValue8[9] = (0xf0&buf[1])>>4;//STN_SWR_2
	SignalValue8[10] = 0xf&buf[2];//STN_TTorqueRatio
	SignalValue8[11] = (0xf0&buf[2])>>4;//STN_BTorqueRatio
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x50;
	DTU_Buffer[2] = 0x3;
	DTU_Buffer[3] = STN_Status_DLC;

	DTU_Buffer[4] = SignalValue8[0];//STN_Start
	DTU_Buffer[5] = SignalValue8[1];//STN_Stop
	DTU_Buffer[6] = SignalValue8[2];//STN_Mask
	DTU_Buffer[7] = SignalValue8[3];//STN_REG
	DTU_Buffer[8] = SignalValue8[4];//STN_TC
	DTU_Buffer[9] = SignalValue8[5];//STN_TV
	DTU_Buffer[10] = SignalValue8[6];//STN_MCErrorReset
	DTU_Buffer[11] = SignalValue8[7];//STN_MCReOn
	DTU_Buffer[12] = SignalValue8[8];//STN_SWR_1
	DTU_Buffer[13] = SignalValue8[9];//STN_SWR_2
	DTU_Buffer[14] = SignalValue8[10];//STN_TTorqueRatio
	DTU_Buffer[15] = SignalValue8[11];//STN_BTorqueRatio
	DTU_Buffer[STN_Status_Length - 2] = 0x0D;
	DTU_Buffer[STN_Status_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < STN_Status_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 12; i++)
	{
		sprintf(filebuffer, "0x350,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName8[i], SignalValue8[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, STN_Status_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//GYRO_A	0x323
uint8_t  GYRO_A_Unpack(uint8_t *buf)
{
	#define  GYRO_A_DLC  12
	#define  GYRO_A_Length  (GYRO_A_DLC+Package_Length)
	uint8_t DTU_Buffer[GYRO_A_Length];
	uint8_t i = 0;

	char *SignalNamef[] = {
		"GYRO_AX",
		"GYRO_AY",
		"GYRO_AZ"};

	float SignalValuef[3];//Signals with float value
		/*
		"GYRO_AX",
		"GYRO_AY",
		"GYRO_AZ"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	GYRO_A_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValuef[0] = (0xffff&(buf[0]|(buf[1]<<8))) * 0.000122 + (-4);
	SignalValuef[1] = (0xffff&(buf[2]|(buf[3]<<8))) * 0.000122 + (-4);
	SignalValuef[2] = (0xffff&(buf[4]|(buf[5]<<8))) * 0.000122 + (-4);
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x23;
	DTU_Buffer[2] = 0x3;
	DTU_Buffer[3] = GYRO_A_DLC;

	DTU_Buffer[4+i] = ((uchar *)SignalValuef[0])[0];//GYRO_AX
	DTU_Buffer[5+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[6+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[7+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[1])[0];//GYRO_AY
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[2])[0];//GYRO_AZ
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[GYRO_A_Length - 2] = 0x0D;
	DTU_Buffer[GYRO_A_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < GYRO_A_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 3; i++)
	{
		sprintf(filebuffer, "0x323,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, GYRO_A_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//OS	0x325
uint8_t  OS_Unpack(uint8_t *buf)
{
	#define  OS_DLC  8
	#define  OS_Length  (OS_DLC+Package_Length)
	uint8_t DTU_Buffer[OS_Length];
	uint8_t i = 0;

	char *SignalNamef[] = {
		"OS_Velocity",
		"OS_SideslipAngle"};

	float SignalValuef[2];//Signals with float value
		/*
		"OS_Velocity",
		"OS_SideslipAngle"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	OS_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValuef[0] = (0xffff&(buf[0]|(buf[1]<<8))) * 0.036;
	SignalValuef[1] = (0xffff&(buf[2]|(buf[3]<<8))) * 0.01;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x25;
	DTU_Buffer[2] = 0x3;
	DTU_Buffer[3] = OS_DLC;

	DTU_Buffer[4+i] = ((uchar *)SignalValuef[0])[0];//OS_Velocity
	DTU_Buffer[5+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[6+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[7+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[1])[0];//OS_SideslipAngle
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[OS_Length - 2] = 0x0D;
	DTU_Buffer[OS_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < OS_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 2; i++)
	{
		sprintf(filebuffer, "0x325,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, OS_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//SNF_KeySensor	0x320
uint8_t  SNF_KeySensor_Unpack(uint8_t *buf)
{
	#define  SNF_KeySensor_DLC  16
	#define  SNF_KeySensor_Length  (SNF_KeySensor_DLC+Package_Length)
	uint8_t DTU_Buffer[SNF_KeySensor_Length];
	uint8_t i = 0;

	char *SignalNamef[] = {
		"SNF_APPS1",
		"SNF_APPS2",
		"SNF_BSE",
		"SNF_STS"};

	float SignalValuef[4];//Signals with float value
		/*
		"SNF_APPS1",
		"SNF_APPS2",
		"SNF_BSE",
		"SNF_STS"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	SNF_KeySensor_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValuef[0] = (0xfff&(buf[0]|(buf[1]<<8))) * 0.034692108 + (-22.0641804);
	SignalValuef[1] = ((0xfff0&(buf[1]|(buf[2]<<8)))>>4) * 0.034692108 + (-22.0641804);
	SignalValuef[2] = (0xfff&(buf[3]|(buf[4]<<8))) * 0.034692108 + (-22.0641804);
	SignalValuef[3] = ((0xfff0&(buf[4]|(buf[5]<<8)))>>4) * 0.146938776 + (-235.8367349);
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x20;
	DTU_Buffer[2] = 0x3;
	DTU_Buffer[3] = SNF_KeySensor_DLC;

	DTU_Buffer[4+i] = ((uchar *)SignalValuef[0])[0];//SNF_APPS1
	DTU_Buffer[5+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[6+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[7+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[1])[0];//SNF_APPS2
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[2])[0];//SNF_BSE
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[3])[0];//SNF_STS
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[3])[1];
	DTU_Buffer[18+i] = ((uchar *)SignalValuef[3])[2];
	DTU_Buffer[19+i] = ((uchar *)SignalValuef[3])[3];
	DTU_Buffer[SNF_KeySensor_Length - 2] = 0x0D;
	DTU_Buffer[SNF_KeySensor_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < SNF_KeySensor_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 4; i++)
	{
		sprintf(filebuffer, "0x320,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, SNF_KeySensor_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//SNF_DataSensor	0x321
uint8_t  SNF_DataSensor_Unpack(uint8_t *buf)
{
	#define  SNF_DataSensor_DLC  22
	#define  SNF_DataSensor_Length  (SNF_DataSensor_DLC+Package_Length)
	uint8_t DTU_Buffer[SNF_DataSensor_Length];
	uint8_t i = 0;

	char *SignalName8[] = {
		"SNF_bSHTD",
		"SNF_bOPT"};
	char *SignalNamef[] = {
		"SNF_DPFL",
		"SNF_DPFR",
		"SNF_DPRL",
		"SNF_DPRR",
		"SNF_HBPSF"};

	uint8_t SignalValue8[2] = {0};
		/*
		"SNF_bSHTD",
		"SNF_bOPT"
		*/
	float SignalValuef[5];//Signals with float value
		/*
		"SNF_DPFL",
		"SNF_DPFR",
		"SNF_DPRL",
		"SNF_DPRR",
		"SNF_HBPSF"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	SNF_DataSensor_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue8[0] = (0x10&buf[7])>>4;//SNF_bSHTD
	SignalValue8[1] = (0x20&buf[7])>>5;//SNF_bOPT
	SignalValuef[0] = (0xfff&(buf[0]|(buf[1]<<8))) * 0.01343;
	SignalValuef[1] = ((0xfff0&(buf[1]|(buf[2]<<8)))>>4) * 0.01343;
	SignalValuef[2] = (0xfff&(buf[3]|(buf[4]<<8))) * 0.01343;
	SignalValuef[3] = ((0xfff0&(buf[4]|(buf[5]<<8)))>>4) * 0.01343;
	SignalValuef[4] = (0xfff&(buf[6]|(buf[7]<<8))) * 0.002014 + (-0.74994);
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x21;
	DTU_Buffer[2] = 0x3;
	DTU_Buffer[3] = SNF_DataSensor_DLC;

	DTU_Buffer[4+i] = ((uchar *)SignalValuef[0])[0];//SNF_DPFL
	DTU_Buffer[5+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[6+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[7+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[1])[0];//SNF_DPFR
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[2])[0];//SNF_DPRL
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[3])[0];//SNF_DPRR
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[3])[1];
	DTU_Buffer[18+i] = ((uchar *)SignalValuef[3])[2];
	DTU_Buffer[19+i] = ((uchar *)SignalValuef[3])[3];
	DTU_Buffer[20+i] = ((uchar *)SignalValuef[4])[0];//SNF_HBPSF
	DTU_Buffer[21+i] = ((uchar *)SignalValuef[4])[1];
	DTU_Buffer[22+i] = ((uchar *)SignalValuef[4])[2];
	DTU_Buffer[23+i] = ((uchar *)SignalValuef[4])[3];
	DTU_Buffer[24] = SignalValue8[0];//SNF_bSHTD
	DTU_Buffer[25] = SignalValue8[1];//SNF_bOPT
	DTU_Buffer[SNF_DataSensor_Length - 2] = 0x0D;
	DTU_Buffer[SNF_DataSensor_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < SNF_DataSensor_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 2; i++)
	{
		sprintf(filebuffer, "0x321,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName8[i], SignalValue8[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, SNF_DataSensor_Counter);
		f_puts(filebuffer, file);
	}
	for(i = 0; i < 5; i++)
	{
		sprintf(filebuffer, "0x321,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, SNF_DataSensor_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//WSN_IMUFL1	0x410
uint8_t  WSN_IMUFL1_Unpack(uint8_t *buf)
{
	#define  WSN_IMUFL1_DLC  16
	#define  WSN_IMUFL1_Length  (WSN_IMUFL1_DLC+Package_Length)
	uint8_t DTU_Buffer[WSN_IMUFL1_Length];
	uint8_t i = 0;

	char *SignalNamef[] = {
		"IMUFL_GYROX",
		"IMUFL_GYROZ",
		"IMUFL_EULERX",
		"IMUFL_EULERZ"};

	float SignalValuef[4];//Signals with float value
		/*
		"IMUFL_GYROX",
		"IMUFL_GYROZ",
		"IMUFL_EULERX",
		"IMUFL_EULERZ"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	WSN_IMUFL1_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValuef[0] = (0xffff&(buf[0]|(buf[1]<<8))) * 0.01;
	SignalValuef[1] = (0xffff&(buf[2]|(buf[3]<<8))) * 0.01;
	SignalValuef[2] = (0xffff&(buf[4]|(buf[5]<<8))) * 0.01;
	SignalValuef[3] = (0xffff&(buf[6]|(buf[7]<<8))) * 0.01;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x10;
	DTU_Buffer[2] = 0x4;
	DTU_Buffer[3] = WSN_IMUFL1_DLC;

	DTU_Buffer[4+i] = ((uchar *)SignalValuef[0])[0];//IMUFL_GYROX
	DTU_Buffer[5+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[6+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[7+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[1])[0];//IMUFL_GYROZ
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[2])[0];//IMUFL_EULERX
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[3])[0];//IMUFL_EULERZ
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[3])[1];
	DTU_Buffer[18+i] = ((uchar *)SignalValuef[3])[2];
	DTU_Buffer[19+i] = ((uchar *)SignalValuef[3])[3];
	DTU_Buffer[WSN_IMUFL1_Length - 2] = 0x0D;
	DTU_Buffer[WSN_IMUFL1_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < WSN_IMUFL1_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 4; i++)
	{
		sprintf(filebuffer, "0x410,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, WSN_IMUFL1_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//WSN_IMUFL2	0x411
uint8_t  WSN_IMUFL2_Unpack(uint8_t *buf)
{
	#define  WSN_IMUFL2_DLC  16
	#define  WSN_IMUFL2_Length  (WSN_IMUFL2_DLC+Package_Length)
	uint8_t DTU_Buffer[WSN_IMUFL2_Length];
	uint8_t i = 0;

	char *SignalNamef[] = {
		"IMUFL_EULERY",
		"IMUFL_ACCX",
		"IMUFL_ACCZ",
		"IMUFL_ACCY"};

	float SignalValuef[4];//Signals with float value
		/*
		"IMUFL_EULERY",
		"IMUFL_ACCX",
		"IMUFL_ACCZ",
		"IMUFL_ACCY"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	WSN_IMUFL2_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValuef[0] = (0xffff&(buf[0]|(buf[1]<<8))) * 0.01;
	SignalValuef[1] = (0xffff&(buf[2]|(buf[3]<<8))) * 0.01;
	SignalValuef[2] = (0xffff&(buf[4]|(buf[5]<<8))) * 0.01;
	SignalValuef[3] = (0xffff&(buf[6]|(buf[7]<<8))) * 0.01;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x11;
	DTU_Buffer[2] = 0x4;
	DTU_Buffer[3] = WSN_IMUFL2_DLC;

	DTU_Buffer[4+i] = ((uchar *)SignalValuef[0])[0];//IMUFL_EULERY
	DTU_Buffer[5+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[6+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[7+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[1])[0];//IMUFL_ACCX
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[2])[0];//IMUFL_ACCZ
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[3])[0];//IMUFL_ACCY
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[3])[1];
	DTU_Buffer[18+i] = ((uchar *)SignalValuef[3])[2];
	DTU_Buffer[19+i] = ((uchar *)SignalValuef[3])[3];
	DTU_Buffer[WSN_IMUFL2_Length - 2] = 0x0D;
	DTU_Buffer[WSN_IMUFL2_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < WSN_IMUFL2_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 4; i++)
	{
		sprintf(filebuffer, "0x411,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, WSN_IMUFL2_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//WSN_IMUFR1	0x412
uint8_t  WSN_IMUFR1_Unpack(uint8_t *buf)
{
	#define  WSN_IMUFR1_DLC  16
	#define  WSN_IMUFR1_Length  (WSN_IMUFR1_DLC+Package_Length)
	uint8_t DTU_Buffer[WSN_IMUFR1_Length];
	uint8_t i = 0;

	char *SignalNamef[] = {
		"IMUFR_GYROX",
		"IMUFR_GYROZ",
		"IMUFR_EULERX",
		"IMUFR_EULERZ"};

	float SignalValuef[4];//Signals with float value
		/*
		"IMUFR_GYROX",
		"IMUFR_GYROZ",
		"IMUFR_EULERX",
		"IMUFR_EULERZ"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	WSN_IMUFR1_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValuef[0] = (0xffff&(buf[0]|(buf[1]<<8))) * 0.01;
	SignalValuef[1] = (0xffff&(buf[2]|(buf[3]<<8))) * 0.01;
	SignalValuef[2] = (0xffff&(buf[4]|(buf[5]<<8))) * 0.01;
	SignalValuef[3] = (0xffff&(buf[6]|(buf[7]<<8))) * 0.01;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x12;
	DTU_Buffer[2] = 0x4;
	DTU_Buffer[3] = WSN_IMUFR1_DLC;

	DTU_Buffer[4+i] = ((uchar *)SignalValuef[0])[0];//IMUFR_GYROX
	DTU_Buffer[5+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[6+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[7+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[1])[0];//IMUFR_GYROZ
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[2])[0];//IMUFR_EULERX
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[3])[0];//IMUFR_EULERZ
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[3])[1];
	DTU_Buffer[18+i] = ((uchar *)SignalValuef[3])[2];
	DTU_Buffer[19+i] = ((uchar *)SignalValuef[3])[3];
	DTU_Buffer[WSN_IMUFR1_Length - 2] = 0x0D;
	DTU_Buffer[WSN_IMUFR1_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < WSN_IMUFR1_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 4; i++)
	{
		sprintf(filebuffer, "0x412,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, WSN_IMUFR1_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//WSN_IMUFR2	0x413
uint8_t  WSN_IMUFR2_Unpack(uint8_t *buf)
{
	#define  WSN_IMUFR2_DLC  16
	#define  WSN_IMUFR2_Length  (WSN_IMUFR2_DLC+Package_Length)
	uint8_t DTU_Buffer[WSN_IMUFR2_Length];
	uint8_t i = 0;

	char *SignalNamef[] = {
		"IMUFR_EULERY",
		"IMUFR_ACCX",
		"IMUFR_ACCZ",
		"IMUFR_ACCY"};

	float SignalValuef[4];//Signals with float value
		/*
		"IMUFR_EULERY",
		"IMUFR_ACCX",
		"IMUFR_ACCZ",
		"IMUFR_ACCY"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	WSN_IMUFR2_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValuef[0] = (0xffff&(buf[0]|(buf[1]<<8))) * 0.01;
	SignalValuef[1] = (0xffff&(buf[2]|(buf[3]<<8))) * 0.01;
	SignalValuef[2] = (0xffff&(buf[4]|(buf[5]<<8))) * 0.01;
	SignalValuef[3] = (0xffff&(buf[6]|(buf[7]<<8))) * 0.01;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x13;
	DTU_Buffer[2] = 0x4;
	DTU_Buffer[3] = WSN_IMUFR2_DLC;

	DTU_Buffer[4+i] = ((uchar *)SignalValuef[0])[0];//IMUFR_EULERY
	DTU_Buffer[5+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[6+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[7+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[1])[0];//IMUFR_ACCX
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[2])[0];//IMUFR_ACCZ
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[3])[0];//IMUFR_ACCY
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[3])[1];
	DTU_Buffer[18+i] = ((uchar *)SignalValuef[3])[2];
	DTU_Buffer[19+i] = ((uchar *)SignalValuef[3])[3];
	DTU_Buffer[WSN_IMUFR2_Length - 2] = 0x0D;
	DTU_Buffer[WSN_IMUFR2_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < WSN_IMUFR2_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 4; i++)
	{
		sprintf(filebuffer, "0x413,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, WSN_IMUFR2_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//WSN_IMURL1	0x414
uint8_t  WSN_IMURL1_Unpack(uint8_t *buf)
{
	#define  WSN_IMURL1_DLC  16
	#define  WSN_IMURL1_Length  (WSN_IMURL1_DLC+Package_Length)
	uint8_t DTU_Buffer[WSN_IMURL1_Length];
	uint8_t i = 0;

	char *SignalNamef[] = {
		"IMURL_GYROX",
		"IMURL_GYROZ",
		"IMURL_EULERX",
		"IMURL_EULERZ"};

	float SignalValuef[4];//Signals with float value
		/*
		"IMURL_GYROX",
		"IMURL_GYROZ",
		"IMURL_EULERX",
		"IMURL_EULERZ"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	WSN_IMURL1_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValuef[0] = (0xffff&(buf[0]|(buf[1]<<8))) * 0.01;
	SignalValuef[1] = (0xffff&(buf[2]|(buf[3]<<8))) * 0.01;
	SignalValuef[2] = (0xffff&(buf[4]|(buf[5]<<8))) * 0.01;
	SignalValuef[3] = (0xffff&(buf[6]|(buf[7]<<8))) * 0.01;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x14;
	DTU_Buffer[2] = 0x4;
	DTU_Buffer[3] = WSN_IMURL1_DLC;

	DTU_Buffer[4+i] = ((uchar *)SignalValuef[0])[0];//IMURL_GYROX
	DTU_Buffer[5+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[6+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[7+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[1])[0];//IMURL_GYROZ
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[2])[0];//IMURL_EULERX
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[3])[0];//IMURL_EULERZ
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[3])[1];
	DTU_Buffer[18+i] = ((uchar *)SignalValuef[3])[2];
	DTU_Buffer[19+i] = ((uchar *)SignalValuef[3])[3];
	DTU_Buffer[WSN_IMURL1_Length - 2] = 0x0D;
	DTU_Buffer[WSN_IMURL1_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < WSN_IMURL1_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 4; i++)
	{
		sprintf(filebuffer, "0x414,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, WSN_IMURL1_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//WSN_IMURL2	0x415
uint8_t  WSN_IMURL2_Unpack(uint8_t *buf)
{
	#define  WSN_IMURL2_DLC  16
	#define  WSN_IMURL2_Length  (WSN_IMURL2_DLC+Package_Length)
	uint8_t DTU_Buffer[WSN_IMURL2_Length];
	uint8_t i = 0;

	char *SignalNamef[] = {
		"IMURL_EULERY",
		"IMURL_ACCX",
		"IMURL_ACCZ",
		"IMURL_ACCY"};

	float SignalValuef[4];//Signals with float value
		/*
		"IMURL_EULERY",
		"IMURL_ACCX",
		"IMURL_ACCZ",
		"IMURL_ACCY"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	WSN_IMURL2_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValuef[0] = (0xffff&(buf[0]|(buf[1]<<8))) * 0.01;
	SignalValuef[1] = (0xffff&(buf[2]|(buf[3]<<8))) * 0.01;
	SignalValuef[2] = (0xffff&(buf[4]|(buf[5]<<8))) * 0.01;
	SignalValuef[3] = (0xffff&(buf[6]|(buf[7]<<8))) * 0.01;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x15;
	DTU_Buffer[2] = 0x4;
	DTU_Buffer[3] = WSN_IMURL2_DLC;

	DTU_Buffer[4+i] = ((uchar *)SignalValuef[0])[0];//IMURL_EULERY
	DTU_Buffer[5+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[6+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[7+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[1])[0];//IMURL_ACCX
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[2])[0];//IMURL_ACCZ
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[3])[0];//IMURL_ACCY
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[3])[1];
	DTU_Buffer[18+i] = ((uchar *)SignalValuef[3])[2];
	DTU_Buffer[19+i] = ((uchar *)SignalValuef[3])[3];
	DTU_Buffer[WSN_IMURL2_Length - 2] = 0x0D;
	DTU_Buffer[WSN_IMURL2_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < WSN_IMURL2_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 4; i++)
	{
		sprintf(filebuffer, "0x415,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, WSN_IMURL2_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//WSN_IMURR1	0x416
uint8_t  WSN_IMURR1_Unpack(uint8_t *buf)
{
	#define  WSN_IMURR1_DLC  16
	#define  WSN_IMURR1_Length  (WSN_IMURR1_DLC+Package_Length)
	uint8_t DTU_Buffer[WSN_IMURR1_Length];
	uint8_t i = 0;

	char *SignalNamef[] = {
		"IMURR_GYROX",
		"IMURR_GYROZ",
		"IMURR_EULERX",
		"IMURR_EULERZ"};

	float SignalValuef[4];//Signals with float value
		/*
		"IMURR_GYROX",
		"IMURR_GYROZ",
		"IMURR_EULERX",
		"IMURR_EULERZ"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	WSN_IMURR1_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValuef[0] = (0xffff&(buf[0]|(buf[1]<<8))) * 0.01;
	SignalValuef[1] = (0xffff&(buf[2]|(buf[3]<<8))) * 0.01;
	SignalValuef[2] = (0xffff&(buf[4]|(buf[5]<<8))) * 0.01;
	SignalValuef[3] = (0xffff&(buf[6]|(buf[7]<<8))) * 0.01;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x16;
	DTU_Buffer[2] = 0x4;
	DTU_Buffer[3] = WSN_IMURR1_DLC;

	DTU_Buffer[4+i] = ((uchar *)SignalValuef[0])[0];//IMURR_GYROX
	DTU_Buffer[5+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[6+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[7+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[1])[0];//IMURR_GYROZ
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[2])[0];//IMURR_EULERX
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[3])[0];//IMURR_EULERZ
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[3])[1];
	DTU_Buffer[18+i] = ((uchar *)SignalValuef[3])[2];
	DTU_Buffer[19+i] = ((uchar *)SignalValuef[3])[3];
	DTU_Buffer[WSN_IMURR1_Length - 2] = 0x0D;
	DTU_Buffer[WSN_IMURR1_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < WSN_IMURR1_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 4; i++)
	{
		sprintf(filebuffer, "0x416,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, WSN_IMURR1_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//WSN_IMURR2	0x417
uint8_t  WSN_IMURR2_Unpack(uint8_t *buf)
{
	#define  WSN_IMURR2_DLC  16
	#define  WSN_IMURR2_Length  (WSN_IMURR2_DLC+Package_Length)
	uint8_t DTU_Buffer[WSN_IMURR2_Length];
	uint8_t i = 0;

	char *SignalNamef[] = {
		"IMURR_EULERY",
		"IMURR_ACCX",
		"IMURR_ACCZ",
		"IMURR_ACCY"};

	float SignalValuef[4];//Signals with float value
		/*
		"IMURR_EULERY",
		"IMURR_ACCX",
		"IMURR_ACCZ",
		"IMURR_ACCY"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	WSN_IMURR2_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValuef[0] = (0xffff&(buf[0]|(buf[1]<<8))) * 0.01;
	SignalValuef[1] = (0xffff&(buf[2]|(buf[3]<<8))) * 0.01;
	SignalValuef[2] = (0xffff&(buf[4]|(buf[5]<<8))) * 0.01;
	SignalValuef[3] = (0xffff&(buf[6]|(buf[7]<<8))) * 0.01;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x17;
	DTU_Buffer[2] = 0x4;
	DTU_Buffer[3] = WSN_IMURR2_DLC;

	DTU_Buffer[4+i] = ((uchar *)SignalValuef[0])[0];//IMURR_EULERY
	DTU_Buffer[5+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[6+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[7+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[1])[0];//IMURR_ACCX
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[2])[0];//IMURR_ACCZ
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[3])[0];//IMURR_ACCY
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[3])[1];
	DTU_Buffer[18+i] = ((uchar *)SignalValuef[3])[2];
	DTU_Buffer[19+i] = ((uchar *)SignalValuef[3])[3];
	DTU_Buffer[WSN_IMURR2_Length - 2] = 0x0D;
	DTU_Buffer[WSN_IMURR2_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < WSN_IMURR2_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 4; i++)
	{
		sprintf(filebuffer, "0x417,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, WSN_IMURR2_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//WSN_TempFL	0x418
uint8_t  WSN_TempFL_Unpack(uint8_t *buf)
{
	#define  WSN_TempFL_DLC  8
	#define  WSN_TempFL_Length  (WSN_TempFL_DLC+Package_Length)
	uint8_t DTU_Buffer[WSN_TempFL_Length];
	uint8_t i = 0;

	char *SignalName8[] = {
		"TTPS_FL_1",
		"TTPS_FL_2",
		"TTPS_FL_3",
		"TTPS_FL_4",
		"TTPS_FL_5",
		"TTPS_FL_6",
		"TTPS_FL_7",
		"TTPS_FL_8"};
	uint8_t SignalValue8[8] = {0};
		/*
		"TTPS_FL_1",
		"TTPS_FL_2",
		"TTPS_FL_3",
		"TTPS_FL_4",
		"TTPS_FL_5",
		"TTPS_FL_6",
		"TTPS_FL_7",
		"TTPS_FL_8"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	WSN_TempFL_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue8[0] = 0xff&buf[0];//TTPS_FL_1
	SignalValue8[1] = 0xff&buf[1];//TTPS_FL_2
	SignalValue8[2] = 0xff&buf[2];//TTPS_FL_3
	SignalValue8[3] = 0xff&buf[3];//TTPS_FL_4
	SignalValue8[4] = 0xff&buf[4];//TTPS_FL_5
	SignalValue8[5] = 0xff&buf[5];//TTPS_FL_6
	SignalValue8[6] = 0xff&buf[6];//TTPS_FL_7
	SignalValue8[7] = 0xff&buf[7];//TTPS_FL_8
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x18;
	DTU_Buffer[2] = 0x4;
	DTU_Buffer[3] = WSN_TempFL_DLC;

	DTU_Buffer[4] = SignalValue8[0];//TTPS_FL_1
	DTU_Buffer[5] = SignalValue8[1];//TTPS_FL_2
	DTU_Buffer[6] = SignalValue8[2];//TTPS_FL_3
	DTU_Buffer[7] = SignalValue8[3];//TTPS_FL_4
	DTU_Buffer[8] = SignalValue8[4];//TTPS_FL_5
	DTU_Buffer[9] = SignalValue8[5];//TTPS_FL_6
	DTU_Buffer[10] = SignalValue8[6];//TTPS_FL_7
	DTU_Buffer[11] = SignalValue8[7];//TTPS_FL_8
	DTU_Buffer[WSN_TempFL_Length - 2] = 0x0D;
	DTU_Buffer[WSN_TempFL_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < WSN_TempFL_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 8; i++)
	{
		sprintf(filebuffer, "0x418,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName8[i], SignalValue8[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, WSN_TempFL_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//WSN_TempFR	0x419
uint8_t  WSN_TempFR_Unpack(uint8_t *buf)
{
	#define  WSN_TempFR_DLC  8
	#define  WSN_TempFR_Length  (WSN_TempFR_DLC+Package_Length)
	uint8_t DTU_Buffer[WSN_TempFR_Length];
	uint8_t i = 0;

	char *SignalName8[] = {
		"TTPS_FR_1",
		"TTPS_FR_2",
		"TTPS_FR_3",
		"TTPS_FR_4",
		"TTPS_FR_5",
		"TTPS_FR_6",
		"TTPS_FR_7",
		"TTPS_FR_8"};
	uint8_t SignalValue8[8] = {0};
		/*
		"TTPS_FR_1",
		"TTPS_FR_2",
		"TTPS_FR_3",
		"TTPS_FR_4",
		"TTPS_FR_5",
		"TTPS_FR_6",
		"TTPS_FR_7",
		"TTPS_FR_8"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	WSN_TempFR_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue8[0] = 0xff&buf[0];//TTPS_FR_1
	SignalValue8[1] = 0xff&buf[1];//TTPS_FR_2
	SignalValue8[2] = 0xff&buf[2];//TTPS_FR_3
	SignalValue8[3] = 0xff&buf[3];//TTPS_FR_4
	SignalValue8[4] = 0xff&buf[4];//TTPS_FR_5
	SignalValue8[5] = 0xff&buf[5];//TTPS_FR_6
	SignalValue8[6] = 0xff&buf[6];//TTPS_FR_7
	SignalValue8[7] = 0xff&buf[7];//TTPS_FR_8
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x19;
	DTU_Buffer[2] = 0x4;
	DTU_Buffer[3] = WSN_TempFR_DLC;

	DTU_Buffer[4] = SignalValue8[0];//TTPS_FR_1
	DTU_Buffer[5] = SignalValue8[1];//TTPS_FR_2
	DTU_Buffer[6] = SignalValue8[2];//TTPS_FR_3
	DTU_Buffer[7] = SignalValue8[3];//TTPS_FR_4
	DTU_Buffer[8] = SignalValue8[4];//TTPS_FR_5
	DTU_Buffer[9] = SignalValue8[5];//TTPS_FR_6
	DTU_Buffer[10] = SignalValue8[6];//TTPS_FR_7
	DTU_Buffer[11] = SignalValue8[7];//TTPS_FR_8
	DTU_Buffer[WSN_TempFR_Length - 2] = 0x0D;
	DTU_Buffer[WSN_TempFR_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < WSN_TempFR_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 8; i++)
	{
		sprintf(filebuffer, "0x419,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName8[i], SignalValue8[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, WSN_TempFR_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//WSN_TempRL	0x41A
uint8_t  WSN_TempRL_Unpack(uint8_t *buf)
{
	#define  WSN_TempRL_DLC  8
	#define  WSN_TempRL_Length  (WSN_TempRL_DLC+Package_Length)
	uint8_t DTU_Buffer[WSN_TempRL_Length];
	uint8_t i = 0;

	char *SignalName8[] = {
		"TTPS_RL_1",
		"TTPS_RL_2",
		"TTPS_RL_3",
		"TTPS_RL_4",
		"TTPS_RL_5",
		"TTPS_RL_6",
		"TTPS_RL_7",
		"TTPS_RL_8"};
	uint8_t SignalValue8[8] = {0};
		/*
		"TTPS_RL_1",
		"TTPS_RL_2",
		"TTPS_RL_3",
		"TTPS_RL_4",
		"TTPS_RL_5",
		"TTPS_RL_6",
		"TTPS_RL_7",
		"TTPS_RL_8"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	WSN_TempRL_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue8[0] = 0xff&buf[0];//TTPS_RL_1
	SignalValue8[1] = 0xff&buf[1];//TTPS_RL_2
	SignalValue8[2] = 0xff&buf[2];//TTPS_RL_3
	SignalValue8[3] = 0xff&buf[3];//TTPS_RL_4
	SignalValue8[4] = 0xff&buf[4];//TTPS_RL_5
	SignalValue8[5] = 0xff&buf[5];//TTPS_RL_6
	SignalValue8[6] = 0xff&buf[6];//TTPS_RL_7
	SignalValue8[7] = 0xff&buf[7];//TTPS_RL_8
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x1a;
	DTU_Buffer[2] = 0x4;
	DTU_Buffer[3] = WSN_TempRL_DLC;

	DTU_Buffer[4] = SignalValue8[0];//TTPS_RL_1
	DTU_Buffer[5] = SignalValue8[1];//TTPS_RL_2
	DTU_Buffer[6] = SignalValue8[2];//TTPS_RL_3
	DTU_Buffer[7] = SignalValue8[3];//TTPS_RL_4
	DTU_Buffer[8] = SignalValue8[4];//TTPS_RL_5
	DTU_Buffer[9] = SignalValue8[5];//TTPS_RL_6
	DTU_Buffer[10] = SignalValue8[6];//TTPS_RL_7
	DTU_Buffer[11] = SignalValue8[7];//TTPS_RL_8
	DTU_Buffer[WSN_TempRL_Length - 2] = 0x0D;
	DTU_Buffer[WSN_TempRL_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < WSN_TempRL_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 8; i++)
	{
		sprintf(filebuffer, "0x41A,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName8[i], SignalValue8[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, WSN_TempRL_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//WSN_TempRR	0x41B
uint8_t  WSN_TempRR_Unpack(uint8_t *buf)
{
	#define  WSN_TempRR_DLC  8
	#define  WSN_TempRR_Length  (WSN_TempRR_DLC+Package_Length)
	uint8_t DTU_Buffer[WSN_TempRR_Length];
	uint8_t i = 0;

	char *SignalName8[] = {
		"TTPS_RR_1",
		"TTPS_RR_2",
		"TTPS_RR_3",
		"TTPS_RR_4",
		"TTPS_RR_5",
		"TTPS_RR_6",
		"TTPS_RR_7",
		"TTPS_RR_8"};
	uint8_t SignalValue8[8] = {0};
		/*
		"TTPS_RR_1",
		"TTPS_RR_2",
		"TTPS_RR_3",
		"TTPS_RR_4",
		"TTPS_RR_5",
		"TTPS_RR_6",
		"TTPS_RR_7",
		"TTPS_RR_8"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	WSN_TempRR_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue8[0] = 0xff&buf[0];//TTPS_RR_1
	SignalValue8[1] = 0xff&buf[1];//TTPS_RR_2
	SignalValue8[2] = 0xff&buf[2];//TTPS_RR_3
	SignalValue8[3] = 0xff&buf[3];//TTPS_RR_4
	SignalValue8[4] = 0xff&buf[4];//TTPS_RR_5
	SignalValue8[5] = 0xff&buf[5];//TTPS_RR_6
	SignalValue8[6] = 0xff&buf[6];//TTPS_RR_7
	SignalValue8[7] = 0xff&buf[7];//TTPS_RR_8
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x1b;
	DTU_Buffer[2] = 0x4;
	DTU_Buffer[3] = WSN_TempRR_DLC;

	DTU_Buffer[4] = SignalValue8[0];//TTPS_RR_1
	DTU_Buffer[5] = SignalValue8[1];//TTPS_RR_2
	DTU_Buffer[6] = SignalValue8[2];//TTPS_RR_3
	DTU_Buffer[7] = SignalValue8[3];//TTPS_RR_4
	DTU_Buffer[8] = SignalValue8[4];//TTPS_RR_5
	DTU_Buffer[9] = SignalValue8[5];//TTPS_RR_6
	DTU_Buffer[10] = SignalValue8[6];//TTPS_RR_7
	DTU_Buffer[11] = SignalValue8[7];//TTPS_RR_8
	DTU_Buffer[WSN_TempRR_Length - 2] = 0x0D;
	DTU_Buffer[WSN_TempRR_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < WSN_TempRR_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 8; i++)
	{
		sprintf(filebuffer, "0x41B,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName8[i], SignalValue8[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, WSN_TempRR_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//MCFL_SetPoints	0X182
uint8_t  MCFL_SetPoints_Unpack(uint8_t *buf)
{
	#define  MCFL_SetPoints_DLC  16
	#define  MCFL_SetPoints_Length  (MCFL_SetPoints_DLC+Package_Length)
	uint8_t DTU_Buffer[MCFL_SetPoints_Length];
	uint8_t i = 0;

	char *SignalName8[] = {
		"MCFL_cInverterOn",
		"MCFL_cDCOn",
		"MCFL_cEnable",
		"MCFL_cErrorReset"};
	char *SignalNamef[] = {
		"MCFL_TargetTorque",
		"MCFL_TorqueLimitP",
		"MCFL_TorqueLimitN"};

	uint8_t SignalValue8[4] = {0};
		/*
		"MCFL_cInverterOn",
		"MCFL_cDCOn",
		"MCFL_cEnable",
		"MCFL_cErrorReset"
		*/
	float SignalValuef[3];//Signals with float value
		/*
		"MCFL_TargetTorque",
		"MCFL_TorqueLimitP",
		"MCFL_TorqueLimitN"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	MCFL_SetPoints_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue8[0] = 0x1&buf[1];//MCFL_cInverterOn
	SignalValue8[1] = (0x2&buf[1])>>1;//MCFL_cDCOn
	SignalValue8[2] = (0x4&buf[1])>>2;//MCFL_cEnable
	SignalValue8[3] = (0x8&buf[1])>>3;//MCFL_cErrorReset
	SignalValuef[0] = (0xffff&(buf[2]|(buf[3]<<8))) * 0.0098;
	SignalValuef[1] = (0xffff&(buf[4]|(buf[5]<<8))) * 0.0098;
	SignalValuef[2] = (0xffff&(buf[6]|(buf[7]<<8))) * 0.0098;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x82;
	DTU_Buffer[2] = 0x1;
	DTU_Buffer[3] = MCFL_SetPoints_DLC;

	DTU_Buffer[4] = SignalValue8[0];//MCFL_cInverterOn
	DTU_Buffer[5] = SignalValue8[1];//MCFL_cDCOn
	DTU_Buffer[6] = SignalValue8[2];//MCFL_cEnable
	DTU_Buffer[7] = SignalValue8[3];//MCFL_cErrorReset
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[0])[0];//MCFL_TargetTorque
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[1])[0];//MCFL_TorqueLimitP
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[2])[0];//MCFL_TorqueLimitN
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[18+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[19+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[MCFL_SetPoints_Length - 2] = 0x0D;
	DTU_Buffer[MCFL_SetPoints_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < MCFL_SetPoints_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 4; i++)
	{
		sprintf(filebuffer, "0X182,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName8[i], SignalValue8[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCFL_SetPoints_Counter);
		f_puts(filebuffer, file);
	}
	for(i = 0; i < 3; i++)
	{
		sprintf(filebuffer, "0X182,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCFL_SetPoints_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//MCFR_SetPoints	0X183
uint8_t  MCFR_SetPoints_Unpack(uint8_t *buf)
{
	#define  MCFR_SetPoints_DLC  16
	#define  MCFR_SetPoints_Length  (MCFR_SetPoints_DLC+Package_Length)
	uint8_t DTU_Buffer[MCFR_SetPoints_Length];
	uint8_t i = 0;

	char *SignalName8[] = {
		"MCFR_cInverterOn",
		"MCFR_cDCOn",
		"MCFR_cEnable",
		"MCFR_cErrorReset"};
	char *SignalNamef[] = {
		"MCFR_TargetTorque",
		"MCFR_TorqueLimitP",
		"MCFR_TorqueLimitN"};

	uint8_t SignalValue8[4] = {0};
		/*
		"MCFR_cInverterOn",
		"MCFR_cDCOn",
		"MCFR_cEnable",
		"MCFR_cErrorReset"
		*/
	float SignalValuef[3];//Signals with float value
		/*
		"MCFR_TargetTorque",
		"MCFR_TorqueLimitP",
		"MCFR_TorqueLimitN"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	MCFR_SetPoints_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue8[0] = 0x1&buf[1];//MCFR_cInverterOn
	SignalValue8[1] = (0x2&buf[1])>>1;//MCFR_cDCOn
	SignalValue8[2] = (0x4&buf[1])>>2;//MCFR_cEnable
	SignalValue8[3] = (0x8&buf[1])>>3;//MCFR_cErrorReset
	SignalValuef[0] = (0xffff&(buf[2]|(buf[3]<<8))) * 0.0098;
	SignalValuef[1] = (0xffff&(buf[4]|(buf[5]<<8))) * 0.0098;
	SignalValuef[2] = (0xffff&(buf[6]|(buf[7]<<8))) * 0.0098;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x83;
	DTU_Buffer[2] = 0x1;
	DTU_Buffer[3] = MCFR_SetPoints_DLC;

	DTU_Buffer[4] = SignalValue8[0];//MCFR_cInverterOn
	DTU_Buffer[5] = SignalValue8[1];//MCFR_cDCOn
	DTU_Buffer[6] = SignalValue8[2];//MCFR_cEnable
	DTU_Buffer[7] = SignalValue8[3];//MCFR_cErrorReset
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[0])[0];//MCFR_TargetTorque
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[1])[0];//MCFR_TorqueLimitP
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[2])[0];//MCFR_TorqueLimitN
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[18+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[19+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[MCFR_SetPoints_Length - 2] = 0x0D;
	DTU_Buffer[MCFR_SetPoints_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < MCFR_SetPoints_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 4; i++)
	{
		sprintf(filebuffer, "0X183,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName8[i], SignalValue8[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCFR_SetPoints_Counter);
		f_puts(filebuffer, file);
	}
	for(i = 0; i < 3; i++)
	{
		sprintf(filebuffer, "0X183,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCFR_SetPoints_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//MCFL_ActualValue1	0x280
uint8_t  MCFL_ActualValue1_Unpack(uint8_t *buf)
{
	#define  MCFL_ActualValue1_DLC  17
	#define  MCFL_ActualValue1_Length  (MCFL_ActualValue1_DLC+Package_Length)
	uint8_t DTU_Buffer[MCFL_ActualValue1_Length];
	uint8_t i = 0;

	char *SignalName8[] = {
		"MCFL_bReverse",
		"MCFL_bSystemReady",
		"MCFL_bError",
		"MCFL_bWarn",
		"MCFL_bQuitDCOn",
		"MCFL_bDCOn",
		"MCFL_bQuitInverterOn",
		"MCFL_bInverterOn",
		"MCFL_bDerating"};
	char *SignalName16[] = {
		"MCFL_DCVoltage",
		"MCFL_ActualVelocity"};

	char *SignalNamef[] = {
		"MCFL_ActualTorque"};

	uint8_t SignalValue8[9] = {0};
		/*
		"MCFL_bReverse",
		"MCFL_bSystemReady",
		"MCFL_bError",
		"MCFL_bWarn",
		"MCFL_bQuitDCOn",
		"MCFL_bDCOn",
		"MCFL_bQuitInverterOn",
		"MCFL_bInverterOn",
		"MCFL_bDerating"
		*/
	uint16_t SignalValue16[2] = {0};
		/*
		"MCFL_DCVoltage",
		"MCFL_ActualVelocity"
		*/
	float SignalValuef[1];//Signals with float value
		/*
		"MCFL_ActualTorque"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	MCFL_ActualValue1_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue8[0] = 0xff&buf[0];//MCFL_bReverse
	SignalValue8[1] = 0x1&buf[1];//MCFL_bSystemReady
	SignalValue8[2] = (0x2&buf[1])>>1;//MCFL_bError
	SignalValue8[3] = (0x4&buf[1])>>2;//MCFL_bWarn
	SignalValue8[4] = (0x8&buf[1])>>3;//MCFL_bQuitDCOn
	SignalValue8[5] = (0x10&buf[1])>>4;//MCFL_bDCOn
	SignalValue8[6] = (0x20&buf[1])>>5;//MCFL_bQuitInverterOn
	SignalValue8[7] = (0x40&buf[1])>>6;//MCFL_bInverterOn
	SignalValue8[8] = (0x80&buf[1])>>7;//MCFL_bDerating
	SignalValue16[0] = 0xffff&(buf[2]|(buf[3]<<8));//MCFL_DCVoltage
	SignalValue16[1] = 0xffff&(buf[6]|(buf[7]<<8));//MCFL_ActualVelocity
	SignalValuef[0] = (0xffff&(buf[4]|(buf[5]<<8))) * 0.0098;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x80;
	DTU_Buffer[2] = 0x2;
	DTU_Buffer[3] = MCFL_ActualValue1_DLC;

	DTU_Buffer[4] = SignalValue8[0];//MCFL_bReverse
	DTU_Buffer[5] = SignalValue8[1];//MCFL_bSystemReady
	DTU_Buffer[6] = SignalValue8[2];//MCFL_bError
	DTU_Buffer[7] = SignalValue8[3];//MCFL_bWarn
	DTU_Buffer[8] = SignalValue8[4];//MCFL_bQuitDCOn
	DTU_Buffer[9] = SignalValue8[5];//MCFL_bDCOn
	DTU_Buffer[10] = SignalValue8[6];//MCFL_bQuitInverterOn
	DTU_Buffer[11] = SignalValue8[7];//MCFL_bInverterOn
	DTU_Buffer[12] = SignalValue8[8];//MCFL_bDerating
	DTU_Buffer[13] = (SignalValue16[0]&0xff);//MCFL_DCVoltage
	DTU_Buffer[14] = (SignalValue16[0]&0xff00)>>8;
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[0])[0];//MCFL_ActualTorque
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[18+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[19] = (SignalValue16[1]&0xff);//MCFL_ActualVelocity
	DTU_Buffer[20] = (SignalValue16[1]&0xff00)>>8;
	DTU_Buffer[MCFL_ActualValue1_Length - 2] = 0x0D;
	DTU_Buffer[MCFL_ActualValue1_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < MCFL_ActualValue1_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 9; i++)
	{
		sprintf(filebuffer, "0x280,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName8[i], SignalValue8[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCFL_ActualValue1_Counter);
		f_puts(filebuffer, file);
	}
	for(i = 0; i < 2; i++)
	{
		sprintf(filebuffer, "0x280,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName16[i], SignalValue16[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCFL_ActualValue1_Counter);
		f_puts(filebuffer, file);
	}
	for(i = 0; i < 1; i++)
	{
		sprintf(filebuffer, "0x280,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCFL_ActualValue1_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//MCFL_ActualValue2	0x284
uint8_t  MCFL_ActualValue2_Unpack(uint8_t *buf)
{
	#define  MCFL_ActualValue2_DLC  8
	#define  MCFL_ActualValue2_Length  (MCFL_ActualValue2_DLC+Package_Length)
	uint8_t DTU_Buffer[MCFL_ActualValue2_Length];
	uint8_t i = 0;

	char *SignalName32[] = {
		"MCFL_DiagnosticNum",
		"MCFL_ErrorInfo"};

	uint32_t SignalValue32[2] = {0};
		/*
		"MCFL_DiagnosticNum",
		"MCFL_ErrorInfo"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	MCFL_ActualValue2_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue32[0] = 0xffffffff&(buf[0]|(buf[1]<<8))|(buf[2]<<16))|(buf[3]<<24));//MCFL_DiagnosticNum
	SignalValue32[1] = 0xffffffff&(buf[4]|(buf[5]<<8))|(buf[6]<<16))|(buf[7]<<24));//MCFL_ErrorInfo
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x84;
	DTU_Buffer[2] = 0x2;
	DTU_Buffer[3] = MCFL_ActualValue2_DLC;

	DTU_Buffer[4] = (SignalValue32[0]&0xff);//MCFL_DiagnosticNum
	DTU_Buffer[5] = (SignalValue32[0]&0xff00)>>8;
	DTU_Buffer[6] = (SignalValue32[0]&0xff0000)>>16;
	DTU_Buffer[7] = (SignalValue32[0]&0xff000000)>>24;
	DTU_Buffer[8] = (SignalValue32[1]&0xff);//MCFL_ErrorInfo
	DTU_Buffer[9] = (SignalValue32[1]&0xff00)>>8;
	DTU_Buffer[10] = (SignalValue32[1]&0xff0000)>>16;
	DTU_Buffer[11] = (SignalValue32[1]&0xff000000)>>24;
	DTU_Buffer[MCFL_ActualValue2_Length - 2] = 0x0D;
	DTU_Buffer[MCFL_ActualValue2_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < MCFL_ActualValue2_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 2; i++)
	{
		sprintf(filebuffer, "0x284,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName32[i], SignalValue32[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCFL_ActualValue2_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//MCFL_ActualValue3	0x288
uint8_t  MCFL_ActualValue3_Unpack(uint8_t *buf)
{
	#define  MCFL_ActualValue3_DLC  12
	#define  MCFL_ActualValue3_Length  (MCFL_ActualValue3_DLC+Package_Length)
	uint8_t DTU_Buffer[MCFL_ActualValue3_Length];
	uint8_t i = 0;

	char *SignalNamef[] = {
		"MCFL_TempMotor",
		"MCFL_TempInverter",
		"MCFL_TempIGBT"};

	float SignalValuef[3];//Signals with float value
		/*
		"MCFL_TempMotor",
		"MCFL_TempInverter",
		"MCFL_TempIGBT"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	MCFL_ActualValue3_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValuef[0] = (0xffff&(buf[0]|(buf[1]<<8))) * 0.1;
	SignalValuef[1] = (0xffff&(buf[2]|(buf[3]<<8))) * 0.1;
	SignalValuef[2] = (0xffff&(buf[4]|(buf[5]<<8))) * 0.1;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x88;
	DTU_Buffer[2] = 0x2;
	DTU_Buffer[3] = MCFL_ActualValue3_DLC;

	DTU_Buffer[4+i] = ((uchar *)SignalValuef[0])[0];//MCFL_TempMotor
	DTU_Buffer[5+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[6+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[7+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[1])[0];//MCFL_TempInverter
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[2])[0];//MCFL_TempIGBT
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[MCFL_ActualValue3_Length - 2] = 0x0D;
	DTU_Buffer[MCFL_ActualValue3_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < MCFL_ActualValue3_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 3; i++)
	{
		sprintf(filebuffer, "0x288,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCFL_ActualValue3_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//MCFR_ActualValue1	0x281
uint8_t  MCFR_ActualValue1_Unpack(uint8_t *buf)
{
	#define  MCFR_ActualValue1_DLC  17
	#define  MCFR_ActualValue1_Length  (MCFR_ActualValue1_DLC+Package_Length)
	uint8_t DTU_Buffer[MCFR_ActualValue1_Length];
	uint8_t i = 0;

	char *SignalName8[] = {
		"MCFR_bReverse",
		"MCFR_bSystemReady",
		"MCFR_bError",
		"MCFR_bWarn",
		"MCFR_bQuitDCOn",
		"MCFR_bDCOn",
		"MCFR_bQuitInverterOn",
		"MCFR_bInverterOn",
		"MCFR_bDerating"};
	char *SignalName16[] = {
		"MCFR_DCVoltage",
		"MCFR_ActualVelocity"};

	char *SignalNamef[] = {
		"MCFR_ActualTorque"};

	uint8_t SignalValue8[9] = {0};
		/*
		"MCFR_bReverse",
		"MCFR_bSystemReady",
		"MCFR_bError",
		"MCFR_bWarn",
		"MCFR_bQuitDCOn",
		"MCFR_bDCOn",
		"MCFR_bQuitInverterOn",
		"MCFR_bInverterOn",
		"MCFR_bDerating"
		*/
	uint16_t SignalValue16[2] = {0};
		/*
		"MCFR_DCVoltage",
		"MCFR_ActualVelocity"
		*/
	float SignalValuef[1];//Signals with float value
		/*
		"MCFR_ActualTorque"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	MCFR_ActualValue1_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue8[0] = 0xff&buf[0];//MCFR_bReverse
	SignalValue8[1] = 0x1&buf[1];//MCFR_bSystemReady
	SignalValue8[2] = (0x2&buf[1])>>1;//MCFR_bError
	SignalValue8[3] = (0x4&buf[1])>>2;//MCFR_bWarn
	SignalValue8[4] = (0x8&buf[1])>>3;//MCFR_bQuitDCOn
	SignalValue8[5] = (0x10&buf[1])>>4;//MCFR_bDCOn
	SignalValue8[6] = (0x20&buf[1])>>5;//MCFR_bQuitInverterOn
	SignalValue8[7] = (0x40&buf[1])>>6;//MCFR_bInverterOn
	SignalValue8[8] = (0x80&buf[1])>>7;//MCFR_bDerating
	SignalValue16[0] = 0xffff&(buf[2]|(buf[3]<<8));//MCFR_DCVoltage
	SignalValue16[1] = 0xffff&(buf[6]|(buf[7]<<8));//MCFR_ActualVelocity
	SignalValuef[0] = (0xffff&(buf[4]|(buf[5]<<8))) * 0.0098;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x81;
	DTU_Buffer[2] = 0x2;
	DTU_Buffer[3] = MCFR_ActualValue1_DLC;

	DTU_Buffer[4] = SignalValue8[0];//MCFR_bReverse
	DTU_Buffer[5] = SignalValue8[1];//MCFR_bSystemReady
	DTU_Buffer[6] = SignalValue8[2];//MCFR_bError
	DTU_Buffer[7] = SignalValue8[3];//MCFR_bWarn
	DTU_Buffer[8] = SignalValue8[4];//MCFR_bQuitDCOn
	DTU_Buffer[9] = SignalValue8[5];//MCFR_bDCOn
	DTU_Buffer[10] = SignalValue8[6];//MCFR_bQuitInverterOn
	DTU_Buffer[11] = SignalValue8[7];//MCFR_bInverterOn
	DTU_Buffer[12] = SignalValue8[8];//MCFR_bDerating
	DTU_Buffer[13] = (SignalValue16[0]&0xff);//MCFR_DCVoltage
	DTU_Buffer[14] = (SignalValue16[0]&0xff00)>>8;
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[0])[0];//MCFR_ActualTorque
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[18+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[19] = (SignalValue16[1]&0xff);//MCFR_ActualVelocity
	DTU_Buffer[20] = (SignalValue16[1]&0xff00)>>8;
	DTU_Buffer[MCFR_ActualValue1_Length - 2] = 0x0D;
	DTU_Buffer[MCFR_ActualValue1_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < MCFR_ActualValue1_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 9; i++)
	{
		sprintf(filebuffer, "0x281,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName8[i], SignalValue8[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCFR_ActualValue1_Counter);
		f_puts(filebuffer, file);
	}
	for(i = 0; i < 2; i++)
	{
		sprintf(filebuffer, "0x281,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName16[i], SignalValue16[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCFR_ActualValue1_Counter);
		f_puts(filebuffer, file);
	}
	for(i = 0; i < 1; i++)
	{
		sprintf(filebuffer, "0x281,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCFR_ActualValue1_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//MCFR_ActualValue2	0x285
uint8_t  MCFR_ActualValue2_Unpack(uint8_t *buf)
{
	#define  MCFR_ActualValue2_DLC  8
	#define  MCFR_ActualValue2_Length  (MCFR_ActualValue2_DLC+Package_Length)
	uint8_t DTU_Buffer[MCFR_ActualValue2_Length];
	uint8_t i = 0;

	char *SignalName32[] = {
		"MCFR_DiagnosticNum",
		"MCFR_ErrorInfo"};

	uint32_t SignalValue32[2] = {0};
		/*
		"MCFR_DiagnosticNum",
		"MCFR_ErrorInfo"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	MCFR_ActualValue2_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue32[0] = 0xffffffff&(buf[0]|(buf[1]<<8))|(buf[2]<<16))|(buf[3]<<24));//MCFR_DiagnosticNum
	SignalValue32[1] = 0xffffffff&(buf[4]|(buf[5]<<8))|(buf[6]<<16))|(buf[7]<<24));//MCFR_ErrorInfo
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x85;
	DTU_Buffer[2] = 0x2;
	DTU_Buffer[3] = MCFR_ActualValue2_DLC;

	DTU_Buffer[4] = (SignalValue32[0]&0xff);//MCFR_DiagnosticNum
	DTU_Buffer[5] = (SignalValue32[0]&0xff00)>>8;
	DTU_Buffer[6] = (SignalValue32[0]&0xff0000)>>16;
	DTU_Buffer[7] = (SignalValue32[0]&0xff000000)>>24;
	DTU_Buffer[8] = (SignalValue32[1]&0xff);//MCFR_ErrorInfo
	DTU_Buffer[9] = (SignalValue32[1]&0xff00)>>8;
	DTU_Buffer[10] = (SignalValue32[1]&0xff0000)>>16;
	DTU_Buffer[11] = (SignalValue32[1]&0xff000000)>>24;
	DTU_Buffer[MCFR_ActualValue2_Length - 2] = 0x0D;
	DTU_Buffer[MCFR_ActualValue2_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < MCFR_ActualValue2_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 2; i++)
	{
		sprintf(filebuffer, "0x285,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName32[i], SignalValue32[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCFR_ActualValue2_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//MCFR_ActualValue3	0x289
uint8_t  MCFR_ActualValue3_Unpack(uint8_t *buf)
{
	#define  MCFR_ActualValue3_DLC  12
	#define  MCFR_ActualValue3_Length  (MCFR_ActualValue3_DLC+Package_Length)
	uint8_t DTU_Buffer[MCFR_ActualValue3_Length];
	uint8_t i = 0;

	char *SignalNamef[] = {
		"MCFR_TempMotor",
		"MCFR_TempInverter",
		"MCFR_TempIGBT"};

	float SignalValuef[3];//Signals with float value
		/*
		"MCFR_TempMotor",
		"MCFR_TempInverter",
		"MCFR_TempIGBT"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	MCFR_ActualValue3_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValuef[0] = (0xffff&(buf[0]|(buf[1]<<8))) * 0.1;
	SignalValuef[1] = (0xffff&(buf[2]|(buf[3]<<8))) * 0.1;
	SignalValuef[2] = (0xffff&(buf[4]|(buf[5]<<8))) * 0.1;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x89;
	DTU_Buffer[2] = 0x2;
	DTU_Buffer[3] = MCFR_ActualValue3_DLC;

	DTU_Buffer[4+i] = ((uchar *)SignalValuef[0])[0];//MCFR_TempMotor
	DTU_Buffer[5+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[6+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[7+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[1])[0];//MCFR_TempInverter
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[2])[0];//MCFR_TempIGBT
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[MCFR_ActualValue3_Length - 2] = 0x0D;
	DTU_Buffer[MCFR_ActualValue3_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < MCFR_ActualValue3_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 3; i++)
	{
		sprintf(filebuffer, "0x289,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCFR_ActualValue3_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//MCRL_SetPoints	0X184
uint8_t  MCRL_SetPoints_Unpack(uint8_t *buf)
{
	#define  MCRL_SetPoints_DLC  16
	#define  MCRL_SetPoints_Length  (MCRL_SetPoints_DLC+Package_Length)
	uint8_t DTU_Buffer[MCRL_SetPoints_Length];
	uint8_t i = 0;

	char *SignalName8[] = {
		"MCRL_cInverterOn",
		"MCRL_cDCOn",
		"MCRL_cEnable",
		"MCRL_cErrorReset"};
	char *SignalNamef[] = {
		"MCRL_TargetTorque",
		"MCRL_TorqueLimitP",
		"MCRL_TorqueLimitN"};

	uint8_t SignalValue8[4] = {0};
		/*
		"MCRL_cInverterOn",
		"MCRL_cDCOn",
		"MCRL_cEnable",
		"MCRL_cErrorReset"
		*/
	float SignalValuef[3];//Signals with float value
		/*
		"MCRL_TargetTorque",
		"MCRL_TorqueLimitP",
		"MCRL_TorqueLimitN"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	MCRL_SetPoints_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue8[0] = 0x1&buf[1];//MCRL_cInverterOn
	SignalValue8[1] = (0x2&buf[1])>>1;//MCRL_cDCOn
	SignalValue8[2] = (0x4&buf[1])>>2;//MCRL_cEnable
	SignalValue8[3] = (0x8&buf[1])>>3;//MCRL_cErrorReset
	SignalValuef[0] = (0xffff&(buf[2]|(buf[3]<<8))) * 0.0098;
	SignalValuef[1] = (0xffff&(buf[4]|(buf[5]<<8))) * 0.0098;
	SignalValuef[2] = (0xffff&(buf[6]|(buf[7]<<8))) * 0.0098;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x84;
	DTU_Buffer[2] = 0x1;
	DTU_Buffer[3] = MCRL_SetPoints_DLC;

	DTU_Buffer[4] = SignalValue8[0];//MCRL_cInverterOn
	DTU_Buffer[5] = SignalValue8[1];//MCRL_cDCOn
	DTU_Buffer[6] = SignalValue8[2];//MCRL_cEnable
	DTU_Buffer[7] = SignalValue8[3];//MCRL_cErrorReset
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[0])[0];//MCRL_TargetTorque
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[1])[0];//MCRL_TorqueLimitP
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[2])[0];//MCRL_TorqueLimitN
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[18+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[19+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[MCRL_SetPoints_Length - 2] = 0x0D;
	DTU_Buffer[MCRL_SetPoints_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < MCRL_SetPoints_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 4; i++)
	{
		sprintf(filebuffer, "0X184,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName8[i], SignalValue8[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCRL_SetPoints_Counter);
		f_puts(filebuffer, file);
	}
	for(i = 0; i < 3; i++)
	{
		sprintf(filebuffer, "0X184,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCRL_SetPoints_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//MCRR_SetPoints	0X185
uint8_t  MCRR_SetPoints_Unpack(uint8_t *buf)
{
	#define  MCRR_SetPoints_DLC  16
	#define  MCRR_SetPoints_Length  (MCRR_SetPoints_DLC+Package_Length)
	uint8_t DTU_Buffer[MCRR_SetPoints_Length];
	uint8_t i = 0;

	char *SignalName8[] = {
		"MCRR_cInverterOn",
		"MCRR_cDCOn",
		"MCRR_cEnable",
		"MCRR_cErrorReset"};
	char *SignalNamef[] = {
		"MCRR_TargetTorque",
		"MCRR_TorqueLimitP",
		"MCRR_TorqueLimitN"};

	uint8_t SignalValue8[4] = {0};
		/*
		"MCRR_cInverterOn",
		"MCRR_cDCOn",
		"MCRR_cEnable",
		"MCRR_cErrorReset"
		*/
	float SignalValuef[3];//Signals with float value
		/*
		"MCRR_TargetTorque",
		"MCRR_TorqueLimitP",
		"MCRR_TorqueLimitN"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	MCRR_SetPoints_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue8[0] = 0x1&buf[1];//MCRR_cInverterOn
	SignalValue8[1] = (0x2&buf[1])>>1;//MCRR_cDCOn
	SignalValue8[2] = (0x4&buf[1])>>2;//MCRR_cEnable
	SignalValue8[3] = (0x8&buf[1])>>3;//MCRR_cErrorReset
	SignalValuef[0] = (0xffff&(buf[2]|(buf[3]<<8))) * 0.0098;
	SignalValuef[1] = (0xffff&(buf[4]|(buf[5]<<8))) * 0.0098;
	SignalValuef[2] = (0xffff&(buf[6]|(buf[7]<<8))) * 0.0098;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x85;
	DTU_Buffer[2] = 0x1;
	DTU_Buffer[3] = MCRR_SetPoints_DLC;

	DTU_Buffer[4] = SignalValue8[0];//MCRR_cInverterOn
	DTU_Buffer[5] = SignalValue8[1];//MCRR_cDCOn
	DTU_Buffer[6] = SignalValue8[2];//MCRR_cEnable
	DTU_Buffer[7] = SignalValue8[3];//MCRR_cErrorReset
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[0])[0];//MCRR_TargetTorque
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[1])[0];//MCRR_TorqueLimitP
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[2])[0];//MCRR_TorqueLimitN
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[18+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[19+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[MCRR_SetPoints_Length - 2] = 0x0D;
	DTU_Buffer[MCRR_SetPoints_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < MCRR_SetPoints_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 4; i++)
	{
		sprintf(filebuffer, "0X185,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName8[i], SignalValue8[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCRR_SetPoints_Counter);
		f_puts(filebuffer, file);
	}
	for(i = 0; i < 3; i++)
	{
		sprintf(filebuffer, "0X185,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCRR_SetPoints_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//MCRL_ActualValue1	0x282
uint8_t  MCRL_ActualValue1_Unpack(uint8_t *buf)
{
	#define  MCRL_ActualValue1_DLC  17
	#define  MCRL_ActualValue1_Length  (MCRL_ActualValue1_DLC+Package_Length)
	uint8_t DTU_Buffer[MCRL_ActualValue1_Length];
	uint8_t i = 0;

	char *SignalName8[] = {
		"MCRL_bReverse",
		"MCRL_bSystemReady",
		"MCRL_bError",
		"MCRL_bWarn",
		"MCRL_bQuitDCOn",
		"MCRL_bDCOn",
		"MCRL_bQuitInverterOn",
		"MCRL_bInverterOn",
		"MCRL_bDerating"};
	char *SignalName16[] = {
		"MCRL_DCVoltage",
		"MCRL_ActualVelocity"};

	char *SignalNamef[] = {
		"MCRL_ActualTorque"};

	uint8_t SignalValue8[9] = {0};
		/*
		"MCRL_bReverse",
		"MCRL_bSystemReady",
		"MCRL_bError",
		"MCRL_bWarn",
		"MCRL_bQuitDCOn",
		"MCRL_bDCOn",
		"MCRL_bQuitInverterOn",
		"MCRL_bInverterOn",
		"MCRL_bDerating"
		*/
	uint16_t SignalValue16[2] = {0};
		/*
		"MCRL_DCVoltage",
		"MCRL_ActualVelocity"
		*/
	float SignalValuef[1];//Signals with float value
		/*
		"MCRL_ActualTorque"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	MCRL_ActualValue1_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue8[0] = 0xff&buf[0];//MCRL_bReverse
	SignalValue8[1] = 0x1&buf[1];//MCRL_bSystemReady
	SignalValue8[2] = (0x2&buf[1])>>1;//MCRL_bError
	SignalValue8[3] = (0x4&buf[1])>>2;//MCRL_bWarn
	SignalValue8[4] = (0x8&buf[1])>>3;//MCRL_bQuitDCOn
	SignalValue8[5] = (0x10&buf[1])>>4;//MCRL_bDCOn
	SignalValue8[6] = (0x20&buf[1])>>5;//MCRL_bQuitInverterOn
	SignalValue8[7] = (0x40&buf[1])>>6;//MCRL_bInverterOn
	SignalValue8[8] = (0x80&buf[1])>>7;//MCRL_bDerating
	SignalValue16[0] = 0xffff&(buf[2]|(buf[3]<<8));//MCRL_DCVoltage
	SignalValue16[1] = 0xffff&(buf[6]|(buf[7]<<8));//MCRL_ActualVelocity
	SignalValuef[0] = (0xffff&(buf[4]|(buf[5]<<8))) * 0.0098;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x82;
	DTU_Buffer[2] = 0x2;
	DTU_Buffer[3] = MCRL_ActualValue1_DLC;

	DTU_Buffer[4] = SignalValue8[0];//MCRL_bReverse
	DTU_Buffer[5] = SignalValue8[1];//MCRL_bSystemReady
	DTU_Buffer[6] = SignalValue8[2];//MCRL_bError
	DTU_Buffer[7] = SignalValue8[3];//MCRL_bWarn
	DTU_Buffer[8] = SignalValue8[4];//MCRL_bQuitDCOn
	DTU_Buffer[9] = SignalValue8[5];//MCRL_bDCOn
	DTU_Buffer[10] = SignalValue8[6];//MCRL_bQuitInverterOn
	DTU_Buffer[11] = SignalValue8[7];//MCRL_bInverterOn
	DTU_Buffer[12] = SignalValue8[8];//MCRL_bDerating
	DTU_Buffer[13] = (SignalValue16[0]&0xff);//MCRL_DCVoltage
	DTU_Buffer[14] = (SignalValue16[0]&0xff00)>>8;
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[0])[0];//MCRL_ActualTorque
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[18+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[19] = (SignalValue16[1]&0xff);//MCRL_ActualVelocity
	DTU_Buffer[20] = (SignalValue16[1]&0xff00)>>8;
	DTU_Buffer[MCRL_ActualValue1_Length - 2] = 0x0D;
	DTU_Buffer[MCRL_ActualValue1_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < MCRL_ActualValue1_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 9; i++)
	{
		sprintf(filebuffer, "0x282,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName8[i], SignalValue8[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCRL_ActualValue1_Counter);
		f_puts(filebuffer, file);
	}
	for(i = 0; i < 2; i++)
	{
		sprintf(filebuffer, "0x282,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName16[i], SignalValue16[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCRL_ActualValue1_Counter);
		f_puts(filebuffer, file);
	}
	for(i = 0; i < 1; i++)
	{
		sprintf(filebuffer, "0x282,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCRL_ActualValue1_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//MCRL_ActualValue2	0x286
uint8_t  MCRL_ActualValue2_Unpack(uint8_t *buf)
{
	#define  MCRL_ActualValue2_DLC  8
	#define  MCRL_ActualValue2_Length  (MCRL_ActualValue2_DLC+Package_Length)
	uint8_t DTU_Buffer[MCRL_ActualValue2_Length];
	uint8_t i = 0;

	char *SignalName32[] = {
		"MCRL_DiagnosticNum",
		"MCRL_ErrorInfo"};

	uint32_t SignalValue32[2] = {0};
		/*
		"MCRL_DiagnosticNum",
		"MCRL_ErrorInfo"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	MCRL_ActualValue2_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue32[0] = 0xffffffff&(buf[0]|(buf[1]<<8))|(buf[2]<<16))|(buf[3]<<24));//MCRL_DiagnosticNum
	SignalValue32[1] = 0xffffffff&(buf[4]|(buf[5]<<8))|(buf[6]<<16))|(buf[7]<<24));//MCRL_ErrorInfo
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x86;
	DTU_Buffer[2] = 0x2;
	DTU_Buffer[3] = MCRL_ActualValue2_DLC;

	DTU_Buffer[4] = (SignalValue32[0]&0xff);//MCRL_DiagnosticNum
	DTU_Buffer[5] = (SignalValue32[0]&0xff00)>>8;
	DTU_Buffer[6] = (SignalValue32[0]&0xff0000)>>16;
	DTU_Buffer[7] = (SignalValue32[0]&0xff000000)>>24;
	DTU_Buffer[8] = (SignalValue32[1]&0xff);//MCRL_ErrorInfo
	DTU_Buffer[9] = (SignalValue32[1]&0xff00)>>8;
	DTU_Buffer[10] = (SignalValue32[1]&0xff0000)>>16;
	DTU_Buffer[11] = (SignalValue32[1]&0xff000000)>>24;
	DTU_Buffer[MCRL_ActualValue2_Length - 2] = 0x0D;
	DTU_Buffer[MCRL_ActualValue2_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < MCRL_ActualValue2_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 2; i++)
	{
		sprintf(filebuffer, "0x286,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName32[i], SignalValue32[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCRL_ActualValue2_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//MCRL_ActualValue3	0x28A
uint8_t  MCRL_ActualValue3_Unpack(uint8_t *buf)
{
	#define  MCRL_ActualValue3_DLC  12
	#define  MCRL_ActualValue3_Length  (MCRL_ActualValue3_DLC+Package_Length)
	uint8_t DTU_Buffer[MCRL_ActualValue3_Length];
	uint8_t i = 0;

	char *SignalNamef[] = {
		"MCRL_TempMotor",
		"MCRL_TempInverter",
		"MCRL_TempIGBT"};

	float SignalValuef[3];//Signals with float value
		/*
		"MCRL_TempMotor",
		"MCRL_TempInverter",
		"MCRL_TempIGBT"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	MCRL_ActualValue3_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValuef[0] = (0xffff&(buf[0]|(buf[1]<<8))) * 0.1;
	SignalValuef[1] = (0xffff&(buf[2]|(buf[3]<<8))) * 0.1;
	SignalValuef[2] = (0xffff&(buf[4]|(buf[5]<<8))) * 0.1;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x8a;
	DTU_Buffer[2] = 0x2;
	DTU_Buffer[3] = MCRL_ActualValue3_DLC;

	DTU_Buffer[4+i] = ((uchar *)SignalValuef[0])[0];//MCRL_TempMotor
	DTU_Buffer[5+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[6+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[7+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[1])[0];//MCRL_TempInverter
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[2])[0];//MCRL_TempIGBT
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[MCRL_ActualValue3_Length - 2] = 0x0D;
	DTU_Buffer[MCRL_ActualValue3_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < MCRL_ActualValue3_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 3; i++)
	{
		sprintf(filebuffer, "0x28A,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCRL_ActualValue3_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//MCRR_ActualValue1	0x283
uint8_t  MCRR_ActualValue1_Unpack(uint8_t *buf)
{
	#define  MCRR_ActualValue1_DLC  17
	#define  MCRR_ActualValue1_Length  (MCRR_ActualValue1_DLC+Package_Length)
	uint8_t DTU_Buffer[MCRR_ActualValue1_Length];
	uint8_t i = 0;

	char *SignalName8[] = {
		"MCRR_bReverse",
		"MCRR_bSystemReady",
		"MCRR_bError",
		"MCRR_bWarn",
		"MCRR_bQuitDCOn",
		"MCRR_bDCOn",
		"MCRR_bQuitInverterOn",
		"MCRR_bInverterOn",
		"MCRR_bDerating"};
	char *SignalName16[] = {
		"MCRR_DCVoltage",
		"MCRR_ActualVelocity"};

	char *SignalNamef[] = {
		"MCRR_ActualTorque"};

	uint8_t SignalValue8[9] = {0};
		/*
		"MCRR_bReverse",
		"MCRR_bSystemReady",
		"MCRR_bError",
		"MCRR_bWarn",
		"MCRR_bQuitDCOn",
		"MCRR_bDCOn",
		"MCRR_bQuitInverterOn",
		"MCRR_bInverterOn",
		"MCRR_bDerating"
		*/
	uint16_t SignalValue16[2] = {0};
		/*
		"MCRR_DCVoltage",
		"MCRR_ActualVelocity"
		*/
	float SignalValuef[1];//Signals with float value
		/*
		"MCRR_ActualTorque"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	MCRR_ActualValue1_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue8[0] = 0xff&buf[0];//MCRR_bReverse
	SignalValue8[1] = 0x1&buf[1];//MCRR_bSystemReady
	SignalValue8[2] = (0x2&buf[1])>>1;//MCRR_bError
	SignalValue8[3] = (0x4&buf[1])>>2;//MCRR_bWarn
	SignalValue8[4] = (0x8&buf[1])>>3;//MCRR_bQuitDCOn
	SignalValue8[5] = (0x10&buf[1])>>4;//MCRR_bDCOn
	SignalValue8[6] = (0x20&buf[1])>>5;//MCRR_bQuitInverterOn
	SignalValue8[7] = (0x40&buf[1])>>6;//MCRR_bInverterOn
	SignalValue8[8] = (0x80&buf[1])>>7;//MCRR_bDerating
	SignalValue16[0] = 0xffff&(buf[2]|(buf[3]<<8));//MCRR_DCVoltage
	SignalValue16[1] = 0xffff&(buf[6]|(buf[7]<<8));//MCRR_ActualVelocity
	SignalValuef[0] = (0xffff&(buf[4]|(buf[5]<<8))) * 0.0098;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x83;
	DTU_Buffer[2] = 0x2;
	DTU_Buffer[3] = MCRR_ActualValue1_DLC;

	DTU_Buffer[4] = SignalValue8[0];//MCRR_bReverse
	DTU_Buffer[5] = SignalValue8[1];//MCRR_bSystemReady
	DTU_Buffer[6] = SignalValue8[2];//MCRR_bError
	DTU_Buffer[7] = SignalValue8[3];//MCRR_bWarn
	DTU_Buffer[8] = SignalValue8[4];//MCRR_bQuitDCOn
	DTU_Buffer[9] = SignalValue8[5];//MCRR_bDCOn
	DTU_Buffer[10] = SignalValue8[6];//MCRR_bQuitInverterOn
	DTU_Buffer[11] = SignalValue8[7];//MCRR_bInverterOn
	DTU_Buffer[12] = SignalValue8[8];//MCRR_bDerating
	DTU_Buffer[13] = (SignalValue16[0]&0xff);//MCRR_DCVoltage
	DTU_Buffer[14] = (SignalValue16[0]&0xff00)>>8;
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[0])[0];//MCRR_ActualTorque
	DTU_Buffer[16+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[17+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[18+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[19] = (SignalValue16[1]&0xff);//MCRR_ActualVelocity
	DTU_Buffer[20] = (SignalValue16[1]&0xff00)>>8;
	DTU_Buffer[MCRR_ActualValue1_Length - 2] = 0x0D;
	DTU_Buffer[MCRR_ActualValue1_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < MCRR_ActualValue1_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 9; i++)
	{
		sprintf(filebuffer, "0x283,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName8[i], SignalValue8[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCRR_ActualValue1_Counter);
		f_puts(filebuffer, file);
	}
	for(i = 0; i < 2; i++)
	{
		sprintf(filebuffer, "0x283,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName16[i], SignalValue16[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCRR_ActualValue1_Counter);
		f_puts(filebuffer, file);
	}
	for(i = 0; i < 1; i++)
	{
		sprintf(filebuffer, "0x283,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCRR_ActualValue1_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//MCRR_ActualValue2	0x287
uint8_t  MCRR_ActualValue2_Unpack(uint8_t *buf)
{
	#define  MCRR_ActualValue2_DLC  8
	#define  MCRR_ActualValue2_Length  (MCRR_ActualValue2_DLC+Package_Length)
	uint8_t DTU_Buffer[MCRR_ActualValue2_Length];
	uint8_t i = 0;

	char *SignalName32[] = {
		"MCRR_DiagnosticNum",
		"MCRR_ErrorInfo"};

	uint32_t SignalValue32[2] = {0};
		/*
		"MCRR_DiagnosticNum",
		"MCRR_ErrorInfo"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	MCRR_ActualValue2_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValue32[0] = 0xffffffff&(buf[0]|(buf[1]<<8))|(buf[2]<<16))|(buf[3]<<24));//MCRR_DiagnosticNum
	SignalValue32[1] = 0xffffffff&(buf[4]|(buf[5]<<8))|(buf[6]<<16))|(buf[7]<<24));//MCRR_ErrorInfo
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x87;
	DTU_Buffer[2] = 0x2;
	DTU_Buffer[3] = MCRR_ActualValue2_DLC;

	DTU_Buffer[4] = (SignalValue32[0]&0xff);//MCRR_DiagnosticNum
	DTU_Buffer[5] = (SignalValue32[0]&0xff00)>>8;
	DTU_Buffer[6] = (SignalValue32[0]&0xff0000)>>16;
	DTU_Buffer[7] = (SignalValue32[0]&0xff000000)>>24;
	DTU_Buffer[8] = (SignalValue32[1]&0xff);//MCRR_ErrorInfo
	DTU_Buffer[9] = (SignalValue32[1]&0xff00)>>8;
	DTU_Buffer[10] = (SignalValue32[1]&0xff0000)>>16;
	DTU_Buffer[11] = (SignalValue32[1]&0xff000000)>>24;
	DTU_Buffer[MCRR_ActualValue2_Length - 2] = 0x0D;
	DTU_Buffer[MCRR_ActualValue2_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < MCRR_ActualValue2_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 2; i++)
	{
		sprintf(filebuffer, "0x287,%s,%02d,%02d:%02d:%02d,%02d\r\n", SignalName32[i], SignalValue32[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCRR_ActualValue2_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}

/*******************************************************************/
//MCRR_ActualValue3	0x28B
uint8_t  MCRR_ActualValue3_Unpack(uint8_t *buf)
{
	#define  MCRR_ActualValue3_DLC  12
	#define  MCRR_ActualValue3_Length  (MCRR_ActualValue3_DLC+Package_Length)
	uint8_t DTU_Buffer[MCRR_ActualValue3_Length];
	uint8_t i = 0;

	char *SignalNamef[] = {
		"MCRR_TempMotor",
		"MCRR_TempInverter",
		"MCRR_TempIGBT"};

	float SignalValuef[3];//Signals with float value
		/*
		"MCRR_TempMotor",
		"MCRR_TempInverter",
		"MCRR_TempIGBT"
		*/
	TCHAR filebuffer[100];
	RTC_TimeTypeDef RTC_Time;
	MCRR_ActualValue3_Counter++;//帧计数

	//Unpack CAN signals from buf
	SignalValuef[0] = (0xffff&(buf[0]|(buf[1]<<8))) * 0.1;
	SignalValuef[1] = (0xffff&(buf[2]|(buf[3]<<8))) * 0.1;
	SignalValuef[2] = (0xffff&(buf[4]|(buf[5]<<8))) * 0.1;
	//装填DTU_Buffer
	//第一帧固定包头,第二第三帧分别装载ID低两位和高两位（按顺序）
	DTU_Buffer[0] = 0x3A;
	DTU_Buffer[1] = 0x8b;
	DTU_Buffer[2] = 0x2;
	DTU_Buffer[3] = MCRR_ActualValue3_DLC;

	DTU_Buffer[4+i] = ((uchar *)SignalValuef[0])[0];//MCRR_TempMotor
	DTU_Buffer[5+i] = ((uchar *)SignalValuef[0])[1];
	DTU_Buffer[6+i] = ((uchar *)SignalValuef[0])[2];
	DTU_Buffer[7+i] = ((uchar *)SignalValuef[0])[3];
	DTU_Buffer[8+i] = ((uchar *)SignalValuef[1])[0];//MCRR_TempInverter
	DTU_Buffer[9+i] = ((uchar *)SignalValuef[1])[1];
	DTU_Buffer[10+i] = ((uchar *)SignalValuef[1])[2];
	DTU_Buffer[11+i] = ((uchar *)SignalValuef[1])[3];
	DTU_Buffer[12+i] = ((uchar *)SignalValuef[2])[0];//MCRR_TempIGBT
	DTU_Buffer[13+i] = ((uchar *)SignalValuef[2])[1];
	DTU_Buffer[14+i] = ((uchar *)SignalValuef[2])[2];
	DTU_Buffer[15+i] = ((uchar *)SignalValuef[2])[3];
	DTU_Buffer[MCRR_ActualValue3_Length - 2] = 0x0D;
	DTU_Buffer[MCRR_ActualValue3_Length - 1] = 0x0A;

	//发送串口数据
	for(i = 0; i < MCRR_ActualValue3_Length; i++)
	{
		while(USART_GetFlagStatus(USART1,USART_FLAG_TC )==RESET);
		USART_SendData(USART1, DTU_Buffer[i]);
	}


	//获取当前时间
	RTC_GetTime(RTC_Format_BIN, &RTC_Time);
	//打开文件
	f_open(file, filename, FA_OPEN_ALWAYS|FA_WRITE);
	f_lseek(file, f_size(file));
	//写入数据
	for(i = 0; i < 3; i++)
	{
		sprintf(filebuffer, "0x28B,%s,%.2f,%02d:%02d:%02d,%02d\r\n", SignalNamef[i], SignalValuef[i], RTC_Time.RTC_Hours,RTC_Time.RTC_Minutes,RTC_Time.RTC_Seconds, MCRR_ActualValue3_Counter);
		f_puts(filebuffer, file);
	}
	//关闭文件
	return 0;
}


//////End of Unpack_Function//////

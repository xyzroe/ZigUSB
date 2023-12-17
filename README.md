ZigUSB was developed as a device that allows you to control and monitor the power of a device connected via USB.

Using this device, you can remotely control the power of the USB port to turn on or off the connected device. And also monitor the current voltage and current. And it's not a bad Zigbee network router.

Frequent use cases: converting a "stupid" USB lamp into a "smart" one; connecting modems / sticks / adapters, which sometimes require a power reset; monitoring the current consumption of any connected device.

Possibilities:
- Power on/off by push button and via Zigbee network.
- Automatic restart loop of the connected device with a single Zigbee command.
- Monitoring of voltage and current supplied to the connected device, INA219 chip.
- Setting the maximum USB current using a variable resistor on the board (1.0-3.2A)
- For power management, a MIC2545A USB switch chip is used.
- E18-MS1PA2-PCB (CC2530 with +20dBi amplifier) ​​was used as the Zigbee chip, which allows it to be used in remote places, and at the same time act as a good router for other devices.
- USB data transfer is available. This may be needed when connecting a USB modem to a router that does not know how to manage USB power, and the modem may need to be rebooted.
 - Designed for AK-N-12 case.


### Overview  
  
#### Touch version  
<div align="center">
<img width="20%" src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/top_touch.png">
<img width="20%" src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/bottom_touch.png">
</div>  

#### Button version  
<div align="center">
<img width="20%" src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/top.png">
<img width="20%" src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/bottom.png">
</div>

### Photos

#### Touch version  
<table>
<tr>
<td width="50%">
<img src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/top_case_touch.jpeg">
</td>
<td>
<img src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/back_case_touch.jpeg">
</td>
</tr>
<tr>
<td width="50%">
<img src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/top_pcb_touch.jpeg">
</td>
<td>
<img src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/back_pcb_touch.jpeg">
</td>
</tr>
</table>

#### Button version  
<table>
<tr>
<td width="50%">
<img src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/top_case.jpeg">
</td>
<td>
<img src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/back_case.jpeg">
</td>
</tr>
<tr>
<td width="50%">
<img src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/top_pcb.jpeg">
</td>
<td>
<img src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/back_pcb.jpeg">
</td>
</tr>
</table>





### Schematic
<div align="center"><img width="90%" src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/hardware/Schematic_ZigUSB.png"></div>
<div align="center"><img width="90%" src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/hardware/Schematic_ZigUSB_touch.png"></div>




### PTVO Config 

#### Touch version  
<div align="center"><img width="70%" src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/ptvo_1_touch.png"></div>  

#### Button version  
<div align="center"><img width="70%" src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/ptvo_1.png"></div>  

  
#### zigbee2mqtt & Home Assistant overview

<div align="center">

</div>


<table>
<tbody>
<tr>
<td><img width="50%" src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/z2m_device.png"></td>
<td rowspan="2"><img src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/ha.png"></td>
</tr>
<tr>
<td><img width="70%" src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/z2m_exposes.png"></td>
</tr>
</tbody>
</table>

### Hardware files

#### Touch version  
[Gerber](https://raw.githubusercontent.com/xyzroe/ZigUSB/main/hardware/Gerber_ZigUSB_touch.zip)  
[BOM](https://raw.githubusercontent.com/xyzroe/ZigUSB/main/hardware/BOM_ZigUSB_touch.csv)  or  [iBOM](https://xyzroe.cc/ZigUSB/hardware/iBOM_ZigUSB_touch.html)  🚀

#### Button version  
[Gerber](https://raw.githubusercontent.com/xyzroe/ZigUSB/main/hardware/Gerber_ZigUSB.zip)  
[BOM](https://raw.githubusercontent.com/xyzroe/ZigUSB/main/hardware/BOM_ZigUSB.csv)  or  [iBOM](https://xyzroe.cc/ZigUSB/hardware/zigbee_usb_power_switch_final_rev0.html)  🚀

### Firmware files
[NEW z2m external converter](https://github.com/xyzroe/ZigUSB/tree/main/firmware/ZigUSB_updated.js)
[OLD z2m external converter](https://github.com/xyzroe/ZigUSB/tree/main/firmware/ZigUSB.js)
  
[All FW .hex, PTVO .ini, .txt and converter .js files](https://github.com/xyzroe/ZigUSB/tree/main/firmware)  

### Where to buy?  
Tindie stopped supporting shipments from Ukraine, so now you can only buy on my partners’ website (shipping worldwide)  
  
<a href="https://mind.in.ua/"><img src="https://static.tildacdn.com/tild3433-3934-4565-b362-386238366331/logo_full.png" alt="Go to mind.in.ua" height="120"></a>


### Like ♥️?
[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/xyzroe)

<br>  

[![Made in Ukraine](https://img.shields.io/badge/made_in-ukraine-ffd700.svg?labelColor=0057b7)](https://stand-with-ukraine.pp.ua)  


### Inspired by
1. The original project of USB switch by [Kasito](https://kasito.ru/zigbee-vyklyuchatel-usb-nagruzki/)
2. Zigbee configurable firmware [PTVO](https://ptvo.info) 

<br>  
ZigUSB is licensed under the

[GNU General Public License v3.0](https://raw.githubusercontent.com/xyzroe/ZigUSB/main/LICENSE)

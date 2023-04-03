ZigUSB was developed as a device that allows you to control and monitor the power of a device connected via USB.

Options available:
 - Power on/off at the push of a button and via Zigbee network.
 - Automatic restart cycle of the connected device using one Zigbee command.
 - Monitoring of voltage and current supplied to the connected device via USB.
 - Setting the maximum USB current using a variable resistor on the board.
 - As Zigbee chip was used E18-MS1PA2-PCB (CC2530 with an amplifier), which allows it to be used in remote places, and at the same time act as a good router for other devices.
 - Designed to use AK-N-12 case.


### Overview

<div align="center">
<img width="20%" src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/top.png">
<img width="20%" src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/bottom.png">
</div>

### Photos
<table>
<tr>
<td width="50%">
<img src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/top_case.jpg">
</td>
<td>
<img src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/back_case.jpg">
</td>
</tr>
<tr>
<td width="50%">
<img src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/top_pcb.jpg">
</td>
<td>
<img src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/images/back_pcb.jpg">
</td>
</tr>
</table>





### Schematic
<div align="center"><img width="90%" src="https://raw.githubusercontent.com/xyzroe/ZigUSB/main/hardware/Schematic_ZigUSB.png"></div>




### PTVO Config 
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
[Gerber](https://raw.githubusercontent.com/xyzroe/ZigUSB/main/hardware/Gerber_ZigUSB.zip)  
[BOM](https://raw.githubusercontent.com/xyzroe/ZigUSB/main/hardware/BOM_ZigUSB.csv)  

### Firmware files
[FW .hex and converter .js files](https://github.com/xyzroe/ZigUSB/tree/main/firmware)  
[PTVO .ini file](https://raw.githubusercontent.com/xyzroe/ZigUSB/main/firmware/ZigUSB.ini)  
[PTVO .txt file](https://raw.githubusercontent.com/xyzroe/ZigUSB/main/firmware/ZigUSB.txt)  

### Where to buy?

<a href="https://www.tindie.com/stores/mind/?ref=offsite_badges&utm_source=sellers_xyzroe&utm_medium=badges&utm_campaign=badge_large"><img src="https://d2ss6ovg47m0r5.cloudfront.net/badges/tindie-larges.png" alt="I sell on Tindie" height="120"></a>

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
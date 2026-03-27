# Macrie

## Overview
This project is a custom macro pad with custom RP2040 MCU :)). It combines a fully designed CAD model, electronics, and firmware into a nice project (i think). The design includesenclosure, PCB, and hardware.

## Why I Made This
It looks like Ai but i really want to tel about it ;p
I started this project because I wanted to better understand combining MCU'S with other things, and i can focus on cad or writing filmware

## Features
- Just macropad ;)

## 3D Model
<img width="1920" height="1080" alt="RENDER" src="https://github.com/user-attachments/assets/34ac93e1-5292-425c-a477-f4631a573645" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9b5e7f92-55c3-4a26-8ac6-6e74eebefb68" />
READ THAT!!! : You can ask where the cover is. I didn’t add it even though there are mounting holes in the enclosure. I decided not to create a cover because I want to show the project to others without having to take anything off. I know it’s a bit unusual, but that’s the idea... I prefer to present it from a more technical side :).




## PCB

<img width="539" height="638" alt="image" src="https://github.com/user-attachments/assets/789046c0-60b7-4c88-8d97-fee9b66dedfa" />
<img width="506" height="557" alt="image" src="https://github.com/user-attachments/assets/1bcb1863-9dc6-4d53-ae0f-4b1b6e0af551" />


ERRORS

THEY ARE JUST TERMICAL SO CHILL - it won't burn
<img width="740" height="191" alt="image" src="https://github.com/user-attachments/assets/97226c06-39e6-4d84-b96f-85ff779d8189" />

## Wiring Diagram
<img width="1144" height="786" alt="image" src="https://github.com/user-attachments/assets/a078f9f1-01ca-4da8-8aaf-e118e07a89e1" />


## Files Included
This repository contains everything needed to review and reproduce the project:

- `/CAD` – source CAD files and exported STEP model
- `/hardware` – PCB design files and gerbers
- `/Firmware` – take a guess
- `BOM.csv` – bill of materials with links



## How to flash RP2040
You dont have to do anything. use circutpython to flash macropad code and pray it will work. you dont have to do anything. you just flash code using USBC

## Bill of Materials

## BOM

| Name | Purpose | Quantity | Total Cost (USD) | Link | Distributor |
|------|--------|----------|------------------|------|-------------|
| PCB | PCB (i can't send link for PCB for JLCPCB) | 5 | 2.00 | https://plainraw.com/raw/e9d4483de526 | JLCPCB |
| 5.1kΩ ±1% 125mW | Resistor CC1/CC2 | 100 | 0.24 | https://www.lcsc.com/product-detail/C27834.html | LCSC |
| 27Ω ±0.25% 100mW Resistor | Impedance Match | 10 | 0.36 | https://www.lcsc.com/product-detail/C5266071.html | LCSC |
| Crystal 12MHz | Crystal for stable MCU operation | 5 | 1.18 | https://www.lcsc.com/product-detail/C2901628.html | LCSC |
| W25Q128JVSIM TR | Flash memory | 1 | 3.58 | https://www.lcsc.com/product-detail/C401671.html | LCSC |
| AMS1117-3.3 | 5V to 3.3V regulator | 5 | 1.13 | https://www.lcsc.com/product-detail/C6186.html | LCSC |
| C2040 | MCU | 1 | 0.95 | https://www.lcsc.com/product-detail/C2040.html | LCSC |
| 1kΩ 125mW 150V Resistor | Resistor for crystal | 100 | 0.25 | https://www.lcsc.com/product-detail/C95781.html | LCSC |
| USB-C | USB-C for power and data | 5 | 0.92 | https://www.lcsc.com/product-detail/C165948.html | LCSC |
| 10uF ±10% 50V Ceramic Capacitor | Used around AMS1117-3.3 | 5 | 0.24 | https://www.lcsc.com/product-detail/C2932476.html | LCSC |
| 18pF ±5% 50V Ceramic Capacitor | Used with crystal | 100 | 0.67 | https://www.lcsc.com/product-detail/C113825.html | LCSC |
| 100nF ±10% 50V Ceramic Capacitor X7R 0805 | Decoupling capacitors | 50 | 0.31 | https://www.lcsc.com/product-detail/C1711.html | LCSC |
| 1uF ±10% 50V Ceramic Capacitor | Decoupling capacitors | 20 | 0.28 | https://www.lcsc.com/product-detail/C28323.html | LCSC |

You can use this all. dont forget to star my work :))

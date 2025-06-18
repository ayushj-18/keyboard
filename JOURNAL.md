---
title: "The Procastinate Board"
author: "Ayush Jaiswal"
description: "Making this personal keyboard so that I don't procastinate making a keyboard later on"
created_at: "2025-06-12"
---

# Project Idea/Inspo

I really wanted to make a keyboard to just gain insights on how electronics like keyboards work. After doing the hackpad, I got inspired to make a full keyboard looking at the keyboards other members made. Welp how hard can it be :smile:

Inspo- https://www.montechpc.com/mkey-tkl

Total time spent: 29h 

# Day 1: June 12th, 2025

## Time Spent: 2h
Started the schematic and spent time deciding my keyboard schematic. It will be a TKL keyboard with a rotary encoder.
Made a matrix on MS Paint to understand how the basic structure of my PCB and firmware will be. Watched some videos on how keyboards work.

![image](https://github.com/user-attachments/assets/78e52dfd-f240-4533-a118-3dcbde5f10cd)


# Day 2: June 13th, 2025

## Time Spent: 1h+7h 
Literally spent the entire day researching, asking people questions in slack (i love everyone is so helpful) and I basically completed the entire schematic and assigned all footprints. Made a basic draft of my BOM and thats about it. 
I did struggle so much on figuring out how microcontrollers work and which one will I need. I also had a hard time assigning footprints but I pulled through. 
My goal for tomorrow will definitly be to make the PCB and start the 3D modeling.

![image](https://github.com/user-attachments/assets/6dbeb918-e56a-4f57-acaf-ed31cbed7eef)

# Day 3: June 14th, 2025

## Time Spent: 1h+8h
Ok so I made the entire PCB, which took the entirety of the 8h of the day. I forgot one crucial thing, which was to add a 0.1uf capacitor after every rgb. Hope my entire project doesn't get rejected for this, I burnt 8 hours into this and forgot something :sob:. Anyways, I am pretty sure I won't be running the craziest animations out there, so I hope it won't be an issue. Here's the 3d view and the PCB. 

![image](https://github.com/user-attachments/assets/a60f2909-a369-43c4-8306-4323ec5364b6)
![image](https://github.com/user-attachments/assets/72cdecb3-90cf-4837-a2cd-be4bca3591ce)
![image](https://github.com/user-attachments/assets/edc7c68e-b111-449a-963b-3677bec1642f)

# Day 4: June 15th, 2025

## Time Spent: 1h+7h
I have completed the schematic, I realized I didn't have a USB C for my RP2040 stamp so I added that in the PCB. Researched more about resistors, microcontrollers and had trouble doing the firmware. The Firmware took around 2 hours, quite less than I expected. Thanks to cyao's hackpad tutorial the 3D modeling was a breeze, even though I am not that experienced with onshape. Onshape was a breeze but still felt really long.
![image](https://github.com/user-attachments/assets/f79e1e7a-50a3-49f0-84f2-c33fd5935488)
![image](https://github.com/user-attachments/assets/824a1051-c43b-4512-8a64-8fe3f4d80c6c)


# Day 5: June 16th, 2025 (from midnight)

## Time Spent: 2h
It's currently 2am or so But I have made an entire BOM, Got all my CAD Files here, double checked my firmware & I don't think I can't do much if I messed up my PCB :sob:. Fingers are crossed if I didn't mess up anything. I really wanna start my 3rd project soon which will take so long to research. I am aware that I don't have capacitators for my rgb light setup, but it won't be an issue. My brightness wouldn't be set to too high. Idk if I should have any pictures here because all I did was the BOM and doomscrolled a bit in between.

# Day 6: June 17th, 2025 

## Time Spent: 8h
Since it's still getting reviewed, I decided to completely redesign my rgb part of the pcb, recommeneded by @Kai Pereira. He said to add capacitators after each rgb. I decided to do that which took the majority of the day and alot of frustration. I also had a really bad time rewiring everything, but I completed this and slept peacefully. ofc this took 10 hours (extended till tmrw)
![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)

# Day 7: June 18th, 2025

## Time spent: 2h+4h
Still didn't get reviewed, I decided to also polish the CAD in the hope of 1 extra point. Working on it, might take a bit of my sanity but atleast my onshape is better than KiCAD. Forgot to mention this before but I switched my RP2040 stamp to a RP2035 stamp because RP2040 stamps aren't available in the market.


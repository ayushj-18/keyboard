---
title: "The Procastinate Board"
author: "Ayush Jaiswal"
description: "Making this personal keyboard so that I don't procastinate making a keyboard later on"
created_at: "2025-06-12"
---

# Project Idea/Inspo

I really wanted to make a keyboard to just gain insights on how electronics like keyboards work. After doing the hackpad, I got inspired to make a full keyboard looking at the keyboards other members made. Welp how hard can it be :smile:

Inspo- https://www.montechpc.com/mkey-tkl

Total time spent: 48h 

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
It's currently 2am or so But I have made an entire BOM, Got all my CAD Files here, double checked my firmware & I don't think I can't do much if I messed up my PCB :sob:. Fingers are crossed if I didn't mess up anything. I really wanna start my 3rd project soon which will take so long to research. I am aware that I don't have capacitators for my rgb light setup, but it won't be an issue. My brightness wouldn't be set to too high. Idk if I should have any pictures here because all I did was the BOM and doomscrolled a bit in between. (only worked on it 12am-2am). no journal picture :sob:

# Day 6: June 17th, 2025 

## Time Spent: 5h
Since it's still getting reviewed, I decided to completely redesign my rgb part of the pcb, recommeneded by @Kai Pereira. He said to add capacitators after each rgb. I decided to do that which took the majority of the day and alot of frustration. I also had a really bad time rewiring everything, but I completed this and slept peacefully. ofc this took 10 hours (extended till tmrw). Journal pic got lost :(


# Day 7: June 18th, 2025

## Time spent: 2h+2h+1h
Still didn't get reviewed, I decided to also polish the CAD in the hope of 1 extra point. Working on it, might take a bit of my sanity but atleast my onshape is better than KiCAD. Forgot to mention this before but I switched my RP2040 stamp to a RP2035 stamp because RP2040 stamps aren't available in the market.

Ok I went crazy on polishing the CAD and I decided to add some art! My 2 favourite albums, well not really I have one more, "Alone At Prom" but I couldn't generate a good enough silkscreen art for it :( . <br>
![Day 7 pic](https://github.com/ayushj-18/procastinateboard/blob/main/screenshots/readme-ss/3DFrontviewPCB.png)

# Day 8: June 19th, 2025

## Time spent: 2h+4h
2am right now, yeah I was just polishing CAD. Decided to add some keyswitches, but they are the wrong ones. But frick it, we ball! (CAD doesn't matter anyways since it wont be 3D printed ;)<br>
![Day 8 pic](https://github.com/ayushj-18/procastinateboard/blob/main/screenshots/journal-ss/Day8pic1.png) <br>
BRUHHH I forgot to add stabilizers. JUST WHEN I THOUGHT I WAS DONE WITH THE PCB. took like 2 seconds but the frustration was insane. I don't feel like updating my step file for the PCB LOL DEAL WITH IT AHAH. <br>
![Day 8 pic](https://github.com/ayushj-18/procastinateboard/blob/main/screenshots/readme-ss/IsometricViewCAD.png) <br>
COMPLETED CAD!!!!!!!!! YIPPPPEEEEEEE!!!!! PROJECT IS DONE PLEASE REVIEW!!!!!
will put the stl files in a bit after the splits. <br>
![Day 8 pic](https://github.com/ayushj-18/procastinateboard/blob/main/screenshots/readme-ss/IsometricViewCAD.png)<br>

# Day 9: June 20th, 2025

## Time spent: 2h
Decided to redo the LEDs cause I messed up. Thanks Kai for pointing that out again ;). Also put stl split files & step files because alexren forced me to. I am officially 100% done with non hardware work for this project!

# Day 10-13: June 23rd, 2025
Waiting to get reviewed, realized I didn't have stabilizers for my BOM, updated that. Small price change for one of my projects- ![image](https://github.com/user-attachments/assets/443c3637-0087-46a2-92ef-e911db6db8de)


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

## Day 1: June 12th, 2025

### Time Spent: 2 h  
Started the schematic and spent time deciding my keyboard schematic. It will be a TKL keyboard with a rotary encoder. Made a matrix on MS Paint to understand how the basic structure of my PCB and firmware will be. Watched some videos on how keyboards work.

![Day 1 Matrix](https://raw.githubusercontent.com/ayushj-18/procastinateboard/main/assets/78e52dfd-f240-4533-a118-3dcbde5f10cd.png)

---

## Day 2: June 13th, 2025

### Time Spent: 8 h  
Literally spent the entire day researching, asking people questions in Slack (I love how helpful everyone is) and I basically completed the entire schematic and assigned all footprints. Made a basic draft of my BOM and that’s about it. I struggled with figuring out how microcontrollers work and which one I’d need. I also had a hard time assigning footprints but I pulled through.  
My goal for tomorrow is to make the PCB and start the 3D modeling.

![Day 2 Schematic](https://raw.githubusercontent.com/ayushj-18/procastinateboard/main/assets/6dbeb918-e56a-4f57-acaf-ed31cbed7eef.png)

---

## Day 3: June 14th, 2025

### Time Spent: 9 h  
Completed the entire PCB, which took a full 8 h of the day — and I forgot one crucial thing (adding a 0.1 µF capacitor after each RGB LED). I hope it won't come back to bite me. I probably won’t run crazy animations, so fingers crossed. Here’s the 3D view and PCB screenshots:

![Day 3 View 1](https://raw.githubusercontent.com/ayushj-18/procastinateboard/main/assets/a60f2909-a369-43c4-8306-4323ec5364b6.png)  
![Day 3 View 2](https://raw.githubusercontent.com/ayushj-18/procastinateboard/main/assets/72cdecb3-90cf-4837-a2cd-be4bca3591ce.png)  
![Day 3 View 3](https://raw.githubusercontent.com/ayushj-18/procastinateboard/main/assets/edc7c68e-b111-449a-963b-3677bec1642f.png)

---

## Day 4: June 15th, 2025

### Time Spent: 8 h  
Finalized the schematic, realized I forgot a USB‑C connector for the RP2035 stamp, so I added that. Researched more about resistors and microcontrollers, and did the firmware in ~2 hours (faster than expected). Onshape modeling was long but intuitive thanks to the hackpad reference.  

![Day 4 View 1](https://raw.githubusercontent.com/ayushj-18/procastinateboard/main/assets/f79e1e7a-50a3-49f0-84f2-c33fd5935488.png)  
![Day 4 View 2](https://raw.githubusercontent.com/ayushj-18/procastinateboard/main/assets/824a1051-c43b-4512-8a64-8fe3f4d80c6c.png)

---

## Day 5: June 16th, 2025

### Time Spent: 2 h  
Took care of the BOM, verified CAD files, and double-checked firmware. No images here since it was just spreadsheet work and Reddit doomscrolling.

---

## Day 6: June 17th, 2025

### Time Spent: 8 h  
After feedback from @Kai Pereira, I redesigned the RGB section to include capacitors after each LED. Frustrating, but it’s done.  

*(Image not added — schematic unchanged from earlier)*

---

## Day 7: June 18th, 2025

### Time Spent: ~5 h  
Still under review, so I polished the CAD and added some album art silkscreens ("Alone At Prom" wasn’t working well, so just two).  

![Day 7 CAD View](https://raw.githubusercontent.com/ayushj-18/procastinateboard/main/assets/824a1051-c43b-4512-8a64-8fe3f4d80c6c.png)

---

## Day 8: June 19th, 2025

### Time Spent: ~6 h  
Final CAD polish, added switches (but mispositioned stabilizers at first—frustrating), but it’s finally locked. CAD is complete. STLs coming after the split boards.  

![Day 8 Board View](https://raw.githubusercontent.com/ayushj-18/procastinateboard/main/assets/Day8pic1.png)  
![Day 8 Front Layer](https://raw.githubusercontent.com/ayushj-18/procastinateboard/main/assets/3DFrontviewPCB.png)  
![Day 8 Isometric CAD](https://raw.githubusercontent.com/ayushj-18/procastinateboard/main/assets/IsometricViewCAD.png)

---

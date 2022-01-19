import cv2
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd

temps = ["amongUsSettings", "amongUsSettingsRed", "amongUsVictory", "apexLegendsLogo", "apexskull", "bars1", "bars2", "bars3", "bars4", "chest", "crafting", "fortniteBeta", "fortniteLogo", "fortnitePickaxe",
 "forzaGearFive", "forzaGearFour", "forzaGearOne", "forzaGearReverse", "forzaGearThree", "forzaGearTwo", "freeFireProfile", "freefireSettings", "furnace", "genshinUIDOPAQUE", "GOWBLUETREE", "GOWCROSS", "GOWLOGO",
  "GOWYELLOWTREE", "minecraftBigInventory", "shieldInventory", "squadsleft", "terrariamenu", "twohearts" ] 


count = 2
ansArray = []
# methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF]
method = cv2.TM_CCOEFF_NORMED
ans = 0
for img in os.listdir("path/to/data"):
    src = cv2.imread('path/to/data//'+img)
    src = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    for tempa in temps:
        temp = cv2.imread("C:/Varun/Codenges/ML/exun2021/finals/features/"+tempa+".jpg")
        temp = cv2.cvtColor(temp, cv2.COLOR_RGB2GRAY)
        src2 = src.copy()
        result = cv2.matchTemplate(src2, temp, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_loc == (605, 14) and tempa=="amongUsSettings": 
            ans = "1"
        elif max_loc == (604, 12) and tempa=="amongUsSettingsRed":
            ans = "1"
        elif max_loc == (202, 31) and tempa=="amongUsVictory":
            ans = "1"
        elif max_loc == (24, 14) and tempa=="apexLegendsLogo":
            ans = "2"
        elif (max_loc == (412, 296) or max_loc == (412, 294)) and tempa=="fortnitePickaxe":
            ans = "3"
        elif max_loc == (43, 14) and tempa=="fortniteLogo":
            ans = "3"
        elif max_loc == (439, 22) and tempa=="fortniteBeta":
            ans = "3"
        elif max_loc == (625, 0) and tempa=="freefireSettings":
            ans = "5"
        elif max_loc == (0, 0) and tempa=="freeFireProfile":
            ans = "5"
        elif max_loc == (331, 74) and tempa=="minecraftBigInventory":
            ans = "8"
        elif max_loc == (565, 282) and tempa=="forzaGearFive":
            ans = "4"
        elif max_loc == (565, 282) and tempa=="forzaGearOne":
            ans = "4"
        elif max_loc == (566, 282) and tempa=="forzaGearReverse":
            ans = "4"
        elif max_loc == (565, 281) and tempa=="forzaGearThree":
            ans = "4"
        elif max_loc == (566, 284) and tempa=="forzaGearFour":
            ans = "4"
        elif max_loc == (557, 346) and tempa=="genshinUIDOPAQUE":
            ans = "6"
        elif max_loc == (560, 314) and tempa=="GOWCROSS":
            ans = "7"
        elif max_loc == (559, 313) and tempa=="GOWYELLOWTREE":
            ans = "7"
        elif max_loc == (0, 0) and tempa=="GOWLOGO":
            ans = "7"
        elif max_loc == (159, 333) and tempa=="shieldInventory":
            ans = "8"
        elif max_loc == (331, 116) and tempa=="crafting":
            ans = "8"
        elif max_loc == (212, 74) and tempa=="chest":
            ans = "8"
        elif max_loc == (250, 324) and tempa=="twohearts":
            ans = "8"
        elif max_loc == (0, 0) and tempa=="bars1": 
            ans = "9"
        elif max_loc == (0, 0) and tempa=="bars2":
            ans = "9"
        elif max_loc == (0, 0) and tempa=="bars3":
            ans = "9"
        elif max_loc == (0, 0) and tempa=="bars4":
            ans = "9"
        elif max_loc == (622, 0) and tempa=="terrariamenu":
            ans = "10"
        elif (max_loc == (574, 13) or max_loc == (539, 27) or max_loc == (540, 27)) and tempa=="apexskull":
            ans = "2"
        elif max_loc == (557, 15) and tempa=="apexLegendsLogo":
            ans = "2"
    ansArray.append([str(img), ans])
    print(ans)
    print(count)
    count += 1

ans = pd.DataFrame(ansArray, columns=['id', 'game_id'])
ans.to_csv('answer.csv', index=False)

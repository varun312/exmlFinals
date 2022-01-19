# Submission for exML final task from Code Warriors

This is the submission for the final task of exml from team CW. 

## Dataset
The dataset was obtained from recorded live streams from twitch. Various small streamers were chosen to download the video from as they tend to have no face cam and less text in chat thus making the data better. Videos were downloaded with [twitch-dl](https://github.com/ihabunek/twitch-dl)

    twitch-dl download -q 360p {VIDEO ID}

Then 1000 random frames from the video were stored in a folder to be used as the data. ([frameExtractor.py](https://github.com/varun312/exmlFinals/blob/main/frameExtractor.py))

[Link to dataset]https://drive.google.com/file/d/1eIhf9AVr6egiIEKWfV_nROn6ru96N3_2/view?usp=sharing)

## Approach 

The Python bindings of openCV2 was used to detect a set array of features from the analyzed dataset. These were feature(s) that were present on every image of that category. For example, every image of Genshin Impact had a UID in the bottom right corner

![enter image description here](https://cdn.discordapp.com/attachments/750660009439920189/933379812075110430/unknown.png)  

A full list of these features, their corresponding game with image can be found in [features.md](https://github.com/varun312/exmlFinals/blob/main/features.md). 

This results in having multiple features for some games such as Fortnite, in which sometimes you are inside a match, where the default pickaxe is used as a feature. While other times you are in the lobby, in which case the fortnite logo at the corner is used. 

The program has looped through the training dataset and has stored all such features and their corresponding locations. At runtime the project attempts to locate each feature and if the position of the detected feature matches that of the training data, the program considers it as the game to which the detected feature belongs to.

Finally, the programs loops through all images and all features for each image, and the final data is compiled through pandas.   


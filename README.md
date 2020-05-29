# DDLC-Development-Tool-Kit

The DDLC-Development-Tool-Kit is something I have put together to help make DDLC Modding a lot easier. Currently there are a lot of great tools out there such as the Mood Posing Tool. A custom renpy launcher for DDLC and more. (Credits and links at the end). So I decided to put together a tool kit which has them all linked and wrapped up nicely together. This has helped save me lots of time and I hope it can help save other modders out there some time too! Feel free to contact me if you have any issues!

Update 29/05/2020: It was brought to my attention it is better to link to these tools rather than try to directly host them which I agree with so I will be restructuring the toolkit to suit that purpose and instead contain detailed instructions of how to do it this way instead. Also at some point I may write a script to automatically do all of this for you, eventually.

In the meantime I will work on instructions which are detailed and easy to follow. Note: This is NOT a substitute for documentation from each of the tools in the toolkits sources, but should suffice for getting started or a quick setup.

# Installation instructions:

If you need screenshots see the screenshot folder which will have a sc for each step (to be added).

The tool kit will not work out of the box. You need to follow these setup steps.

1. You will need to download the tools by following this setup from the official sources.
2. You will need to have a zipped download of DDLC. Official files can be downloaded at http://ddlc.moe
3. Now you'll want to open up the renpy application stored in 'DDMMaker-7.3.5-sdk'. (this is a modified version of renpy). Download it from: https://github.com/GanstaKingofSA/DDLC-ModMaker
4. Then open settings to set two things up. 
5. The first is set the location of the zipped version of DDLC, wherever you have it stored, for me I create a toolkit folder and store it in there for convinience but it really doesn't matter where you store it, so long as you link the location properly. Also based on feedback do not put your mod within the DDMMaker-7.3.5-sdk folder.
6. The second is setting the projects directory. The important thing about the projects directory is that this is where all of your projects will be stored. E.g. I have a project called 'DDPI' in the projects directory, the next files below 'DDPI' are the files for that mod.
7. The final note for this tool is that in order to specify the renpy version (here I'm using version 7 for compatibility with the MPT) you need to specify it. Simply create a file called renpy-version and include the number so in this case 7 in the text file.
8. The neat think about this is that it is actually able to be integrated with the MPT, amazing right! So now there's two sections, one for a new project (way easier) and one for existing ones. Also note when building you are going to have to ensure you execute the mod with base ddlc in renpy 7 so the lib and renpy folders are renpy 7 and the files compiled as renpy 7.

# New project

1. Simply open DDMMaker and click install MPT Then follow the instructions to install the MPT. Click on new project, follow the on screen instructions and that's it, done!
2. As a side note, when it says place the unpacked MPT zip next to base DDLC this is what it means. Within the MPT zip there will be an 'MPT unpacked zip' Extract this zip out of the MPT full zip, but do not unzip the unpacked version.
3. If that's tough to wrap your head around here is a link to the unpacked zip directly: https://drive.google.com/file/d/1WV2MelgXc06Yj_hpDJ6oSQF2VdZYrBz7/view?usp=sharing

Note: This will be updated with more info in future.

# Existing project.

1. A little more complex, for this we are going to have to manually patch our project.
2. Now onto the Mood Posing Tool, if you haven't heard of it, it's an amazing tool which makes adding in different sprites and custom poses much easier. In the credits a link to their post is available for more information.
3. Download the MPT unpacked zip from https://drive.google.com/file/d/1WV2MelgXc06Yj_hpDJ6oSQF2VdZYrBz7/view?usp=sharing
4. Now this is the key part. when this is unzipped you are left with an actual mod which is a demo for the tool(once you merge it with a copy of base ddlc). To actually get the MPT in your mod once you have unzipped the unpacked zip you'll want to follow the file path as follows: DDLC_MPT-1.0-unpacked.zip\DDLC_Mood_Posing_Tool\game\mod_assets. Here there will be an 'MPT' folder this is the tool you want.
5. Copy this folder into your mods mod_assets folder, then you're good to go.
4. (Ignore this point if you know how the MPT tool works) An important note for the MPT is that you must be using renpy v7, how you upgrade to v7 and other stuff I will not explain here. You can see detailed instructions and examples under both the MPT release post, and documentation as well as from the DDLCModTemplate 2.0, all of which are linked in the credits.

# Continuing on...

9. Some notes on the other stuff included.
10. The ModTemplateExample folder is an example of a sample project which shows how exactly you would lay this out in a project, provided you are using the (almost default) template for ddlc mods. (See credits for link).
11. The rpa tool is commonly used to help deal with extracting rpyc files from rpa files. This tool is also used for the reverse process. The main reason is to help save space. An example is the 'images.rpa' file in base ddlc will contain the images used in the game. (see credits for download)
12. Finally the unrpyc tool is used to decompile rpyc files. rpyc files are binary files which are compiled by renpy when running and then left over. You only need these for your scripts to work. However, you really only want to get rid of your rpy files once you're done with your mod to save space. So if you have the rpyc file for say script.rpyc using the unrpyc tool will allow you to get script.rpy out so you can actually read it. (in english not unreadable binary data, no not 1's and 0's I mean literally unreadable by humans). (see credits for download)

13. I believe that's it for now, but this is very much prone to change based on feedback! (and motivation)
updated: 29/05/2020

# Template Notes:

You will need to merge this with the original DDLC game files for this to work.
Template works with the DDMM v7, just put it in the projects folder
Also it works with base DDLC, copy and paste the game, lib, renpy folders into base ddlc folder and click replace.
Launch DDLC and you'll see it works.
The main thing to note is if you have issues when building your project you can copy it's included renpy and lib folders into your project, that will fix any issues with not being renpy v7 as those folders are v7 and when you re compile all your files will automatically compile into v7.
update 29/05/2020: Template will be added back soon after some changes are made to make it easier, screenshots and more will be added to this guide if requested and when I have motivation.

# Credits

Obviously, this is a collection tool kit of various tools to make life easier. I did not make these tools and none of this would be possible without them so here are the credits for all these wonderful people. (I really tried to credit everyone, if I have been an idiot and forgotten someone let me know).

DDMMaker: https://github.com/GanstaKingofSA/DDLC-ModMaker by GangstaKingofSA
DDLCModTemplate: https://github.com/GanstaKingofSA/DDLCModTemplate2.0 by GangstaKingofSA
MPT: https://www.reddit.com/r/DDLCMods/comments/emennq/mood_posing_tool_mpt_v10_release_for_ddlc_modding/?utm_source=share&utm_medium=web2x by Chronos, Yagamirai and Terra.
unrypc: https://github.com/CensoredUsername/unrpyc by CensoredUsername
rpatool: https://github.com/Shizmob/rpatool by Shizmob
renpy-7.3.5-sdk: https://www.renpy.org/latest.html
This guide and the custom example template: Me! Karim!

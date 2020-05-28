# DDLC-Development-Tool-Kit

The DDLC-Development-Tool-Kit is something I have put together to help make DDLC Modding a lot easier. Currently there are a lot of great tools out there such as the Mood Posing Tool. A custom renpy launcher for DDLC and more. (Credits and links at the end). So I decided to put together a tool kit which has them all linked and wrapped up nicely together. This has helped save me lots of time and I hope it can help save other modders out there some time too! Feel free to contact me if you have any issues!

# Installation instructions:

If you need screenshots see the screenshot folder which will have a sc for each step (will link it into here at some point)
The tool kit will not work out of the box just yet. You need to follow these setup steps.
1. Download the 'Tool Kit' folder. (That's the actual toolkit the rest of this repo is tutorials, credits etc.)
2. You will need to have a zipped download of DDLC. Official files can be downloaded at http://ddlc.moe
3. Now you'll want to open up the renpy application stored in 'DDMMaker-7.3.5-sdk'. (this is a modified version of renpy).
4. Then open settings to set two things up. 
5. The first is set the location of the zipped version of DDLC, wherever you have it stored, I store mine within the toolkit folder for convinience but it really doesn't matter where you store it. 
6. The second is setting the projects directory. The important thing about the projects directory is that this is where all of your projects will be stored. E.g. I have a project called 'DDPI' in the projects directory, the next files below 'DDPI' are the files for that mod.
7. The final note for this tool is that in order to specify the renpy version (here I'm using version 7 for compatibility with the MPT) you need to specify it. Simply create a file called renpy-version and include the number so in this case 7 in the text file.

8. Now onto the Mood Posing Tool, if you haven't heard of it, it's an amazing tool which makes adding in different sprites and custom poses much easier. In the credits a link to their post is available for more information. To use the MPT simply place it in the 'mod_assets' folder of your project and you're good to go!
9. (Ignore this point if you know how the MPT tool works) Please note this guide is reliant on you using renpy v7. This is needed by the MPT in order for it to work with layered images. This also means that in any new projects you do use you'll need to include the renpy v7 files. This is more of a specific issue for when you're building your project. To make it easier if you have no clue what I'm talking about (or you're too lazy to read Chronos' documentation for the MPT) you can always copy the library and renpy folders included in the example project into your own. Another thing to note is that this is NOT neccessary while you are using the 'DDMMaker-7.3.5-sdk', this is only necessaary for when you are building your project to be compatible with base ddlc. I will add more details here if people want it but this is really a MPT specific thing.

10. The ModTemplateExample folder is an example of a sample project which shows how exactly you would lay this out in a project, provided you are using the (almost default) template for ddlc mods. (See credits for link).
11. The rpa tool is commonly used to help deal with extracting rpyc files from rpa files. This tool is also used for the reverse process. The main reason is to help save space. An example is the 'images.rpa' file in base ddlc will contain the images used in the game.
12. Finally the unrpyc tool is used to decompile rpyc files. rpyc files are binary files which are compiled by renpy when running and then left over. You only need these for your scripts to work. However, you really only want to get rid of your rpy files once you're done with your mod to save space. So if you have the rpyc file for say script.rpyc using the unrpyc tool will allow you to get script.rpy out so you can actually read it. (in english not unreadable binary data, no not 1's and 0's I mean literally unreadable by humans).
13. I believe that's it for now, but this is very much prone to change based on feedback! (and motivation)

# Credits

Obviously, this is a collection tool kit of various tools to make life easier. I did not make these tools and none of this would be possible without them so here are the credits for all these wonderful people. (I really tried to credit everyone, if I have been an idiot and forgotten someone let me know)

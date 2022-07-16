# Valo Tracker - Discord Bot


## Setup

### **To add the bot to a discord server**
Simply use the following link to add the bot to the server </br> 
<a href="https://discord.com/api/oauth2/authorize?client_id=991063792454619157&permissions=277025467392&scope=bot">Discord Invite</a> </br>

### **Important Information**
* This bot is a prototype, not functionally finished.</br>

* I plan to add a few more commands to make the bot a bit more user-friendly, one such command being the `!help`.

* The code provided should serve as a good bases to add a few more layers of functionality to the bot.

* The code might also have some not yet identified bugs, so use at your own risk.

### **Commands**
* `!track {username}#{tag}`</br>
**Explantaion**: Finds information regarding a particular user.

## Development

### **Information about the bot**
The bot mainly uses <a href = "https://github.com/Henrik-3/unofficial-valorant-api">Henrik's Unofficial Valorant API</a> to get player and match information for a specified **Username** and **Tag**, for example, Liferafter#7796. </br></br>
The code request information twice from two end points, mainly
 ```
/valorant/v1/account/{name}/{tag}
``` 
and 
```
/valorant/{version}/by-puuid/{mode}/{region}/{puuid}
```

All the information is formatted and sent to the discord channel where the command was invoked.
</br>

The all the methods of `compMatchHistory` return a boolean value, so that it is easier to manage my **higly coupled code** where another method cannot be invoked before another method is invoked.

The hieararchy that it follows is:

1. `getAccData()` </br>
2. `formatAccData()` </br>
3. `getMmrHistory()`</br>
4. `formatMmrData()`</br>
5. `getPrevMmr()`</br>

The code ended up being highly coupled because of how I instantiate import class attributes.

And also becuase of my attempt to reduce the amount of class being made to the API.

> **Side Note** - It is not highly coupled interms of Software Design, since it is just one object, that has no relations to any other object. The objects methods are too dependent on the objects other methods, to the point that it makes the object itself a bit un-intuitive. And hence I used highly-coupled to describe the amount of dependence within the code; Since one buggy method would break the rest of the code.

### **Information about the Code**
There are two parts to the bot itself, the `discordUI.py` and `matchHistory.py`.</br>
There is also a third file for tests: `tests_matchhistory.py`.
<hr>

**discordUI.py** Is the module that holds the code for all the interactions between discord and the bot. </br></br>
There are two important aspects to that code: </br>
1. Initialized the commands module so that I could directly write commands, with the prefix "!"
2. Bot connects to Discords API using the a **Token** that should be unique to the both.

*Why are these important then?* </br>

 The information about the prefix and commands module should help a person write more commands for their bots. </br>

 For more information visit the <a href = https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html>discord documentation</a>.
 
 Second, the bots Token isn't provided in the code uploaded to github, since all bots have unique tokens that connect to particular bots, my Token could be used for malicious purposes. 
 
 To add your own Token, crate a `.env` file, and add this line to it:
 ```
 TOKEN = 'Your Token Here'
 ``` 
 Make sure the `.env` file exists in the same directory as the `discordUI.py`.
<hr>

**matchHistory.py** contains the class `compMatchHistory` which has all the methods needed for the current bot. </br></br>

* `getAccData()`</br>
    * Returns a boolean value 
        * **True** if executed properly 
        * **False** if execution failed 
    * Modifies `accountData` attribute of `compMatchHistory` 
* `formatAccData()` </br>
    * Returns a boolean value 
        * **True** if executed properly 
        * **False** if execution failed
    * Modifies `region` and `puuid` attribute of `compMatchHistory`
* `getMmrHistory()`</br>
    * Returns a boolean value 
        * **True** if executed properly 
        * **False** if execution failed
    * Modifies `mmrData` attribute of `compMatchHistory`
* `formatMmrData()`</br>
    * Returns a boolean value 
        * **True** if executed properly 
        * **False** if execution failed
    * Modifies `mmrChange` and `currentRank` attribute of `compMatchHistory`
* `getPrevMmr()`</br>
    * Returns a boolean value 
        * **True** if executed properly 
        * **False** if execution failed
    * Modifies `ranks` attribute of `compMatchHistory`
* `checkErrorCode(jsonData)`</br>
    * Parameters: A Json response object
    * Returns a boolean value
        * **True** if executed properly 
        * **False** if execution failed
    * Modifies `statusRequest` and `errorMsg`

> **Side Note** - The *Modifies* information is only for when the object returns true, meaning it executes without any errors.

<hr>

**tests_matchHistory.py** has prewritten tests to help anyone check if the code works properly if there were changes made to pre-existing methods in the `compMatchHistory`</br></br>

The code basically just uses a bunch of `assertEqual`'s to see if a function is working properly for a particular **username** and **tag** pair.

It would be needed for new methods implemented to have new tests for the code.

The tests themselves use the `unittest` module built into python.

The code coverage for current tests is **96%**.
<hr>

### **Dependecies**

The current <a href= 'requirements.txt'>requirements.txt</a> file contains all the third party modules, the code is dependent on.

You can simply pip-install those requirements.

### **Dockerfile**
You can also use the<a href='Dockerfile'> Dockerfile</a> in this repo to build and run a Docker Image. 
> **Side Note** - Don't forget to add your *Bot Token* to the <a href='Dockerfile'> Dockerfile</a> before building an image.


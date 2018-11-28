# glopi
An easy interface for the api for GitKraken Glo, kinda like Trello.

# Installation
Requires python3 to be installed and the pip module `pyautogui`. It also requires you to have Firefox installed and in your path (it should be normally). You have to be already logged in Firefox already. You can do a quick / automated install (including download) below:
```
git clone https://github.com/Oj18/glopi.git
cd glopi
chmod +x *
sudo ./install.sh
```
To check / install requirements, `(apt) python3, (apt) python3-pip, (pip) pyautogui`

# Get the ID of a board (required for everything)
This is very important. Not the end of the link. The end of the link is something like this:
```
end of link to the board:
W6FQH4WGZA4AVVZp

the proper board id:
5ba1501f8586640e00555669
```

Currently the only way I have discovered how to get the ID is:
```
1. Open Glo in Firefox
2. Click a different (Glo) board than the one you want
3. Open inspector / console
4. Click on the network tab
5. Click / select the board you want the id of
6. Look at the (should be) top GET with type JSON
7. Click it to bring up the info to the right
8. Look in Headers > Request URL it should look like:
https://app.gitkraken.com/api/glo/boards/5bfdbb08d6e667001a7969a4?fields=archived_date,invited_members,external_provider_members,members,id,name,columns,columns.name,labels,labels.sync_provider_id,sync_provider,sync_provider.type,sync_provider.options

The long seemingly random string, in this case, 5bfdbb08d6e667001a7969a4, is the ID of the board, which you can use with Glopi.
```

# Commands / Usage
Things in <> mean that you should use your own value, like <BOARD_ID> you should put your own board ID there. Things in square brackets are optional.

## Changelog
The changelog commands makes a changelog-like output. It is like this:
```
<left-most column>:
<the cards here>

<one to the right>:
<the cards for that column here>

etc.
```
It goes from the left to the right. Usage:
```
./glopi.sh changelog <BOARD_ID> [<FILE_NAME>]
```
If you don't put a file name after then it will print out the output in the terminal, if you do put a file name it will save the output there and not print anything in the terminal.

## The standard, --help (or --usage) and --version
```
./glopi.sh --version
```
Will get the current version, like `Glopi Alpha 2` (latest)

```
./glopi.sh --help
or
./glopi.sh --usage
```
Will get 'help' (tell you to read this), might make proper help later on, as that is not a big priority.
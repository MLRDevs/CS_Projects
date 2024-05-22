# Change Permissions on a File

*Forces*: When working with loads of files, you don't want the wrong people to be able to edit or change any of the files you are working with

*Solution*: the change permissions command allows you to change the permissions on a file to who can access it or edit it in any way

### How permisions on files work

permissions for files and directories are broken into three categories:
* user
* group
* others

there is an easy way to tell if you are dealing with a file or a directory:
* if the permissions start with a '-' then its a file
* if the permissions start with a 'd' then its a directory

each category has three permissions:
* read
* write
* execute

these can all be changed, so for example

    -rwx-r-xr-x

the user can read, write, and execute the file but everyone else can only read and execute


### Example

```
cd Desktop                  // change the current working directory ot the Desktop
ls -l                       // see what is on the desktop, -l to see permissions

// -rw-rw-rw-               // everyone can read and write the file

chmod -w testfile.txt       // change the permissions of the file for the user
// -r--rw-rw-               // user can now only read the file

chmod g-w testfile.txt      // change the permissions of the file for a group
// -r--r--rw-               // now the group can only read the file

chmod +w testfile.txt       // add the write permission to the user
// -rw-r--rw-               // the user can now read and write the file

chmod o-w testfile.txt      // change the permissions for others
// -rw-r--r--               // others can now only read the file

chmod a=r oldstuff          // change permissions for everyone with the "oldstuff" directory
// dr--r--r--               // everyone can now only read the directory

```

*Preceding Patterns*

[Change Directory Command](/ChangeDirectory.md)

[ls Command](/lsCommand.md)

*Following Patterns*

[Copy File](/CopyFileCommand.md)

[Delete File](/DeleteFileCommand.md)
# Copy File

*Forces*: when working with a lot of files that constantly change, it's good to keep backups of the old files

*Solution*: The copy file command allows you to copy a file from your current working directory into anywhere on the machine

```
cd Desktop                  // Change the current working directory to the Desktop
mkdir oldstuff              // create a new directory
cp oldfile.txt oldstuff     // copy the file "oldfile.txt" and put it in the new directory
rm oldfile.txt              // delete the file in the current working directory
ls                          // check to make sure the file was deleted
cd oldstuff                 // change the current working directory to the new directory
ls                          // check to make sure the file was copied into the new directory
```

*Preceding Patterns*

[Change Directory Command](/ChangeDirectory.md)

[Make Directory Command](/MakeDirectoryCommand.md)

[Make File Command](/MakeFileCommand.md)

[ls Command](/lsCommand.md)

[Delete File Command](/DeleteFileCommand.md)

*Following Patterns*

[Open File Command](/OpenFileCommand.md)
// Alex Miller
// Count directory structures and print them
#include <iostream>
#include <cstdlib>
#include <string>
#include <dirent.h> // readdir
#include <string.h> // strcat, strcpy
#include <sys/stat.h> // length of file
#include <unistd.h> // readlink
#include <list> // list of inodes
#include <assert.h> // assert
#include <vector> // vector for permissions
using namespace std;

string gettype(struct dirent* dr) { // get the type of the thing found inside the directory
    if (dr->d_type == DT_DIR)  return "(d)"; // directory
    else if (dr->d_type == DT_REG) return "(f)"; // file
    else if (dr->d_type == DT_LNK) return "(l)"; // link
    return "";

}
void ErrorCheck(bool b, string m) { // error checking
    if (b) {
        cout << endl;
        perror(m.c_str());
        exit(0);
    }
}
char* getnewpath(char* path, char* name) { // get new path to a directory
    int tl = strlen(path) + strlen(name) + 2; // size of string
    char* newpath = new char[tl];

    // copy contents and cat them together
    strcpy(newpath,path);
    strcat(newpath,"/");
    strcat(newpath,name);
    return newpath;
}
void getperms(struct stat fs) { // get the permissions of the files
    string perms = "";
    char bit = '-';
    vector<mode_t> types({S_IRUSR,S_IWUSR,S_IXUSR,S_IRGRP,S_IWGRP,S_IXGRP,S_IROTH,S_IWOTH,S_IXOTH}); // list of all the file permissions
    int j = 0;
    for(auto i = types.begin(); i != types.end(); ++i) { // loop through each one instead of if stating all of them
        if (j == 0 || j == 3 || j == 6) bit = 'r'; // read
        else if (j == 1 || j == 4 || j == 7) bit = 'w'; // write
        else bit = 'x'; // execute
        if ((fs.st_mode & types.at(j)) != 0) perms += bit; // if it's the right permission add it
        else perms += '-'; // if not then just dash
        j++;
    }
    cout << perms << ", "; // print the answer

}
int getfilesize(char* filename) { // get the length of the file
    struct stat filestat;
    ErrorCheck(stat(filename, &filestat) != 0, "GETTING FILE SIZE");
    getperms(filestat); // get the permissions of the file
    return filestat.st_size;
}
bool searchaddlist(list<int> &nodelist, struct dirent *dp) { // search if the inode number is already in list, add if not
    for(auto const& i : nodelist) { // loop through the list
        if (i == dp->d_ino) return true;
    }
    nodelist.push_back(dp->d_ino); // add to list
    return false;

}
void Dirs (char* path, list<int> &listnodes) { // recurse through each directory printing whats inside of them
    DIR* dir = opendir(path);
    ErrorCheck(dir == nullptr, "COULD NOT OPEN DIRECTORY");
    struct dirent *dp;
    while ((dp=readdir(dir)) != NULL) { // main loop for current directory
        if (strcmp(dp->d_name,".") != 0 && strcmp(dp->d_name,"..") != 0) { // not using "." and ".."
            if (gettype(dp) == "(d)") { // if directory, go into directory and recurse
                assert(dp->d_type == DT_DIR); // assert
                if (searchaddlist (listnodes,dp)) continue;
                cout << path << "/" << dp->d_name << " " << "(d)" << endl;
                char* newpath = getnewpath(path, dp->d_name);
                Dirs(newpath, listnodes); // recurse on new filepath
            }
            else if (gettype(dp) == "(f)") { // if file, print the path and the file size
                assert(dp->d_type == DT_REG); // assert
                char* newpath = getnewpath(path, dp->d_name);
                if (searchaddlist (listnodes,dp)) continue;
                cout << path << "/" << dp->d_name << " " << "(f, " << getfilesize(newpath) << ")" << endl;
            }
            else if (gettype(dp) == "(l)") { // if link, print the name and where the link goes
                if (searchaddlist (listnodes,dp)) continue;
                struct stat sb;
                ErrorCheck(lstat(getnewpath(path,dp->d_name),&sb) == -1, "GETTING LINK");
                char* l = new char[sb.st_size+1]; // buffer
                ErrorCheck(l == nullptr, "LINK BUFFER");
                ssize_t link = readlink(getnewpath(path,dp->d_name),l,sb.st_size+1);
                ErrorCheck(link == -1, "COULD NOT READ LINK");
                l[link] = '\0'; // set the null byte
                cout << path << "/" << dp->d_name << " " << "(l -> " << l << ")" << endl;
                delete[] l; //deallocate
            }
        }
        // printing "." and ".."
        else cout << path << "/" << dp->d_name << " " << gettype(dp) << endl;
    }
    ErrorCheck(closedir(dir) == -1, "COULD NOT CLOSE DIRECTORY"); // close directory

}
int main(int argc, char** argv) { // main method

    // get the path
    char* path = argv[1];

    // create the list of the inodes and run
    list<int> nodelist;
    Dirs(path, nodelist);

    return 0;
}
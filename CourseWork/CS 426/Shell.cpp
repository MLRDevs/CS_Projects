// Alex Miller
// Big Assignment Shell

#include <iostream>
#include <cstdlib>
#include <string>
#include <unistd.h> // fork
#include <sys/wait.h> // wait
#include <string.h> // strcmp
#include "readline/readline.h" // readline
#include "readline/history.h" // history
#include <fstream> // stream for history file
#include <fcntl.h> // O_RDONLY flags
#include <vector> // for args list
using namespace std;

void ErrorCheck(bool b, string m);
string getprevline(string hf);
char** getargslist(char** &args, vector<string> argslist);
void Redirection(vector<string> &argslist);
bool CheckSemiColon(vector<string> argslist);
void DoSemiColons(vector<string> argslist);
void DoDot(vector<string> argslist);
vector<string> StoVS (string line);
void DoBang(vector<string> argslist);
void ChangePrompt(vector<string> argslist);
void RunCommand(vector<string> argslist);
int main();


void ErrorCheck(bool b, string m) { // error handling
    if (b) {
        perror(m.c_str());
        main();
    }
}

string getprevline(string hf) { // get the last command used so no duplicates next to each other when started back up
    ifstream file(hf);
    string lastcommand;
    if (file.is_open()) { // if file is open then get every line 
        string line;
        while (getline(file, line)) lastcommand = line; // loop stops when the last line is gotten
    }
    file.close();
    if (lastcommand == "") return ""; // if there was no command in history
    return lastcommand;
}

char** getargslist(char** &args, vector<string> argslist) { // convert string vector to a char* vector
    for (int i=0; i < argslist.size(); i++) {
        args[i] = argslist[i].data();
    }
    return args;
}

void Redirection(vector<string> &argslist) { // check for redirection in the command
    bool redir = false;
    for (int i=0; i < argslist.size()-1; i++ ) { // loop through all the args
        if (argslist[i] == ">") { // into file
            int fd = open(argslist[i+1].c_str(),O_WRONLY | O_CREAT, 0660);
            ErrorCheck(dup2(fd,1) == -1,"DUP2 > ");
            redir = true;
        }
        else if (argslist[i] == "<") { // from file
            int fd = open(argslist[i+1].c_str(),O_RDONLY, 0660);
            ErrorCheck(dup2(fd,0) == -1, "DUP2 < ");
            redir = true;
        }
        else if (argslist[i] == ">>") { // append mode
            int fd = open(argslist[i+1].c_str(), O_WRONLY | O_APPEND, 0660);
            ErrorCheck(dup2(fd,1) == -1, "DUP2 >> ");
            redir = true;
        }
        if (redir == true) { // get rid of the redirection and file and just keep the command
            argslist.erase(argslist.begin() + i);
            argslist.erase(argslist.begin() + i+1);
        }
    }
}

bool CheckSemiColon(vector<string> argslist) { // return true if command has a semi colon
    for (int i=0; i < argslist.size(); i++) {
        if (argslist[i][argslist[i].length()-1] == ';') return true;
    }
    return false;
}
void DoSemiColons(vector<string> argslist) { // deal with the semicolons
    string cmd = "";
    vector<string> newcmd; // new vector to hold each command
    for (int i=0; i < argslist.size(); i++) { // loop through vector
        for (int j=0; j < argslist[i].length(); j++) { // loop through each string
            if (argslist[i][j] != ' ' && argslist[i][j] != ';') {
                if (j == argslist[i].length()-1 && argslist[i][j] != ';') { // get args for command
                    cmd += argslist[i][j];
                    newcmd.push_back(cmd);
                    cmd = "";
                    if (i == argslist.size()-1) RunCommand(newcmd); // last command to run
                }
                else cmd += argslist[i][j];
            }
            else if (argslist[i][j] == ';' || i == argslist.size()-1) { // run command and clear vector for next command
                newcmd.push_back(cmd);
                cmd = "";
                RunCommand(newcmd);
                newcmd.clear();
            }
        }
    }
}
void DoDot(vector<string> commands) { // deal with dot commands with files
    string cf = commands[1];
    ifstream file(cf);

    if (file.is_open()) { // if file is open then get every line 
        string line;
        vector<string> argslist;
        string cmd = "";
        while (getline(file, line)) { // get each line in file
            argslist = StoVS(line); // change to vector<string>
            RunCommand(argslist); // run the command
            argslist.clear();
            cmd = "";
        }
    }
    else {
        ErrorCheck(true, "DOT COMMAND");
    }
    file.close();
}
vector<string> StoVS (string line) { // string to vector string to run command
    vector<string> argslist;
    string cmd = "";
    for (int i=0; i < line.length(); i++) { // get each arg
        if (line[i] != ' ') {
            cmd += line[i];
            if (i == line.length()-1) { // if last arg
                argslist.push_back(cmd);
                cmd = "";
            }
        }
        else {
            argslist.push_back(cmd); // add arg to vector
            cmd = "";
        }
    }
    return argslist;
}
void DoBang(vector<string> argslist, int num) { // deal with the bang commands
    char cmdspot = argslist[0][1];
    string hf = string(getenv("HOME")) + "/.myshell_History.txt";

    ifstream file(hf);
    vector<string> cmdlist; // vector string of all commands in history
    string line;
    string cmd = "";
    if (file.is_open()) { // if file is open then get every line 
        while(getline(file,line)) {
            cmdlist.push_back(line);
        }
    }
    else {
        cout << "BANG: opening history file" << endl;
        return;
    }
    file.close();

    if (num == 0) { // for numbers
        string cmdspot = argslist[0].substr(1,argslist[0].length()-1);
        int index = 0;
        try {
            index = stoi(cmdspot);
        } catch(out_of_range) { // band amount of of range of the history file
            cout << "BANG: out of range" << endl;
            return;
        }
        if (index > cmdlist.size()) { // if index is not inside the size
            cout << "BANG: index too high" << endl;
            return;
        } 
        line = cmdlist[cmdlist.size()-index-1]; // get the line at the index from most recent to least
        if (line[0] == '!') { // do not let continuous use of bang for infinite loop
            cout << "BANG: cannot select another bang" << endl;
            return;
        } 
    }
    else if (num == 1) { // for letters
        for(int i=cmdlist.size()-1; i > 0; i--) { // if its a letter, go backwards for most recent use of a command starting with that letter
            if (cmdlist[i][0] == cmdspot) {
                line = cmdlist[i];
                break;
            }
        }
        if (line == "") {
            cout << "BANG: command not found" << endl;
            return;
        }
    }

    // close file and run command
    argslist.clear();
    argslist = StoVS(line);
    RunCommand(argslist);
}
void ChangePrompt(vector<string> argslist) { // change the prompt of the termainal
    string fullcommand = "";
    for (int i=0; i < argslist.size(); i++) { // get the whole new command prompt into one string
        if (argslist[i][0] != '\"') fullcommand += argslist[i];
        if (i != argslist.size()-1) fullcommand += ' ';
    }
    string prompt = fullcommand.substr(5, fullcommand.length()-3);
    ErrorCheck(setenv("PROMPT", prompt.c_str(),1) == -1, "CHANGE PROMPT: "); // change the prompt variable
}
void RunCommand(vector<string> argslist) { // run the command given
    int status; // for waitpid
    if (strcmp(argslist[0].c_str(),"exit") == 0) exit(0); // exit
    else if (CheckSemiColon(argslist)) DoSemiColons(argslist); // deal with semicolons
    else if (argslist[0][0] == '.') DoDot(argslist); // dot file commands
    else if (argslist[0][0] == '!') { // bang commands
        if (((int)argslist[0][1]) >= 49 && ((int)argslist[0][1]) <= 57) DoBang(argslist,0); // number
        else DoBang(argslist, 1); // letter
    }
    else if (strcmp(argslist[0].c_str(),"cd") == 0) ErrorCheck(chdir(argslist[1].c_str()) == -1, "DIRECTORY"); // changing directory
    else { // else fork
        int pid = fork();
        ErrorCheck(pid == -1, "FORK");
        if (pid == 0) { // child process
            Redirection(argslist); // check for redirection
            char** args = getargslist(args, argslist); // change the vector to a char** for execvp
            args[argslist.size()] = NULL; // null terminate
            ErrorCheck(execvp(args[0], args) == -1,"COMMAND"); // execute command
            exit(1);
        }
        else { // parent process
            ErrorCheck(waitpid(pid,&status,0) == -1, "WAITPID");
        }
    }
}

int main() { // main method

    // xterm man
    // const char* inXterm = getenv("TERM"); // get xterm flag
    // if (string(inXterm) != "xterm") { // if not running in xterm already
    //     system("xterm -fa 'Monospace' -fs 20 -fg white -bg black -cr green -e ./myShell");
    //     exit(0); // exit original terminal program was called from so to not run twice
    // }

    string historyfile = string(getenv("HOME")) + "/.myshell_History.txt"; // save history in home directory
    read_history(historyfile.c_str()); // load history
    const char* prevline = getprevline(historyfile).c_str(); // previous line

    while (true) { // main loop for shell

        char* line; // line taking in the command

        string prompt;
        if (getenv("PROMPT") == nullptr) prompt = "Miller~$: ";
        else prompt = string(getenv("PROMPT"));

        line = readline(prompt.c_str());
        vector<string> argslist;

        if (!(strcmp(prevline,line) == 0)) { // if the command is the same as the last command then don't add it to history
            if (*line) {
                add_history(line);
                write_history(historyfile.c_str()); // write to history file
                prevline = strdup(line);
            }
        }

        char* token = strtok(line," ");
        while (token != nullptr) {
            argslist.push_back(token);
            token = strtok(nullptr," ");
        }

        free(line); // free up the line

        // if the command is to change the prompt, here instead of in RunCommand() due to threads
        if (strcmp(argslist[0].substr(0,3).c_str(), "PS1") == 0) ChangePrompt(argslist);
        else RunCommand(argslist); // run command
    }
}
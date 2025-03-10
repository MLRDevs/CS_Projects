// Alex Miller
// Server programming, accepting client and sending whatever they want

#include <iostream>		// cout, cerr, etc
#include <stdio.h>		// perror
#include <string.h>		// bcopy
#include <netinet/in.h>		// struct sockaddr_in
#include <unistd.h>		// read, write, etc
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <assert.h>
#include <fstream>
#include <sys/wait.h> // waitpid

using namespace std;

const int BUFSIZE=10240;

int MakeServerSocket(const char *port) {
	const int MAXNAMELEN = 255;
	const int BACKLOG = 3;	
	char localhostname[MAXNAMELEN]; // local host name
	int s; 		
	int len;
	struct sockaddr_in sa; 
	struct hostent *hp;
	struct servent *sp;
	int portnum;	
	int ret;


	hp = gethostbyname("localhost");

	sscanf(port, "%d", &portnum);
	if (portnum ==  0) {
		sp=getservbyname(port, "tcp");
		portnum = ntohs(sp->s_port);
	}
	sa.sin_port = htons(portnum);

	bcopy((char *)hp->h_addr, (char *)&sa.sin_addr, hp->h_length);
	sa.sin_addr.s_addr = INADDR_ANY;
	sa.sin_family = AF_INET;

	s = socket(AF_INET, SOCK_STREAM, 0);

	ret = bind(s, (struct sockaddr *)&sa, sizeof(sa));
	if (ret < 0)
		perror("Bad");
	listen(s, BACKLOG);
	cout << "Waiting for connection on port " << port << endl;
	return s;
}
bool ErrorCheck(bool b, string s) { // error check, returns true if error, false if not
	if (b) {
		cout << s << endl;
		return true;
	}
	return false;
}
string getTypeRequest(string s) { // get the content type
	if (s == "txt" ) return "text/plain";
	else if (s == "jpg") return "image/jpeg";
	else if (s == "html") return "text/html";
	else if (s == "gif") return "image/gif";
	return "ERROR";
}
bool RefuseChrome(char* buf, int bufsz) { // refuse any connection made from chrome
	string check = "";
	int spot = 0;
	for (int i=0; i < bufsz/2; i++) { // go through whole buf
		for (int j = i; j < i+13; j++) { // add chars from buf to string
			check += buf[j];
			spot = j;
		}
		if (check == "Google Chrome") { // return true if it is chrome
			return true;
		}
		else check = ""; // reset string if not
	}
	return false;
}
int getFilesz(fstream &in) { // get the size of the file
	in.seekg(0,ios::end);
	return in.tellg();
}
string GetReqandCheck(int fd, char* buf) { // get what the user wants, and check if user is using chrome

	// read in the data and get what the user wants
    int len = read(fd, buf, BUFSIZE);
	if (ErrorCheck(len == -1, "Bad Read")) exit(0);
    buf[len] = 0;
    string req;
    for (int i=5; i < BUFSIZE; i++) { // get just the thing the user wants
        if (buf[i] == ' ') break;
        req += buf[i];
    }
	if (RefuseChrome(buf,len)) { // refuse any connection from chrome browser
		string header = "HTTP/1.1 401 Unauthorized. cannot use Chrome\r\n";
		len = write(fd, header.c_str(), header.length());
		if (ErrorCheck(len == -1,"Bad write")) exit(0);
		exit(0);
	}
	return req;
}
string GetFileType(string req) { // return the type of file the user is asking for

	// getting the file type
	string type = "";
	bool after = false; // bool for after '.' in file type
	for (int i=0; i < req.length(); i++) {
		if (after) type += req[i]; // get the chars for the file type
		else if (req[i] == '.') after = true;
	}
	return getTypeRequest(type); // change it so that it can be used in metadata
}
void Connection(int fd, char* buf) { // method that does everything, instead of using "goto" can just return 
    
	
    string req = GetReqandCheck(fd,buf); // get the file the user wants

	string type = GetFileType(req); // get the type of file the user is asking for

	// open file
	int len;
	fstream in(req, ios::in | ios::binary); // open in binary so images can be used as well
	if (in.fail()) { // file does not exist
		string header = "HTTP/1.1 404 NOT FOUND\r\n";
		len = write(fd,header.c_str(),header.length());
		if (ErrorCheck(len == -1,"Bad Write")) exit(0);
		exit(0); // exit if file does not exist
	}

	// get the file size
	int filesz = getFilesz(in);
	in.seekg(0, ios::beg);

	// Write to the web client
	string header = "HTTP/1.0 200 OK\r\nContent-Type: " + type + "\r\nContent-Size: " + to_string(filesz) + "\r\n";
	if (header.length() != write(fd, header.c_str(), header.length())) exit(0);
	len = write(fd, "\r\n", 2);
	if (ErrorCheck(len == -1, "Bad write")) exit(0);

	char* filebuffer = new char[filesz]; // buf to put the file contents into
		
	// get the file to the browser
	in.read(filebuffer, filesz);
	in.close(); // done with file so close it
	len = write(fd, filebuffer, filesz);
	if (ErrorCheck(len == -1, "Bad write")) exit(0);

	delete[] filebuffer; // deallocate the data
	exit(0); // end kid process
}
int main(int argc, char *argv[]) { // main method


	int s; 			// socket descriptor
	int len;		// length of reveived data
	char buf[BUFSIZE];	// buffer in which to read
	int ret;		// return code from various system calls


	s = MakeServerSocket(argv[1]); // make socket

	while (1) { // while program is running 
		struct sockaddr_in sa;
		int sa_len = sizeof(sa);
		int fd = accept(s, (struct sockaddr *)&sa, (unsigned int *)&sa_len); // accept the request
		assert(fd != -1);

		int ret = fork(); // create two connections
		if (ErrorCheck(ret == -1, "Error with fork")) exit(0); // error check
		if (ret == 0) Connection(fd,buf); // kid do work, exit at end of method
		else { // what parent does
			int temp;
			while (waitpid(-1,&temp,WNOHANG) > 0) waitpid(-1,&temp,WNOHANG); // while there is a kid, get the exit code
			close(fd);
		}
	}
}

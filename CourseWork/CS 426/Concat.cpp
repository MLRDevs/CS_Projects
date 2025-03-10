// Alex Miller
// takes files as args and concat the contents into a a new file as the last arg using mmap

#include <iostream>
#include <cstdlib>
#include <string>
#include <sys/mman.h> // mmap
#include <fcntl.h> // open, O_RDONLY, etc
#include <sys/stat.h> // length of file
#include <unistd.h> // close file
#include <cstring> // memcpy
using namespace std;


void ErrorCheck(bool b, string m) { // method for error checking
    if (b) { // if b, then error
        cout << "ERROR: " + m  << endl;
        exit(1);
    }
}
int main(int argc, char** argv) { // main method

    // file size of the output file
    int fs = 0;

    ErrorCheck(argc < 4, "YOU NEED TO ENTER MORE ARGS"); // check to make sure user entered args

    // test if all the files exist and get file sizes
    for (int i=1; i < argc-1; i++) { // go through all the files
        int fd = open(argv[i], O_EXCL, 0);
        ErrorCheck(fd == -1, "FILE DOES NOT EXIST"); // error

        // get file size
        struct stat filestat;
        const char* filename = argv[i];
        ErrorCheck(stat(filename, &filestat) != 0, "GETTING FILE SIZE"); // error

        fs += filestat.st_size;
        close(fd);
    }

    // output file creation
    int ofd = open(argv[argc-1], O_RDWR | O_CREAT | O_EXCL, 0644); // creates output file
    ErrorCheck(ftruncate(ofd, fs) == -1, "OUTPUT FILE ALREADY EXISTS"); // error

    // map the output file
    void *outputfile = mmap(NULL, fs, O_RDWR, MAP_SHARED, ofd, 0);
    ErrorCheck(outputfile == MAP_FAILED, "MAPPING OUTPUT FILE"); // error
    close(ofd);

    // sequential for outputfile
    madvise(outputfile,fs,MADV_SEQUENTIAL);

    int offset = 0; // manage the offset
    for (int i=1; i < argc-1; i++) { // most of the work

        // open the arg
        int ifd = open(argv[i], O_EXCL, 0);
        ErrorCheck(ifd == -1, "FILE DOES NOT EXIST"); // error

        // get the size of the arg file
        struct stat filestat;
        const char* filename = argv[i];
        ErrorCheck(stat(filename, &filestat) != 0, "GETTING FILE SIZE"); // error

        // map the arg file
        void *originfile = mmap(NULL, filestat.st_size, PROT_READ, MAP_PRIVATE, ifd, 0);
        ErrorCheck(originfile == MAP_FAILED, "MAPPING ORIGIN FILE"); // error
        close(ifd);

        // sequential for input file
        madvise(originfile,filestat.st_size,MADV_SEQUENTIAL);

        // copy the contents of the arg file to the output file
        memcpy((char*)outputfile+offset, originfile, filestat.st_size);
        ErrorCheck(munmap(originfile, filestat.st_size) == -1, "ORIGIN MUNMAP FAILED"); // error 
        offset += filestat.st_size; // change offset so no overwriting
    }
    // cleanup
    ErrorCheck(munmap(outputfile, fs) == -1, "OUTPUT MUNMAP FAILED"); // error

    return 0;
}
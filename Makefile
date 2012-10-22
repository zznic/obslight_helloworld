CC=gcc
CFLAGS=-Wall
prefix=/usr

helloworld:	helloworld.o
		$(CC) -o helloworld helloworld.o $(CFLAGS)

helloworld.o:	helloworld.c
		$(CC) -o helloworld.o -c helloworld.c

	

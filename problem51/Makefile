file=testFunc
input = $(patsubst %.c,%.o,$(wildcard *.c))
CC=gcc
CFLAGS=-Wall -Wextra -std=c99 -O3 -g


$(file): $(input) $(file).o

.PHONY: clean run crun cmake
clean:
	-$(RM) $(file) *.o

run: $(file)
	./$(file)

crun:
	make clean
	make run

cmake:
	make clean
	make

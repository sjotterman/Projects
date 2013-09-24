# Makefile for fib


run_fib: run_fib.o fib.o
	g++ -Wall run_fib.o fib.o -o run_fib

run_fib.o: run_fib.cpp fib.h
	g++ -Wall -c run_fib.cpp

fib.o: fib.cc fib.h
	g++ -Wall -c fib.cpp


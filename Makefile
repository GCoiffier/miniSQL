MAINFILE = src/main.py
TESTFILE = src/test.py
PACKAGE = miniSQL_
GRAMMAR = src/parser/miniSQL.g4

ANTLR4 = ~/lib/antlr-4.7-complete.jar

all: run

$(PACKAGE)Visitor.py $(PACKAGE)Lexer.py $(PACKAGE)Lexer.tokens $(PACKAGE)Parser.py $(PACKAGE).tokens : $(GRAMMAR)
	java -jar $(ANTLR4) $< -Dlanguage=Python3 -visitor -no-listener

antlr: $(PACKAGE)Visitor.py $(PACKAGE)Lexer.py

run: $(MAINFILE)
	python3 $<

test: $(TESTFILE)
	python3 $<

clean:
	rm src/parser/__pycache__/*
	rm src/database/__pycache__/*
	rm src/__pycache__/*

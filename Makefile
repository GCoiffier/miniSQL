MAINFILE = src/main.py
PACKAGE = miniSQL_
GRAMMAR = src/parser/miniSQL.g4

ANTLR4 = ~/lib/antlr-4.7-complete.jar

all: run

$(PACKAGE)Listener.py $(PACKAGE)Lexer.py $(PACKAGE)Lexer.tokens $(PACKAGE)Parser.py $(PACKAGE).tokens : $(GRAMMAR)
	java -jar $(ANTLR4) $< -Dlanguage=Python3

antlr: $(PACKAGE)Listener.py $(PACKAGE)Lexer.py

run: $(MAINFILE) antlr
	python3 $<

clean:
	rm src/parser/miniSQL*.py
	rm src/parser/miniSQL*.tokens

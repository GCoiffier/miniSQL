MAINFILE = src/main.py
PACKAGE = miniSQL_
GRAMMAR = src/parser/miniSQL.g4

ANTLR4 = ~/lib/antlr-4.7-complete.jar

all: run

$(PACKAGE)Visitor.py $(PACKAGE)Lexer.py $(PACKAGE)Lexer.tokens $(PACKAGE)Parser.py $(PACKAGE).tokens : $(GRAMMAR)
	java -jar $(ANTLR4) $< -Dlanguage=Python3 -visitor -no-listener

antlr: $(PACKAGE)Visitor.py $(PACKAGE)Lexer.py

run: $(MAINFILE)
	python3 $<

clean:
	rm -f src/parser/miniSQL*.py
	rm -f src/parser/miniSQL*.tokens

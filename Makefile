##
## EPITECH PROJECT, 2021
## B-CNA-410-NAN-4-1-trade-arthur.adam
## File description:
## Makefile
##

NAME            =	searching

RM              =	@rm -f

SOURCES     	=	sources/

PYTEST			=	pytest

all: $(NAME)

$(NAME):
	@cp $(SOURCES)searching.py $@
	@chmod +x $@

clean:
		$(RM) -r __pycache__
		$(RM) -r $(SOURCES)__pycache__

fclean: clean
		$(RM) $(NAME)

tests_run:
		$(PYTEST) -rA . --benchmark-compare

re: fclean all

.PHONY: all clean fclean re

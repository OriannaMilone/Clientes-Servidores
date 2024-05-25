ejecutarMoragon:
	@python3 serv3.py &
	@make compilarC file=$(file)
	@./ejecutable

compilarC:
	@gcc -o ejecutable $(file)
all:
	@echo "Compilación y ejecución de la práctica"

clean:
	@echo "Limpiando..."

save_credential:
	@git config --global credential.helper cache

commit_and_push:
	@git add ../*
	@git commit -am "$(MSG)"
	@git push

commit:
	@$(MAKE) commit_and_push MSG="$(filter-out $@, $(MAKECMDGOALS))"

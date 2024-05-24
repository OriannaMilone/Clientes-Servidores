ejecutarServ:
	@nohup python3 serv5.py > salida.log 2>&1 &

terminarServ:
	@killall python3 serv5.py

ejecutarCli:
	@python3 cli5.py

all:
	@echo "Compilación y ejecución de la práctica"

clean:
	@echo "Limpiando..."

save_credential:
	git config --global credential.helper cache

commit_and_push:
	git add ../*
	git commit -am "$(MSG)"
	git push

commit:
	@$(MAKE) commit_and_push MSG="$(filter-out $@, $(MAKECMDGOALS))"

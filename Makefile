mount:
	sshfs broccoli.floatingeye.net:/home/mlehotay/broccoli broccoli
umount:
	sudo umount broccoli
upload:
	cp main.py broccoli/app/main.py
	cp templates/index.html broccoli/app/templates/index.html
	cp templates/result.html broccoli/app/templates/result.html
make login:
	ssh broccoli.floatingeye.net

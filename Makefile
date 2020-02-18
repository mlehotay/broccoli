mount:
	sshfs broccoli.floatingeye.net:/home/mlehotay/broccoli broccoli
umount:
	sudo umount broccoli
upload:
	cp main.py broccoli/app/main.py
	cp templates/index.html broccoli/app/templates/
	cp templates/result.html broccoli/app/templates/
	cp templates/survey.html broccoli/app/templates/
	cp templates/thankyou.html broccoli/app/templates/
	cp -r images/ broccoli/app/static/
make login:
	ssh broccoli.floatingeye.net

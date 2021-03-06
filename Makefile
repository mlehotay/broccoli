mount:
	sshfs broccoli.floatingeye.net:/home/mlehotay/broccoli broccoli

umount:
	sudo umount broccoli

upload:
	rm -rf broccoli/app/

	mkdir broccoli/app
	cp foods.py broccoli/app/
	cp main.py broccoli/app/

	mkdir broccoli/app/static
	mkdir broccoli/app/static/images
	cp -r images/*.jpg broccoli/app/static/images/

	mkdir broccoli/app/templates
	cp templates/index.html broccoli/app/templates/
	cp templates/recommend.html broccoli/app/templates/
	cp templates/survey.html broccoli/app/templates/
	cp templates/thankyou.html broccoli/app/templates/
	cp templates/gtag.js broccoli/app/templates/

	mkdir broccoli/app/data
	mkdir broccoli/app/data/json
	cp data/db.py broccoli/app/data/
	cp data/foods.csv broccoli/app/data/

download:
	cp -pr broccoli/backup/ .

make login:
	ssh broccoli.floatingeye.net

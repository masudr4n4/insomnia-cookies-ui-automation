build:
	docker login
	docker-compose -f Devops/docker-compose.yml up --build -d

start:
	docker-compose -f Devops/docker-compose.yml up -d	

stop:
	docker-compose -f Devops/docker-compose.yml down

restart: stop start

connect:
	docker-compose -f Devops/docker-compose.yml exec e2e-tests /bin/bash

tests:
	docker-compose -f Devops/docker-compose.yml exec -T e2e-tests pytest -O Linux -U http://web.stage.insomniacookies.com/ -H "True" --junitxml=junit/test-results.xml --alluredir=allure -x --reruns 2 --reruns-delay 3

perm:
	docker-compose -f Devops/docker-compose.yml exec -T e2e-tests chmod 777 -R allure
	docker-compose -f Devops/docker-compose.yml exec -T e2e-tests chmod 777 -R junit

cleanup:
	docker-compose -f Devops/docker-compose.yml exec -T e2e-tests rm -r allure
	docker-compose -f Devops/docker-compose.yml exec -T e2e-tests rm -r junit

single_run:
	docker-compose -f Devops/docker-compose.yml run  -T e2e-tests pytest -O Linux -U http://web.stage.insomniacookies.com/ -H "True" --junitxml=junit/test-results.xml --alluredir=allure -x --reruns 2 --reruns-delay 3

##############################################################################################
# Variables
##############################################################################################

current_dir := $(realpath .)
APP_PATH = ${current_dir}/src/main.py

##############################################################################################
# Commands
##############################################################################################

.PHONY: installations
installations: ## Local needed installations
	@echo Installing needed modules...
	@echo.
	@python -m pip install -r src/config/requirements.txt
	@echo.

.PHONY: snowflake-upload
snowflake-upload: ## Execute basic sql script into snowflake cloud db
	@echo Activating Python Virtual Environment...
	@echo.
	@python ${APP_PATH}


##############################################################################################
# Complex commands
##############################################################################################

.PHONY: build
build: installations snowflake-upload

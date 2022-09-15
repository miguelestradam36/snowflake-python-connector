##############################################################################################
# Variables
##############################################################################################

current_dir := $(realpath .)
APP_PATH = ${current_dir}/src/main.py

##############################################################################################
# Commands
##############################################################################################

.PHONY: create-venv 
create-venv: ## Create pyvenv
	@echo Builiding Python Virtual Environment...
	@python -m venv app\venv
	@echo.

.PHONY: activate-venv
activate-venv: ## Activate pyvenv
	@echo Activating Python Virtual Environment...
	@app\venv\Scripts\activate.bat
	@echo.


##############################################################################################
# Complex commands
##############################################################################################

.PHONY: build
build-venv: installations snowflake-upload

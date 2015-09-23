End-to-end test for ReMind
==========================

The only test so far is an end-to-end regression script which excercises the whole system from front to back. It uses Python and Selenium, running Firefox automatically to simulate a user interacting with the system.

Run on debian based OS
----------------------

	# Install selenium
	virtualenv venv
	source venv/bin/activate
	pip install -r requirements.txt
	
	# Run script
	python systest.py http://localhost:8000

The URL points to the Re:Mind instance to be tested.


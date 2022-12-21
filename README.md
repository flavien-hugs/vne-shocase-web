# PROPERTY MANAGEMENT APPLICATION

This software is a rental management and sales software for real estate and land. It includes a mobile application and a web application.

This application includes:
- Real estate management : Real estate agency interfaces
- Listing of managed properties and landlords
- Census of rental units
- Registration of tenants and their assignment to individual rental units (apartments)
- Registration of deposits and advances
- Recording and tracking of rental payments
- Automatic deduction of Management fees every 10th of the month
- Edition of contracts with lessors
- Editing of lease contracts and settlement receipts
- Alert on payment withdrawals and settlement arrears
- Automatic calculation of penalties on late payments after the 15th of the month (penalty 10% of rent)
- Eviction alert after 3 months passed without payment
- Tenants receive alerts by SMS

- Homeowner Interfaces.
All of the above functionality except for the homeowner registration.
NB: Homeowners do not have the ability to initiate legal proceedings. In fact, in case of non-payment over 3 months, homeowners receive the same alerts as our company, the administrator who takes care of informing his bailiffs to initiate the procedure.

- Global Administrator
- Real estate agency management
- Management of homeowners not affiliated with an agency
- Receive delinquency alerts and eviction notices

NB: all alerts are not only receivable by SMS, but also on the software


## Installation et test

- step 1 : clone the project
	```
  	git clone https://github.com/flavien-hugs/hotel-ministre-website.git
  	```

- step 2 : enter the project directory
  	```
  	cd hotel-ministre-website
  	```

- step 3 : Install dependences
  	```
  	pipenv shell and pipenv install
  	or
  	make install
 	```

- step 4: run project
  	```
  	python run.py
  	```

- step 5: Navigate to:
	```
	http://localhost:5000/
	```


### Credit

Code: [flavien-hugs](https://twitter.com/flavien_hugs)

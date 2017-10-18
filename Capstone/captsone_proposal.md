## Name

Loan Term Compliance Monitoring

## Product Overview

*What is your MVP web app going to do?*

Allow a user to describe loan covenants (such as debt:income ratio < 4;
or debt service coverage ratio > 1.2) for a loan within the portfolio.

The user will then connect to their client's financial data via Intuit's Quickbooks API.
Then the user will be able to identify API outputs as measurements of loan covenants and
that data connection will allow the user to receive alerts for non-compliance


*How does a user interact with it on a high level?*

* Add loan to portfolio
* Create loan covenants
* Choose Quickbooks API outputs as compliance measurements
* View portfolio compliance status in aggregate


## Specific Functionality

Spend some time drawing out on paper mockups _every_ page of your MVP site.

* Home Page (compliance dashboard)
  * view of non-compliance
    * automated list of noncompliance, with details of metric (who, what, when, etc.)
    * automated list of near noncompliance, with details of metric (who, what, when, etc.)
  * view of portfolio data
    * aggregate data, like total portfolio volume, etc.
  * link to add new business
  * link to update existing business
* Create/Edit business
  * update information
  * add new loan
  * edit existing loan
* Create new loan
      * amount, details
      * term, convenants
 * Create Covenants
   * covenants based on operators and conditions
   * chooses datapoint from Quickbooks API to measure covenant
 * update/edit existing loan

TBD:
* Borrower portal/view?
* What interaction does the user need to have with QB API?

~~Annotate _every_ component of the interface _every_ action the user can take.~~

If there is any actions your app needs to take in the background describe _each_ of them and how they change the underlying data your app saves.

**Pick the minimum feature set for your product to work.**
~~Everything else should go in the "further work" section.~~

User selects a datapoint (current ratio) operator (greater than) a measurement (2.0).
User then chooses which datapoint from the Quickbooks API will be used for monitoring.
User sees a dashboard that shows if the current financial statements read compliant or noncompliant.


You don't have to submit the mockup drawings, but do write out a description of _every_ page and component and action.
I literally mean _every_.

## Data Model

~~What are the persistent "nouns" you need to save across pages in your project MVP?~~
~~What do they represent?~~

Store data per loan per business within a portfolio.
Measure against Quickbooks API data.

#### Tables
1. Users
   * login, password, name, email, name of business, title, etc.
2. Businesses
   * name, address, phone, email, loan_name
3. Loans
   * amount, maturity date, payment schedule, loan conditions
4. Loan conditions
   * datapoint, operator, standard (for example: DSCR, greater than, 1.2), noncompliance status, days since compliance
5. Noncompliance
   * loan names, conditions not compliant, degree of noncompliance

We'll be using a relational database which models things like a spreadsheet.
There are fixed fields and every instance

How do you need to _search_ for specific instances of nouns?

## Technical Components

What are the "moving parts" of your MVP?


*  Connection to quickbooks API
*  This big one is going to be accurately identifying what to look for within the quickbooks api.  And to do so through a GUI.
*  database of portfolio
*  dashboard of compliance

What are the things like "modules" you're going to write?



How do they talk to each other?

_Make decisions_ here and now.
Do research and prototyping to figure out what libraries and technologies will help you solve your problems.
Write up which ones you'll use.
It's okay if they end up not working and you have to change your plans.

This is _more specific_ than "Django backend, CSS style, etc."
Please specify what specific technical problems you'll have to solve and a guess at the solution.

## Schedule

Write out the order in which you will tackle your technical components of your MVP.

What are the easy parts?
*  making the shell pages with basic styling. S tshirt.

What are the hard parts?
*  Connecting to Quickbooks API and understanding request returns. L tshirt.
*  Allowing users to easily point to API returns. XL tshirt.
*  Ensuring database tables relate to one another correctly. M tshirt.


Can you guess how long you'll take for each?

Work on the tough and crucial parts first.

## Further Work

All of the above parts are _just addressing your MVP_.
Here you should outline other features you'd like to implement if you get "done" early.
Order them by importance towards your high-level goal and what order you'll work on them later.

Don't work on any of these features until **all of MVP is complete**.
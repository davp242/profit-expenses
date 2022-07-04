# July 2 2022

Goals for Sunday: make menu function with options to enter new profit or new expense. Probably will try
using nested lists? ie profit[[name, address, flt(dollar amount)][name, address, flt(dollar amount)]] etc.
to track them. Create functions for profit and expense entries and focus on getting them to correctly
update the data sets, focus on getting the values to save to something simple like a .txt file eventually
and worry about moving it to a spreadsheet later on. Still afraid to work with fancy APIs

# July 3 2022

Got the framework for creating new orders, but running into a problem when trying to append the list of incomplete orders. If they don't complete the order, it should append the current information into the incomp_orders list, and if they do, it should get the extra information and append it all into the orders list. For some reason even the incomplete orders are still going into orders[] instead of incomp_orders[]. Uploading to github and waiting until I can get advice from more experience coder.

Got it looked at and found out the issue was with parameter names (thank you Matt from WYWM). Also got a piece of advice to try using classes and objects instead of treating them all like nested lists, so I'll try that alongside it (thank you Chris from WYWM)
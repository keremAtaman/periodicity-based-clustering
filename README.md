# periodicity-based-clustering
This project aims to segment online forex customers based on their periodicity - that is, how often they engage with the platform or do trades in the said platform.

1. For each customer, for each day, acquire the data for whether they engaged with the platform and whether they have done a trade
    - NOTE: non-business days may need to be filtered out for better results
2. Run Facebook's Prophet, ARIMA and various other periodicity detecting algorithms on the data. Record the results of each per customer
3. Observe when those algorithms agree or disagree with each other. 
4. For client where the algorithms agree or disagree a lot, manually observe if agreement/disagreement is fair.
    - NOTE: this will require visualization of the data
5. Choose the highest accuracy algo, and use it's data to group customers
6. Observe the groupings (how many groupings there are, are they accurate etc)
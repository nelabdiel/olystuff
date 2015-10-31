# olystuff
This code scrapes the IWF (International Weightlifting Federation) website and pulls the top 1015 lifters' totals and their respective body weights.

Here's the link to the website: http://www.iwf.net/results/ranking-list/?ranking_year=2015&ranking_agegroup=Senior&ranking_gender=M&ranking_category=all&ranking_lifter=all&x=18&y=10

Calculates Sinclair coefficient for every lifter and then records the Sinclair total.

Here's a link with information about the Sinclair Coefficient and the Sinclair total: http://www.iwf.net/wp-content/uploads/downloads/2013/02/Sinclair_Coefficients_2013.pdf

It produces the graph for body weight vs Sinclair total for every weight class.

Then it produces the graph for body weight vs total for all lifters, and the graph for body weight vs Sinclair total for all lifters.

This still is work in progress.

Ultimately the idea would be to develop a better comparison than the sinclair total, for lifters in different weight classes.

What I believe to be the issue with the Sinclair is that it uses as a reference a lifter from the 105+ weight class which, as you can see from the graph is a heavily scattered weight class.

(written for python 3)

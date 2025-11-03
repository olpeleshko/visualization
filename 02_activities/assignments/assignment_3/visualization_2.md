> What software did you use to create your data visualization?

Tableau Public (web)

> Who is your intended audience? 
- City Planners
- Toronto Parking Authority Employees
- Local residents
- Users of parking lots owned by TPA (e.g. commuters, visitors, etc.)
- Taxpayers who may be funding construction and upkeep of parking lots

> What information or message are you trying to convey with your visualization? 
- Identify optimal parking lot capacity to keep peak utilization at appropriate levels (e.g. 50-90%)
- Advocate for building smaller, more sparsely distributed parking lots to better meet parking demand
- Identify outliers with an extremely high utilization that could indicate data entry error or immediate mitigation

> What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots? 
- Use of scatter plot with Total Available spaces for X axis and Average Daily Peak Occupancy % on the Y axis
- Tooltip to provide information about each data point on the plot (parking lot location, Total Available spaces, Average Daily Peak Occupancy %)
- Line of best fit to visualize relationship between the two variables
- Filters by Quarter/Year to interactively explore trends over time

> How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 
The data set is partially reproducible since it was created in Tableau. As such, anyone who attempts to reproduce this data visualization from scratch will need to go through manual steps in Tableau UI to do so.

> How did you ensure that your data visualization is accessible?  
- Used high contrast colours (dark blue / white)
- Ran the map through Colour Blind simulator
- Added tooltips for visual elements

> Who are the individuals and communities who might be impacted by your visualization?
- People who use parking lots (e.g. commuters, visitors, etc.)
- Residents who live close to current or any future parking lots (e.g. because of traffic, construction noise from building new parking lots / demolishing existing ones, idling, etc.)
- Parking lot attendants and parking enforcement officers
- Local businesses

> How did you choose which features of your chosen dataset to include or exclude from your visualization?
- Avg. Average Daily Peak Occupancy %: - key performance metric
- Total Available Spaces - visualize relationship between this metric and Avg. Average Daily Peak Occupancy
- Quarter and/or Year - analyze trends over time

> What ‘underwater labour’ contributed to your final data visualization product?
-  Toronto Parking Authority employees who recorded / collected the data for each parking lot
- Analysts who verified, aggregated and published the data set across parking lots
- Tableau IT teams who build and maintain visualization features
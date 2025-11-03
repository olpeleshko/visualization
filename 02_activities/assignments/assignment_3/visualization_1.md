> What software did you use to create your data visualization?

Tableau Public (web)

> Who is your intended audience? 
- City Planners
- Toronto Parking Authority Employees
- Local residents
- Users of parking lots owned by TPA (e.g. commuters, visitors, etc.)

> What information or message are you trying to convey with your visualization? 
- Identify underserved areas that may need extra parking capacity (Bloordale Village, Spadina Fort York, Cloverdale, etc.)
- Identify areas with underutilized parking capacity (Fairhaven, New Toronto)
- Trends over time (2024 vs. Q1/Q2 2024)

> What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots? 
- Use of an interactive map to allow users to visualize the location of parking lots and their proximity to each other
- Blue/white/red colour pallete (with appropriate thresholds) to highlight under/over-utilized parking lots
- Filters (by utilization, parking capacity, year) to interactively explore data

> How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 
The data set is partially reproducible since it was created in Tableau. As such, anyone who attempts to reproduce this data visualization from scratch will need to go through manual steps in Tableau UI to do so.

> How did you ensure that your data visualization is accessible?  
- Increased the contrast between visual elements and by selecting an appropriate colour pallete and reducing map detail
- Ran the map through Colour Blind simulator
- Added a legend and tooltips for visual elements
- Added filters to allow users increase/decrease number of visual elements as they see fit

> Who are the individuals and communities who might be impacted by your visualization?
- People who use parking lots (e.g. commuters, visitors, etc.)
- Residents who live close to current or any future parking lots (e.g. because of traffic, noise from construcing new parking lots / demolishing existing ones, idling, etc.)
- Parking lot attendants and parking enforcement officers
- Local businesses

> How did you choose which features of your chosen dataset to include or exclude from your visualization?
- Avg. Average Daily Peak Occupancy %: - key performance metric
- Total Available Spaces - allow users to filter based on this attribute to identify trends
- Quarter and Year - allow filters to filter filter based on this attribute to visualize changes over time

> What ‘underwater labour’ contributed to your final data visualization product?
-  Toronto Parking Authority employees who recorded / collected the data for each parking lot
- Analysts who verified, aggregated and published the data set across parking lots
- Tableau IT teams who build and maintain visualization features
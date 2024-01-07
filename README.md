
# Fear, volatility and the new normal of the german Day-Ahead-Auction
## An analysis of prices in 2023, 2022 and the time before

The last two years have been like no other in Europe's electricity markets. A war in Ukraine, the ongoing energy revolution with increasing renewable energy feed-in, unstable weather conditions and the shutdown of nuclear power plants are just some of the upheavals in European power markets. In this analysis, I would like to take a closer look at the German Day-Ahead-Auction prices. This analysis does not claim to be complete or comprehensive in tracking all price-influencing events, but it does try to give some statistical insight into how the price level has changed over time.

#### Price levels

In the following visualisations, I have analysed data from the beginning of 2020 to the end of 2023. First, to get an understanding of the general long-term price level, the German Day-Ahead-Auction Price is plotted. For this graph, the daily average price has been calculated to smooth out the daily price fluctuations, which can be caused by hour-specific demand, renewable production, or other fundamental price drivers.

![Figure 1: Price Levels](https://github.com/marlonmei/DayAhead/blob/main/images/image1_price_over_time.png)

In 2020, the price level was relatively stable throughout the year at around 30 EUR/MWh. However, due to the pandemic and the resulting decrease in electricity consumption, especially in the industrial and commercial sector, prices fell in early spring. After slowly recovering to pre-pandemic levels, prices rose rapidly at the end of 2021.This was mainly due to increased demand for electricity as a result of the rapid economic recovery following the relaxation of pandemic regulations. 
By this point, prices had already tripled compared to pre-pandemic levels. In 2022, electricity markets finally went haywire. In February, Russia invaded Ukraine, which led to an ongoing war between the two countries and severely disrupted global energy markets. During this time, Russia was the most important supplier of natural gas, accounting for around 40% of Germany's natural gas imports. With the start of the war in Europe, this supply wasn't guaranteed and, in time, wasn't wanted. In 2022, gas-fired power plants were responsible for around 10% of electricity generation, so the commodity price also had a strong impact on the electricity markets. The 2022 auction peak price of 871 EUR/MWh was reached on 29 August. This is an increase of more than 7 times compared to the peak price of 2019.
After another price peak at the end of 2022, prices seem to have normalised again in 2023. However, at an average of around 100 EUR/MWh, the price level is still significantly higher than during the pandemic or before.

### Volatility

Looking at these price developments, the price volatility in 2022 is particularly striking. Accordingly, I have calculated some measures of dispersion to quantify the volatility. Figure 2 shows the daily spread between the maximum and minimum price.

![Figure 2: Price Spreads](https://github.com/marlonmei/DayAhead/blob/main/images/image2_price_spread.png)

It shows that during the 24 hours of a day, the price range used to be around 30-50 EUR/MWh. Similar to the overall price level, this value has risen sharply in 2022, with spreads of 300-400 EUR/MWh occurring regularly. Spreads during the day are particularly interesting for flexibility providers such as battery storage operators. These providers can use price spreads for arbitrage trades.

![Figure 3: Standard Deviation](https://github.com/marlonmei/DayAhead/blob/main/images/image3_standard_deviation.png)

Another measure of dispersion is the standard deviation, which quantifies the amount by which prices vary from their mean and is a common indicator of volatility in financial markets. Figure 3 shows the hourly standard deviation for each month. Similar to the previous graphs, volatility was highest in 2023. As the indicator is calculated on an hourly basis for each month, volatility peaks during the day are also visible. In the morning and evening, volatility peaks are caused by particularly high residential demand. These peaks were very noticeable in March, June or October 2022. This spike in demand during certain hours has not been a major issue in the past, as the 2020 data shows, but it can significantly increase volatility in a year like 2022.

![Figure 4: Frequency Distribution](https://github.com/marlonmei/DayAhead/blob/main/images/image4_frequency_distribution.png)

Finally, Figure 4 shows the frequency distribution of the day-ahead auction prices for each year. In 2020, the histogram is clearly normally distributed. In 2021, this distribution flattens and becomes skewed to the right, mainly due to the volatile prices at the end of the year. The flattening and shift to higher prices is then reinforced in 2022, to the point where prices are almost uniformly distributed. Finally, in 2023, a mixture of a bimodal and a normal distribution is outlined, with most prices around the 100 EUR/MWh average, but also a small peak around 0 EUR/MWh.

### Negative Prices

The previous figures already showed that prices also go negative for several hours a year. Negative prices are usually caused by very low demand and high feed-in of renewable energy. A sunny and windy weekend day, for example, can quickly lead to negative prices.

![Figure 5: Negative Hours](https://github.com/marlonmei/DayAhead/blob/main/images/image5_negative_hours.png)

Figure 5 visualises the number of negative hours per week. Obviously, weeks with generally high price levels have fewer hours with negative prices, as the data for the end of 2021 and the whole of 2022 show. Overall, 2023 was the year with the most hours with negative prices. At the end of that year, very windy conditions in December were responsible for a high production of wind power plants. However, this is a constant throughout the year. At the end of the year, during the Christmas period, prices turn negative. This is a time when commercial and industrial demand is particularly low. If the low demand is combined with windy days like in 2023, prices can be negative for longer periods.

![Figure 6: Consecutive Hours](https://github.com/marlonmei/DayAhead/blob/main/images/image6_consecutive_negative_hours.png)

Since 2014, the EEG has introduced a rule that if the price is negative for 6 consecutive hours, the power plant operator is not rewarded with a market premium. The 2021 EEG tightens this rule by lowering the cap to 4 consecutive hours. The aim of the rule is to encourage renewable power plants to withdraw from the market during these hours, as they are typically responsible for negative prices. As price levels have normalized in 2023, the number of consecutive six-hour periods with negative prices has also increased, as shown in Figure 6.

### Summary

To sum up, we have seen another unique year for electricity price developments in 2023. The overall price level as well as the volatility of the Day-Ahead Auction prices are still significantly higher than in the period before the outstanding developments in 2022. The increasing share of renewables increases this volatility and is also responsible for the high number of hours with negative prices.

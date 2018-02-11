function main(svg, data, params, viewWidth, viewHeight)
{
  var margin = {top: 20, right: 30, bottom: 30, left: 40},
      width = viewWidth - margin.left - margin.right,
      height = viewHeight - margin.top - margin.bottom;

   // from: https://bl.ocks.org/d3noob/bdf28027e0ce70bd132edc64f1dd7ea4
   var x = d3.scaleBand()
              .range([0, width])
              .padding(0.1);
    var y = d3.scaleLinear()
              .range([height, 0]);

    // append the svg object to the body of the page
    // append a 'group' element to 'svg'
    // moves the 'group' element to the top left margin
    var chart = svg
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform",
              "translate(" + margin.left + "," + margin.top + ")");


      // format the data
      data.forEach(function(d) {
        d.y = +d.y;
      });

      // Scale the range of the data in the domains
      x.domain(data.map(function(d) { return d.x; }));
      y.domain([0, d3.max(data, function(d) { return d.y; })]);

      // append the rectangles for the bar chart
      chart.selectAll(".bar")
          .data(data)
        .enter().append("rect")
          .attr("fill", "steelblue")
          .attr("x", function(d) { return x(d.x); })
          .attr("width", x.bandwidth())
          .attr("y", function(d) { return y(d.y); })
          .attr("height", function(d) { return height - y(d.y); });

      // add the x Axis
      chart.append("g")
          .attr("transform", "translate(0," + height + ")")
          .call(d3.axisBottom(x));

      // add the y Axis
      chart.append("g")
          .call(d3.axisLeft(y).ticks(10));
}

import React from 'react';
import { ChartComponent, SeriesCollectionDirective, SeriesDirective, Inject, LineSeries, DateTime, Legend, Tooltip } from '@syncfusion/ej2-react-charts';

// import { lineCustomSeries } from '../../data/dummy';
import { useStateContext } from '../../contexts/ContextProvider';

const LineChart = ({ data, y, yT, cname, ymax, yi }) => {
  const { currentMode } = useStateContext();
  const lineCustomSeries = [{
    dataSource: data,
    xName: 'segment',
    yName: y,
    name: cname,
    width: '2',
    marker: { visible: true, width: 10, height: 10 },
    type: 'Line',
  }];

  return (
    <ChartComponent
      id="line-chart"
      height="420px"
      primaryXAxis={{ valueType: 'Double', title: 'Segment', labelFormat: '{value}', minimum: 0, maximum: 15, interval: 1 }}
      primaryYAxis={{ title: yT, rangePadding: 'None', minimum: 0, maximum: ymax, interval: yi, labelFormat: '{value}', lineStyle: { width: 0 }, majorTickLines: { width: 0 }, minorTickLines: { width: 0 } }}
      font
      chartArea={{ border: { width: 0 } }}
      tooltip={{ enable: true }}
      background={currentMode === 'Dark' ? '#33373E' : '#fff'}
      legendSettings={{ background: 'white' }}
    >
      <Inject services={[LineSeries, DateTime, Legend, Tooltip]} />
      <SeriesCollectionDirective>
        {/* eslint-disable-next-line react/jsx-props-no-spreading */}
        {lineCustomSeries.map((item, index) => <SeriesDirective key={index} {...item} />)}
      </SeriesCollectionDirective>
    </ChartComponent>
  );
};

export default LineChart;

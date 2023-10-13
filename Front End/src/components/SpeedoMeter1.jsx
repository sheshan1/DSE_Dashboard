import React from 'react';
import ReactSpeedometer from 'react-d3-speedometer';

export default function Speedometer({ value }) {
  const options = {
    minValue: 0,
    maxValue: 10,
    segments: 10,
    valueFormat: '.1f',
    customSegmentStops: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    segmentColors: [
      '#a9d70b',
      '#f9c802',
      '#ff0000',
    ],
  };

  return (
    <ReactSpeedometer
      value={value}
      minValue={options.minValue}
      maxValue={options.maxValue}
      segments={options.segments}
      valueFormat={options.valueFormat}
      customSegmentStops={options.customSegmentStops}
      segmentColors={options.segmentColors}
      needleTransition="easeBounceInOut"
      needleTransitionDuration={3000}
    />
  );
}

import React from 'react';
import Speedometer from 'react-d3-speedometer';

export default function SpeedoMeter({ speed }) {
  return (
    <div>
      <Speedometer
        value={speed}
        minValue={0}
        maxValue={60}
        valueFormat="d"
        needleColor="red"
        startColor="green"
        maxSegmentLabels={6}
        segments={10}
        endColor="red"
        width={400}
        labelFontSize={13}
        valueTextFontSize={20}
        valueTextFontWeight={350}
        needleTransition="easeBounceInOutcd "
        paddingHorizontal={15}
        paddingVertical={15}
        needleTransitionDuration={3000}
        currentValueText={`Speed: ${speed.toFixed(2)} km/h`}
        currentValuePlaceholderStyle="#{value}"
        arcLength={360} // Set the arc length to 360 degrees
        // forceRender="true"
        // fluidWidth="true"
      />
    </div>
  );
}

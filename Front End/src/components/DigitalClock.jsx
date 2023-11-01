import React from 'react';
import Typography from '@mui/material/Typography';

const clockStyle = {
  // border: '5px solid #000',
  // borderRadius: '5%',
  padding: '1%',
  width: '300px',
  // height: '60%',
  textAlign: 'center',
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'center',
};

const DigitalClock = ({ time, busStop }) => (
  <div style={clockStyle}>
    <Typography variant="h5">
      <p style={{ fontSize: '1.2em' }}>Arrival Time to</p>
      <p style={{ fontSize: '1.3em', color: 'blue' }}>{busStop}</p>
      <p style={{ fontSize: '1.2em' }}>Bus Stop</p>
      <p style={{ fontSize: '1.4em', color: 'red' }}>{time}</p>
    </Typography>
  </div>
);
export default DigitalClock;

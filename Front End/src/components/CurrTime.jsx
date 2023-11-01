import React from 'react';
import Typography from '@mui/material/Typography';

const clockStyle = {
  // border: '1px solid #000',
  // borderRadius: '5%',
  padding: '1%',
  width: '300',
  // height: '60%',
  textAlign: 'center',
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'center',
};

const CurrTime = ({ ctime }) => (
  <div style={clockStyle}>
    <Typography variant="h4">
      <p style={{ fontSize: '0.8em' }}>Current Time</p>
      <p style={{ fontSize: '1.2em', color: 'blue' }}>{ctime}</p>
    </Typography>
  </div>
);
export default CurrTime;

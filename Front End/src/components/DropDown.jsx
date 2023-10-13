import React, { useState, useEffect } from 'react';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormHelperText from '@mui/material/FormHelperText';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import APIService from '../APIs/APIService';

export default function DropDown({ onSelect }) {
  const [busId, setbusId] = React.useState('');
  const [deviceIds, setDeviceIds] = useState([]);

  const handleChange = (event) => {
    const selectedValue = event.target.value;
    setbusId(selectedValue);
    onSelect(event);
  };

  useEffect(() => {
    // Make API call to get unique device IDs
    APIService.getDeviceIds()
      .then((data) => setDeviceIds(data))
      .catch((error) => console.error('Error:', error));
  }, []);

  return (
    <div>
      <FormControl required sx={{ m: 1, minWidth: 200 }}>
        <InputLabel id="demo-simple-select-required-label">Select a Bus</InputLabel>
        <Select
          labelId="demo-simple-select-required-label"
          id="demo-simple-select-required"
          value={busId}
          label="busId *"
          onChange={handleChange}
        >
          <MenuItem value="">None</MenuItem>
          {deviceIds && deviceIds.map((deviceId) => (
            <MenuItem key={deviceId} value={deviceId}>
              {deviceId}
            </MenuItem>
          ))}
        </Select>
        <FormHelperText>Required</FormHelperText>
      </FormControl>
    </div>
  );
}

import React, { useEffect, useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import '../App.css';
import L from 'leaflet';
import bus from '../data/bus-solid.svg';
import busRed from '../data/bus-solid-red.svg';
// import bus_red from '../data/bus-solid-red.svg';
import DropDown from '../components/DropDown';
import SpeedoMeter from '../components/SpeedoMeter';
import APIService from '../APIs/APIService';

const OpenSMap = () => {
  const [busStops, setBusStops] = useState([]);
  const [speed, setSpeed] = useState(0);
  const [busesData, setBusesData] = useState([]);
  const [busData, setBusData] = useState();
  const [selectedDeviceId, setSelectedDeviceId] = useState();
  const busIcon = new L.Icon({ iconUrl: bus, iconSize: [32, 32], iconAnchor: [16, 32], popupAnchor: [0, -32] });
  const selected = new L.Icon({ iconUrl: busRed, iconSize: [32, 32], iconAnchor: [16, 32], popupAnchor: [0, -32] });

  const handleBusSelect = (event) => {
    const selectedValue = event.target.value;
    setSelectedDeviceId(selectedValue);
    // console.log(selectedDeviceId);
    if (selectedValue === '') {
      setBusData(null); // or setBusData({})
    }
  };

  const getData = () => {
    APIService.getAllBusData()
      .then((res) => {
        if (res && res.length > 0) {
          setBusesData(res);
        }
      })
      .catch((err) => {
        console.error(err);
      });

    if (selectedDeviceId) {
      console.log(selectedDeviceId);
      APIService.getBusData(selectedDeviceId)
        .then((res) => {
          setBusData(res);
          setSpeed(res.speed);
        })
        .catch((err) => {
          console.error(err);
        });
    } else {
      // setBusData('None');
      setSpeed(0);
    }
  };

  useEffect(() => {
    // Initial load of bus stops
    APIService.getBusStops()
      .then((res) => {
        setBusStops(res);
      })
      .catch((err) => {
        console.error(err);
      });

    // Fetch bus data every 1 second
    const interval = setInterval(getData, 1000);

    return () => clearInterval(interval); // Clear interval on component unmount
  }, [selectedDeviceId]);

  return (
    <div>
      <div><DropDown onSelect={handleBusSelect} /></div>
      <MapContainer center={[7.29246, 80.635]} zoom={13}>
        <TileLayer
          attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.osm.org/{z}/{x}/{y}.png"
        />
        {busStops.map((stop) => (
          <Marker
            key={stop.id}
            position={[stop.latitude, stop.longitude]}
          >
            <Popup>
              <div>
                <strong>Address:</strong> {stop.address}<br />
                <strong>Direction:</strong> {stop.direction}<br />
                <strong>Stop ID:</strong> {stop.stop_id}<br />
                <strong>Route ID:</strong> {stop.route_id}<br />
              </div>
            </Popup>
          </Marker>
        ))}
        {busesData.map((data) => (
          <Marker
            key={data.deviceid}
            position={[data.latitude, data.longitude]}
            icon={busIcon}
          >
            <Popup>
              <div>
                <strong>Bus ID:</strong> {data.id}<br />
                <strong>Device ID:</strong> {data.deviceid}<br />
                <strong>Route ID:</strong> {data.routeid}<br />
                <strong>Speed:</strong> {data.speed}<br />
                <strong>Time:</strong> {data.time}<br />
                <strong>Latitude:</strong> {data.latitude}<br />
                <strong>Longitude:</strong> {data.longitude}<br />
                <strong>Direction:</strong> {data.direction}<br />
              </div>
            </Popup>
          </Marker>
        ))}
        {busData && (
          <Marker
            key={busData.deviceid}
            position={[busData.latitude, busData.longitude]}
            icon={selected}
          >
            <Popup>
              <div>
                <strong>Bus ID:</strong> {busData.id}<br />
                <strong>Device ID:</strong> {busData.deviceid}<br />
                <strong>Route ID:</strong> {busData.routeid}<br />
                <strong>Speed:</strong> {busData.speed}<br />
                <strong>Time:</strong> {busData.time}<br />
                <strong>Latitude:</strong> {busData.latitude}<br />
                <strong>Longitude:</strong> {busData.longitude}<br />
                <strong>Direction:</strong> {busData.direction}<br />
              </div>
            </Popup>
          </Marker>
        )}
      </MapContainer>
      <div>
        {selectedDeviceId && <SpeedoMeter speed={speed} />}
      </div>
    </div>
  );
};

export default OpenSMap;

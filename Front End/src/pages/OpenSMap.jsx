import React, { useEffect, useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import './styles.css';
import L from 'leaflet';
import avatar from '../data/bus-solid (1).svg';
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
// import { faBus } from '@fortawesome/free-solid-svg-icons';
// // import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
// // import { faEnvelope } from '@fortawesome/free-solid-svg-icons';
import APIService from '../APIs/APIService';

const OpenSMap = () => {
  const [busStops, setBusStops] = useState([]);
  const [busData, setBusData] = useState(null);
  const stopIcon = new L.Icon({ iconUrl: avatar, iconSize: [32, 32], iconAnchor: [16, 32], popupAnchor: [0, -32] });

  useEffect(() => {
    // Initial load of bus stops
    APIService.getBusStops()
      .then((res) => {
        setBusStops(res);
      })
      .catch((err) => {
        console.error(err);
      });

    // Fetch bus data every 3 seconds
    const interval = setInterval(() => {
      APIService.getBusData()
        .then((res) => {
          setBusData(res.data);
        })
        .catch((err) => {
          console.error(err);
        });
    }, 3000);

    return () => clearInterval(interval); // Clear interval on component unmount
  }, []);

  return (
    <div>
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
        {busData && (
          <Marker
            position={[busData.latitude, busData.longitude]}
            icon={stopIcon}
          >
            <Popup>
              <div>
                <strong>Bus ID:</strong> {busData.id}<br />
                <strong>Device ID:</strong> {busData.deviceid}<br />
                {/* Add other bus data fields here */}
              </div>
            </Popup>
          </Marker>
        )}
      </MapContainer>
    </div>
  );
};

export default OpenSMap;

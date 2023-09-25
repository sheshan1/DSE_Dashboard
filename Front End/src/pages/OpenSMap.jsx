import React, { useEffect, useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import './styles.css';
import APIService from '../APIs/APIService';

const OpenSMap = () => {
  const [busStops, setBusStops] = useState([]);

  useEffect(() => {
    APIService.getBusStops().then((res) => {
      setBusStops(res);
    })
      .catch((err) => {
        console.error(err);
      });
  }, []);

  return (
    <div>
      <MapContainer center={[7.29246, 80.635]} zoom={13}>
        <TileLayer
          attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.osm.org/{z}/{x}/{y}.png"
        />
        {busStops.map((stop) => (
          <Marker key={stop.id} position={[stop.latitude, stop.longitude]}>
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
      </MapContainer>
    </div>
  );
};

export default OpenSMap;

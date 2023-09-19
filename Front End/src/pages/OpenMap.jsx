import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import './styles.css';

const OpenMap = () => {
  const locations = [[7.29119, 80.6377], [7.29246, 80.635]];

  return (
    <div>
      <MapContainer center={[7.29246, 80.635]} zoom={13}>
        <TileLayer
          attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.osm.org/{z}/{x}/{y}.png"
        />
        {locations.map((location) => (
          <Marker key={location} position={location}>
            <Popup>
              A pretty CSS3 popup. <br /> Easily customizable.
            </Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
  );
};

export default OpenMap;

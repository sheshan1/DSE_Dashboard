import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import './styles.css';
// import { Header } from '../components';

const OpenMap = () => (
  <div>
    {/* <Header category="App" title="OpenMap" /> */}
    <MapContainer center={[51.505, -0.091]} zoom={13}>
      <TileLayer
        attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.osm.org/{z}/{x}/{y}.png"
      />
      <Marker position={[51.505, -0.091]}>
        <Popup>
          A pretty CSS3 popup. <br /> Easily customizable.
        </Popup>
      </Marker>
    </MapContainer>
  </div>
);

export default OpenMap;

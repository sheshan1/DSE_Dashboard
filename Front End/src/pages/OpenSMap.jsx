import React, { useEffect, useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import '../App.css';
import L from 'leaflet';
// import { Clock } from '../components/Clock';
import bus from '../data/bus-solid.svg';
import busRed from '../data/bus-solid-red.svg';
import DropDown from '../components/DropDown';
import SpeedoMeter from '../components/SpeedoMeter';
import DigitalClock from '../components/DigitalClock';
import CurrTime from '../components/CurrTime';
import APIService from '../APIs/APIService';
import { LineChart } from '../components';

const OpenSMap = () => {
  const [busStops, setBusStops] = useState([]);
  const [speed, setSpeed] = useState(0);
  const [time, setTime] = useState(0);
  const [busStop, setBusStop] = useState();
  const [ctime, setCtime] = useState(0);
  const [busesData, setBusesData] = useState([]);
  const [segmentcluste, setSegmentcluste] = useState([]);
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
    APIService.getCurrTime()
      .then((res) => {
        setCtime(res.current_time);
      })
      .catch((err) => {
        console.error(err);
      });

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
      APIService.getBusData(selectedDeviceId)
        .then((res) => {
          setBusData(res);
          setSpeed(res.speed);
          setTime(res.predicted_time);
        })
        .catch((err) => {
          console.error(err);
        });
    } else {
      // setBusData('None');
      setSpeed(0);
    }

    if (selectedDeviceId) {
      APIService.getBusStop(selectedDeviceId)
        .then((res) => {
          setBusStop(res.bus_stop);
        })
        .catch((err) => {
          console.error(err);
        });
    } else {
      // setBusData('None');
      setSpeed(0);
    }

    if (selectedDeviceId) {
      APIService.getSegmentCluster(selectedDeviceId)
        .then((res) => {
          setSegmentcluste(res);
        })
        .catch((err) => {
          console.error(err);
        });
    } else {
      setSegmentcluste([]);
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
      <div className="flex gap-10 m-4 flex-wrap justify-center">
        <div className="bg-white dark:text-gray-200 dark:bg-secondary-dark-bg p-4 rounded-2xl flex justify-center items-center">
          <div className="flex justify-between items-center gap-8">
            <p className="text-xl font-semibold">Track a Bus</p>
            <span><DropDown onSelect={handleBusSelect} /></span>
          </div>
        </div>
        <div className="bg-white dark:text-gray-200 dark:bg-secondary-dark-bg p-4 rounded-2xl flex justify-center items-center">
          <div className="flex justify-between items-center gap-5 mb-8">
            <CurrTime ctime={ctime} />
          </div>
        </div>
      </div>

      <div className="bg-white dark:text-gray-200 dark:bg-secondary-dark-bg p-6 rounded-2xl">
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
                  <strong>Device ID:</strong> {data.deviceid}<br />
                  <span style={{ color: 'red' }}>
                    <strong>Arrivel Time:</strong> {data.predicted_time}<br />
                  </span>
                  <strong>Speed:</strong> {data.speed}<br />
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
                  <strong>Device ID:</strong> {busData.deviceid}<br />
                  <strong>Arrival Time:</strong>{busData.predicted_time}<br />
                  <strong>Speed:</strong> {busData.speed}<br />
                  <strong>Latitude:</strong> {busData.latitude}<br />
                  <strong>Longitude:</strong> {busData.longitude}<br />
                  <strong>Direction:</strong> {busData.direction}<br />
                  <strong>Acceleration:</strong> {busData.acceleration}<br />
                </div>
              </Popup>
            </Marker>
          )}
        </MapContainer>
      </div>

      <div className="flex gap-10 m-5 flex-wrap justify-center">
        <div className="bg-white dark:text-gray-200 dark:bg-secondary-dark-bg p-4 rounded-2xl flex justify-center items-center">
          {selectedDeviceId && <SpeedoMeter speed={speed} className="mr-4" />}
        </div>
        <div className="bg-white dark:text-gray-200 dark:bg-secondary-dark-bg p-6 rounded-2xl flex justify-center items-center">
          {selectedDeviceId && <DigitalClock time={time} busStop={busStop} />}
        </div>
        <div className="bg-white dark:text-gray-200 dark:bg-secondary-dark-bg p-4 rounded-2xl flex justify-center items-center">
          {selectedDeviceId && <LineChart data={segmentcluste} y="norm_cluster" yT="Cluster Label" cname="Clusters" ymax={2} yi={1} />}
          <div>
            {selectedDeviceId && <p style={{ fontSize: '1.2em', color: 'green', fontWeight: 'bold' }}>Cluster 0: Typical</p>}
            {selectedDeviceId && <p style={{ fontSize: '1.2em', color: 'green', fontWeight: 'bold' }}>Cluster 1: High-Intensity</p>}
            {selectedDeviceId && <p style={{ fontSize: '1.2em', color: 'green', fontWeight: 'bold' }}>Cluster 2: Low-Intensity</p>}
          </div>
        </div>
      </div>
    </div>
  );
};

export default OpenSMap;

export default class APIService {
  static getBusStops() {
    return fetch('http://127.0.0.1:5000/map', {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    })
      .then((resp) => resp.json());
  }

  static getBusData(deviceid) {
    return fetch(`http://127.0.0.1:5000/get_data/${deviceid}`, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    })
      .then((resp) => resp.json());
  }

  static getDeviceIds() {
    return fetch('http://127.0.0.1:5000/get_deviceids', {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    })
      .then((resp) => resp.json());
  }

  static getAllBusData() {
    return fetch('http://127.0.0.1:5000/get_matching_data', {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    })
      .then((resp) => resp.json());
  }

  static getCurrTime() {
    return fetch('http://127.0.0.1:5000/get_currentTime', {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    })
      .then((resp) => resp.json());
  }

  static getSegmentCluster(deviceid) {
    return fetch(`http://127.0.0.1:5000/get_normCluster/${deviceid}`, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    })
      .then((resp) => resp.json());
  }

  static getBusStop(deviceid) {
    return fetch(`http://127.0.0.1:5000/get_busstop/${deviceid}`, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    })
      .then((resp) => resp.json());
  }

  static getAvgSpeed() {
    return fetch('http://127.0.0.1:5000/get_avgSpeed', {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    })
      .then((resp) => resp.json());
  }
}

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
}

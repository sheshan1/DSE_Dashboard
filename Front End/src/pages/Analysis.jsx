import React, { useEffect, useState } from 'react';
import { LineChart } from '../components';
import APIService from '../APIs/APIService';

const Analysis = () => {
  const [avgSpeed, setAvgSpeed] = useState(0);

  useEffect(() => {
    APIService.getAvgSpeed()
      .then((res) => {
        setAvgSpeed(res);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div className="mt-24">
      <div className="flex gap-10 m-4 flex-wrap justify-center">
        <div className="bg-white dark:text-gray-200 dark:bg-secondary-dark-bg p-6 rounded-2xl w-400 md:w-1200">
          <div className="flex justify-between items-center gap-2 mb-10">
            <p className="text-xl font-semibold">Average Speed of Segments</p>
          </div>
          <div className="md:w-full overflow-auto flex justify-center items-center gap-2 mb-10">
            <LineChart data={avgSpeed} y="avg_speed" yT="Average Speed (Kmph)" cname="Average Speed of Segments" ymax={14} yi={2} />
            <div>
              <p style={{ fontSize: '1em', color: 'Blue', fontWeight: 'bold' }}>Segment Names</p>
              <p style={{ fontSize: '1em', color: 'black' }}>1: Kandy - Wales Park</p>
              <p style={{ fontSize: '1em', color: 'black' }}>2: Wales Park - Mahamaya</p>
              <p style={{ fontSize: '1em', color: 'black' }}>3: Mahamaya - Lewella junction</p>
              <p style={{ fontSize: '1em', color: 'black' }}>4: Lewella junction - Talwatta</p>
              <p style={{ fontSize: '1em', color: 'black' }}>5: Talwatta - Tennekumbura Bridge</p>
              <p style={{ fontSize: '1em', color: 'black' }}>6: Tennekumbura Bridge - Kalapura Junction Busstop</p>
              <p style={{ fontSize: '1em', color: 'black' }}>7: Kalapura Junction Busstop - Nattarampotha Junction Bus Stop</p>
              <p style={{ fontSize: '1em', color: 'black' }}>8: Nattarampotha Junction Bus Stop - Kundasale New town</p>
              <p style={{ fontSize: '1em', color: 'black' }}>9: Kundasale New town - Warapitiya</p>
              <p style={{ fontSize: '1em', color: 'black' }}>10: Warapitiya - Pallekele</p>
              <p style={{ fontSize: '1em', color: 'black' }}>11: Pallekele - Pachchakaatuwa</p>
              <p style={{ fontSize: '1em', color: 'black' }}>12: Pachchakaatuwa - Balagolla</p>
              <p style={{ fontSize: '1em', color: 'black' }}>13: Balagolla - BOI</p>
              <p style={{ fontSize: '1em', color: 'black' }}>14: BOI - Kengalla</p>
              <p style={{ fontSize: '1em', color: 'black' }}>15: Kengalla - Digana</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Analysis;

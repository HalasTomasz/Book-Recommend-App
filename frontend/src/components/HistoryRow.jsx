import React from 'react'
import HistorySlicer from './HistorySlicer'
import { MdChevronLeft, MdChevronRight } from 'react-icons/md';

export default function HistoryRow({list}) {
  const slideLeft = () => {
    var slider = document.getElementById('slider' + 10);
    slider.scrollLeft = slider.scrollLeft - 500;
  };
  
  const slideRight = () => {
    var slider = document.getElementById('slider' + 10);
    slider.scrollLeft = slider.scrollLeft + 500;
  };

  return (
    <div className='relative flex items-center group'>
      <MdChevronLeft
        onClick={slideLeft}
        className='bg-white left-0 rounded-full absolute opacity-50 hover:opacity-100 cursor-pointer z-10 hidden group-hover:block'
        size={40}
      />
      <div
        id={'slider'+10}
        className='w-full h-full overflow-x-scroll whitespace-nowrap scroll-smooth scrollbar-hide relative'
      >
        {list.map((item, id) => (
            <HistorySlicer key={id} item={item} />
          ))}
      </div>

      <MdChevronRight
        onClick={slideRight}
        className='bg-white right-0 rounded-full absolute opacity-50 hover:opacity-100 cursor-pointer z-10 hidden group-hover:block'
        size={40}
      />
    </div>
  );
};


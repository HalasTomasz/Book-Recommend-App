import React, { useEffect, useState } from 'react';
import BookSlicer from './BookSlicer';
import { MdChevronLeft, MdChevronRight } from 'react-icons/md';


export default function Row({title, list, rowID }) {
    
  const [book, setBooks] = useState([]);

  useEffect(() => {
    setBooks(list);
  }, [list]);

  const slideLeft = () => {
    var slider = document.getElementById('slider' + rowID);
    slider.scrollLeft = slider.scrollLeft - 500;
  };

  const slideRight = () => {
    var slider = document.getElementById('slider' + rowID);
    slider.scrollLeft = slider.scrollLeft + 500;
  };


  return (
    <>
      <h2 className='text-white font-bold md:text-xl p-4'>{title}</h2>
      <div className='relative flex items-center group'>
        <MdChevronLeft
          onClick={slideLeft}
          className='bg-white left-0 rounded-full absolute opacity-50 hover:opacity-100 cursor-pointer z-10 hidden group-hover:block'
          size={40}
        />
        <div
          id={'slider' + rowID}
          className='w-full h-full overflow-x-scroll whitespace-nowrap scroll-smooth scrollbar-hide relative'
        >
          {book.map((item, id) => {
             if (item.Alogritm_ID === parseInt(rowID,10)) {
              return <BookSlicer key={id} item={item} />
             }
             return null
          })}
        </div>
        <MdChevronRight
          onClick={slideRight}
          className='bg-white right-0 rounded-full absolute opacity-50 hover:opacity-100 cursor-pointer z-10 hidden group-hover:block'
          size={40}
        />
      </div>
    </>
  );
};


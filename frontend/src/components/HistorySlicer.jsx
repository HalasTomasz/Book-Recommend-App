import React from 'react'
import { useState } from 'react';
import { useDispatch } from 'react-redux';
import {returnHistoryBook} from '../actions/historyAction'
export default function HistorySlicer({item}) {
    console.log(item)
    const date = item.Date_Taken.substr(0, 10)
    const [returned,SetReturned] = useState(item.Returned)
    const dispatch = useDispatch()

    function returnBook(){

        dispatch(returnHistoryBook(item.Book_ID,item.AllRenatls_ID))
        SetReturned(!returned)
    }
  return (

      <div className='w-[160px] max-[640px]:h-60 sm:h-64 md:h-72 lg:h-96 sm:w-[200px] md:w-[240px] lg:w-[280px] inline-block cursor-pointer relative p-2'>
        <img
          className='w-full  h-full block '
          src={item.Book_Image}
          alt={item?.Name}
        />
        <div  className='absolute top-0 left-0 w-full h-full hover:bg-black/60 opacity-0 hover:opacity-100 text-white overflow-auto'>
        <p className='whitespace-normal text-xs md:text-sm font-bold h-full text-center flex justify-center items-center'>
          {item?.Name}
        </p>
        <p>
        </p>
      </div>
      {!returned &&
          <button 
            onClick={returnBook}
            className="w-full h-auto bg-black text-[#00df9a]  rounded-md font-medium pt-2 mt-2 mb-1 inline-block">
              Return Book
          </button>}
          {returned &&
          <button 
            className="w-full h-auto invisible rounded-md font-medium pt-2 mt-2 mb-1  inline-block"> A
          </button>}
          </div>
  )
}

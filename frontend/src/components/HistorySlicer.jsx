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
    <div className=' w-[160px] max-[640px]:h-60 sm:h-64 md:h-72 lg:h-96 sm:w-[200px] md:w-[240px] lg:w-[280px] inline-block  relative p-2'>
      <img
        className='w-full block h-full pb-2'
        src={item.Book_Image}
        alt={item?.Name}
      />
      <p className="text-red-700  rounded text-xl flex-shrink-0 w-auto flex-wrap"> {item.Auhtor_Name} </p>
      <h3 className="text-2xl font-bold text-indigo-800 my-2 h-20 break-words">a a {item.Name}</h3>
      <p className="capitalize text-[#00df9a]">Borrow Date: {date}</p>
      {/*{!returned &&
              <button 
                onClick={returnBook}
                className="w-full bg-black text-[#00df9a] inline-block rounded-md font-medium my-6 py-3">
                  Return Book
        </button>} */}
   </div>
  )
}

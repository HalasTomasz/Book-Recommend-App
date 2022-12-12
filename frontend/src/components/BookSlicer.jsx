import React from 'react';
import {useNavigate } from "react-router-dom"

export default function BoookSlicer({ item }){
  const navigate = useNavigate();

  function handleClick(e){
    e.preventDefault()
    navigate(`/books/${item.Book_ID}`)
    //window.location.reload()
  }

  return (
    <div className='w-[160px] max-[640px]:h-60 sm:h-64 md:h-72 lg:h-96 sm:w-[200px] md:w-[240px] lg:w-[280px] inline-block cursor-pointer relative p-2'>
      <img
        className='w-full block h-full'
        src={item.Book_Image}
        alt={item?.Name}
      />
      <div onClick={handleClick} className='absolute top-0 left-0 w-full h-full hover:bg-black/60 opacity-0 hover:opacity-100 text-white overflow-auto'>
        <p className='whitespace-normal text-xs md:text-sm font-bold h-full text-center flex justify-center items-center'>
          {item?.Name}
        </p>
        <p>
        </p>
      </div>
    </div>
  );
};
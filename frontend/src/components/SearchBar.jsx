import React, { useState, useEffect} from "react";
import {BiSearch} from 'react-icons/bi'
import {useDispatch, useSelector} from 'react-redux'
import {listBooks} from '../actions/bookAction'

export default function SearchBar() {

    const [filterOnData, setFilterOnData] = useState([]);
    const [words, setWords] = useState("");
    const dispatch = useDispatch()
    const bookList = useSelector(state => state.bookList)
    const {error, loading, books} = bookList
  
    useEffect(() => {
      dispatch(listBooks())
    },[dispatch])

    const handleFilter = (event) => {
        const wordWeLookFor = event.target.value;
        setWords(wordWeLookFor); 
        const newFilter = books.filter((value) => {
          return value.Name.toLowerCase().includes(words.toLowerCase());
        })
        console.log(newFilter)
        if (wordWeLookFor === "") {
            setFilterOnData([]);
        } else {
            setFilterOnData(newFilter);
        }};
      
        const clearInput = () => {
            setFilterOnData([]);
            setWords("");
        };
      
        return (
          <div className="h-screen bg-gray-500">
          <div className="grid items-center justify-center pt-6">
            <div className="w-full border-b-4 border-black py-1 px-4">
              <div className="relative block">
                  <form className=' static bg-white'>
                      <input
                          value={words}
                          onChange={handleFilter}
                          className='bg-primary p-3 md:text-md font-medium border-2 border-green-900 focus:outline-none focus:border-2 focus:border-gray-300 w-full md:w-[350px] rounded-full  md:top-0'
                          placeholder='Search for books'
                      />
                      <button
                          className='absolute md:right-5 right-6 top-4 border-l-2 border-pink-300 pl-4 text-2xl text-gray-400'
                      >
                          <BiSearch />
                      </button>
                  </form>
              </div>
            </div>
            {filterOnData.length !== 0 && (
              <div className="bg-white  overflow-hidden">
                {filterOnData.slice(0, 8).map((value, key) => {
                  return (
                    <a className="" href={`/books/${value.Book_ID}`} >
                      <p>{value.Name} </p>
                    </a>
                  );
                })} 
              </div>)}
            </div>
            </div>
        );
      }